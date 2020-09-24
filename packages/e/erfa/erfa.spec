#
# spec file for package erfa
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


%define lname	liberfa1
Name:           erfa
Version:        1.7.1
Release:        0
Summary:        Essential Routines for Fundamental Astronomy
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://github.com/liberfa/erfa
Source:         https://github.com/liberfa/erfa/releases/download/v%{version}/erfa-%{version}.tar.gz
BuildRequires:  pkgconfig

%description
ERFA is a C library containing key algorithms for astronomy, and is based on
the SOFA library published by the International Astronomical Union (IAU).

%package -n %{lname}
Summary:        Essential Routines for Fundamental Astronomy
Group:          System/Libraries

%description -n %{lname}
ERFA is a C library containing key algorithms for astronomy, and is based on
the SOFA library published by the International Astronomical Union (IAU).

ERFA is intended to replicate the functionality of SOFA (aside from possible
bugfixes in ERFA that have not yet been included in SOFA), but is licensed
under a three-clause BSD license to enable its compatibility with a wide
range of open source licenses. Permission for this release has been obtained
from the SOFA board, and is avilable in the LICENSE file included in this
source distribution.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description    devel
This package contains libraries and header files for developing
applications that use %{name}.

%package        devel-static
Summary:        Static development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description    devel-static
This package contains libraries and header files for developing
applications that link statically to %{name}.

%prep
%setup -q

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
%configure
make %{?_smp_mflags}

%install
%make_install
# *.la should not be packaged (see packaging guidelines: static Libraries)
rm %{buildroot}%{_libdir}/liberfa.la

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSE
%doc INFO README.rst
%{_libdir}/liberfa.so.1
%{_libdir}/liberfa.so.1.*

%files devel
%{_includedir}/*.h
%{_libdir}/liberfa.so
%{_libdir}/pkgconfig/erfa.pc

%files devel-static
%{_libdir}/liberfa.a

%changelog
