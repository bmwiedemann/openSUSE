Format: 3.0 (quilt)
Source: keepassxc
Binary: keepassxc
Architecture: any
Version: 2.8.0-1.1
Maintainer: KeePassXC Team <team@keepassxc.org>
Homepage: https://keepassxc.org/
Standards-Version: 4.6.2
Vcs-Browser: https://github.com/keepassxreboot/keepassxc
Vcs-Git: https://github.com/keepassxreboot/keepassxc.git
Build-Depends: asciidoctor,
               cmake (>= 3.16),
               debhelper (>= 12),
               libbotan-3-dev | libbotan-2-dev (>= 2.19.1),
               libgl-dev,
               libkeyutils-dev,
               libminizip-dev,
               libpcsclite-dev,
               libqrencode-dev,
               libreadline-dev,
               libusb-1.0-0-dev,
               pkgconf,
               libx11-dev,
               libxi-dev,
               libxkbcommon-dev,
               libxtst-dev,
               libzxcvbn-dev,
               qt6-base-dev (>= 6.2.4),
               qt6-l10n-tools,
               qt6-svg-dev,
               qt6-tools-dev,
               qt6-tools-dev-tools,
               zlib1g-dev
Package-List:
 keepassxc deb utils optional arch=any
DEBTRANSFORM-TAR: keepassxc-2.8.0-src.tar.xz
