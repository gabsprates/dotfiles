from plugin_system import Plugin


class PluginOne(Plugin):
    def initialize(self):
        print("PluginOne initialized!")

    def execute(self):
        print("PluginOne executed!")
