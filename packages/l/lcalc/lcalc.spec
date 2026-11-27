#
# spec file for package lcalc
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lname libLfunction2
Name:           lcalc
Version:        2.2.2
Release:        0
Summary:        L-function calculator
License:        GPL-2.0-or-later
URL:            https://gitlab.com/sagemath/lcalc
Source0:        https://gitlab.com/-/project/12934202/uploads/79611ba9b2a4ca214df935f43978e2de/lcalc-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  make
BuildRequires:  pari-devel
BuildRequires:  pkgconfig
Requires:       %{lname} = %{version}

%description
Michael Rubinstein's L-function calculator and C++ library for calculating
with L-functions.

%package -n %{lname}
Summary:        L-function computation library

%description -n %{lname}
Shared library for calculating with L-functions.

%package -n libLfunction-devel
Summary:        Development files for libLfunction
Requires:       %{lname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n libLfunction-devel
Development and header files for the L-function computation library.

%prep
%autosetup -n lcalc-%{version}

%build
%configure --disable-static --with-pari
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm %{buildroot}/usr/share/doc/lcalc/INSTALL

%ldconfig_scriptlets -n %{lname}

%files
%license doc/COPYING
%{_bindir}/lcalc
%{_mandir}/man1/lcalc.1%{?ext_man}
%{_datadir}/doc/lcalc

%files -n %{lname}
%{_libdir}/libLfunction.so.2*

%files -n libLfunction-devel
%{_includedir}/lcalc
%{_libdir}/libLfunction.so
%{_libdir}/pkgconfig/lcalc.pc

%changelog
