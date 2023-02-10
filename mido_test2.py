import sys
import os
import subprocess
import mido
from mido import MidiFile, Message, tempo2bpm
from midi2audio import FluidSynth

# from mido.midifiles.meta import MetaSpec
import shared


def work_it():
    ports()
    filename = "cantaloop.mid"
    mid = MidiFile(filename)
    # mid = mido.MidiFile("Fantasy.mid")
    # mid = mido.MidiFile("Bob_Seger_Turn_The_Page.mid")
    # mid = mido.MidiFile("cantaloop.mid")
    # mid = mido.MidiFile("MARS11-1.mid")
    # mid = mido.MidiFile("Moondance.mid")

    # mid = mido.MidiFile("Fantasy.mid")
    # mid = mido.MidiFile("Bob_Seger_Turn_The_Page.mid")
    # mid = mido.MidiFile("cantaloop.mid")
    # mid = mido.MidiFile("MARS11-1.mid")
    # mid = mido.MidiFile("Moondance.mid")

    outport = "TiMidity:TiMidity port 0 128:0"
    setup_vars()

    parse_midi_file2(mid)
    print(f"{shared.tempo=}")
    print(f"{shared.time_signature=}")
    print(f"{shared.key_signature=}")
    print(f"{shared.tracks}")
    songlength = mid.length
    print(f"Song length: {int(songlength/60)} minutes, {int(songlength%60)} seconds.")
    sound_font = "FluidR3_GM.sf2"
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
    # FluidSynth("FluidR3_GM.sf2")
    # FluidSynth().play_midi(filename)


def setup_vars():
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


def parse_midi_file2(filedata):
    cntr = 0
    miditype = filedata.type
    print(f"{miditype=}")
    for i, track in enumerate(filedata.tracks):
        for msg in track:
            if msg.is_meta:
                mesg = str(msg)
                if msg.type == "key_signature":
                    print(msg)


def parse_midi_file(filedata):
    cntr = 0
    for i, track in enumerate(filedata.tracks):
        for msg in track:
            if msg.is_meta:
                mesg = str(msg)
                mesg = mesg[11:]
                # print(mesg)
                if "track_name" in mesg:
                    pos = mesg.find("name=") + 6
                    pos2 = mesg.find("'", pos + 1)
                    # print(f"{pos},{pos2}")
                    tn = mesg[pos:pos2]
                    print(f"Track: {i} Name: {tn}")
                    trackinfo = [i, tn]
                    shared.tracks.append(trackinfo)
                elif "end_of_track" in mesg:
                    pass
                    # print(f"Track: {i} ENDOFTRACK")
                elif "number" in mesg:
                    print(f"Track: {i} number")
                elif "text" in mesg:
                    print(f"Track: {i} text")
                elif "copyright" in mesg:
                    print(f"Track: {i} copyright")
                elif "instrument_name" in mesg:
                    print(f"Track: {i} instrument")
                elif "lyrics" in mesg:
                    pass
                    # print(f"Track: {i} lyrics")
                elif "marker" in mesg:
                    pass
                    # print(f"Track: {i} marker")
                elif "cue_marker" in mesg:
                    pass
                    # print(f"Track: {i} cue marker")
                elif "device_name" in mesg:
                    pass
                    # print(f"Track: {i} device")
                elif "channel_prefix" in mesg:
                    pass
                    # print(f"Track: {i} channel prefix")
                elif "midi_port" in mesg:
                    pass
                    # print(f"Track: {i} midi port")
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
                    print(f"Track: {i} - Time Sig: {tsig}")
                    shared.time_signature = tsig
                elif "key_signature" in mesg:
                    pos1 = mesg.find("key='") + 5
                    pos2 = mesg.find("'", pos1)
                    # print(f"{pos1}-{pos2}")
                    keysig = mesg[pos1:pos2]
                    print(f"Track: {i} key_sig: {keysig}")
                    shared.key_signature = keysig
                elif "sequencer_specific" in mesg:
                    pass
                    # print("")
                    # print(f"Track: {i} seq specific")
                else:
                    print(f"Track: {i} unknown message")
            cntr += 1


def play_file(output, filename, print_messages):
    midi_file = MidiFile(filename)

    print(f"Playing {midi_file.filename}.")
    length = midi_file.length
    print(
        "Song length: {} minutes, {} seconds.".format(
            int(length / 60), int(length % 60)
        )
    )
    print("Tracks:")
    for i, track in enumerate(midi_file.tracks):
        print(f"  {i:2d}: {track.name.strip()!r}")

    for message in midi_file.play(meta_messages=True):
        if print_messages:
            sys.stdout.write(repr(message) + "\n")
            sys.stdout.flush()

        if isinstance(message, Message):
            output.send(message)
        elif message.type == "set_tempo":
            print("Tempo changed to {:.1f} BPM.".format(tempo2bpm(message.tempo)))

    print()


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


if __name__ == "__main__":
    work_it()
