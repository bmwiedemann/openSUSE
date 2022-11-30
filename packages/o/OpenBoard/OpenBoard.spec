#
# spec file for package OpenBoard
#
# Copyright (c) 2022 SUSE LLC
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


%define         dest_dir %{_libdir}/%{name}
%define         namelc openboard
%define         fqname ch.%{namelc}.%{name}
%define         githash  9de37af2df1a7c0d88f71c94ab2db1815d082862
%define         gitshort 9de37af
%define         gitdate  20221129
%define         buildver 1129
Name:           OpenBoard
Version:        1.7.0~git%{gitdate}.%{gitshort}
Release:        0
Summary:        Interactive whiteboard for schools and universities
License:        GPL-3.0-or-later
Group:          Amusements/Teaching/Other
URL:            https://openboard.ch
Source0:        https://github.com/OpenBoard-org/OpenBoard/archive/%{githash}.zip#/OpenBoard-%{githash}.zip
# https://github.com/OpenBoard-org/OpenBoard/pull/551
Patch551:       0551-common-background-drawing.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/569
Patch569:       0569-scale-mirror-pixmap.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/677
Patch677:       0677-pdf-export-page-size.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/686
Patch686:       0686-shortcut-configuration.patch
# https://github.com/OpenBoard-org/OpenBoard/pull/698
Patch698:       0698-add-cmake-build-system.patch
# https://github.com/letsfindaway/OpenBoard/pull/117
Patch9117:      9117-disable-software-update.patch
# no github url available
Patch9686:      9686-cmake-add-shortcut-manager.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  ffmpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  pkgconfig(Qt5WebEngineWidgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(quazip1-qt5)
Recommends:     onboard

%description
OpenBoard is an open source cross-platform interactive white board
application designed primarily for use in schools. It was
originally forked from Open-Sankoré, which was itself based on
Uniboard.

This build is based on the development branch 1.7-dev and includes
a set of additional patches for features and bug fixes.

%prep
%autosetup -p1 -n %{name}-%{githash}

# remove x flag from any resource files
find resources -type f -print0 | xargs -0 chmod a-x

# remove leftover version control file
rm resources/library/applications/Calculator.wgt/.gitignore

%build
%cmake
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
