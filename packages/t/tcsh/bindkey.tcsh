#
# bindkey.tcsh		Bind keys on escape sequences of xterm
#			and linux console
#
# Copyright: 1993-2007 Werner Fink, 1996-2002 SuSE Linux AG, Germany
# Copyright: 2007 SuSE  LINUX Products GmbH, Nuernberg, Germany.
#
# Author:  Werner Fink <feedback@suse.de>

#
# Default values
#
if ( ! ${?TERM} ) setenv TERM linux
if ( ! ${?CSHEDIT} ) setenv CSHEDIT emacs

#
# VI line editing
#
if ( "$CSHEDIT" == "vi" ) then
	bindkey    -v
else
	bindkey    "^[ "	magic-space
	bindkey    "^[!"	expand-history
endif
#
# Common standard keypad and cursor
#
bindkey    "^[[1~"		beginning-of-line
bindkey    "^[[2~"		yank
bindkey    "^[[3~"		delete-char
bindkey    "^[[4~"		end-of-line
bindkey    "^[[5~"		history-search-backward
bindkey    "^[[6~"		history-search-forward
bindkey -r "\233"
bindkey    "\2331~"		beginning-of-line
bindkey    "\2332~"		yank
bindkey    "\2333~"		delete-char
bindkey    "\2334~"		end-of-line
bindkey    "\2335~"		history-search-backward
bindkey    "\2336~"		history-search-forward
if ( "$TERM" =~ xterm* ) then
	bindkey    "^[[2;2~"	yank
	bindkey    "^[[3;2~"	delete-char
	bindkey    "^[[5;2~"	history-search-backward
	bindkey    "^[[6;2~"	history-search-forward
	bindkey    "^[[2;3~"	yank
	bindkey    "^[[3;3~"	delete-char
	bindkey    "^[[5;3~"	history-search-backward
	bindkey    "^[[6;3~"	history-search-forward
	bindkey    "^[[2;4~"	yank
	bindkey    "^[[3;4~"	delete-char
	bindkey    "^[[5;4~"	history-search-backward
	bindkey    "^[[6;4~"	history-search-forward
	bindkey    "^[[2;5~"	yank
	bindkey    "^[[3;5~"	delete-char
	bindkey    "^[[5;5~"	history-search-backward
	bindkey    "^[[6;5~"	history-search-forward
	bindkey    "^[[2;6~"	yank
	bindkey    "^[[3;6~"	delete-char
	bindkey    "^[[5;6~"	history-search-backward
	bindkey    "^[[6;6~"	history-search-forward
	bindkey    "^[[2;7~"	yank
	bindkey    "^[[3;7~"	delete-char
	bindkey    "^[[5;7~"	history-search-backward
	bindkey    "^[[6;7~"	history-search-forward
	bindkey    "^[[2;8~"	yank
	bindkey    "^[[3;8~"	delete-char
	bindkey    "^[[5;8~"	history-search-backward
	bindkey    "^[[6;8~"	history-search-forward
endif
bindkey    "^[[C"		forward-char
bindkey    "^[[D"		backward-char
bindkey    "^[[A"		up-history
bindkey    "^[[B"		down-history
bindkey -r "\217"
bindkey    "\217C"		forward-char
bindkey    "\217D"		backward-char
bindkey    "\217A"		up-history
bindkey    "\217B"		down-history
bindkey    "\233C"		forward-char
bindkey    "\233D"		backward-char
bindkey    "\233A"		up-history
bindkey    "\233B"		down-history
#
# Cursor keys in keypad mode
#
bindkey    "^C[OC"		forward-char
bindkey    "^C[OD"		backward-char
bindkey    "^C[OA"		up-history
bindkey    "^C[OB"		down-history
#
# Cursor keys in ANSI mode
#
bindkey    "^C[[C"		forward-char
bindkey    "^C[[D"		backward-char
bindkey    "^C[[A"		up-history
bindkey    "^C[[B"		down-history
#
# Cursor keys in 8 bit keypad mode
#
bindkey    "^C^MOC"		forward-char
bindkey    "^C^MOD"		backward-char
bindkey    "^C^MOA"		up-history
bindkey    "^C^MOB"		down-history
#
# Cursor keys in 8 bit ANSI mode
#
bindkey    "^C^M[C"		forward-char
bindkey    "^C^M[D"		backward-char
bindkey    "^C^M[A"		up-history
bindkey    "^C^M[B"		down-history
bindkey    "^C^[[D"		backward-char
#
if ( "$TERM" =~ xterm* ) then
	bindkey -c "^[[E"	"source /etc/csh.cshrc"
	bindkey -c "^[[1;2E"	"source /etc/csh.cshrc"
	bindkey -c "^[[1;3E"	"source /etc/csh.cshrc"
	bindkey -c "^[[1;4E"	"source /etc/csh.cshrc"
	bindkey -c "^[[1;5E"	"source /etc/csh.cshrc"
	bindkey -c "^[[1;6E"	"source /etc/csh.cshrc"
	bindkey -c "^[[1;7E"	"source /etc/csh.cshrc"
	bindkey -c "^[[1;8E"	"source /etc/csh.cshrc"
	bindkey    "^[[2C"	forward-word
	bindkey    "^[[2D"	backward-word
	bindkey    "^[[2A"	history-search-backward
	bindkey    "^[[2B"	history-search-forward
	bindkey    "^[[1;2C"    forward-word
	bindkey    "^[[1;2D"    backward-word
	bindkey    "^[[1;2A"    history-search-backward
	bindkey    "^[[1;2B"    history-search-forward
	bindkey    "^[[1;3C"    forward-word
	bindkey    "^[[1;3D"    backward-word
	bindkey    "^[[1;3A"    history-search-backward
	bindkey    "^[[1;3B"    history-search-forward
	bindkey    "^[[1;4C"    forward-word
	bindkey    "^[[1;4D"    backward-word
	bindkey    "^[[1;4A"    history-search-backward
	bindkey    "^[[1;4B"    history-search-forward
	bindkey    "^[[5C"	forward-word
	bindkey    "^[[5D"	backward-word
	bindkey    "^[[5A"	history-search-backward
	bindkey    "^[[5B"	history-search-forward
	bindkey    "^[[1;5C"    forward-word
	bindkey    "^[[1;5D"    backward-word
	bindkey    "^[[1;5A"    history-search-backward
	bindkey    "^[[1;5B"    history-search-forward
	bindkey    "^[[1;6C"    forward-word
	bindkey    "^[[1;6D"    backward-word
	bindkey    "^[[1;6A"    history-search-backward
	bindkey    "^[[1;6B"    history-search-forward
	bindkey    "^[[1;7C"    forward-word
	bindkey    "^[[1;7D"    backward-word
	bindkey    "^[[1;7A"    history-search-backward
	bindkey    "^[[1;7B"    history-search-forward
	bindkey    "^[[1;8C"    forward-word
	bindkey    "^[[1;8D"    backward-word
	bindkey    "^[[1;8A"    history-search-backward
	bindkey    "^[[1;8B"    history-search-forward

	bindkey    "\2332C"	forward-word
	bindkey    "\2332D"	backward-word
	bindkey    "\2332A"	history-search-backward
	bindkey    "\2332B"	history-search-forward
	bindkey    "\2331;2C"   forward-word
	bindkey    "\2331;2D"   backward-word
	bindkey    "\2331;2A"   history-search-backward
	bindkey    "\2331;2B"   history-search-forward
	bindkey    "\2331;3C"   forward-word
	bindkey    "\2331;3D"   backward-word
	bindkey    "\2331;3A"   history-search-backward
	bindkey    "\2331;3B"   history-search-forward
	bindkey    "\2331;4C"   forward-word
	bindkey    "\2331;4D"   backward-word
	bindkey    "\2331;4A"   history-search-backward
	bindkey    "\2331;4B"   history-search-forward
	bindkey    "\2335C"	forward-word
	bindkey    "\2335D"	backward-word
	bindkey    "\2335A"	history-search-backward
	bindkey    "\2335B"	history-search-forward
	bindkey    "\2331;5C"   forward-word
	bindkey    "\2331;5D"   backward-word
	bindkey    "\2331;5A"   history-search-backward
	bindkey    "\2331;5B"   history-search-forward
	bindkey    "\2331;6C"   forward-word
	bindkey    "\2331;6D"   backward-word
	bindkey    "\2331;6A"   history-search-backward
	bindkey    "\2331;6B"   history-search-forward
	bindkey    "\2331;7C"   forward-word
	bindkey    "\2331;7D"   backward-word
	bindkey    "\2331;7A"   history-search-backward
	bindkey    "\2331;7B"   history-search-forward
	bindkey    "\2331;8C"   forward-word
	bindkey    "\2331;8D"   backward-word
	bindkey    "\2331;8A"   history-search-backward
	bindkey    "\2331;8B"   history-search-forward
else
	bindkey -c "^[[G"	"source /etc/csh.cshrc"
endif
#
# Avoid network problems
#   ... \177 (ASCII-DEL) and \010 (ASCII-BS)
#       do `backward-delete-char'
# Note: `delete-char' is maped to \033[3~
#       Therefore xterm's responce on pressing
#       key Delete or KP-Delete should be
#       \033[3~ ... NOT \177
#
bindkey    "^?"		backward-delete-char
bindkey    "^H"		backward-delete-char
if ( "$TERM" =~ xterm* ) then
	#
	# XTerm in UTF-8 mode
	#
	bindkey    "^[\303\277"	backward-delete-word
	bindkey    "^[ÿ"	backward-delete-word
endif
#
# Home and End
#
if ( "$TERM" =~ xterm* ) then
	#
	# Normal keypad and cursor of xterm
	#
	bindkey    "^[[1~"	history-search-backward
	bindkey    "^[[4~"	set-mark-command
	bindkey    "^[[H"	beginning-of-line
	bindkey    "^[[F"	end-of-line
	bindkey    "^[[1;2H"	beginning-of-line
	bindkey    "^[[1;2F"	end-of-line
	bindkey    "^[[1;3H"	beginning-of-line
	bindkey    "^[[1;3F"	end-of-line
	bindkey    "^[[1;4H"	beginning-of-line
	bindkey    "^[[1;4F"	end-of-line
	bindkey    "^[[1;5H"	beginning-of-line
	bindkey    "^[[1;5F"	end-of-line
	bindkey    "^[[1;6H"	beginning-of-line
	bindkey    "^[[1;6F"	end-of-line
	bindkey    "^[[1;7H"	beginning-of-line
	bindkey    "^[[1;7F"	end-of-line
	bindkey    "^[[1;8H"	beginning-of-line
	bindkey    "^[[1;8F"	end-of-line
	bindkey    "\2331;2H"	beginning-of-line
	bindkey    "\2331;2F"	end-of-line
	bindkey    "\2331;3H"	beginning-of-line
	bindkey    "\2331;3F"	end-of-line
	bindkey    "\2331;4H"	beginning-of-line
	bindkey    "\2331;4F"	end-of-line
	bindkey    "\2331;5H"	beginning-of-line
	bindkey    "\2331;5F"	end-of-line
	bindkey    "\2331;6H"	beginning-of-line
	bindkey    "\2331;6F"	end-of-line
	bindkey    "\2331;7H"	beginning-of-line
	bindkey    "\2331;7F"	end-of-line
	bindkey    "\2331;8H"	beginning-of-line
	bindkey    "\2331;8F"	end-of-line
	bindkey    "^[[2H"	beginning-of-line
	bindkey    "^[[2F"	end-of-line
	bindkey    "^[[5H"	beginning-of-line
	bindkey    "^[[5F"	end-of-line
	# Home and End of application keypad and cursor of xterm
	bindkey    "^[OH"	beginning-of-line
	bindkey    "^[OF"	end-of-line
	bindkey    "^[O2H"	beginning-of-line
	bindkey    "^[O2F"	end-of-line
	bindkey    "^[O5H"	beginning-of-line
	bindkey    "^[O5F"	end-of-line
else
if ( "$TERM" =~ kvt* ) then
	bindkey    "^[[1~"	history-search-backward
	bindkey    "^[[4~"	set-mark-command
	bindkey    "^[OH"	beginning-of-line
	bindkey    "^[OF"	end-of-line
endif
	#
	# TERM=linux or console
	#
	bindkey    "^[[1~"	beginning-of-line
	bindkey    "^[[4~"	end-of-line
endif
#
# Application keypad and cursor of xterm
#
if ( "$TERM" =~ xterm* ) then
	bindkey    "^[OD"	backward-char
	bindkey    "^[OC"	forward-char
	bindkey    "^[OA"	up-history
	bindkey    "^[OB"	down-history
	bindkey -c "^[OE"	"source /etc/csh.cshrc"
	bindkey    "^[O2D"	backward-word
	bindkey    "^[O2C"	forward-word
	bindkey    "^[O2A"	history-search-backward
	bindkey    "^[O2B"	history-search-forward
	bindkey    "^[O3D"	backward-word
	bindkey    "^[O3C"	forward-word
	bindkey    "^[O3A"	history-search-backward
	bindkey    "^[O3B"	history-search-forward
	bindkey    "^[O4D"	backward-word
	bindkey    "^[O4C"	forward-word
	bindkey    "^[O4A"	history-search-backward
	bindkey    "^[O4B"	history-search-forward
	bindkey    "^[O5D"	backward-word
	bindkey    "^[O5C"	forward-word
	bindkey    "^[O5A"	history-search-backward
	bindkey    "^[O5B"	history-search-forward
	bindkey    "^[O6D"	backward-word
	bindkey    "^[O6C"	forward-word
	bindkey    "^[O6A"	history-search-backward
	bindkey    "^[O6B"	history-search-forward
	bindkey    "^[O7D"	backward-word
	bindkey    "^[O7C"	forward-word
	bindkey    "^[O7A"	history-search-backward
	bindkey    "^[O7B"	history-search-forward
	bindkey    "^[O8D"	backward-word
	bindkey    "^[O8C"	forward-word
	bindkey    "^[O8A"	history-search-backward
	bindkey    "^[O8B"	history-search-forward
	# DEC keyboard KP_F1 - KP_F4 or
	# XTerm of XFree86 in VT220 mode F1 - F4
	bindkey -s "^[OP"	"^["
	bindkey    "^[OQ"	vi-undo
	bindkey    "^[OR"	undefined-key
	bindkey    "^[OS"	kill-line
	bindkey -s "^[O2P"	"^["
	bindkey    "^[O2Q"	vi-undo
	bindkey    "^[O2R"	undefined-key
	bindkey    "^[O2S"	kill-line
	bindkey -s "^[O3P"	"^["
	bindkey    "^[O3Q"	vi-undo
	bindkey    "^[O3R"	undefined-key
	bindkey    "^[O3S"	kill-line
	bindkey -s "^[O4P"	"^["
	bindkey    "^[O4Q"	vi-undo
	bindkey    "^[O4R"	undefined-key
	bindkey    "^[O4S"	kill-line
	bindkey -s "^[O5P"	"^["
	bindkey    "^[O5Q"	vi-undo
	bindkey    "^[O5R"	undefined-key
	bindkey    "^[O5S"	kill-line
	bindkey -s "^[O6P"	"^["
	bindkey    "^[O6Q"	vi-undo
	bindkey    "^[O6R"	undefined-key
	bindkey    "^[O6S"	kill-line
	bindkey -s "^[O7P"	"^["
	bindkey    "^[O7Q"	vi-undo
	bindkey    "^[O7R"	undefined-key
	bindkey    "^[O7S"	kill-line
	bindkey -s "^[O8P"	"^["
	bindkey    "^[O8Q"	vi-undo
	bindkey    "^[O8R"	undefined-key
	bindkey    "^[O8S"	kill-line
	bindkey -s "^[O1;2P"	"^["
	bindkey    "^[O1;2Q"	vi-undo
	bindkey    "^[O1;2R"	undefined-key
	bindkey    "^[O1;2S"	kill-line
	bindkey -s "^[O1;3P"	"^["
	bindkey    "^[O1;3Q"	vi-undo
	bindkey    "^[O1;3R"	undefined-key
	bindkey    "^[O1;3S"	kill-line
	bindkey -s "^[O1;4P"	"^["
	bindkey    "^[O1;4Q"	vi-undo
	bindkey    "^[O1;4R"	undefined-key
	bindkey    "^[O1;4S"	kill-line
	bindkey -s "^[O1;5P"	"^["
	bindkey    "^[O1;5Q"	vi-undo
	bindkey    "^[O1;5R"	undefined-key
	bindkey    "^[O1;5S"	kill-line
	bindkey -s "^[O1;6P"	"^["
	bindkey    "^[O1;6Q"	vi-undo
	bindkey    "^[O1;6R"	undefined-key
	bindkey    "^[O1;6S"	kill-line
	bindkey -s "^[O1;7P"	"^["
	bindkey    "^[O1;7Q"	vi-undo
	bindkey    "^[O1;7R"	undefined-key
	bindkey    "^[O1;7S"	kill-line
	bindkey -s "^[O1;8P"	"^["
	bindkey    "^[O1;8Q"	vi-undo
	bindkey    "^[O1;8R"	undefined-key
	bindkey    "^[O1;8S"	kill-line
endif
if ( "$TERM" =~ gnome* ) then
	# or gnome terminal F1 - F4
	bindkey -s "^[OP"	"^["
	bindkey    "^[OQ"	vi-undo
	bindkey    "^[OR"	undefined-key
	bindkey    "^[OS"	kill-line
endif
#
# Function keys F1 - F12
#
if ( "$TERM" =~ linux* ) then
	#
	# On console the first five function keys
	#
	bindkey -s "^[[[A"	"^["
	bindkey    "^[[[B"	vi-undo
	bindkey    "^[[[C"	undefined-key
	bindkey    "^[[[D"	kill-line
	bindkey    "^[[[E"	undefined-key
else
	#
	# The first five standard function keys
	#
	bindkey -s "^[[11~"	"^["
	bindkey    "^[[12~"	vi-undo
	bindkey    "^[[13~"	undefined-key
	bindkey    "^[[14~"	kill-line
	bindkey    "^[[15~"	undefined-key
endif
bindkey    "^[[17~"		undefined-key
bindkey    "^[[18~"		undefined-key
bindkey    "^[[19~"		undefined-key
bindkey    "^[[20~"		undefined-key
bindkey    "^[[21~"		undefined-key
bindkey    "^[[23~"		undefined-key
bindkey    "^[[24~"		undefined-key
bindkey    "^[[25~"		undefined-key
bindkey    "^[[26~"		undefined-key
# DEC keyboard: F15=^[[28~ is Help
bindkey    "^[[28~"		undefined-key
# DEC keyboard: F16=^[[29~ is Menu
bindkey    "^[[29~"		undefined-key
bindkey    "^[[31~"		undefined-key
bindkey    "^[[32~"		undefined-key
bindkey    "^[[33~"		undefined-key
bindkey    "^[[34~"		undefined-key
bindkey    "^[[35~"		undefined-key
bindkey    "^[[36~"		undefined-key
bindkey    "\23317~"		undefined-key
bindkey    "\23318~"		undefined-key
bindkey    "\23319~"		undefined-key
bindkey    "\23320~"		undefined-key
bindkey    "\23321~"		undefined-key
bindkey    "\23323~"		undefined-key
bindkey    "\23324~"		undefined-key
bindkey    "\23325~"		undefined-key
bindkey    "\23326~"		undefined-key
bindkey    "\23328~"		undefined-key
bindkey    "\23329~"		undefined-key
bindkey    "\23331~"		undefined-key
bindkey    "\23332~"		undefined-key
bindkey    "\23333~"		undefined-key
bindkey    "\23334~"		undefined-key
bindkey    "\23335~"		undefined-key
bindkey    "\23336~"		undefined-key
if ( "$TERM" =~ xterm* ) then
	bindkey    "^[[1;2P"	undefined-key
	bindkey    "^[[1;2Q"	undefined-key
	bindkey    "^[[1;2R"	undefined-key
	bindkey    "^[[1;2S"	undefined-key
	bindkey    "^[[15;2~"	undefined-key
	bindkey    "^[[17;2~"	undefined-key
	bindkey    "^[[18;2~"	undefined-key
	bindkey    "^[[19;2~"	undefined-key
	bindkey    "^[[20;2~"	undefined-key
	bindkey    "^[[21;2~"	undefined-key
	bindkey    "^[[23;2~"	undefined-key
	bindkey    "^[[24;2~"	undefined-key
	bindkey    "^[[1;3P"	undefined-key
	bindkey    "^[[1;3Q"	undefined-key
	bindkey    "^[[1;3R"	undefined-key
	bindkey    "^[[1;3S"	undefined-key
	bindkey    "^[[15;3~"	undefined-key
	bindkey    "^[[17;3~"	undefined-key
	bindkey    "^[[18;3~"	undefined-key
	bindkey    "^[[19;3~"	undefined-key
	bindkey    "^[[20;3~"	undefined-key
	bindkey    "^[[21;3~"	undefined-key
	bindkey    "^[[23;3~"	undefined-key
	bindkey    "^[[24;3~"	undefined-key
	bindkey    "^[[1;4P"	undefined-key
	bindkey    "^[[1;4Q"	undefined-key
	bindkey    "^[[1;4R"	undefined-key
	bindkey    "^[[1;4S"	undefined-key
	bindkey    "^[[15;4~"	undefined-key
	bindkey    "^[[17;4~"	undefined-key
	bindkey    "^[[18;4~"	undefined-key
	bindkey    "^[[19;4~"	undefined-key
	bindkey    "^[[20;4~"	undefined-key
	bindkey    "^[[21;4~"	undefined-key
	bindkey    "^[[23;4~"	undefined-key
	bindkey    "^[[24;4~"	undefined-key
	bindkey    "^[[1;5P"	undefined-key
	bindkey    "^[[1;5Q"	undefined-key
	bindkey    "^[[1;5R"	undefined-key
	bindkey    "^[[1;5S"	undefined-key
	bindkey    "^[[15;5~"	undefined-key
	bindkey    "^[[17;5~"	undefined-key
	bindkey    "^[[18;5~"	undefined-key
	bindkey    "^[[19;5~"	undefined-key
	bindkey    "^[[20;5~"	undefined-key
	bindkey    "^[[21;5~"	undefined-key
	bindkey    "^[[23;5~"	undefined-key
	bindkey    "^[[24;5~"	undefined-key
	bindkey    "^[[1;6P"	undefined-key
	bindkey    "^[[1;6Q"	undefined-key
	bindkey    "^[[1;6R"	undefined-key
	bindkey    "^[[1;6S"	undefined-key
	bindkey    "^[[15;6~"	undefined-key
	bindkey    "^[[17;6~"	undefined-key
	bindkey    "^[[18;6~"	undefined-key
	bindkey    "^[[19;6~"	undefined-key
	bindkey    "^[[20;6~"	undefined-key
	bindkey    "^[[21;6~"	undefined-key
	bindkey    "^[[23;6~"	undefined-key
	bindkey    "^[[24;6~"	undefined-key
	bindkey    "^[[1;7P"	undefined-key
	bindkey    "^[[1;7Q"	undefined-key
	bindkey    "^[[1;7R"	undefined-key
	bindkey    "^[[1;7S"	undefined-key
	bindkey    "^[[15;7~"	undefined-key
	bindkey    "^[[17;7~"	undefined-key
	bindkey    "^[[18;7~"	undefined-key
	bindkey    "^[[19;7~"	undefined-key
	bindkey    "^[[20;7~"	undefined-key
	bindkey    "^[[21;7~"	undefined-key
	bindkey    "^[[23;7~"	undefined-key
	bindkey    "^[[24;7~"	undefined-key
	bindkey    "^[[1;8P"	undefined-key
	bindkey    "^[[1;8Q"	undefined-key
	bindkey    "^[[1;8R"	undefined-key
	bindkey    "^[[1;8S"	undefined-key
	bindkey    "^[[15;8~"	undefined-key
	bindkey    "^[[17;8~"	undefined-key
	bindkey    "^[[18;8~"	undefined-key
	bindkey    "^[[19;8~"	undefined-key
	bindkey    "^[[20;8~"	undefined-key
	bindkey    "^[[21;8~"	undefined-key
	bindkey    "^[[23;8~"	undefined-key
	bindkey    "^[[24;8~"	undefined-key
endif
#
if ( "$TERM" =~ xterm* ) then
	#
	# Application keypad and cursor of xterm
	# with NumLock ON
	#
	# Operators
	bindkey -s "^[Oo"	"/"
	bindkey -s "^[Oj"	"*"
	bindkey -s "^[Om"	"-"
	bindkey -s "^[Ok"	"+"
	bindkey -s "^[Ol"	","
	bindkey    "^[OM"	newline
	bindkey -s "^[On"	"."
	# Numbers
	bindkey -s "^[Op"	"0"
	bindkey -s "^[Oq"	"1"
	bindkey -s "^[Or"	"2"
	bindkey -s "^[Os"	"3"
	bindkey -s "^[Ot"	"4"
	bindkey -s "^[Ou"	"5"
	bindkey -s "^[Ov"	"6"
	bindkey -s "^[Ow"	"7"
	bindkey -s "^[Ox"	"8"
	bindkey -s "^[Oy"	"9"
	# Operators
	bindkey -s "\217o"	"/"
	bindkey -s "\217j"	"*"
	bindkey -s "\217m"	"-"
	bindkey -s "\217k"	"+"
	bindkey -s "\217l"	","
	bindkey    "\217M"	newline
	bindkey -s "\217n"	"."
	# Numbers
	bindkey -s "\217p"	"0"
	bindkey -s "\217q"	"1"
	bindkey -s "\217r"	"2"
	bindkey -s "\217s"	"3"
	bindkey -s "\217t"	"4"
	bindkey -s "\217u"	"5"
	bindkey -s "\217v"	"6"
	bindkey -s "\217w"	"7"
	bindkey -s "\217x"	"8"
	bindkey -s "\217y"	"9"
	# Shift+Alt+KP_<0...9> of konsole
	bindkey    "^[0"	yank
	bindkey    "^[1"	end-of-line
	bindkey    "^[2"	down-history
	bindkey    "^[3"	history-search-forward
	bindkey    "^[4"	backward-word
	bindkey -c "^[5"	"source /etc/csh.cshrc"
	bindkey    "^[6"	forward-word
	bindkey    "^[7"	beginning-of-line
	bindkey    "^[8"	up-history
	bindkey    "^[9"	history-search-backward
endif
#
if ( "$TERM" =~ kterm* ) then
	bindkey    "^[[\000"	undefined-key
endif
#
if ( "$TERM" =~ mlterm* ) then
	bindkey -c "^[[E"	"source /etc/csh.cshrc"
	bindkey    "^[OH"	beginning-of-line
	bindkey    "^[OF"	end-of-line
	bindkey    "^[^[OH"	beginning-of-line
	bindkey    "^[^[OF"	end-of-line
	bindkey    "^[[1;2C"	forward-word
	bindkey    "^[[1;2D"	backward-word
	bindkey    "^[[1;2A"	history-search-backward
	bindkey    "^[[1;2B"	history-search-forward
	bindkey    "^[[1;3C"	forward-word
	bindkey    "^[[1;3D"	backward-word
	bindkey    "^[[1;3A"	history-search-backward
	bindkey    "^[[1;3B"	history-search-forward
	bindkey    "^[[1;4C"	forward-word
	bindkey    "^[[1;4D"	backward-word
	bindkey    "^[[1;4A"	history-search-backward
	bindkey    "^[[1;4B"	history-search-forward
	bindkey    "^[[1;5C"	forward-word
	bindkey    "^[[1;5D"	backward-word
	bindkey    "^[[1;5A"	history-search-backward
	bindkey    "^[[1;5B"	history-search-forward
	bindkey    "^[[1;6C"	forward-word
	bindkey    "^[[1;6D"	backward-word
	bindkey    "^[[1;6A"	history-search-backward
	bindkey    "^[[1;6B"	history-search-forward
	bindkey    "^[[1;7C"	forward-word
	bindkey    "^[[1;7D"	backward-word
	bindkey    "^[[1;7A"	history-search-backward
	bindkey    "^[[1;7B"	history-search-forward
	bindkey    "^[[1;8C"	forward-word
	bindkey    "^[[1;8D"	backward-word
	bindkey    "^[[1;8A"	history-search-backward
	bindkey    "^[[1;8B"	history-search-forward
	bindkey    "^[[11;2~"	undefined-key
	bindkey    "^[[12;2~"	undefined-key
	bindkey    "^[[13;2~"	undefined-key
	bindkey    "^[[14;2~"	undefined-key
	bindkey    "^[[15;2~"	undefined-key
	bindkey    "^[[17;2~"	undefined-key
	bindkey    "^[[18;2~"	undefined-key
	bindkey    "^[[19;2~"	undefined-key
	bindkey    "^[[20;2~"	undefined-key
	bindkey    "^[[21;2~"	undefined-key
	bindkey    "^[[23;2~"	undefined-key
	bindkey    "^[[24;2~"	undefined-key
	bindkey    "^[[11;3~"	undefined-key
	bindkey    "^[[12;3~"	undefined-key
	bindkey    "^[[13;3~"	undefined-key
	bindkey    "^[[14;3~"	undefined-key
	bindkey    "^[[15;3~"	undefined-key
	bindkey    "^[[17;3~"	undefined-key
	bindkey    "^[[18;3~"	undefined-key
	bindkey    "^[[19;3~"	undefined-key
	bindkey    "^[[20;3~"	undefined-key
	bindkey    "^[[21;3~"	undefined-key
	bindkey    "^[[23;3~"	undefined-key
	bindkey    "^[[24;3~"	undefined-key
	bindkey    "^[[11;4~"	undefined-key
	bindkey    "^[[12;4~"	undefined-key
	bindkey    "^[[13;4~"	undefined-key
	bindkey    "^[[14;4~"	undefined-key
	bindkey    "^[[15;4~"	undefined-key
	bindkey    "^[[17;4~"	undefined-key
	bindkey    "^[[18;4~"	undefined-key
	bindkey    "^[[19;4~"	undefined-key
	bindkey    "^[[20;4~"	undefined-key
	bindkey    "^[[21;4~"	undefined-key
	bindkey    "^[[23;4~"	undefined-key
	bindkey    "^[[24;4~"	undefined-key
	bindkey    "^[[11;5~"	undefined-key
	bindkey    "^[[12;5~"	undefined-key
	bindkey    "^[[13;5~"	undefined-key
	bindkey    "^[[14;5~"	undefined-key
	bindkey    "^[[15;5~"	undefined-key
	bindkey    "^[[17;5~"	undefined-key
	bindkey    "^[[18;5~"	undefined-key
	bindkey    "^[[19;5~"	undefined-key
	bindkey    "^[[20;5~"	undefined-key
	bindkey    "^[[21;5~"	undefined-key
	bindkey    "^[[23;5~"	undefined-key
	bindkey    "^[[24;5~"	undefined-key
	bindkey    "^[[11;6~"	undefined-key
	bindkey    "^[[12;6~"	undefined-key
	bindkey    "^[[13;6~"	undefined-key
	bindkey    "^[[14;6~"	undefined-key
	bindkey    "^[[15;6~"	undefined-key
	bindkey    "^[[17;6~"	undefined-key
	bindkey    "^[[18;6~"	undefined-key
	bindkey    "^[[19;6~"	undefined-key
	bindkey    "^[[20;6~"	undefined-key
	bindkey    "^[[21;6~"	undefined-key
	bindkey    "^[[23;6~"	undefined-key
	bindkey    "^[[24;6~"	undefined-key
	bindkey    "^[[11;7~"	undefined-key
	bindkey    "^[[12;7~"	undefined-key
	bindkey    "^[[13;7~"	undefined-key
	bindkey    "^[[14;7~"	undefined-key
	bindkey    "^[[15;7~"	undefined-key
	bindkey    "^[[17;7~"	undefined-key
	bindkey    "^[[18;7~"	undefined-key
	bindkey    "^[[19;7~"	undefined-key
	bindkey    "^[[20;7~"	undefined-key
	bindkey    "^[[21;7~"	undefined-key
	bindkey    "^[[23;7~"	undefined-key
	bindkey    "^[[24;7~"	undefined-key
	bindkey    "^[[11;8~"	undefined-key
	bindkey    "^[[12;8~"	undefined-key
	bindkey    "^[[13;8~"	undefined-key
	bindkey    "^[[14;8~"	undefined-key
	bindkey    "^[[15;8~"	undefined-key
	bindkey    "^[[17;8~"	undefined-key
	bindkey    "^[[18;8~"	undefined-key
	bindkey    "^[[19;8~"	undefined-key
	bindkey    "^[[20;8~"	undefined-key
	bindkey    "^[[21;8~"	undefined-key
	bindkey    "^[[23;8~"	undefined-key
	bindkey    "^[[24;8~"	undefined-key
	# Shift+Alt+KP_<0...9>
	bindkey    "^[0"	yank
	bindkey    "^[1"	end-of-line
	bindkey    "^[2"	down-history
	bindkey    "^[3"	history-search-forward
	bindkey    "^[4"	backward-word
	bindkey -c "^[5"	"source /etc/csh.cshrc"
	bindkey    "^[6"	forward-word
	bindkey    "^[7"	beginning-of-line
	bindkey    "^[8"	up-history
	bindkey    "^[9"	history-search-backward
endif
#
if ( "$TERM" =~ rxvt-unicode* ) then
	bindkey    '^[[23$'	undefined-key
	bindkey    '^[[24$'	undefined-key
	bindkey    "^[[11\^"	undefined-key
	bindkey    "^[[12\^"	undefined-key
	bindkey    "^[[13\^"	undefined-key
	bindkey    "^[[14\^"	undefined-key
	bindkey    "^[[15\^"	undefined-key
	bindkey    "^[[17\^"	undefined-key
	bindkey    "^[[18\^"	undefined-key
	bindkey    "^[[19\^"	undefined-key
	bindkey    "^[[20\^"	undefined-key
	bindkey    "^[[21\^"	undefined-key
	bindkey    "^[[23\^"	undefined-key
	bindkey    "^[[24\^"	undefined-key
	bindkey -s "^[Oo"	"/"
	bindkey -s "^[Oj"	"*"
	bindkey -s "^[Om"	"-"
	bindkey -s "^[Ok"	"+"
	bindkey -s "^[Ol"	","
	bindkey    "^[OM"	newline
	bindkey -s "^[On"	"."
	bindkey -s "^[Op"	"0"
	bindkey -s "^[Oq"	"1"
	bindkey -s "^[Or"	"2"
	bindkey -s "^[Os"	"3"
	bindkey -s "^[Ot"	"4"
	bindkey -s "^[Ou"	"5"
	bindkey -s "^[Ov"	"6"
	bindkey -s "^[Ow"	"7"
	bindkey -s "^[Ox"	"8"
	bindkey -s "^[Oy"	"9"
	bindkey    "^[^[Oo"	undefined-key
	bindkey    "^[^[Oj"	undefined-key
	bindkey    "^[^[Om"	undefined-key
	bindkey    "^[^[Ok"	undefined-key
	bindkey    "^[^[Ol"	delete-char
	bindkey    "^[^[OM"	newline
	bindkey    "^[^[On"	delete-char
	bindkey    "^[^[Op"	yank
	bindkey    "^[^[Oq"	end-of-line
	bindkey    "^[^[Or"	down-history
	bindkey    "^[^[Os"	history-search-forward
	bindkey    "^[^[Ot"	backward-char
	bindkey -s "^[^[Ou"	"source /etc/csh.cshrc"
	bindkey    "^[^[Ov"	forward-char
	bindkey    "^[^[Ow"	beginning-of-line
	bindkey    "^[^[Ox"	up-history
	bindkey    "^[^[Oy"	history-search-backward
	bindkey    "^[Oc"	forward-word
	bindkey    "^[Od"	backward-word
	bindkey    "^[Oa"	history-search-backward
	bindkey    "^[Ob"	history-search-forward
	bindkey    "^[[c"	forward-word
	bindkey    "^[[d"	backward-word
	bindkey    "^[[a"	history-search-backward
	bindkey    "^[[b"	history-search-forward
	bindkey    "^[^[[c"	forward-word
	bindkey    "^[^[[d"	backward-word
	bindkey    "^[^[[a"	history-search-backward
	bindkey    "^[^[[b"	history-search-forward
	bindkey    "^[^[[C"	forward-word
	bindkey    "^[^[[D"	backward-word
	bindkey    "^[^[[A"	history-search-backward
	bindkey    "^[^[[B"	history-search-forward
	bindkey    "^[[2\^"	yank
	bindkey    "^[[3\^"	delete-char
	bindkey    "^[[5\^"	history-search-backward
	bindkey    "^[[6\^"	history-search-forward
	bindkey    "^[[7\^"	beginning-of-line
	bindkey    "^[[8\^"	end-of-line
	bindkey    '^[[2$'	yank
	bindkey    '^[[3$'	delete-char
	bindkey    '^[[5$'	history-search-backward
	bindkey    '^[[6$'	history-search-forward
	bindkey    '^[[7$'	beginning-of-line
	bindkey    '^[[8$'	end-of-line
	bindkey    '^[^[[2$'	yank
	bindkey    '^[^[[3$'	delete-char
	bindkey    '^[^[[5$'	history-search-backward
	bindkey    '^[^[[6$'	history-search-forward
	bindkey    '^[^[[7$'	beginning-of-line
	bindkey    '^[^[[8$'	end-of-line
	bindkey    "^[="	newline
	# Shift+Ctrl+(Alt+)KP_<0...9> generates
	# \000 ... \011 (^@ upto TAB) we ignore these
endif
#
#  EMACS line editing
#
if ( "$CSHEDIT" == "emacs" ) then 
	#
	# ... xterm application cursor
	#
    	if ( "$TERM" =~ xterm* ) then
	     bindkey    "^[^[OD"	backward-word
	     bindkey    "^[^[OC"	forward-word
	     bindkey    "^[^[OA"	up-history
	     bindkey    "^[^[OB"	down-history
	     bindkey    "^^[OD"		backward-char
	     bindkey    "^^[OC"		forward-char
	     bindkey    "^^[OA"		up-history
	     bindkey    "^^[OB"		down-history
    	endif
	#
	# Standard cursor
	#
	bindkey    "^[^[[D"	backward-word
	bindkey    "^[^[[C"	forward-word
	bindkey    "^[^[[A"	up-history
	bindkey    "^[^[[B"	down-history
	bindkey    "^^[[D"	backward-char
	bindkey    "^^[[C"	forward-char
	bindkey    "^^[[A"	up-history
	bindkey    "^^[[B"	down-history
endif
#
# Screen
#
if ( "$TERM" =~ screen* ) then
	bindkey    "\e[1;2D"	backward-word
	bindkey    "\e[1;2C"	forward-word
	bindkey    "\e[1;2A"	up-history
	bindkey    "\e[1;2B"	down-history
	bindkey    "\e[1;2H"	beginning-of-line
	bindkey    "\e[1;2F"	end-of-line
	bindkey    "\e[2;2~"	yank
	bindkey    "\e[3;2~"	delete-char
	bindkey    "\e[5;2~"	history-search-backward
	bindkey    "\e[6;2~"	history-search-forward
	bindkey    "\e[1;5D"	backward-word
	bindkey    "\e[1;5C"	forward-word
	bindkey    "\e[1;5A"	up-history
	bindkey    "\e[1;5B"	down-history
	bindkey    "\e[1;5H"	beginning-of-line
	bindkey    "\e[1;5F"	end-of-line
	bindkey    "\e[2;5~"	yank
	bindkey    "\e[3;5~"	delete-char
	bindkey    "\e[5;5~"	history-search-backward
	bindkey    "\e[6;5~"	history-search-forward
	bindkey    "\e[1;3D"	backward-word
	bindkey    "\e[1;3C"	forward-word
	bindkey    "\e[1;3A"	up-history
	bindkey    "\e[1;3B"	down-history
	bindkey    "\e[1;3H"	beginning-of-line
	bindkey    "\e[1;3F"	end-of-line
	bindkey    "\e[2;3~"	yank
	bindkey    "\e[3;3~"	delete-char
	bindkey    "\e[5;3~"	history-search-backward
	bindkey    "\e[6;3~"	history-search-forward
#
	bindkey    "\e[1;2P"	undefined-key
	bindkey    "\e[1;2Q"	undefined-key
	bindkey    "\e[1;2R"	undefined-key
	bindkey    "\e[1;2S"	undefined-key
	bindkey    "\e[15;2~"	undefined-key
	bindkey    "\e[17;2~"	undefined-key
	bindkey    "\e[18;2~"	undefined-key
	bindkey    "\e[19;2~"	undefined-key
	bindkey    "\e[20;2~"	undefined-key
	bindkey    "\e[21;2~"	undefined-key
	bindkey    "\e[23;2~"	undefined-key
	bindkey    "\e[24;2~"	undefined-key
#
	bindkey    "\e[1;5P"	undefined-key
	bindkey    "\e[1;5Q"	undefined-key
	bindkey    "\e[1;5R"	undefined-key
	bindkey    "\e[1;5S"	undefined-key
	bindkey    "\e[15;5~"	undefined-key
	bindkey    "\e[17;5~"	undefined-key
	bindkey    "\e[18;5~"	undefined-key
	bindkey    "\e[19;5~"	undefined-key
	bindkey    "\e[20;5~"	undefined-key
	bindkey    "\e[21;5~"	undefined-key
	bindkey    "\e[23;5~"	undefined-key
	bindkey    "\e[24;5~"	undefined-key
#
	bindkey    "\e[1;3P"	undefined-key
	bindkey    "\e[1;3Q"	undefined-key
	bindkey    "\e[1;3R"	undefined-key
	bindkey    "\e[1;3S"	undefined-key
	bindkey    "\e[15;3~"	undefined-key
	bindkey    "\e[17;3~"	undefined-key
	bindkey    "\e[18;3~"	undefined-key
	bindkey    "\e[19;3~"	undefined-key
	bindkey    "\e[20;3~"	undefined-key
	bindkey    "\e[21;3~"	undefined-key
	bindkey    "\e[23;3~"	undefined-key
	bindkey    "\e[24;3~"	undefined-key
endif
#
# end bindkey.tcsh
#
