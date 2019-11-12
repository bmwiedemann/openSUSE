#
# spec file for package qgroundcontrol
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           qgroundcontrol
Version:        3.6.0~pre.1570775458.0d1bb4844
Release:        0
Summary:        An operator control unit / ground control software for micro air vehicles
License:        GPL-3.0-only
Group:          Other
Url:            http://www.qgroundcontrol.org/
Source0:        qgroundcontrol-%{version}.tar.xz
Patch2:         fix-install.patch
# ModemManager has the broken design to grab any serial port first
# as background daemon. this breaks any other app which needs to access the device
# on boot up (for firmware update here)
Conflicts:      ModemManager
%if 0%{?fedora_version}
BuildRequires:  python2
BuildRequires:  systemd-devel
%else
BuildRequires:  libqt5-qtlocation-private-headers-devel
BuildRequires:  libudev-devel
%endif

BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Core) >= 5.11
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Positioning)
BuildRequires:  pkgconfig(Qt5ScriptTools)
BuildRequires:  pkgconfig(Qt5SerialPort)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(Qt5Qwt6)
%endif

BuildRequires:  SDL2-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  libicu-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libudev-devel
BuildRequires:  openssl-devel
# is not building atm
#BuildRequires:  libxbee3-devel
BuildRequires:  fdupes

#qml deps
Requires:       libqt5-qtgraphicaleffects
Requires:       libqt5-qtquickcontrols

%description
QGroundControl is an operator control unit / ground control software
for micro air vehicles. It allows to visualize and control a micro
air vehicle during development and operation, both indoors and
outdoors. With a flexible software architecture, it supports multiple
MAV types/autopilot projects.

%prep
%setup -q
%patch2 -p1
mkdir build

%build
cd build
qmake-qt5 ../qgroundcontrol.pro
make %{?_smp_mflags}

%install
cd build
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/
cp -R release/flightgear %{buildroot}/%{_datadir}/%{name}/
install -p -m 755 release/QGroundControl %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/usr/share/{applications,pixmaps}
install -p -m 0644 ../deploy/qgroundcontrol.desktop %{buildroot}/usr/share/applications/
install -p -m 0644 ../resources/icons/qgroundcontrol.png %{buildroot}/usr/share/pixmaps/
sed -i -e 's/^Categories=.*/Categories=Development;Building;/' %{buildroot}/usr/share/applications/qgroundcontrol.desktop
%fdupes %{buildroot}%{_prefix}

%files
%license COPYING.md
%doc README.md
%attr(0755,root,root) %{_bindir}/QGroundControl
%{_datadir}/%{name}
/usr/share/applications/*
/usr/share/pixmaps/*

%changelog
