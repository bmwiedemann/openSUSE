#
# spec file for package kst
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2011 Christian Trippe ctrippe@opensuse.org
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


Name:           kst
Version:        2.1.0
Release:        0
Summary:        Real-Time Data Viewing and Plotting Tool with Basic Data Analysis Functionality
License:        GPL-2.0-or-later
URL:            https://kst-plot.kde.org/
Source:         kst-plot-%{version}.tar.zst
# PATCH-FIX-OPENSUSE
Patch0:         fix-hdf5-include-path.patch
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gsl-devel
BuildRequires:  hdf5-devel
BuildRequires:  libmatio-devel
BuildRequires:  libnetcdf_c++-devel
BuildRequires:  libqt5-linguist
BuildRequires:  netcdf-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(cfitsio)
Obsoletes:      python-kst < %{version}

%description
Kst is a data plotting and viewing program. Some of the features include:

- Robust plotting of live "streaming" data
- Powerful keyboard and mouse plot manipulation
- Powerful plug-in and extension support
- Large selection of built-in plotting and data manipulation functions,
  such as histograms, equations, and power spectra
- Color mapping and contour mapping capabilities for three-dimensional data
- Monitoring of events and notification support
- Built-in filtering and curve fitting capabilities
- Convenient command line interface
- Powerful graphical user interface

%package devel
Summary:        Development files for kst
Requires:       kst = %{version}
Requires:       cmake(Qt5Concurrent)
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5PrintSupport)
Requires:       cmake(Qt5Widgets)
Requires:       cmake(Qt5Xml)

%description devel
Development libraries and headers needed to build software
making use of kst

%prep
%autosetup -p1 -n kst-plot-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
EXTRA_FLAGS="-Dkst_install_prefix=%{_prefix} \
             -Dkst_rpath=0 \
             -Dkst_install_libdir=%{_lib} \
             -Dkst_release=1 \
             -Dkst_dbgsym=1 \
             -Dkst_python=0 \
             -Dkst_qt5=1"

%cmake $EXTRA_FLAGS

%cmake_build

%install
%cmake_install

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%license COPYING*
%doc AUTHORS NEWS README
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%dir %{_datadir}/icons/hicolor/*/mimetypes
%{_bindir}/kst2
%{_datadir}/applications/kst2.desktop
%{_datadir}/icons/hicolor/*/*/*kst.*
%{_libdir}/kst2/
%{_libdir}/libkst*.so.*
%{_mandir}/man1/kst2.1%{?ext_man}
%{_datadir}/mime/packages/x-kst.xml

%files devel
%license COPYING*
%{_libdir}/*.so
%{_libdir}/libkst2app.a

%changelog
