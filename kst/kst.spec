#
# spec file for package kst
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           kst
Version:        2.0.8
Release:        0
Summary:        Real-Time Data Viewing and Plotting Tool with Basic Data Analysis Functionality
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Visualization/Graph
URL:            http://kst-plot.kde.org/
Source:         Kst-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gsl2-support.patch -- fixes build with GSL-2.0
Patch0:         gsl2-support.patch
# PATCH-FIX-UPSTREAM -- Fix-build-with-Qt-511.patch -- Fixes build with Qt 5.11
Patch1:         Fix-build-with-Qt-511.patch
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  getdata-devel
BuildRequires:  gsl-devel
BuildRequires:  libcfitsio-devel
BuildRequires:  libmatio-devel
BuildRequires:  libnetcdf
BuildRequires:  libnetcdf_c++-devel
BuildRequires:  netcdf-devel
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
Requires:       libnetcdf
Obsoletes:      python-kst < %{version}
%if 0%{?suse_version} >= 1500
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
%else
BuildRequires:  libqt4-devel
%endif

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
%if 0%{?suse_version} >= 1500
Requires:       pkgconfig(Qt5Concurrent)
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5Network)
Requires:       pkgconfig(Qt5PrintSupport)
Requires:       pkgconfig(Qt5Widgets)
Requires:       pkgconfig(Qt5Xml)
%else
Requires:       libqt4-devel
%endif

%description devel
Development libraries and headers needed to build software
making use of %{name}

%prep
%autosetup -p1 -n Kst-2.0.8

%build
EXTRA_FLAGS="-Dkst_install_prefix=%{_prefix} \
             -Dkst_rpath=0 \
             -Dkst_install_libdir=%{_lib} \
             -Dkst_release=1 \
             -Dkst_dbgsym=1 \
             -Dkst_python=0 \
%if 0%{?suse_version} >= 1500
             -Dkst_qt5=1"
%else
             -Dkst_qt4=1"
%endif

%cmake $EXTRA_FLAGS
make %{?_smp_mflags}

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
