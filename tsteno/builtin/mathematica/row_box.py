from tsteno.notebook.row_box import RowBox as RowBoxObj
from tsteno.atoms.module import Module, ModuleArg, ARG_FLAG_ALL_NEXT


class RowBox(Module):

    def run(self, boxes):
        return RowBoxObj(boxes)

    def get_arguments(self):
        return [
            ModuleArg()
        ]

    def run_test(self, test):
        pass
