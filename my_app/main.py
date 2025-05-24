from plugin_system import PluginManager

if __name__ == "__main__":
    plugin_manager = PluginManager(plugin_dir="plugins")
    plugin_manager.load_plugins()
    plugin_manager.initialize_plugins()
    plugin_manager.execute_plugins()
