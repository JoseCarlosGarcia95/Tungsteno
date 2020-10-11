class Notebook:
    def __init__(self, cells, nb_properties):
        self.cells = cells
        self.nb_properties = nb_properties

    def cli(self, evaluation):
        nb_result = []
        for cell in self.cells:
            one_nb_result = cell.cli()

            if isinstance(one_nb_result, list):
                nb_result = nb_result + one_nb_result

        nb_input_code = "".join(nb_result)
        evaluation.evaluate_code(nb_input_code)
