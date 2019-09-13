#
# /etc/profile.d/texlive.sh
#

#
# Expand TEXINPUTS
#
if test -d $HOME/TeX/ ; then
    #
    # Hmmm ... texmf/ should be used instead of TeX/
    #
    if test -n "$TEXINPUTS" ; then
	TEXINPUTS="$TEXINPUTS:$HOME/TeX//:"
    else
	TEXINPUTS="$HOME/TeX//:"
    fi
fi
if test -d /usr/doc/.TeX/ ; then
    if test -n "$TEXINPUTS" ; then
	TEXINPUTS="$TEXINPUTS:/usr/doc/.TeX:"
    else
	TEXINPUTS="/usr/doc/.TeX:"
    fi
fi
