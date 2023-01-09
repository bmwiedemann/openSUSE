#
# spec file for package qFlipper
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           qFlipper
Version:        1.2.2+git7.1672595968.84566a5
Release:        0
Summary:        Graphical desktop application for updating Flipper Zero firmware
License:        GPL-3.0-or-later
URL:            https://github.com/flipperdevices/qFlipper
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Quick3D)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-base = %{version}-%{release}
Requires:       %{name}-libflipperproto = %{version}-%{release}

%description
Graphical desktop application for updating Flipper Zero firmware

* Update Flipper's firmware and supplemental data with a press of one button
* Repair a broken firmware installation
* Stream Flipper's display and control it remotely
* Install firmware from a .dfu file
* Backup and restore settings, progress and pairing data

%package cli
Summary:        Commandline application for updating Flipper Zero firmware
Requires:       %{name}-base = %{version}-%{release}
Requires:       %{name}-libflipperproto = %{version}-%{release}

%description cli
Commandline application for updating Flipper Zero firmware

* Update Flipper's firmware and supplemental data with a press of one button
* Repair a broken firmware installation
* Stream Flipper's display and control it remotely
* Install firmware from a .dfu file
* Backup and restore settings, progress and pairing data

%package libflipperproto
Summary:        Application for updating Flipper Zero firmware - protocol library

%description libflipperproto
Application for updating Flipper Zero firmware - protocol library

%package base
Summary:        Application for updating Flipper Zero firmware - udev rules
BuildArch:      noarch

%description base
Application for updating Flipper Zero firmware - udev rules

%prep
%setup -q
gitver=$(echo %{version} | cut -d+ -f1)
gitdate=$(echo %{version} | tr '.' ' ' | rev | cut -d' ' -f2 | rev)
githash=$(echo %{version} | tr '.' ' ' | rev | cut -d' ' -f1 | rev)
sed -i -e "s|^[ \t]*GIT_VERSION = .*|GIT_VERSION = $gitver|" qflipper_common.pri
sed -i -e "s|^[ \t]*GIT_COMMIT = .*|GIT_COMMIT = $githash|" qflipper_common.pri
sed -i -e "s|^[ \t]*GIT_TIMESTAMP = .*|GIT_TIMESTAMP = $gitdate|" qflipper_common.pri
sed -i -e "s|^RULES_DIR=.*|RULES_DIR=\\\${PREFIX}%{_udevrulesdir}|" setup_rules.sh

%build
%qmake5 qFlipper.pro -spec linux-g++ CONFIG+=qtquickcompiler DEFINES+=DISABLE_APPLICATION_UPDATES
%make_build qmake_all
%make_build

%install
%qmake5_install
echo i | PREFIX=%{buildroot} sh setup_rules.sh

%files
%license LICENSE
%doc README.md screenshot.png
%{_bindir}/qFlipper
%{_datadir}/applications/qFlipper.desktop
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/512x512/apps/qFlipper.png

%files cli
%{_bindir}/qFlipper-cli

%files base
%{_prefix}/lib/udev/rules.d/42-flipperzero.rules

%files libflipperproto
%dir %{_prefix}/lib/qFlipper
%dir %{_prefix}/lib/qFlipper/plugins
%{_prefix}/lib/qFlipper/plugins/libflipperproto0.so

%changelog
