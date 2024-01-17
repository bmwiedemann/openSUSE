#
# /etc/profile.d/texlive.csh
#

#
# Expand TEXINPUTS
#
if ( -d ${HOME}/TeX/ ) then
    #
    # Hmmm ... texmf/ should be used instead of TeX/
    #
    if ( ${?TEXINPUTS} ) then
	setenv TEXINPUTS ${TEXINPUTS}:${HOME}/TeX//:
    else
	setenv TEXINPUTS ${HOME}/TeX//:
    endif
endif
if ( -d /usr/doc/.TeX/ ) then
    if ( ${?TEXINPUTS} ) then
	setenv TEXINPUTS ${TEXINPUTS}:/usr/doc/.TeX:
    else
	setenv TEXINPUTS /usr/doc/.TeX:
    endif
endif
