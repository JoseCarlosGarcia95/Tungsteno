""" Parser read tokens generated by tokenizer, and generate final tokens for
kernel """
from .tokenizer import NumberToken, IdentifierToken, ClosureToken, StringToken
from .tokenizer import FunctionIdentifierToken, ListSeparatorToken, BinOpToken
from .tokenizer import ListToken, UnaryOpToken

from collections import namedtuple

OpInfo = namedtuple('OpInfo', 'prec assoc function')

BIN_OPINFO_MAP = {
    '=':    OpInfo(0, 'LEFT', 'Set'),
    '<':    OpInfo(0, 'LEFT', 'LessThan'),
    '<=':   OpInfo(0, 'LEFT', 'LessEqual'),
    '>':    OpInfo(0, 'LEFT', 'GreaterThan'),
    '>=':   OpInfo(0, 'LEFT', 'GreaterEqual'),
    '==':   OpInfo(0, 'LEFT', 'Equal'),
    '!=':   OpInfo(0, 'LEFT', 'NotEqual'),

    '+':    OpInfo(1, 'LEFT', 'Plus'),
    '-':    OpInfo(1, 'LEFT', 'Minus'),

    '*':    OpInfo(2, 'LEFT', 'Product'),
    '/':    OpInfo(2, 'LEFT', 'Div'),

    '^':    OpInfo(3, 'RIGHT', 'Pow'),
}
""" Contains information of how to parse operation symbols """

UNARY_OPINFO_MAP = {
    '++': 'Increment'
}


class ParserOutput:
    """ Class result after parsing token """

    @staticmethod
    def is_match(token):
        """ Check if given character match with token character list

        Arguments:
            **token**: Token to be checked.

        Return:
            True if match, false if not.
        """
        raise Exception("Method not defined")

    @staticmethod
    def parse(parser):
        """ After a match, generate a token class from the tokenizer.

        Arguments:
            **parser**: parse given items

        Return:
            *(ParserOutput)* Pre-evaluate parser-output
        """
        raise Exception("Method not defined")


class ExpressionParserOutput(ParserOutput):
    """
    Represent Tungsten Language expression.
    """

    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    @staticmethod
    def is_match(token):
        return isinstance(token, NumberToken) or \
            isinstance(token, IdentifierToken) or \
            isinstance(token, StringToken)

    @staticmethod
    def parse(parser, min_prec=0):
        atom_lhs = ExpressionParserOutput.compute_atom(parser)

        while (parser.current_pos < len(parser.tokens) and
               not isinstance(parser.curtok, ClosureToken) and
               parser.curtok is not None):

            cur = parser.curtok
            op = cur.get_value()
            prec, assoc, function = BIN_OPINFO_MAP[op]

            if cur is None or not isinstance(cur, BinOpToken) or \
               prec < min_prec:
                break

            next_min_prec = prec + 1 if assoc == 'LEFT' else prec
            parser.get_next_token()
            atom_rhs = ExpressionParserOutput.parse(parser, next_min_prec)

            atom_lhs = FunctionExpressionParserOutput(function, [
                atom_lhs, atom_rhs
            ])

        return atom_lhs

    @staticmethod
    def compute_atom(parser):
        """
        Return parser-output from the next token.

        Arguments:
            **parser**: Current parser class.

        Return:
            *(ExpressionParserOutput)*: Pre-compiled eval.
        """
        token = parser.curtok
        next_token = parser.get_next_token()

        if token is None:
            return None

        if isinstance(token, NumberToken):
            if next_token is not None and isinstance(next_token, UnaryOpToken):
                parser.get_next_token()
                return FunctionExpressionParserOutput(
                    UNARY_OPINFO_MAP[next_token.value],
                    [NumberExpressionParserOutput(token.get_value())]
                )
            return NumberExpressionParserOutput(token.get_value())
        elif isinstance(token, StringToken):
            return StringParserOutput(token.get_value())
        elif isinstance(token, FunctionIdentifierToken):
            return FunctionExpressionParserOutput(
                token.fname,
                ExpressionParserOutput.calculate_arguments(token.arguments)
            )
        elif isinstance(token, IdentifierToken):
            if next_token is not None and isinstance(next_token, UnaryOpToken):
                parser.get_next_token()
                return FunctionExpressionParserOutput(
                    UNARY_OPINFO_MAP[next_token.value],
                    [ExpressionParserOutput(token.get_value())]
                )
            return ExpressionParserOutput(token.get_value())

        raise Exception("Unknown token type")

    @staticmethod
    def calculate_arguments(arguments):
        """
        Calculate parser-output arguments for functions.

        Arguments:
            **arguments**: Token list as arguments.
        """
        token_group = []
        parser_output_args = []

        for arg in arguments:
            if isinstance(arg, ListSeparatorToken):
                arg_parser = Parser(token_group)
                arg_parser_result = arg_parser.get_all_parser_output()

                if len(arg_parser_result) == 1:
                    arg_parser_result = arg_parser_result[0]

                parser_output_args.append(arg_parser_result)

                token_group = []
            else:
                token_group.append(arg)

        if len(token_group) > 0:
            arg_parser = Parser(token_group)
            arg_parser_result = arg_parser.get_all_parser_output()

            if len(arg_parser_result) == 1:
                arg_parser_result = arg_parser_result[0]

            parser_output_args.append(arg_parser_result)

        return parser_output_args

    def __repr__(self):
        return str(self.value)


class NumberExpressionParserOutput(ExpressionParserOutput):
    """ Represent number parser-output class """
    pass


class StringParserOutput(ExpressionParserOutput):
    """ Represent number parser-output class """
    pass


class FunctionExpressionParserOutput(ExpressionParserOutput):
    """ Represent function parser-output """
    __slots__ = ['fname', 'arguments']

    def __init__(self, fname, arguments):
        self.fname = fname
        self.arguments = arguments

    def __repr__(self):
        output = self.fname + "["
        for arg in self.arguments:
            output += str(arg) + ", "
        output = output[:-2]
        output += "]"

        return output


class ListExpressionParserOutput(ParserOutput):
    @staticmethod
    def is_match(token):
        return isinstance(token, ListToken)

    @staticmethod
    def parse(parser):
        token = parser.curtok
        parser.get_next_token()

        items = ListExpressionParserOutput.calculate_items(token.items)

        return FunctionExpressionParserOutput('List', items)

    @staticmethod
    def calculate_items(arguments):
        """
        Calculate parser-output arguments for functions.

        Arguments:
            **arguments**: Token list as arguments.
        """
        token_group = []
        parser_output_args = []

        for arg in arguments:
            if isinstance(arg, ListSeparatorToken):
                arg_parser = Parser(token_group)
                arg_parser_result = arg_parser.get_next_parser_output()
                parser_output_args.append(arg_parser_result)

                token_group = []
            else:
                token_group.append(arg)

        if len(token_group) > 0:
            arg_parser = Parser(token_group)
            arg_parser_result = arg_parser.get_next_parser_output()
            parser_output_args.append(arg_parser_result)

        return parser_output_args


class Parser:
    """ Read tokens and generate parser-output """
    AVAILABLE_PARSER_OUT = [
        ExpressionParserOutput,
        ListExpressionParserOutput
    ]

    __slots__ = ['tokens', 'current_pos', 'curtok', 'toklen']

    def __init__(self, tokens):
        self.tokens = tokens
        self.current_pos = -1
        self.toklen = len(self.tokens)
        self.get_next_token()

    def get_next_token(self):
        """
        Read next token from tokenizer list.

        Return:
            **Token**: Next token from token list.
        """
        self.current_pos = self.current_pos + 1
        if self.toklen > self.current_pos:
            self.curtok = self.tokens[self.current_pos]
        else:
            self.curtok = None
        return self.curtok

    def get_current_token(self):
        """
        Current token from list.

        Return:
            **Token**: Current token.
        """
        return self.curtok

    def get_next_parser_output(self):
        """
        Calculate next parser output.

        Return:
            *(ParserOutput)*: Next parser output.
        """
        if self.curtok is None:
            return None

        if isinstance(self.curtok, ClosureToken):
            self.get_next_token()
            return self.get_next_parser_output()

        for parser_output in Parser.AVAILABLE_PARSER_OUT:
            if parser_output.is_match(self.curtok):
                return parser_output.parse(self)

        raise Exception("Unexpected " + str(self.curtok))

    def get_all_parser_output(self):
        """
        A list with all parser-output
        Return:
            *(List[ParserOutput])*: A list of parser output.
        """
        parser_output = self.get_next_parser_output()
        parser_output_all = []

        while parser_output is not None:
            parser_output_all.append(parser_output)
            parser_output = self.get_next_parser_output()

        return parser_output_all
