from plugin_system import Plugin


class PluginTwo(Plugin):
    def initialize(self):
        print("PluginTwo initialized!")

    def execute(self):
        print("PluginTwo executed!")
