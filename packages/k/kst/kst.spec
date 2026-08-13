#
# spec file for package kst
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define qt6_version 6.4.0
Name:           kst
Version:        3.0.0
Release:        0
Summary:        Real-Time Data Viewing and Plotting Tool with Basic Data Analysis Functionality
License:        GPL-2.0-or-later
URL:            https://kst-plot.kde.org/
Source0:        https://sourceforge.net/projects/kst/files/Kst%%20%{version}/kst-plot-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Concurrent) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Designer) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Network) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  cmake(hdf5)
BuildRequires:  cmake(tiff)
BuildRequires:  pkgconfig(cfitsio)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(matio)
# Not available in Leap 16
%if 0%{?suse_version} > 1600
# Not available for all archs
%ifnarch %arm %ix86 s390x
BuildRequires:  pkgconfig(netcdf-cxx4)
%endif
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

%prep
%autosetup -p1 -n kst-plot-%{version}

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects

rm -r cmake/3rdparty

%cmake_qt6

%qt6_build

%install
%qt6_install

# Useless
rm -r %{buildroot}%{_includedir}
rm -r %{buildroot}%{_libdir}/kst/libKst6App.a

%fdupes %{buildroot}

%ldconfig_scriptlets

%files
%license COPYING*
%doc AUTHORS NEWS README
%{_bindir}/kst
%{_datadir}/applications/org.kde.kst.desktop
%{_datadir}/icons/hicolor/*/*/*kst.*
%{_datadir}/metainfo/org.kde.kst.metainfo.xml
%{_datadir}/mime/packages/x-kst.xml
%{_libdir}/kst/
%{_mandir}/man1/kst.1%{?ext_man}

%changelog
