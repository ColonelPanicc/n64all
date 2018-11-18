# N64 All
A project for DurHack 2018.

Designed by John Jennings, George Price, Ryan Collins, Mike Croall, Oliver McCloud, and Sara Chen.

![alt text](https://github.com/georgeprice/n64all/blob/master/mario.png "System Architecture")

**NB: Docker here doesn't yet work. Don't try to run with Docker as you'll probably fail.**
## Why?
- We don't know. It was fun.

## Build Instructions
### 0. ROMS
Place your roms into the roms folder. The Mario Kart rom is tested to work with the filename mariokart.z64`.

### 1. Mupen Input Controller
First, you'll need to build the C plugin for mupen. This polls a REST api, and fetches the controller values for each controller.

You'll need to install the following dependencies for this to work:
- lib-json

Navigate to the root of the repo, and download the git submodule source dependencies, by running:

```bash
git submodule init
git submodule update
```

Following this, we are ready to compile.

Navigate to the emulator_input_plugin folder, and then run:

```bash
make install
```

**NB: Sudo might need to be used here to delete previously built versions of the plugin**

### 2.0 Run the main mario server
This is found in the api folder.

Download dependencies using:

```bash
pipenv install
```

And then drop into a pipenv shell and run using hug.

```bash
pipenv shell
hug -t index.py
```

### 3.0 (optional) Start other bots/apps
Stupid bot, and the Xbox client are both ones that can be run by executing the Python script.

### 4.0  Run the emulator
Navigate to the top level of the dirrectory structure:

```bash
mupen64plus --gfx mupen64plus-video-glide64 --windowed  --input emulator_input_plugin/emulator_input_plugin.so roms/mariokart.z64
```
