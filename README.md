# README.md

This repository contains the files from my **Full Circle Magazine issue #191 (March 2023)**.

**NOTE: This is currently an EARLY RELEASE REPOSITORY.**

This repository contains Python code for a standalone Python program called *mido_test.py*, a *requirements.txt* file to make the installation of the extra libries easier, a Python project written in **PAGE** called *MidiInfo* which includes 4 files (MidiInfo.tcl, MidiInfo.py, MidiInfo_support.py and the shared.py file which are required to run the program), a grahics folder for the PAGE project, a themes folder which is required for the PAGE project and at least 4 freely available midi files.

## Assumptions

I am going to assume that you have the following programs already installed on your Linux system...

Fluidsynth
Python version 3.8 or greater
Pip version for Python 3.8 or greater

To install Fluidsynth on your system, in a terminal type


    sudo apt-get install -y fluidsynth

If you don't want to use the requirements.txt, there are two python libraries that you need to install.

    pip3 install mido


To get the midi files to play, I used alsa and alsa_seq.  You can check to see if you already have alsa installed by typeing in a terminal "alsa -version"



    $ alsa -version

which return the following information

    Usage: /sbin/alsa {unload|reload|force-unload|force-reload|suspend|resume}

If you need to install alsa

    sudo apt install alsa-tools


Sometimes, alsa and pulseaudio don't play nicely together.  If this happens to you, you can use the following command to restart both.  Note: this usually takes about a minute on my machine.

    pulseaudio -k && sudo alsa force-reload && sleep 2 && pulseaudio -k && sudo alsa force-reload


You can also test your fluidsynth installation by using the command line with the following command

    fluidsynth -a alsa -m alsa_seq -i /usr/share/sounds/sf2/FluidR3_GM.sf2 <midifilename>

