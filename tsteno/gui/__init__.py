import os
import eel
import sympy
import traceback
import difflib
import tsteno.notebook.export

from sympy import mathematica_code as mcode
from tsteno.notebook import Notebook
from tsteno.atoms.plot import Plot
from tsteno.atoms.rule import RuleSet

evaluation = None
output = None
eel_configuration = {}


@eel.expose
def ping():
    return 'pong'


@eel.expose
def evaluate(code):
    global output

    output_result = []

    def gui_printer(obj):
        if obj is None or isinstance(obj, Notebook):
            return

        to_print = obj

        if isinstance(to_print, RuleSet):
            to_print = str(to_print)
        elif not isinstance(to_print, str) and not isinstance(to_print, Plot):
            to_print = mcode(to_print)

        output_result.append(to_print)

    output.deregister_output_handlers()
    output.register_output_handler(gui_printer)

    try:
        eval_result = evaluation.evaluate_code(code)
    except Exception as err:
        print(traceback.format_exc())
        print(err)
        return {'processor': 'error', 'error': str(err)}

    if isinstance(eval_result, sympy.Expr):
        return {
            'processor': 'default',
            'result': "\n".join(output_result)
        }
    elif isinstance(eval_result, Plot):
        plot_data = [{
            'x': eval_result.x,
            'y': eval_result.y,
            'type': 'scatter',
            'mode': 'lines',
            'marker': {
                    'color': 'red'
            }
        }]

        if eval_result.z is not None:
            plot_data[0]['z'] = eval_result.z
            plot_data[0]['type'] = 'surface'

        return {
            'processor': 'plot',
            'plot_data': plot_data
        }

    return {'processor': 'default', 'result': "\n".join(output_result)}


@eel.expose
def read_file(input_file):
    nb_file = open(input_file, 'r')
    eval_result = evaluation.evaluate_code(nb_file.read())

    if not isinstance(eval_result, Notebook):
        raise Exception("Expected notebook")

    return eval_result.dump()


@eel.expose
def read_notebook(file_data):
    eval_result = evaluation.evaluate_code(file_data)

    if not isinstance(eval_result, Notebook):
        raise Exception("Expected notebook")

    return eval_result.dump()


@eel.expose
def suggestions(input):
    global evaluation

    options = []
    input_len = len(input)

    if input_len < 2:
        return options

    definitions = evaluation.get_all_definitions()

    for definition in definitions:
        seq = difflib.SequenceMatcher(None, input, definition)

        options.append({
            'name': definition,
            'value': definition,
            'score': seq.ratio()
        })

    options.sort(key=lambda op: op['score'], reverse=True)
    options = options[:10]

    return options


@eel.expose
def searchFunction(search):
    global evaluation

    search_results = []

    for definition in evaluation.builtin_modules.keys():
        module_def = evaluation.builtin_modules[definition]
        seq = difflib.SequenceMatcher(None, search, definition)

        description = ''

        if module_def.__doc__ is not None:
            description = module_def.__doc__.replace('    ', '')

        mult = 1
        if search in definition:
            mult = 2
        if seq.ratio() > 0:
            search_results.append({
                'functionName': definition,
                'description': description,
                'score': mult * seq.ratio()
            })

        if len(description) > 0:
            abstract = description.strip().split("\n")[0]
            seq = difflib.SequenceMatcher(None, search, abstract)
            mult = 1
            if search in abstract:
                mult = 2
            if seq.ratio() > 0:
                search_results.append({
                    'functionName': definition,
                    'description': description,
                    'score': seq.ratio() * mult
                })

    search_results.sort(key=lambda op: op['score'], reverse=True)

    return search_results[:3]


@eel.expose
def get_eel_configuration():
    global eel_configuration
    return eel_configuration


@eel.expose
def export_nb(cells):
    return tsteno.notebook.export.export_nb(cells)


def init_gui(kernel, input_file):
    global evaluation
    global output
    global eel_configuration

    if input_file is not None:
        eel_configuration['input_file'] = input_file

    output = kernel.get_kext('output')
    evaluation = kernel.get_kext('eval')

    eel.init(os.path.join(os.path.dirname(__file__), 'static'))
    eel.start('', mode='web', all_interfaces=False)
