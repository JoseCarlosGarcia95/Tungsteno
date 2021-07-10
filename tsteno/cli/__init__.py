import click
from sys import platform

if platform == "linux" or platform == "linux2":
    import readline
from sympy import mathematica_code as mcode
from tsteno import VERSION, CODENAME, COPYRIGHT
from tsteno.kernel.kernel import Kernel
from tsteno.kernel.kexts.log import LogLevel
from tsteno.gui import init_gui
from tsteno.notebook import Notebook
from tsteno.atoms.rule import RuleSet


@click.command()
@click.option('--debug', '-d', is_flag=True,
              help='Initialize tsteno kernel in debug mode')
@click.option('--cli', '-c', is_flag=True, help='CLI mode')
@click.option('--launcher', '-l', is_flag=True, help='Launcher mode')
@click.option('--input', '-i', 'input_', help="*.nb file for input")
@click.option('--http-port', '-p', 'http_port', help='HTTP port', default=8000)
def main(debug, cli, launcher, input_, http_port):
    kernel_opts = {}
    if debug:
        kernel_opts = {
            'kext_extensions': {
                'log': {
                    'log_level': LogLevel.DEBUG
                }
            }
        }

    kernel = Kernel(options=kernel_opts)
    evaluation = kernel.get_kext('eval')

    if cli:
        run_cli(kernel)
    elif input_ is not None:
        nb_file = open(input_, 'r')
        eval_result = evaluation.evaluate_code(nb_file.read())

        output = kernel.get_kext('output')

        output.register_output_handler(cli_printer)

        if isinstance(eval_result, Notebook):
            eval_result.cli(evaluation)

        nb_file.close()
    else:
        init_gui(kernel, input_, launcher, http_port)


k = 0


def parse_to_print(to_print):
    if isinstance(to_print, RuleSet):
        return str(to_print)
    elif isinstance(to_print, list):
        out = '{'
        for item in to_print:
            out += parse_to_print(item)
            out += ','
        out = out[:-1]
        return out + '}'
    elif not isinstance(to_print, str):
        return mcode(to_print)
    return to_print


def cli_printer(obj):
    if obj is None or isinstance(obj, Notebook):
        return

    to_print = parse_to_print(obj)
    click.echo("Out[{}]= {}".format(k, to_print))
    # click.echo()


def run_cli(kernel):
    global k
    # Print header
    click.echo("Tungsteno Language {} ({})".format(VERSION, CODENAME))
    click.echo(COPYRIGHT)

    evaluation = kernel.get_kext('eval')
    output = kernel.get_kext('output')

    output.register_output_handler(cli_printer)

    if platform == "linux" or platform == "linux2":
        readline.parse_and_bind("tab: complete")
        readline.set_completer(evaluation.get_autocompletion)

    click.echo()

    while True:
        to_execute = input("In[{}]:= ".format(k))
        try:
            evaluation.evaluate_code(to_execute)
        except Exception as err:
            click.echo(err)
        k = k + 1
