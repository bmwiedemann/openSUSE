buildignore gvfs
buildignore libreoffice-icon-theme-galaxy
buildignore libreoffice-icon-theme-hicontrast
buildignore libreoffice-icon-theme-tango
buildignore libreoffice-base-drivers-mysql
buildignore libreoffice-pyuno
buildignore cairomm
buildignore evolution-data-server
buildignore notification-daemon
buildignore gdm
buildignore akregator
buildignore ImageMagick
install patterns-kde-kde
installPattern kde
install openSUSE-release-livecd-kde
install plasma5-workspace-branding-openSUSE
install baloo5-tools
install NetworkManager
# Don't add libreoffice for now, too large
buildignore libreoffice
buildignore libreoffice-icon-themes
buildignore libreoffice-icon-theme-breeze
# Required by LO, but otherwise too large
buildignore xorg-x11-fonts
buildignore kdenetwork4-filesharing
buildignore gnome-keyring

# Packages for the installer
source "$PWD/list-installer.sh"

buildignore oxygen5-icon-theme-large
buildignore gwenview5

# Resolve have-choice
install plasma-nm5
install phonon4qt5-backend-gstreamer
buildignore ispell

# No fun allowed
buildignore patterns-kde-kde_games

# Not really useful here, except for kcharselect.
buildignore patterns-kde-kde_utilities
install kcharselect

# Moved here from list-common.sh, too big for x11
install xf86-video-vmware i686,x86_64

# No PIM
buildignore patterns-kde-kde_pim

buildignore gdb
buildignore icewm
buildignore libproxy1-pacrunner-webkit
buildignore digikam
buildignore hugin
buildignore gimp-lang
buildignore kate-lang

install partitionmanager

install cifs-utils

# Moved here from list-common.sh. cyrus-sasl is needed by Pidgin in Xfce Live CD
buildignore cyrus-sasl

# From rest_cd_core
install alsa-firmware

# From x11_enhanced, but that pattern can't be installed
[ "$distro" = "tumbleweed" ] && install opensuse-welcome
