#
# spec file for package OpenBoard
#
# Copyright (c) 2024 SUSE LLC
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


%define         namelc openboard
%define         fqname ch.%{namelc}.%{name}
Name:           OpenBoard
Version:        1.7.1
Release:        0
Summary:        Interactive whiteboard for schools and universities
License:        GPL-3.0-or-later
Group:          Amusements/Teaching/Other
URL:            https://openboard.ch
Source0:        https://github.com/OpenBoard-org/OpenBoard/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/OpenBoard-org/OpenBoard/pull/569
Patch569:       0569-scale-mirror-pixmap.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/955
Patch955:       0955-shortcut-configuration.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/961
Patch961:       0961-use-cpp20.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/962
Patch962:       0962-fix-cpp20-compatibility.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/1010
Patch1010:      1010-fix-qapp-cast.patch
# https://github.com/letsfindaway/OpenBoard/pull/117
Patch9117:      9117-disable-software-update.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5MultimediaWidgets)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(quazip1-qt5)
Recommends:     onboard

%description
OpenBoard is an open source cross-platform interactive white board
application designed primarily for use in schools. It was
originally forked from Open-Sankoré, which was itself based on
Uniboard.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if 0%{?suse_version} < 1600
%cmake
%else
%cmake -DCMAKE_CXX_STANDARD=20
%endif
%cmake_build

%install
%cmake_install
%fdupes -s %{buildroot}

%files
%license LICENSE
%doc COPYRIGHT
%{_datadir}/applications/%{fqname}.desktop
%{_datadir}/icons/hicolor/scalable
%{_datadir}/mime/packages/*
%{_datadir}/%{namelc}
%{_bindir}/%{namelc}
%config %{_sysconfdir}/%{namelc}

%changelog
