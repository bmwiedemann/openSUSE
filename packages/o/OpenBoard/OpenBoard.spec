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
Version:        1.7.2
Release:        0
Summary:        Interactive whiteboard for schools and universities
License:        GPL-3.0-or-later
Group:          Amusements/Teaching/Other
URL:            https://openboard.ch
Source0:        https://github.com/OpenBoard-org/OpenBoard/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/OpenBoard-org/OpenBoard/pull/955
Patch955:       0955-shortcut-configuration.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/1165
Patch1165:      1165-fix-some-wayland-problems.patch
# https://github.com/letsfindaway/OpenBoard/pull/117
Patch9117:      9117-disable-software-update.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(quazip1-qt6)
Recommends:     onboard
%if 0%{?suse_version} < 1600
BuildRequires:  gcc10-c++
%endif

%description
OpenBoard is an open source cross-platform interactive white board
application designed primarily for use in schools. It was
originally forked from Open-Sankoré, which was itself based on
Uniboard.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if 0%{?suse_version} < 1600
export CXX=%{_bindir}/g++-10
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
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/icons/hicolor/scalable/mimetypes
%{_datadir}/applications/%{fqname}.desktop
%{_datadir}/icons/hicolor/scalable
%{_datadir}/mime/packages/*
%{_datadir}/%{namelc}
%{_bindir}/%{namelc}
%config %{_sysconfdir}/%{namelc}

%changelog
