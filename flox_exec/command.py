import click
from click import MissingParameter
from click.exceptions import Exit
from plumbum import ProcessExecutionError, local


@click.command(name="exec", context_settings=dict(ignore_unknown_options=True, ))
@click.argument('command', nargs=-1, type=click.UNPROCESSED)
@click.pass_obj
def flox_exec(flox, command, **kwargs):
    """Execute command with Flox context variables"""
    if len(command) < 1:
        raise MissingParameter(message="Command parameter is required", param_type="command")

    command = list(command)
    command_name = command.pop(0)
    command_args = command

    with local.env(FOO="BAR"):
        cmd = local[command_name]
        try:
            (cmd.__getitem__(command_args) > click.get_binary_stream('stdout'))()
        except ProcessExecutionError as e:
            raise Exit(e.retcode)
