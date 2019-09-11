#
# spec file for package votca-xtp
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name: libxc
Summary: Library of exchange and correlation functionals to be used in DFT codes
Version: 4.2.3
%define sover 5
Release: 1
License: MPL-2.0
Group: Productivity/Scientific/Physics
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Source: http://www.tddft.org/programs/octopus/down.php?file=%{name}/%{version}/%{name}-%{version}.tar.gz
URL: http://www.tddft.org/programs/libxc/

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  libtool
BuildRequires:  pkg-config


%description 
Libxc is a library of exchange and correlation functionals. Its
purpose is to be used in codes that implement density-functional
theory. The library includes most of the local density
approximations (LDAs), generalized density approximation (GGAs), and
meta-GGAs. The library provides values for the energy density and its
1st, 2nd, and (for the LDAs) 3rd derivatives.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       libxc%sover = %{version}

%description devel
Libxc is a library of exchange and correlation functionals. Its
purpose is to be used in codes that implement density-functional
theory. The library includes most of the local density
approximations (LDAs), generalized density approximation (GGAs), and
meta-GGAs. The library provides values for the energy density and its
1st, 2nd, and (for the LDAs) 3rd derivatives.

This package contains development headers and libraries for libxc.

%package -n libxc%sover
Summary:        Library of exchange and correlation functionals to be used in DFT codes
Group:          System/Libraries

%description -n libxc%sover
Libxc is a library of exchange and correlation functionals. Its
purpose is to be used in codes that implement density-functional
theory. The library includes most of the local density
approximations (LDAs), generalized density approximation (GGAs), and
meta-GGAs. The library provides values for the energy density and its
1st, 2nd, and (for the LDAs) 3rd derivatives.

This package contains the library of libxc.

%prep
%setup -q

%build
%configure \
   --disable-static \
   --enable-shared
%make_build

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

%post -n libxc%sover -p /sbin/ldconfig
%postun -n libxc%sover -p /sbin/ldconfig

%files -n libxc%sover
%doc README NEWS AUTHORS ChangeLog
%license COPYING
%{_bindir}/xc-info
%{_bindir}/xc-threshold
%{_libdir}/*.so.%{sover}*

%files devel
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
