# N64 All
A project for DurHack 2018.

Designed by John Jennings, George Price, Ryan Collins, Mike Croall, Oliver McCloud, and Sara Chen.

## Build Instructions
### 1. Mupen Input Controller
First, you'll need to build the C plugin for mupen. This polls a REST api, and fetches the controller values for each controller.

You'll need to install the following dependencies for this to work:
- lib-json

Navigate to the root of the repo, and download the git submodule source dependencies, by running:

'''bash
git submodule init
git submodule update
'''

Following this, we are ready to compile.

Navigate to the emulator_input_plugin folder, and then run:

'''bash
make install
'''

**NB: Sudo might need to be used here to delete previously built versions of the plugin**


