install branding-openSUSE
install yast2-trans-stats
install patterns-xfce-xfce
installPattern xfce
buildignore gnome-themes-accessibility
buildignore xlockmore
buildignore unzip-doc
buildignore gtk2-immodule-inuktitut
buildignore gtk2-immodule-thai
buildignore gtk2-immodule-vietnamese
buildignore gtk3-immodule-inuktitut
buildignore gtk3-immodule-thai
buildignore gtk3-immodule-vietnamese
buildignore awesfx
buildignore sbl
buildignore gnome-online-accounts

#temp disabled - until build fuxed
buildignore pragha

# Packages for the installer
source "$PWD/list-installer.sh"

buildignore aspell-en
install libxslt-tools

# Remove useless xfce panel plugins
buildignore xfce4-panel-plugin-xkb
buildignore xfce4-panel-plugin-notes
buildignore engrampa-lang

# Remove Libreoffice as it's too big
buildignore libreoffice

# Save a bit of space
buildignore gdb

buildignore gimp
buildignore pidgin

# Pulls in sane-backends
buildignore simple-scan

# Moved here from list-common.sh, too big for x11
install xf86-video-vmware i686,x86_64

# Moved here from list-common.sh, needed by GNOME now
buildignore xorg-x11-fonts

# make sure pdf support for evince is installed
install evince-plugin-pdfdocument

# From rest_cd_core
install alsa-firmware

# Not compatible with GNOME 41 (nothing provides typelib(Cheese) = 3.0)
buildignore mugshot

# From x11_enhanced, but that pattern can't be installed
install opensuse-welcome
