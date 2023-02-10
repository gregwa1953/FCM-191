#############################################################################
# Generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#  Feb 10, 2023 04:47:45 AM CST  platform: Linux
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
    system_shutdown_png "./graphics/system-shutdown.png" 
    document_open_png "./graphics/document-open.png" 
    information_png "./graphics/information.png" 
    go_next_png "./graphics/go-next.png" 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {DejaVu Sans} -size 10"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #d9d9d9
set vTcl(actual_gui_menu_analog) #d9d9d9
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #d9d9d9
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 0
set vTcl(mode) Absolute
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 718x438+552+276
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 2545 1410
    wm minsize $top 1 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "MidiInfo"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::style configure TFrame -foreground $vTcl(actual_gui_fg)
    ttk::style configure TFrame -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TFrame -background $vTcl(actual_gui_bg)
    ttk::frame "$top.tFr47" \
        -borderwidth 2 -relief groove -width 705 -height 55 
    vTcl:DefineAlias "$top.tFr47" "TFrame1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.tFr47
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button "$site_3_0.tBu48" \
        -command "on_btnExit" -takefocus {} -text "Tbutton" \
        -image system_shutdown_png -compound none -style "Toolbutton" \
        -style Toolbutton 
    vTcl:DefineAlias "$site_3_0.tBu48" "TButton1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    bind $site_3_0.tBu48 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Exit}
    }
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button "$site_3_0.tBu49" \
        -command "on_btnOpen" -takefocus {} -text "Tbutton" \
        -image document_open_png -compound none -style "Toolbutton" \
        -style Toolbutton 
    vTcl:DefineAlias "$site_3_0.tBu49" "TButton2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    bind $site_3_0.tBu49 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Open a MIDI file}
    }
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button "$site_3_0.tBu50" \
        -command "on_btnAbout" -takefocus {} -text "Tbutton" \
        -image information_png -compound none -style "Toolbutton" \
        -style Toolbutton 
    vTcl:DefineAlias "$site_3_0.tBu50" "TButton3" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    bind $site_3_0.tBu50 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Information}
    }
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button "$site_3_0.tBu47" \
        -command "on_btnPlay" -takefocus {} -text "Play" -image go_next_png \
        -compound none -style "Toolbutton" -style Toolbutton 
    vTcl:DefineAlias "$site_3_0.tBu47" "TButton4" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    bind $site_3_0.tBu47 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Try to play the midi file}
    }
    place $site_3_0.tBu48 \
        -in $site_3_0 -x 653 -y 2 -width 38 -relwidth 0 -height 38 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu49 \
        -in $site_3_0 -x 10 -y 2 -anchor nw -bordermode ignore 
    place $site_3_0.tBu50 \
        -in $site_3_0 -x 591 -y 2 -width 43 -relwidth 0 -height 43 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tBu47 \
        -in $site_3_0 -x 290 -y 2 -anchor nw -bordermode ignore 
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa51" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -relief flat -anchor w -justify left -text "Tracks:" -compound left 
    vTcl:DefineAlias "$top.tLa51" "TLabel1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::style configure Scrolledlistbox -background $vTcl(actual_gui_bg)
    ttk::style configure Scrolledlistbox -foreground $vTcl(actual_gui_fg)
    ttk::style configure Scrolledlistbox -font "$vTcl(actual_gui_font_dft_desc)"
    vTcl::widgets::ttk::scrolledlistbox::CreateCmd "$top.scr52" \
        -background $vTcl(actual_gui_bg) -height 75 -highlightcolor black \
        -width 125 
    vTcl:DefineAlias "$top.scr52" "Scrolledlistbox1" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A

    $top.scr52.01 configure -background white \
        -cursor xterm \
        -exportselection 0 \
        -font TkFixedFont \
        -foreground black \
        -height 3 \
        -highlightcolor #d9d9d9 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -listvariable listdata
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa53" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -relief flat -anchor e -justify left -text "Song Length:" \
        -compound left 
    vTcl:DefineAlias "$top.tLa53" "TLabel2" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa54" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10" -relief flat -anchor w \
        -justify left -text "Key Signature:" -textvariable "::Songlength" \
        -compound left 
    vTcl:DefineAlias "$top.tLa54" "TLabel3" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set ::Songlength {Key Signature:}
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa55" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10" -relief flat -anchor w \
        -justify left -text "Key Signature:" -textvariable "::TimeSignature" \
        -compound left 
    vTcl:DefineAlias "$top.tLa55" "TLabel4" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set ::TimeSignature {Key Signature:}
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa56" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -relief flat -anchor e -justify left -text "Time Signature:" \
        -compound left 
    vTcl:DefineAlias "$top.tLa56" "TLabel5" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa57" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -relief flat -anchor e -justify left -text "Key Signature:" \
        -compound left 
    vTcl:DefineAlias "$top.tLa57" "TLabel6" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa58" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10" -relief flat -anchor w \
        -justify left -text "Key Signature:" -textvariable "::KeySignature" \
        -compound left 
    vTcl:DefineAlias "$top.tLa58" "TLabel7" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set ::KeySignature {Key Signature:}
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa59" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -relief flat -anchor e -justify left -text "Tempo:" -compound left 
    vTcl:DefineAlias "$top.tLa59" "TLabel8" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa60" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10" -relief flat -anchor w \
        -justify left -text "Tempo:" -textvariable "::Tempo" -compound left 
    vTcl:DefineAlias "$top.tLa60" "TLabel9" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set ::Tempo {Tempo:}
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa48" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10" -relief flat -anchor w \
        -justify left -text "Tlabel" -textvariable "::MidiFileType" \
        -compound left 
    vTcl:DefineAlias "$top.tLa48" "TLabel11" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    set ::MidiFileType {Tlabel}
    ttk::style configure TLabel -background $vTcl(actual_gui_bg)
    ttk::style configure TLabel -foreground $vTcl(actual_gui_fg)
    ttk::style configure TLabel -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::label "$top.tLa49" \
        -background $vTcl(actual_gui_bg) -foreground $vTcl(actual_gui_fg) \
        -font "-family {DejaVu Sans} -size 10 -weight bold -slant roman -underline 0 -overstrike 0" \
        -relief flat -anchor e -justify left -text "Midi File Type:" \
        -compound left 
    vTcl:DefineAlias "$top.tLa49" "TLabel10" vTcl:WidgetProc "Toplevel1" 1
### SPOT dump_widget_opt A
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.tFr47 \
        -in $top -x 3 -y 5 -width 705 -relwidth 0 -height 55 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa51 \
        -in $top -x 20 -y 90 -width 202 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.scr52 \
        -in $top -x 20 -y 120 -width 266 -relwidth 0 -height 288 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa53 \
        -in $top -x 410 -y 100 -width 112 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa54 \
        -in $top -x 540 -y 100 -width 162 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa55 \
        -in $top -x 540 -y 130 -width 152 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa56 \
        -in $top -x 390 -y 130 -width 132 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa57 \
        -in $top -x 380 -y 160 -width 142 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa58 \
        -in $top -x 540 -y 160 -width 162 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa59 \
        -in $top -x 360 -y 190 -width 162 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa60 \
        -in $top -x 540 -y 190 -width 132 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa48 \
        -in $top -x 540 -y 220 -width 62 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tLa49 \
        -in $top -x 380 -y 220 -width 142 -relwidth 0 -height 19 -relheight 0 \
        -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

