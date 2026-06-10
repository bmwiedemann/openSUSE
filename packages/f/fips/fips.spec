#
# spec file for package fips
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           fips
Version:        3.5.0
Release:        0
Summary:        OpenGL-based FITS image viewer
License:        LGPL-3.0-only
Group:          Productivity/Scientific/Astronomy
URL:            https://github.com/matwey/fips3
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++ >= 8
BuildRequires:  make
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Test)
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
%cmake -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON -DQT_INTERNAL_SKIP_DEPLOYMENT:BOOL=ON
%make_jobs

%install
%cmake_install

%check
%ctest

%files
%doc README.md
%license LICENSE.txt
%{_bindir}/%{name}
%{_datadir}/applications/space.fips.Fips.desktop
%{_datadir}/metainfo/space.fips.Fips.metainfo.xml
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
