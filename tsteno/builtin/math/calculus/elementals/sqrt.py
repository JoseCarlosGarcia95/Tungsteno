import sympy as sp
import numpy as np
from tsteno.atoms.module import ModuleArg, Module


class Sqrt(Module):

    def run(self, x):
        if isinstance(x, float):
            return np.sqrt(x)

        return sp.sqrt(x)

    def get_arguments(self):
        return [
            ModuleArg(),
        ]

    def run_test(self, test):
        evaluation = self.get_kernel().get_kext('eval')

        test.assertEqual(evaluation.evaluate_code(
            'Sqrt[-1]'), evaluation.evaluate_code('I'))

        test.assertEqual(evaluation.evaluate_code(
            'Sqrt[2]'), sp.parse_expr('sqrt(2)'))

        test.assertEqual(evaluation.evaluate_code(
            'Sqrt[25]'), 5)

        test.assertEqual(evaluation.evaluate_code(
            'Sqrt[2.0]'), 1.4142135623730951)
