FROM debian

# APT update, and install basic dependencies
RUN apt-get update -y
RUN apt-get install -y make
RUN apt-get install -y gcc
RUN apt-get install -y mupen64plus
RUN apt-get install -y libjson-c-dev
RUN apt-get install -y mupen64plus-ui-console
RUN apt-get install -y tightvncserver
# RUN apt-get install -y x11-apps
# RUN apt-get install -y xserver-xorg
# RUN apt-get install -y xorg
# RUN apt-get install -y jwm
# RUN apt-get install -y  libxext-dev libxrender-dev libxtst-dev libgl1-mesa-dri



# Add Roms
RUN mkdir /roms
COPY ./roms /roms

# Copy dependencies and source files
COPY ./emulator_input_plugin /app/emulator_input_plugin
COPY ./mupen64plus-core /app/mupen64plus-core

# Make the emulator plugin
RUN cd app/emulator_input_plugin && make install
# Run the command
CMD ["bash", "/app/emulator_input_plugin/run.sh"]