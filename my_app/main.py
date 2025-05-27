#!/bin/env python3

import os
import distro
from plugin_system import PluginManager

if __name__ == "__main__":
    base_path = os.path.dirname(__file__)

    plugin_manager = PluginManager(
        plugin_dir=base_path + "/plugins",
        os_id=distro.id(),
    )

    plugin_manager.load_plugins()
    plugin_manager.initialize_plugins()
    plugin_manager.execute_plugins()
