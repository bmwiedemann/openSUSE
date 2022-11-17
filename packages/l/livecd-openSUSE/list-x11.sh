buildignore NetworkManager-lang
buildignore NetworkManager-applet-lang
buildignore PackageKit
buildignore samba-libs
buildignore release-notes-openSUSE
buildignore gnome-themes-accessibility
buildignore xlockmore
buildignore unzip-doc
buildignore gtk2-immodule-inuktitut
buildignore gtk2-immodule-thai
buildignore gtk2-immodule-vietnamese
buildignore gtk2-lang
buildignore gtk3-immodule-inuktitut
buildignore gtk3-immodule-thai
buildignore gtk3-immodule-vietnamese
buildignore gtk3-lang
buildignore evince-lang
buildignore hexchat-lang
buildignore nano-lang
buildignore zenity-lang
buildignore gsettings-desktop-schema-lang
buildignore gvfs-lang
buildignore libstorage-ng-lang
buildignore joe
buildignore libgphoto2-6-lang
buildignore alsa
buildignore alsa-firmware
buildignore alsa-plugins
buildignore xscreensaver
buildignore PackageKit-gstreamer-plugin
buildignore ImageMagick
buildignore awesfx
buildignore sbl
buildignore gnome-online-accounts
buildignore snapper

# No YaST
buildignore patterns-yast-yast2_basis
buildignore yast2-control-center
buildignore yast2-control-center-qt
# Note: OBS doesn't understand this, but kiwi/zypper do.
buildignore libyui*

buildignore Mesa-libva

# No python2 necessary
buildignore python-base
buildignore python38-pip

# Pulls in libpython2_7
buildignore libpeas-loader-python

buildignore aspell-en
buildignore ModemManager
buildignore avahi
buildignore fprintd
buildignore accountsservice
buildignore MozillaFirefox
buildignore tcpdump

install gparted
install epiphany
# Really ran of out space
buildignore gparted-lang
buildignore epiaphy-lang
buildignore iso-codes-lang
buildignore glib2-lang
buildignore thunar-lang
buildignore xfce4-settings-lang
buildignore xfce4-panel-lang
buildignore xfce-terminal-lang
buildignore exo-lang
buildignore xfdesktop-lang
buildignore xfce4-power-manager-lang
buildignore noto-sans-cjk-fonts
buildignore man-pages-posix
buildignore libvulkan_radeon
buildignore man
buildignore groff
buildignore libqt5-qttranslations
buildignore plymouth
buildignore 7zip
# On Leap it's a hard dep of dhcp-client, needed by NM.
# On TW, NM uses the builtin DHCP client instead.
if [ "$distro" = "tumbleweed" ]; then
	buildignore bind-utils
fi

# tumbler -> libgepup uses libwebkit2gtk-4_0-37, while epiphany uses libwebkit2gtk-4_1-0.
# We can't have both, too big.
buildignore tumbler
# ristretto is not that useful without tumbler
buildignore ristretto

# Moved here from list-common.sh. cyrus-sasl is needed by Pidgin in Xfce Live CD
buildignore cyrus-sasl

# Moved here from list-common.sh. Needed by createrepo_c, which is needed for libzypp-plugin-appdata
buildignore deltarpm

# Too big and not really useful here
buildignore Mesa-dri-nouveau
buildignore libvdpau_nouveau

# Pulls in a lot of libs, only used by libwebkit2gtk/epiphany anyway
buildignore gstreamer-plugins-bad

# Previously required by rest_cd_x11
install patterns-xfce-xfce_basis
installPattern xfce_basis
install evince
install evince-plugin-pdfdocument
install file-roller
install gparted
install hexchat
install leafpad
install lightdm
install lightdm-gtk-greeter
install photorec
install thunar
install thunar-volman
install xfce4-appfinder
install xfce4-notifyd
install xfce4-panel
install xfce4-power-manager
install xfce4-session
install xfce4-settings
install xfconf
install xfdesktop
install xfwm4

# Previously recommended by rest_cd_x11
install dbus-1-x11
install desktop-file-utils
install libgnomesu
install libxfce4ui-tools
install pinentry-gtk2
install shared-mime-info
install xdg-user-dirs-gtk
install xdg-utils
install NetworkManager-applet
install xfce4-panel-plugin-xkb
install xfce4-terminal

buildignore argyllcms

