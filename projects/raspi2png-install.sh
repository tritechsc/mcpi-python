#!/bin/bash
cd ~/;
git clone https://github.com/tritechsc/raspi2png.git;
cd  ~/Desktop;
if [ ! -d ~/Desktop/screenShots ]; then
  mkdir -p ~/Desktop/screenShots;
fi

#/home/pi/raspi2png -p NAME -d SECONDS
