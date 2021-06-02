from sympy import parse_expr
from tsteno.atoms.module import ModuleArg, Module
from tsteno.atoms.module import ARG_FLAG_ALL_NEXT


class D(Module):
    """
    Gives the partial derivative of df/dx
    ```
    D[f, x]
    ```
    """

    def run(self, f, *variables):
        if hasattr(f, 'get_sympy'):
            return f.get_sympy().diff()
        return f.diff(*variables)

    def get_arguments(self):
        return [
            ModuleArg(),
            ModuleArg(ARG_FLAG_ALL_NEXT)
        ]

    def run_test(self, test):
        evaluation = self.get_kernel().get_kext('eval')

        test.assertEqual(evaluation.evaluate_code(
            'D[x^4 * y^2, {x, 3}, {y, 1}]'), parse_expr('48*x*y'))
