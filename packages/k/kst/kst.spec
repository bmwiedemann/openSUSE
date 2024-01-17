#
# spec file for package kst
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.0.8
Release:        0
Summary:        Real-Time Data Viewing and Plotting Tool with Basic Data Analysis Functionality
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Visualization/Graph
URL:            https://kst-plot.kde.org/
Source:         Kst-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gsl2-support.patch -- fixes build with GSL-2.0
Patch0:         gsl2-support.patch
# PATCH-FIX-UPSTREAM -- Fix-build-with-Qt-511.patch -- Fixes build with Qt 5.11
Patch1:         Fix-build-with-Qt-511.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-build-with-CMake-3.20.patch
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gsl-devel
BuildRequires:  libmatio-devel
BuildRequires:  libnetcdf_c++-devel
BuildRequires:  libqt5-linguist
BuildRequires:  netcdf-devel
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
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
Summary:        Development files for %{name}
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       cmake(Qt5Concurrent)
Requires:       cmake(Qt5Core)
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5PrintSupport)
Requires:       cmake(Qt5Widgets)
Requires:       cmake(Qt5Xml)

%description devel
Development libraries and headers needed to build software
making use of %{name}

%prep
%autosetup -p1 -n Kst-2.0.8

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
%suse_update_desktop_file -r %{name}2 Qt KDE Science Math
%fdupes %{buildroot}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc AUTHORS NEWS README
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%dir %{_datadir}/kst
%dir %{_datadir}/kst/locale
%{_bindir}/%{name}2
%{_datadir}/applications/%{name}2.desktop
%{_datadir}/applnk/
%{_datadir}/icons/hicolor/*/apps/*%{name}.*
%{_datadir}/kst/locale/kst_common_*.qm
%{_datadir}/mimelink/
%{_libdir}/%{name}2/
%{_libdir}/lib%{name}*.so.*
%{_mandir}/man1/%{name}2.1%{?ext_man}

%files devel
%license COPYING*
%{_libdir}/*.so
%{_libdir}/lib%{name}2app.a

%changelog
