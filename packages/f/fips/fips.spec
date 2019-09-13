#
# spec file for package fips
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fips
Version:        3.3.1
Release:        0
Summary:        OpenGL-based FITS image viewer
License:        LGPL-3.0-only
Group:          Productivity/Scientific/Astronomy
Url:            https://github.com/matwey/fips3
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Test-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  make
BuildRequires:  update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FIPS is a cross-platform FITS viewer with responsive user interface. Unlike
other FITS viewers FIPS uses GPU hardware via OpenGL to provide usual
functionality such as zooming, panning and level adjustments. OpenGL 2.1 and
later is supported.

FIPS supports all 2D image formats except of 64-bit floating point numbers
(BITPIX=-64). FITS image extension has basic limited support.

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install
%suse_update_desktop_file -i space.fips.Fips

%check
%ctest

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/space.fips.Fips.desktop
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/space.fips.Fips.png
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/256x256/apps
%{_datadir}/icons/hicolor/256x256/apps/space.fips.Fips.png
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/space.fips.Fips.svg

%changelog
