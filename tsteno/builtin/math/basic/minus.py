from sympy import parse_expr
from tsteno.atoms.module import ModuleArg, Module


class Minus(Module):

    def run(self, a, b):
        return a - b

    def get_arguments(self):
        return [
            ModuleArg(), ModuleArg()
        ]

    def run_test(self, test):
        evaluation = self.get_kernel().get_kext('eval')

        # Test numerical minus
        test.assertEqual(evaluation.evaluate_code('1-0.5')[0], .5)

        # Test symbolic minus.
        test.assertEqual(evaluation.evaluate_code('x-2')[0], parse_expr("x-2"))

        # Test symbolic minus.
        test.assertEqual(evaluation.evaluate_code(
            '2*x-x')[0], parse_expr("x"))
