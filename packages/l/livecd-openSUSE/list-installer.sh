# YaST
install patterns-yast-yast2_basis
installPattern yast2_basis

install yast2-bootloader
install yast2-country
install yast2-hardware-detection
install yast2-network
install yast2-proxy
install yast2-storage-ng
# We don't need those
buildignore yast2-samba-client
buildignore yast2-vpn
buildignore yast2-journal
buildignore yast2-auth-client
buildignore yast2-sudo

install yast2-trans-de
if [ "$distro" = "leap" ]; then
        install yast2-trans-cs
        install yast2-trans-da
        install yast2-trans-es
        install yast2-trans-ja
        install yast2-trans-pl
        install yast2-trans-ru
        install yast2-trans-sv
        install yast2-trans-zh_CN
        install yast2-trans-zh_TW
fi

# Packages for the installer
install live-net-installer
install skelcd-openSUSE # Needed for README.BETA
install setxkbmap # Needed by yast2-keyboard
install skelcd-control-openSUSE # Just pulled in for deps
install cracklib-dict-full

# Fonts for the installation (taken from installation-images)
install thai-fonts
install lklug-fonts
install indic-fonts
install arabic-kacst-fonts
# too big
# install un-fonts
# install ipa-gothic-fonts
