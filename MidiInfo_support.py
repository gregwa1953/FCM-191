#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Feb 09, 2023 11:26:49 AM CST  platform: Linux
#    Feb 09, 2023 12:28:51 PM CST  platform: Linux
# ======================================================
#     MidiInfo_support.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #191
# Written by G.D. Walters
# Copyright (c) 2023 by G.D. Walters
# This source code is released under the MIT License
# ======================================================
import sys
import os
import platform
import subprocess
import shared
import mido
from mido import MidiFile, Message, tempo2bpm

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
from tkinter import filedialog as filedialog
from tkinter import messagebox as messagebox

import MidiInfo

_debug = True  # False to eliminate debug printing from callback functions.
location = MidiInfo._location
version = "0.1.0"


def main(*args):
    """Main entry point for the application."""
    global root
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = MidiInfo.Toplevel1(_top1)
    startup()
    root.mainloop()


def startup():
    global sty
    sty = ttk.Style()
    # Cursor stuff
    global busyCursor, preBusyCursors, busyWidgets
    busyCursor = "watch"
    preBusyCursors = None
    busyWidgets = (root,)
    show_program_info()
    load_tcl_themes()
    sty.theme_use("notsodark")
    fix_ttkLabels()
    set_icon()
    setup_vars()
    set_titlebar()
    # ports()
    clear_display()
    centre_screen(718, 438)


def set_titlebar():
    shared.basetitle = f"Midi Info version {version}"
    _top1.title(shared.basetitle)


def clear_display():
    _w1.KeySignature.set("")
    _w1.Songlength.set("")
    _w1.TimeSignature.set("")
    _w1.Tempo.set("")
    _w1.MidiFileType.set("")


def load_tcl_themes():
    # ===================================================
    # This will load the various tcl Themes.
    # ===================================================
    # Load my NotSoDark theme
    global sty
    _top1.tk.call("source", os.path.join(location, "themes", "notsodark.tcl"))


def fix_ttkLabels():
    global sty
    labellist = [
        _w1.TLabel1,
        _w1.TLabel2,
        _w1.TLabel3,
        _w1.TLabel4,
        _w1.TLabel5,
        _w1.TLabel6,
        _w1.TLabel7,
        _w1.TLabel8,
        _w1.TLabel9,
        _w1.TLabel10,
        _w1.TLabel11,
    ]
    _bgcolor = sty.lookup(".", "background")
    _fgcolor = sty.lookup(".", "foreground")
    for lab in labellist:
        lab.config(background=_bgcolor)
        lab.config(foreground=_fgcolor)


def on_btnAbout(*args):
    if _debug:
        print("MidiInfo_support.on_btnAbout")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    titl = "Midi Info"
    msg = "Sorry, About is not finished yet"
    messagebox.showinfo(titl, msg, parent=_top1, icon=messagebox.INFO)


def on_btnExit(*args):
    if _debug:
        print("MidiInfo_support.on_btnExit")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    sys.exit()


def on_btnOpen(*args):
    global filename
    global busyCursor, preBusyCursors, busyWidgets
    if _debug:
        print("MidiInfo_support.on_btnOpen")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()

    filename = filedialog.askopenfilename(
        initialdir=location,
        title="Select A MIDI File",
        filetypes=(("midi files", "*.mid"), ("ALL Files", "*.*")),
    )
    if _debug:
        print(filename)
    # Get the filename of the midi file
    shared.midifilename = os.path.basename(filename)
    print(shared.midifilename)
    # Add it to the titlebar app title
    _top1.title(f"{shared.basetitle} - {shared.midifilename}")
    mid = MidiFile(filename)
    busyStart()
    clear_display()
    parse_midi_file(mid)
    if _debug:
        print(f"{shared.tempo=}")
    _w1.KeySignature.set(shared.key_signature)
    _w1.TimeSignature.set(shared.time_signature)
    _w1.Tempo.set(shared.tempo)
    _w1.MidiFileType.set(shared.miditype)
    songlength = mid.length
    slen = f"{int(songlength/60)} minutes, {int(songlength%60)} seconds."
    _w1.Songlength.set(slen)
    if _debug:

        print(f"{shared.time_signature=}")
        print(f"{shared.key_signature=}")
        print(f"{shared.tracks}")
    # delete_list_items()
    FillListBox()
    busyEnd()


def FillListBox():
    for itm in shared.tracks:
        dat = f"{itm[0]} - {itm[1]}"
        _w1.Scrolledlistbox1.insert("end", dat)
    _w1.Scrolledlistbox1.bind("<<ListboxSelect>>", on_listboxSelect)


def on_listboxSelect(e):
    indx = _w1.Scrolledlistbox1.curselection()
    itm = _w1.Scrolledlistbox1.get(indx[0])
    # SelectedItem.set(f"Selected Item: {indx[0]} - {itm}")
    print(f"Selected Item: {indx[0]} - {itm}")


def delete_list_items():
    if _debug:
        print("DeleteListItems")
    sys.stdout.flush()
    _w1.Scrolledlistbox1.delete(0, END)


def setup_vars():
    shared.midifilename = ""
    shared.miditype = ""
    shared.trackname = ""
    shared.tracknumber = ""
    shared.tracks = []
    shared.tracktext = ""
    shared.copyright = ""
    shared.instrument_name = ""
    shared.lyrics = ""
    shared.marker = ""
    shared.cue_marker = ""
    shared.device_name = ""
    shared.channel_prefix = ""
    shared.tempo = ""
    shared.midi_port = ""
    shared.time_signature = ""
    shared.key_signature = ""
    shared.sequencer_specific = ""


def parse_midi_file(filedata):
    global busyCursor, preBusyCursors, busyWidgets

    delete_list_items()
    cntr = 0
    shared.tracks = []
    shared.miditype = filedata.type
    for i, track in enumerate(filedata.tracks):
        for msg in track:
            if msg.is_meta:
                mesg = str(msg)
                mesg = mesg[11:]
                if "track_name" in mesg:
                    pos = mesg.find("name=") + 6
                    pos2 = mesg.find("'", pos + 1)
                    # print(f"{pos},{pos2}")
                    tn = mesg[pos:pos2]
                    if _debug:
                        print(f"Track: {i} Name: {tn}")
                    trackinfo = [i, tn]
                    shared.tracks.append(trackinfo)
                elif "end_of_track" in mesg:
                    pass
                    # print(f"Track: {i} ENDOFTRACK")
                elif "number" in mesg:
                    if _debug:
                        print(f"Track: {i} number")
                elif "text" in mesg:
                    pass
                    # if _debug:
                    #     print(f"Track: {i} text")
                elif "copyright" in mesg:
                    if _debug:
                        print(f"Track: {i} copyright")
                elif "instrument_name" in mesg:
                    if _debug:
                        print(f"Track: {i} instrument")
                elif "lyrics" in mesg:
                    if _debug:
                        print(f"Track: {i} lyrics")
                elif "marker" in mesg:
                    if _debug:
                        print(f"Track: {i} marker")
                elif "cue_marker" in mesg:
                    if _debug:
                        print(f"Track: {i} cue marker")
                elif "device_name" in mesg:
                    if _debug:
                        print(f"Track: {i} device")
                elif "channel_prefix" in mesg:
                    if _debug:
                        print(f"Track: {i} channel prefix")
                elif "midi_port" in mesg:
                    if _debug:
                        print(f"Track: {i} midi port")
                elif "set_tempo" in mesg:
                    # Tempo is in microseconds per beat (quarter note). You can use
                    # :py:func:`bpm2tempo` and :py:func:`tempo2bpm` to convert to and from
                    # beats per minute. Note that :py:func:`tempo2bpm` may return a floating
                    # point number.
                    pos1 = mesg.find("tempo=") + 6
                    pos2 = mesg.find(",", pos1)
                    tempo = mesg[pos1:pos2]
                    timesig = (4, 4)
                    # print(f"tempo={tempo} - timesig={timesig}")
                    bpm = int(mido.midifiles.tempo2bpm(int(tempo)))
                    if _debug:
                        print(f"Track: {i} - tempo: {bpm}")
                    shared.tempo = bpm
                elif "smpte_offset" in mesg:
                    pass
                    # print(f"Track: {i} smpte offset")
                elif "time_signature" in mesg:
                    pos1 = mesg.find("numerator=") + 10
                    pos2 = mesg.find(",", pos1)
                    pos3 = mesg.find("denominator=") + 12
                    pos4 = mesg.find(",", pos3)
                    # print(f"{pos1}-{pos2} = {pos3}-{pos4}")
                    num = mesg[pos1:pos2]
                    denom = mesg[pos3:pos4]
                    tsig = f"{num}/{denom}"
                    if _debug:
                        print(f"Track: {i} - Time Sig: {tsig}")
                    shared.time_signature = tsig
                elif "key_signature" in mesg:
                    pos1 = mesg.find("key='") + 5
                    pos2 = mesg.find("'", pos1)
                    # print(f"{pos1}-{pos2}")
                    keysig = mesg[pos1:pos2]
                    if _debug:
                        print(f"Track: {i} key_sig: {keysig}")
                    shared.key_signature = keysig
                elif "sequencer_specific" in mesg:
                    if _debug:
                        print("")
                    # print(f"Track: {i} seq specific")
                else:
                    if _debug:
                        print(f"Track: {i} unknown message")


def print_ports(heading, port_names):
    print(heading)
    for name in port_names:
        print(f"    '{name}'")
    print()


def ports():
    print()
    print_ports("Available input Ports:", mido.get_input_names())
    print_ports("Available output Ports:", mido.get_output_names())

    for name in [
        "MIDO_DEFAULT_INPUT",
        "MIDO_DEFAULT_OUTPUT",
        "MIDO_DEFAULT_IOPORT",
        "MIDO_BACKEND",
    ]:
        try:
            value = os.environ[name]
            print(f"{name}={value!r}")
        except LookupError:
            print(f"{name} not set.")
    print()
    print(f"Using backend {mido.backend.name}.")
    print()


def play_midi(filename):
    sound_font = "/usr/share/sounds/sf2/FluidR3_GM.sf2"
    subprocess.call(
        [
            "fluidsynth",
            "-a",
            "alsa",
            "-m",
            "alsa_seq",
            "-i",
            "-g",
            "0.2",
            sound_font,
            filename,
            "-r",
            "44100",
        ]
    )


def on_btnPlay(*args):
    global filename
    if _debug:
        print("MidiInfo_support.on_btnPlay")
        for arg in args:
            print("    another arg:", arg)
        sys.stdout.flush()
    play_midi(filename)


def centre_screen(wid, hei):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws / 2) - (wid / 2)
    y = (hs / 2) - (hei / 2)
    root.geometry("%dx%d+%d+%d" % (wid, hei, x, y))


def set_icon():
    # ======================================================
    # Sets the application icon...
    # ======================================================
    global progImagesPath
    img = os.path.join(location, "graphics", "midifile.png")
    shared.p1 = tk.PhotoImage(file=img)
    root.tk.call("wm", "iconphoto", root._w, shared.p1)


def show_program_info():

    global version
    pv = platform.python_version()
    print(f"Running under Python {pv}")

    print(location)
    print(f"Version: {version}")


def busyStart(newcursor=None):
    global preBusyCursors

    if not newcursor:
        newcursor = busyCursor
    newPreBusyCursors = {}
    for component in busyWidgets:
        newPreBusyCursors[component] = component["cursor"]
        component.configure(cursor=newcursor)
        component.update_idletasks()
    preBusyCursors = (newPreBusyCursors, preBusyCursors)


def busyEnd():
    global preBusyCursors

    if not preBusyCursors:
        return
    oldPreBusyCursors = preBusyCursors[0]
    preBusyCursors = preBusyCursors[1]
    for component in busyWidgets:
        try:
            component.configure(cursor=oldPreBusyCursors[component])
        except KeyError:
            pass
        component.update_idletasks()


if __name__ == "__main__":
    MidiInfo.start_up()