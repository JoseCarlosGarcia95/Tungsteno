from sympy import Rational, parse_expr
from tsteno.atoms.module import ModuleArg, Module


class Div(Module):

    def run(self, a, b):

        if isinstance(a, int) and isinstance(b, int):
            return Rational(a, b)

        return a / b

    def get_arguments(self):
        return [
            ModuleArg(), ModuleArg()
        ]

    def run_test(self, test):
        evaluation = self.get_kernel().get_kext('eval')

        # Test numerical division
        test.assertEqual(evaluation.evaluate_code('1.0/2')[0], .5)

        # Test symbolic division.
        test.assertEqual(evaluation.evaluate_code('1/2')[0], parse_expr("1/2"))
