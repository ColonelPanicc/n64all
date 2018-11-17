FROM debian

# APT install dependencies.
RUN apt-get update -y
RUN apt-get install -y make
RUN apt-get install -y mupen64plus
RUN apt-get install -y libjson-c-dev
RUN apt-get install -y mupen64plus-ui-console
RUN mkdir /roms
COPY ./roms /roms
COPY ./emulator_input_plugin /app/emulator_input_plugin
COPY ./mupen64plus-core /app/mupen64plus-core

RUN make /app/emulator_input_plugin

CMD ["/usr/games/mupen64plus", "--input", "/app/emulator_input_plugin/emulator_input_plugin.so", "/roms/mariokart.z64"]