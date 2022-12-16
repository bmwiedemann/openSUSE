#
# spec file for package libxc
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 12
Name:           libxc
Version:        6.0.0
Release:        0
Summary:        Library of exchange and correlation functionals to be used in DFT codes
License:        MPL-2.0
Group:          Productivity/Scientific/Physics
URL:            https://www.tddft.org/programs/libxc/
Source:         https://www.tddft.org/programs/libxc/down.php?file=%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  pkgconfig

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
Requires:       libxc%{sover} = %{version}
# Work-around for incorrectly packaging a binary with the shared lib package
Conflicts:      libxc5 <= 4.2.3

%description devel
Libxc is a library of exchange and correlation functionals. Its
purpose is to be used in codes that implement density-functional
theory. The library includes most of the local density
approximations (LDAs), generalized density approximation (GGAs), and
meta-GGAs. The library provides values for the energy density and its
1st, 2nd, and (for the LDAs) 3rd derivatives.

This package contains development headers and libraries for libxc.

%package -n libxc%{sover}
Summary:        Library of exchange and correlation functionals to be used in DFT codes
Group:          System/Libraries

%description -n libxc%{sover}
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
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libxc%{sover} -p /sbin/ldconfig
%postun -n libxc%{sover} -p /sbin/ldconfig

%files -n libxc%{sover}
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc README NEWS AUTHORS ChangeLog
%license COPYING
%{_bindir}/xc-info
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
