Format: 3.0 (quilt)
Source: keepassxc
Binary: keepassxc
Architecture: any
Version: 2.7.11-1.1
Maintainer: Julian Andres Klode <jak@debian.org>
Homepage: https://www.keepassxc.org/
Standards-Version: 4.4.0
Vcs-Browser: https://salsa.debian.org/debian/keepassxc
Vcs-Git: https://salsa.debian.org/debian/keepassxc.git
Build-Depends: asciidoctor,
               cmake,
               debhelper (>= 10),
               libargon2-dev | libargon2-0-dev,
               libbotan-2-dev (>=2.12.1),
               libusb-1.0-0-dev,
               libminizip-dev,
               libpcsclite-dev,
               libqt5svg5-dev,
               libqt5x11extras5-dev,
               libqrencode-dev,
               libreadline-dev,
               libsodium-dev,
               libxi-dev,
               libxtst-dev,
               libykpers-1-dev,
               libyubikey-dev,
               libzxcvbn-dev,
               qtbase5-dev,
               qtbase5-private-dev,
               qttools5-dev,
               qttools5-dev-tools,
               xauth,
               xvfb,
               zlib1g-dev
Package-List:
 keepassxc deb utils optional arch=any
