import importlib
import sys
import os


class Plugin:
    def initialize(self):
        raise NotImplementedError(
            "Plugins must implement the 'initialize' method.")

    def execute(self):
        raise NotImplementedError(
            "Plugins must implement the 'execute' method.")


class PluginManager:
    def __init__(self, plugin_dir: str, os_id: str):
        self.plugin_dir = plugin_dir + "/" + os_id
        self.plugins = []

    def load_plugins(self):
        # Add plugin directory to sys.path to allow importing
        sys.path.append(self.plugin_dir)

        # Scan the plugin directory for Python files
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                module = importlib.import_module(module_name)

                for attr in dir(module):
                    plugin_class = getattr(module, attr)

                    if isinstance(plugin_class, type) and issubclass(plugin_class, Plugin) and plugin_class is not Plugin:
                        self.plugins.append(plugin_class())

    def initialize_plugins(self):
        for plugin in self.plugins:
            plugin.initialize()

    def execute_plugins(self):
        for plugin in self.plugins:
            plugin.execute()
