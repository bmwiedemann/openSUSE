#
# spec file for package framel
#
# Copyright (c) 2020 SUSE LLC
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


%global shlib lib%{name}8
Name:           framel
Version:        8.40.1
Release:        0
Summary:        Library to manipulate Gravitational Wave Detector data in frame format
License:        LGPL-2.1-or-later
URL:            https://lappweb.in2p3.fr/virgo/FrameL/
Source:         http://software.igwn.org/lscsoft/source/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM framel-fix-pkgconfig.patch badshah400@gmail.com -- Fix include and lib dir paths in pkgconfig file
Patch0:         framel-fix-pkgconfig.patch
BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-setuptools

%description
A Common Data Frame Format for Interferometric Gravitational Wave Detector has
been developed by VIRGO and LIGO. The Frame Library is a software in C
language, with interfaces to python and matlab, dedicated to frame data
manipulation including file input/output.

%package -n %{shlib}
Summary:        Shared library for framel - a library for gravitational wave frame data

%description -n %{shlib}
The Frame Library is a software in C language, with interfaces to python and
matlab, dedicated to frame data manipulation including file input/output.

This package provides the shared library for framel.

%package devel
Summary:        Headers and sources for developing with the gravitational wave frame library
Requires:       %{shlib} = %{version}

%description devel
The Frame Library is a software in C language, with interfaces to python and
matlab, dedicated to frame data manipulation including file input/output.

This package property the headers and sources needed to develop applications
against the frame library.

%package -n python3-%{name}
Summary:        Python module for framel - a library for gravitational wave frame data
Requires:       python3

%description -n python3-%{name}
The Frame Library is a software in C language, with interfaces to python and
matlab, dedicated to frame data manipulation including file input/output.

This package provides the python3 module for frame library.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{name} \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
  -DENABLE_PYTHON=yes

%cmake_build

%install
%cmake_install

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/*

%files -n %{shlib}
%{_libdir}/libframel.so.*

%files devel
%license LICENSE
%doc %{_docdir}/%{name}
%{_includedir}/%{name}/
%{_libdir}/libframel.so
%{_libdir}/pkgconfig/*.pc

%files -n python3-%{name}
%license LICENSE
%{python3_sitearch}/*

%changelog
