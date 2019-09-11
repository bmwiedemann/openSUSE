if ( $?XDG_CURRENT_DESKTOP ) then
	if ( $XDG_CURRENT_DESKTOP != "KDE" ) then
		setenv QT_QPA_PLATFORMTHEME 'qt5ct'
	endif
else
	setenv QT_QPA_PLATFORMTHEME 'qt5ct'
endif
