FROM ubuntu:15.04

COPY . /app/emulator_input_plugin
COPY ../mupen64plus-core /app/mupen64plus-core

RUN make /app/emulator_input_plugin
ROM="mariokart.z64"
CMD mupen64plus --input /app/emulator_input_plugin/emulator_input_plugin.so $ROM
