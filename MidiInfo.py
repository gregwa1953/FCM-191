#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#    Feb 10, 2023 04:44:22 AM CST  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_script = sys.argv[0]
_location = os.path.dirname(_script)

import MidiInfo_support

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = 'gray40' # X11 color: #666666
_ana1color = '#c3c3c3' # Closest X11 color: 'gray76'
_ana2color = 'beige' # X11 color: #f5f5dc
_tabfg1 = 'black' 
_tabfg2 = 'black' 
_tabbg1 = 'grey75' 
_tabbg2 = 'grey89' 
_bgmode = 'light' 
font10 = "-family {DejaVu Sans} -size 10"

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran:
       return
    style = ttk.Style()
    if sys.platform == "win32":
       style.theme_use('winnative')
    style.configure('.',background=_bgcolor)
    style.configure('.',foreground=_fgcolor)
    style.configure('.',font='-family {DejaVu Sans} -size 10')
    style.map('.',background =
       [('selected', _compcolor), ('active',_ana2color)])
    if _bgmode == 'dark':
       style.map('.',foreground =
         [('selected', 'white'), ('active','white')])
    else:
       style.map('.',foreground =
         [('selected', 'black'), ('active','black')])
    style.configure('Vertical.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    style.configure('Horizontal.TScrollbar',  background=_bgcolor,
        arrowcolor= _fgcolor)
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("718x438+552+276")
        top.minsize(1, 1)
        top.maxsize(2545, 1410)
        top.resizable(0,  0)
        top.title("MidiInfo")
        top.configure(highlightcolor="black")

        self.top = top
        self.Songlength = tk.StringVar()
        self.TimeSignature = tk.StringVar()
        self.KeySignature = tk.StringVar()
        self.Tempo = tk.StringVar()
        self.MidiFileType = tk.StringVar()
        self.listdata = tk.StringVar()

        _style_code()
        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(x=3, y=5, height=55, width=705)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")
        self.TButton1 = ttk.Button(self.TFrame1)
        self.TButton1.place(x=653, y=2, height=38, width=38)
        self.TButton1.configure(command=MidiInfo_support.on_btnExit)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Tbutton''')
        photo_location = os.path.join(_location,"./graphics/system-shutdown.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.TButton1.configure(image=_img0)
        self.TButton1.configure(compound='none')
        self.TButton1.configure(style='Toolbutton')
        self.TButton1_tooltip = \
        ToolTip(self.TButton1, '''Exit''')

        self.TButton2 = ttk.Button(self.TFrame1)
        self.TButton2.place(x=10, y=2, height=38, width=38)
        self.TButton2.configure(command=MidiInfo_support.on_btnOpen)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Tbutton''')
        photo_location = os.path.join(_location,"./graphics/document-open.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.TButton2.configure(image=_img1)
        self.TButton2.configure(compound='none')
        self.TButton2.configure(style='Toolbutton')
        self.TButton2_tooltip = \
        ToolTip(self.TButton2, '''Open a MIDI file''')

        self.TButton3 = ttk.Button(self.TFrame1)
        self.TButton3.place(x=591, y=2, height=43, width=43)
        self.TButton3.configure(command=MidiInfo_support.on_btnAbout)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Tbutton''')
        photo_location = os.path.join(_location,"./graphics/information.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.TButton3.configure(image=_img2)
        self.TButton3.configure(compound='none')
        self.TButton3.configure(style='Toolbutton')
        self.TButton3_tooltip = \
        ToolTip(self.TButton3, '''Information''')

        self.TButton4 = ttk.Button(self.TFrame1)
        self.TButton4.place(x=290, y=2, height=38, width=38)
        self.TButton4.configure(command=MidiInfo_support.on_btnPlay)
        self.TButton4.configure(takefocus="")
        self.TButton4.configure(text='''Play''')
        photo_location = os.path.join(_location,"./graphics/go-next.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.TButton4.configure(image=_img3)
        self.TButton4.configure(compound='none')
        self.TButton4.configure(style='Toolbutton')
        self.TButton4_tooltip = \
        ToolTip(self.TButton4, '''Try to play the midi file''')

        self.TLabel1 = ttk.Label(self.top)
        self.TLabel1.place(x=20, y=90, height=19, width=202)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Tracks:''')
        self.TLabel1.configure(compound='left')
        self.Scrolledlistbox1 = ScrolledListBox(self.top)
        self.Scrolledlistbox1.place(x=20, y=120, height=288, width=266)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(cursor="xterm")
        self.Scrolledlistbox1.configure(exportselection="0")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(listvariable=self.listdata)
        self.TLabel2 = ttk.Label(self.top)
        self.TLabel2.place(x=410, y=100, height=19, width=112)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='e')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Song Length:''')
        self.TLabel2.configure(compound='left')
        self.TLabel3 = ttk.Label(self.top)
        self.TLabel3.place(x=540, y=100, height=19, width=162)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Key Signature:''')
        self.TLabel3.configure(textvariable=self.Songlength)
        self.Songlength.set('''Key Signature:''')
        self.TLabel3.configure(compound='left')
        self.TLabel4 = ttk.Label(self.top)
        self.TLabel4.place(x=540, y=130, height=19, width=152)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Key Signature:''')
        self.TLabel4.configure(textvariable=self.TimeSignature)
        self.TimeSignature.set('''Key Signature:''')
        self.TLabel4.configure(compound='left')
        self.TLabel5 = ttk.Label(self.top)
        self.TLabel5.place(x=390, y=130, height=19, width=132)
        self.TLabel5.configure(background="#d9d9d9")
        self.TLabel5.configure(foreground="#000000")
        self.TLabel5.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor='e')
        self.TLabel5.configure(justify='left')
        self.TLabel5.configure(text='''Time Signature:''')
        self.TLabel5.configure(compound='left')
        self.TLabel6 = ttk.Label(self.top)
        self.TLabel6.place(x=380, y=160, height=19, width=142)
        self.TLabel6.configure(background="#d9d9d9")
        self.TLabel6.configure(foreground="#000000")
        self.TLabel6.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(anchor='e')
        self.TLabel6.configure(justify='left')
        self.TLabel6.configure(text='''Key Signature:''')
        self.TLabel6.configure(compound='left')
        self.TLabel7 = ttk.Label(self.top)
        self.TLabel7.place(x=540, y=160, height=19, width=162)
        self.TLabel7.configure(background="#d9d9d9")
        self.TLabel7.configure(foreground="#000000")
        self.TLabel7.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(anchor='w')
        self.TLabel7.configure(justify='left')
        self.TLabel7.configure(text='''Key Signature:''')
        self.TLabel7.configure(textvariable=self.KeySignature)
        self.KeySignature.set('''Key Signature:''')
        self.TLabel7.configure(compound='left')
        self.TLabel8 = ttk.Label(self.top)
        self.TLabel8.place(x=360, y=190, height=19, width=162)
        self.TLabel8.configure(background="#d9d9d9")
        self.TLabel8.configure(foreground="#000000")
        self.TLabel8.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TLabel8.configure(relief="flat")
        self.TLabel8.configure(anchor='e')
        self.TLabel8.configure(justify='left')
        self.TLabel8.configure(text='''Tempo:''')
        self.TLabel8.configure(compound='left')
        self.TLabel9 = ttk.Label(self.top)
        self.TLabel9.place(x=540, y=190, height=19, width=132)
        self.TLabel9.configure(background="#d9d9d9")
        self.TLabel9.configure(foreground="#000000")
        self.TLabel9.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel9.configure(relief="flat")
        self.TLabel9.configure(anchor='w')
        self.TLabel9.configure(justify='left')
        self.TLabel9.configure(text='''Tempo:''')
        self.TLabel9.configure(textvariable=self.Tempo)
        self.Tempo.set('''Tempo:''')
        self.TLabel9.configure(compound='left')
        self.TLabel11 = ttk.Label(self.top)
        self.TLabel11.place(x=540, y=220, height=19, width=62)
        self.TLabel11.configure(background="#d9d9d9")
        self.TLabel11.configure(foreground="#000000")
        self.TLabel11.configure(font="-family {DejaVu Sans} -size 10")
        self.TLabel11.configure(relief="flat")
        self.TLabel11.configure(anchor='w')
        self.TLabel11.configure(justify='left')
        self.TLabel11.configure(text='''Tlabel''')
        self.TLabel11.configure(textvariable=self.MidiFileType)
        self.MidiFileType.set('''Tlabel''')
        self.TLabel11.configure(compound='left')
        self.TLabel10 = ttk.Label(self.top)
        self.TLabel10.place(x=380, y=220, height=19, width=142)
        self.TLabel10.configure(background="#d9d9d9")
        self.TLabel10.configure(foreground="#000000")
        self.TLabel10.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TLabel10.configure(relief="flat")
        self.TLabel10.configure(anchor='e')
        self.TLabel10.configure(justify='left')
        self.TLabel10.configure(text='''Midi File Type:''')
        self.TLabel10.configure(compound='left')

from time import time, localtime, strftime
class ToolTip(tk.Toplevel):
    """ Provides a ToolTip widget for Tkinter. """
    def __init__(self, wdgt, msg=None, msgFunc=None, delay=0.5,
                 follow=True):
        self.wdgt = wdgt
        self.parent = self.wdgt.master
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        self.withdraw()
        self.overrideredirect(True)
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        self.msg = tk.Message(self, textvariable=self.msgVar, bg=_bgcolor,
                   fg=_fgcolor, font="TkDefaultFont",
                   aspect=1000)
        self.msg.grid()
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')
    def spawn(self, event=None):
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)
    def show(self):
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()
    def move(self, event):
        self.lastMotion = time()
        if self.follow is False:
            self.withdraw()
            self.visible = 1
        self.geometry('+%i+%i' % (event.x_root + 20, event.y_root - 10))
        try:
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)
    def hide(self, event=None):
        self.visible = 0
        self.withdraw()
    def update(self, msg):
        self.msgVar.set(msg)
    def configure(self, **kwargs):
        backgroundset = False
        foregroundset = False
        # Get the current tooltip text just in case the user doesn't provide any.
        current_text = self.msgVar.get()
        # to clear the tooltip text, use the .update method
        if 'debug' in kwargs.keys():
            debug = kwargs.pop('debug', False)
            if debug:
                for key, value in kwargs.items():
                    print(f'key: {key} - value: {value}')
        if 'background' in kwargs.keys():
            background = kwargs.pop('background')
            backgroundset = True
        if 'bg' in kwargs.keys():
            background = kwargs.pop('bg')
            backgroundset = True
        if 'foreground' in kwargs.keys():
            foreground = kwargs.pop('foreground')
            foregroundset = True
        if 'fg' in kwargs.keys():
            foreground = kwargs.pop('fg')
            foregroundset = True

        fontd = kwargs.pop('font', None)
        if 'text' in kwargs.keys():
            text = kwargs.pop('text')
            if (text == '') or (text == "\n"):
                text = current_text
            else:
                self.msgVar.set(text)
        reliefd = kwargs.pop('relief', 'flat')
        justifyd = kwargs.pop('justify', 'left')
        padxd = kwargs.pop('padx', 1)
        padyd = kwargs.pop('pady', 1)
        borderwidthd = kwargs.pop('borderwidth', 2)
        wid = self.msg      # The message widget which is the actual tooltip
        if backgroundset:
            wid.config(bg=background)
        if foregroundset:
            wid.config(fg=foreground)
        wid.config(font=fontd)
        wid.config(borderwidth=borderwidthd)
        wid.config(relief=reliefd)
        wid.config(justify=justifyd)
        wid.config(padx=padxd)
        wid.config(pady=padyd)
#                   End of Class ToolTip

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')
def start_up():
    MidiInfo_support.main()

if __name__ == '__main__':
    MidiInfo_support.main()



