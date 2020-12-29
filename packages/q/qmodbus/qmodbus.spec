#
# spec file for package qmodbus
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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

Name:           qmodbus
Version:        0.3.0
Release:        0
Summary:        QT ModBus tools
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            http://qmodbus.sourceforge.net/
#Git-Clone:     https://github.com/ed-chemnitz/qmodbus.git
Source:         https://github.com/ed-chemnitz/qmodbus/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
Provides:       bundled(libmodbus)
Provides:       bundled(QextSerialPort)

%description
QModBus is an implementation of a ModBus master application.
A graphical user interface allows easy communication with ModBus
slaves over serial line interface. QModBus also includes a bus
monitor for sniffing all traffic on the bus.

%prep
%setup -q

%build
%qmake5
%make_jobs

%install
%make_install
install -D -m0755 qmodbus %{buildroot}/%{_bindir}/qmodbus
install -D -m0644 data/logo.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -D -m0644 data/logo.svg %{buildroot}/%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%suse_update_desktop_file -c QModBus %{name} "ModBus master emulator with GUI" %{name} %{name} Development Electronics

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/qmodbus
%{_datadir}/applications/QModBus.desktop
%{_datadir}/icons/hicolor/256x256/apps/qmodbus.png
%{_datadir}/icons/hicolor/scalable/apps/qmodbus.svg

%changelog
