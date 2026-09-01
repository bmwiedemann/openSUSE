#
# spec file for package qdmr
#
# Copyright (c) 2021-2026, Martin Hauke <mardnh@gmx.de>
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

%define sover   0
Name:           qdmr
Version:        0.15.1
Release:        0
Summary:        Graphical code-plug programming tool for DMR radios
License:        GPL-3.0-or-later
URL:            https://dm3mat.darc.de/qdmr/
#Git-Clone:     https://github.com/hmatuschek/qdmr.git
Source:         https://github.com/hmatuschek/qdmr/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  rsvg-convert
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Positioning)
BuildRequires:  pkgconfig(Qt6SerialPort)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6UiTools)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(yaml-cpp)

%description
qDMR is a simple to use and feature-rich code-plug programming software
(CPS) for cheap DMR radios.

Currently supported devices are:
 * Radioddity/Baofeng RD-5R
 * TYT MD-UV390
 * Retevis RT3S
 * Open GD77 firmware (GD77, RD-5R & DM-1801)
 * AnyTone AT-D878UV, AT-D868UVE
 * Radioddity GD77 (untested)

%package -n libdmrconf%{sover}
Summary:        Graphical code-plug programming tool for DMR radios

%description -n libdmrconf%{sover}
qDMR is a simple to use and feature-rich code-plug programming software
(CPS) for cheap DMR radios.

This subpackage contains shared library part of libdmrconf.

%package devel
Summary:        Development files for dmrconf
Requires:       libdmrconf%{sover} = %{version}

%description devel
qDMR is a simple to use and feature-rich code-plug programming software
(CPS) for cheap DMR radios.

This subpackage contains libraries and header files for developing
applications that want to make use of libdmrconf.

%prep
%autosetup -p1

%build
# qt6_standard_project_setup() appends an $ORIGIN install RPATH to every
# non-static target, and %%cmake only strips it on suse_version <= 1500.
%cmake \
  -DBUILD_MAN=ON \
  -DBUILD_TESTS=ON \
  -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
  -DDOCBOOK2MAN_XSLT=docbook_man.opensuse.xsl \
  -DINSTALL_UDEV_PATH=%{_udevrulesdir}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n libdmrconf%{sover}

%files
%license LICENSE
%doc README.md
%{_bindir}/dmrconf
%{_bindir}/qdmr
%{_udevrulesdir}/99-qdmr.rules
%{_datadir}/applications/qdmr.desktop
%{_datadir}/icons/hicolor/*/apps/qdmr.png
%{_datadir}/metainfo/de.darc.dm3mat.qdmr.metainfo.xml
%{_mandir}/man1/dmrconf.1%{?ext_man}
%{_mandir}/man1/qdmr.1%{?ext_man}

%files -n libdmrconf%{sover}
%{_libdir}/libdmrconf.so.%{sover}*

%files devel
%{_includedir}/libdmrconf
%{_libdir}/libdmrconf.so

%changelog
