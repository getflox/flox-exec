from floxcore.config import Configuration
from floxcore.plugin import Plugin

from flox_exec.command import flox_exec


class ExecConfiguration(Configuration):
    def parameters(self):
        return tuple()

    def schema(self):
        pass


class ExecPlugin(Plugin):
    def configuration(self):
        return ExecConfiguration()

    def add_commands(self, cli):
        cli.add_command(flox_exec)


def plugin():
    return ExecPlugin()
