#
# spec file for package volk
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

%global sonum 2
%global soname 2_0

Name:           volk
Version:        2.0.0
Release:        0
Summary:        Vector-Optimized Library of Kernels
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            http://libvolk.org/
Source:         https://github.com/gnuradio/volk/releases/download/v%{version}/volk-v%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  fdupes
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  orc
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Mako
BuildRequires:  python3-six

%description
VOLK provides a library of vector-optimized kernels. It is a subproject
of GNU Radio, but can also be used standalone.

%package devel
Summary:        Development files for VOLK
# Formerly part of gnuradio 3.7.x.y
Requires:       libvolk%{soname} = %{version}
Conflicts:      gnuradio-devel < 3.8.0.0
Provides:       gnuradio-devel:%{_libdir}/pkgconfig/volk.pc
Recommends:     volk_modtool

%description devel
This package provides the the development files for VOLK.

%package -n libvolk%{soname}
Summary:        VOLK shared library
Group:          System/Libraries
Recommends:     volk

%description -n libvolk%{soname}
This package provides the VOLK shared library.

%package -n volk_modtool
Summary:        VOLK modtool

%description -n volk_modtool
This package provides volk_modtool, used for creating new
VOLK kernels.

%prep
%setup -q -n volk-v%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

chmod -x %{buildroot}%{python3_sitearch}/volk_modtool/*py
sed -i -e '1 { \@.*/bin/env.*python.*@ d }' %{buildroot}%{python3_sitearch}/volk_modtool/*py

%fdupes %{buildroot}

%post -n libvolk%{soname} -p /sbin/ldconfig
%postun -n libvolk%{soname} -p /sbin/ldconfig

%files
%license COPYING
%doc CHANGELOG.md README.md
%{_bindir}/volk_profile

%files devel
%{_bindir}/volk-config-info
%{_includedir}/volk
%{_libdir}/cmake/volk
%{_libdir}/libvolk.so
%{_libdir}/pkgconfig/volk.pc

%files -n libvolk%{soname}
%{_libdir}/libvolk.so.%{sonum}*

%files -n volk_modtool
%doc python/volk_modtool/README
%{_bindir}/volk_modtool
%{python3_sitearch}/volk_modtool

%changelog

