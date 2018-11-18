FROM debian

# APT update, and install basic dependencies
RUN apt-get update -y
RUN apt-get install -y make
RUN apt-get install -y gcc
RUN apt-get install -y mupen64plus
RUN apt-get install -y libjson-c-dev
RUN apt-get install -y mupen64plus-ui-console
RUN apt-get install -y alsa-utils
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  lxde-core \
  lxterminal \
  tightvncserver \
  xrdp

# Set user for VNC server (USER is only for build)
ENV USER root
# Set default password

RUN echo "password" > password.txt | cat password.txt password.txt | vncpasswd && \
  rm password.txt
# Expose VNC port
EXPOSE 5901
RUN touch ~/.Xresources
RUN touch /root/.Xauthority

# Set XDRP to use TightVNC port
RUN sed -i '0,/port=-1/{s/port=-1/port=5901/}' /etc/xrdp/xrdp.ini

# Create VNC script that handles restarts, and copy.
RUN echo "rm /tmp/.X1-lock /tmp/.X11-unix/X1; vncserver :1 -geometry 1280x800 -depth 24 && tail -F /root/.vnc/*.log " > /opt/vnc.sh; chmod +x /opt/vnc.sh

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