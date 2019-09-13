#
# spec file for package MotionBox
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


Name:           MotionBox
Version:        1.5.0
Release:        0
Summary:        Qt based network video browser
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Video/Players
URL:            http://omega.gg/MotionBox
Source0:        https://github.com/omega-gg/MotionBox/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/omega-gg/Sky/archive/%{version}.tar.gz#/Sky-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Sky-1.5.0-private_headers.patch
Patch0:         Sky-1.5.0-private_headers.patch
# PATCH-FIX-OPENSUSE MotionBox-1.5.0-paths.patch
Patch1:         MotionBox-1.5.0-paths.patch
# PATCH-FIX-OPENSUSE SKy-1.5.0-soname.patch
Patch2:         Sky-1.5.0-soname.patch
# PATCH-FEATURE-OPENSUSE Sky-1.5.0-use_system_glext.patch
Patch3:         Sky-1.5.0-use_system_glext.patch
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libboost_chrono-devel
BuildRequires:  libboost_random-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtdeclarative-private-headers-devel
BuildRequires:  update-desktop-files
BuildRequires:  vlc-devel
BuildRequires:  wt-devel
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(libtorrent-rasterbar)
Requires:       vlc
ExclusiveArch:  %ix86 x86_64

%description
A network video browser based on Qt.
It streams Torrents, Youtube, Dailymotion, Vimeo and SoundCloud.

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
mv Sky-%{version} Sky

%build
pushd Sky
%qmake5
make %{?_smp_mflags}
popd
pushd dist
sh ./qrc.sh qt5 linux deploy
popd
%qmake5
make %{?_smp_mflags}

%install
mkdir -pv %{buildroot}/%{_bindir} %{buildroot}%{_libdir} %{buildroot}/%{_datadir}/pixmaps
install -m0755 latest/%{name} %{buildroot}/%{_bindir}
install -m0755 Sky/latest/libSkBackend.so Sky/latest/libSkCore.so \
               Sky/latest/libSkGui.so Sky/latest/libSkMedia.so \
               Sky/latest/libSkTorrent.so -t %{buildroot}%{_libdir}
install -Tm0644 content/pictures/icons/icon.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
%suse_update_desktop_file -c %{name} %{name} 'Online video player' %{name} %{name} AudioVideo Video Player

%files
%doc README.md
%license LICENSE.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_libdir}/libSkBackend.so
%{_libdir}/libSkCore.so
%{_libdir}/libSkGui.so
%{_libdir}/libSkMedia.so
%{_libdir}/libSkTorrent.so

%changelog
