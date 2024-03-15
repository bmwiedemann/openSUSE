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
if [ "$distro" = "leap" ]; then
  install plasma5-workspace-branding-openSUSE
  install phonon4qt5-backend-vlc
  buildignore vlc
  buildignore vlc-qt
  install plasma-nm5
  # From x11_enhanced, but that pattern can't be installed
  install opensuse-welcome
  install baloo5-tools
else
  install phonon-vlc-qt6
  buildignore gtk3-metatheme-breeze
  install kf6-baloo-tools
  buildignore libqt5-qttranslations
  buildignore speech-dispatcher

  # Until deleted or replaced by kcm_sddm6
  buildignore kcm_sddm
  # Until built against Qt 6
  buildignore xwaylandvideobridge
  # Needs WebEngine and we don't install docs on the .iso
  buildignore khelpcenter
  # Needs WebEngine and not useful ATM
  buildignore kaccounts-providers
fi
install NetworkManager
# Don't add libreoffice for now, too large
buildignore libreoffice
buildignore libreoffice-icon-themes
buildignore libreoffice-icon-theme-breeze
buildignore kdenetwork4-filesharing
buildignore gnome-keyring
# This pulls in GTK 2. We have ksshaskpass instead.
buildignore openssh-askpass-gnome
# Make sure it's not coming back
buildignore libgtk-2_0-0

# Packages for the installer
source "$PWD/list-installer.sh"

buildignore oxygen5-icon-theme-large
# Needs ibus data files and color emoji fonts, too big.
buildignore plasma5-desktop-emojier

# Resolve have-choice
buildignore ispell

# No fun allowed
buildignore patterns-kde-kde_games
# No PIM
buildignore patterns-kde-kde_pim
# Not really useful here, except for kcharselect.
buildignore patterns-kde-kde_utilities
install kcharselect
# Ignore
buildignore plasma-nm5-openconnect
buildignore plasma-nm5-openvpn 

# Pulls in docbook and friends, ~50MiB.
# Excludedocs is enabled, so documentation is broken anyway
buildignore kdoctools

# Moved here from list-common.sh, too big for x11
install xf86-video-vmware i686,x86_64

buildignore digikam
buildignore gdb
buildignore hugin
buildignore icewm
buildignore ksudoku
buildignore kpat
buildignore kmahjongg
buildignore konversation-lang
buildignore libKF5Auth5-lang
buildignore libproxy1-pacrunner-webkit
buildignore vlc-lang
buildignore kipi-plugins

# Upstream branding, not used by default and HUGE
buildignore breeze5-wallpapers
buildignore breeze6-wallpapers

install partitionmanager

# Moved here from list-common.sh. cyrus-sasl is needed by Pidgin in Xfce Live CD
buildignore cyrus-sasl
# Moved here from list-common.sh, needed by GNOME now
buildignore xorg-x11-fonts

# From rest_cd_core
install alsa-firmware


buildignore bluedevil5
buildignore konsole-part-lang