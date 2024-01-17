#
# spec file for package gmp-ecm
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


%define so_version 1
Name:           gmp-ecm
Version:        7.0.5
Release:        0
Summary:        Elliptic Curve Method for Integer Factorization
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://gitlab.inria.fr/zimmerma/ecm
Source0:        https://gitlab.inria.fr/zimmerma/ecm/uploads/89f6f0d65d3e980cef33dc922004e4b2/ecm-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ecm-auxi.c.patch -- Add missing stdlib.h include
BuildRequires:  gmp-devel >= 5.0.0
BuildRequires:  m4

%description
GMP-ECM reads the numbers to be factored from stdin (one number on each
line) and requires a numerical parameter, the stage 1 bound B1. A reasonable
stage 2 bound B2 for the given B1 is chosen by default, but can be overridden
by a second numerical parameter. By default, GMP-ECM uses the ECM factoring
algorithm.

%package -n libecm%{so_version}
Summary:        Library for Elliptic Curve Integer Factorization
Group:          System/Libraries

%description -n libecm%{so_version}
Library for ecm. To use the library, you need to install ecm-devel, include
"ecm.h" in your source file and link with -lecm.

%package devel
Summary:        Development files for the gmp-ecm package
Group:          Development/Libraries/C and C++
Requires:       libecm%{so_version} = %{version}

%description devel
This package contains header files required when building applications which
use the libecm library.

%prep
%setup -q -n ecm-%{version}

%build
%configure \
%ifnarch x86_64
    --disable-sse2 \
%endif
    --disable-shellcmd \
    --enable-shared \
    --disable-static

%make_build

%install
%make_install

rm %{buildroot}/%{_libdir}/libecm.la

%check
%make_build check

%post -n libecm%{so_version} -p /sbin/ldconfig
%postun -n libecm%{so_version} -p /sbin/ldconfig

%files
%license COPYING COPYING.LIB
%doc AUTHORS NEWS README README.lib
%{_bindir}/ecm
%{_mandir}/man1/ecm.1%{?ext_man}

%files devel
%{_includedir}/ecm.h
%{_libdir}/libecm.so

%files -n libecm%{so_version}
%{_libdir}/libecm.so.*

%changelog
