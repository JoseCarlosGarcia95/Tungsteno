""" Tokenizer generates tokens from input strings """
import string


class Token:
    """ Represent the most abstract type of token """
    __slots__ = ['value']

    def __init__(self, val):
        """ 
        Create a new token from given value

        Keyword arguments:
        val -- token value
        """

        self.value = val

    def get_value(self):
        return self.value

    @staticmethod
    def is_match(character):
        """ Check if given character match with token character list 

        Keyword arguments:
        character -- character to be checked
        """
        raise Exception("Method not defined")

    @staticmethod
    def parse(tokenizer):
        """ After a match, generate a token class from the current buffer. 

        Keyword arguments:
        tokenizer -- current buffer
        """
        raise Exception("Method not defined")

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.value}'


class NumberToken(Token):
    @staticmethod
    def is_match(character):
        return character != None and (character.isdigit() or character == '.')

    @staticmethod
    def parse(tokenizer):
        characters = [tokenizer.get_current_character()]

        while NumberToken.is_match(tokenizer.next_character()):
            characters.append(tokenizer.get_current_character())

        num_str = "".join(characters)

        if "." in characters:
            return NumberToken(float(num_str))

        return NumberToken(int(num_str))


class BinOpToken(Token):

    BINARY_OP_CHARACTERS = ['+', '-', '*', '/', '^']

    @staticmethod
    def is_match(character):
        return character in BinOpToken.BINARY_OP_CHARACTERS

    @staticmethod
    def parse(tokenizer):
        op = tokenizer.get_current_character()

        next_chr = tokenizer.next_character()

        if op == '-' and next_chr == '>':
            tokenizer.next_character()
            return BinOpToken("->")
        if op == '.':
            if next_chr != '/':
                raise IllegalCharacter(tokenizer)
            return BinOpToken("./")

        return BinOpToken(op)


class ClosureToken(Token):

    CLOSURE_CHARACTERS = ["\n", ";"]

    @staticmethod
    def is_match(character):
        return character in ClosureToken.CLOSURE_CHARACTERS

    @staticmethod
    def parse(tokenizer):
        op = tokenizer.get_current_character()
        tokenizer.next_character()

        return ClosureToken(op)


class StringToken(Token):
    @staticmethod
    def is_match(character):
        return character == "\""

    @staticmethod
    def parse(tokenizer):
        characters = []
        finished_string = False

        while tokenizer.next_character() != None:
            if tokenizer.get_current_character() == "\"" and (len(characters) == 0 or characters[-1] != "\\"):
                tokenizer.next_character()
                finished_string = True
                break

            if tokenizer.get_current_character() == "\"":
                characters[-1] = tokenizer.get_current_character()
            else:
                characters.append(tokenizer.get_current_character())

        if not finished_string:
            raise IllegalCharacter(tokenizer)

        return StringToken("".join(characters))


class IdentifierToken(Token):
    SPECIAL_CHARACTERS = ['_']

    @staticmethod
    def is_match(character):
        return character != None and character in string.ascii_letters

    @staticmethod
    def parse(tokenizer):
        characters = [tokenizer.get_current_character()]

        while IdentifierToken.is_match(tokenizer.next_character()) or (
                tokenizer.get_current_character() != None and (
                    tokenizer.get_current_character().isdigit() or
                    tokenizer.get_current_character() in IdentifierToken.SPECIAL_CHARACTERS
                )
        ):
            characters.append(tokenizer.get_current_character())

        if FunctionIdentifierToken.is_match(tokenizer.get_current_character()):
            return FunctionIdentifierToken.parse(tokenizer, "".join(characters))

        return IdentifierToken("".join(characters))


class FunctionIdentifierToken(IdentifierToken):

    __slots__ = ['fname']

    @staticmethod
    def is_match(character):
        return character != None and character == '['

    @staticmethod
    def parse(tokenizer, fname):
        return FunctionIdentifierToken(fname)

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.value}'


class TokenizerError(Exception):
    __slots__ = ['tokenizer', 'msg']

    def __init__(self, msg, tokenizer):
        self.msg = msg
        self.tokenizer = tokenizer

    def __str__(self):
        debug_info = self.tokenizer.debug_information()
        lines = debug_info['buffer'].split("\n")

        extra_information = lines[debug_info['lin']]
        extra_information += "\n" + (' '*(debug_info['col'] - 1)) + '^'

        return f"{self.msg} near line {debug_info['lin'] + 1} and column {debug_info['col'] + 1}:\n{extra_information}"


class IllegalCharacter(TokenizerError):
    def __init__(self, tokenizer):
        super().__init__("Syntax error, illegal character", tokenizer)


class Tokenizer:
    AVAILABLE_TOKENS = [
        NumberToken, BinOpToken,
        StringToken, IdentifierToken,
        ClosureToken
    ]

    BLANK_SPACES = [' ', "\r"]

    __slots__ = ['buffer', 'current_pos',
                 'current_character', 'bufferlen', 'col', 'lin']

    def __init__(self, buffer):
        self.buffer = buffer
        self.bufferlen = len(self.buffer)
        self.current_pos = -1

        self.lin = 0
        self.col = 0

        self.next_character()

    def next_character(self):
        self.current_pos = self.current_pos + 1
        self.current_character = self.buffer[self.current_pos] if self.bufferlen > self.current_pos else None

        if self.current_character == "\n":
            self.lin = self.lin + 1
            self.col = 0
        else:
            self.col = self.col + 1

        return self.current_character

    def get_current_character(self):
        return self.current_character

    def previous_character(self):
        self.current_pos = self.current_pos - 1
        self.current_character = self.buffer[self.current_pos] if 0 <= self.current_pos else None
        if self.current_character == "\n":
            self.lin = self.lin - 1
            self.col = 0
        else:
            self.col = self.col - 1
        return self.current_character

    def debug_information(self):
        return {'buffer': self.buffer, 'lin': self.lin, 'col': self.col}

    def next_token(self):
        while self.current_character in Tokenizer.BLANK_SPACES:
            self.next_character()

        if self.current_character == None:
            return None

        for token in Tokenizer.AVAILABLE_TOKENS:
            if token.is_match(self.current_character):
                return token.parse(self)

        raise IllegalCharacter(self)

    def get_tokens(self):
        tokens = []

        token = self.next_token()

        while token != None:
            tokens.append(token)
            token = self.next_token()

        return tokens