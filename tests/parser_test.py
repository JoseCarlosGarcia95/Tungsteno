import unittest
from tsteno.language.ast import Node
from tsteno.language.parser import Parser
from tsteno.language.tokenizer import Tokenizer

parser = Parser()
tokenizer = Tokenizer()


class TestTokenizer(unittest.TestCase):
    def test_parseNumber(self):
        global tokenizer, parser
        tokens = tokenizer.get_tokens("12345")

        nodes = list(parser.get_nodes(list(tokens)))

        self.assertEqual(len(nodes), 1)
        one_node = nodes[0]

        self.assertEqual(one_node, 12345)

    def test_opOrder(self):
        global tokenizer, parser

        tokens = tokenizer.get_tokens("1+2*3")

        nodes = list(parser.get_nodes(list(tokens)))

        self.assertEqual(len(nodes), 1)

        one_node = nodes[0]

        self.assertEqual(one_node.head, 'Plus')
        self.assertEqual(one_node.childrens[0], 1)
        self.assertIsInstance(one_node.childrens[1], Node)

        product = one_node.childrens[1]
        self.assertEqual(product.head, 'Product')
        self.assertEqual(product.childrens[0], 2)
        self.assertEqual(product.childrens[1], 3)

    def test_listDefinition(self):
        global tokenizer, parser

        tokens = list(tokenizer.get_tokens("{1, 2, 3}"))
        nodes = list(parser.get_nodes(tokens))

        node_list = nodes[0]
        self.assertEqual(node_list.head, 'List')
        self.assertEqual(node_list.childrens[0], 1)
        self.assertEqual(node_list.childrens[1], 2)
        self.assertEqual(node_list.childrens[2], 3)

    def test_moduleDefinition(self):
        return
        global tokenizer, parser

        tokens = list(tokenizer.get_tokens("""Module[{x, y},
            x=x+1
            Return[x+1]
            ]"""))

        nodes = list(parser.get_nodes(tokens))

        module = nodes[0]

        self.assertEqual(module.head, 'Module')

        arguments = module.childrens
        self.assertEqual(len(arguments), 2)

        list_arg = arguments[0]
        self.assertEqual(list_arg.head, 'List')
        self.assertEqual(list_arg.childrens[0].get_value(), 'x')
        self.assertEqual(list_arg.childrens[1].get_value(), 'y')

        module_fn = arguments[1]
        self.assertEqual(len(module_fn), 2)


if __name__ == '__main__':
    unittest.main()
