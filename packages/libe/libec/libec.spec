#
# spec file for package libec
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


%define lname   libec16
Name:           libec
Version:        20261021
Release:        0
Summary:        Programs and library for computing with elliptic curves
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/JohnCremona/eclib
Source0:        https://github.com/JohnCremona/eclib/releases/download/v%{version}/eclib-%{version}.tar.bz2
BuildRequires:  binutils
BuildRequires:  boost-devel
BuildRequires:  flint-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  ntl-devel
BuildRequires:  pari-devel
BuildRequires:  pkgconfig
Requires:       %{lname} = %{version}
Provides:       eclib = %{version}

%description
eclib includes a library and programs for calculations on elliptic
curves and modular forms, including the mwrank program for 2-descent
on elliptic curves over Q.

%package -n %{lname}
Summary:        Library for computing with elliptic curves
Group:          System/Libraries

%description -n %{lname}
eclib is a library for computing with elliptic curves and modular forms.
This package contains the shared library libec.

%package devel
Summary:        Development files for eclib
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       flint-devel
Requires:       ntl-devel
Requires:       pari-devel
Provides:       eclib-devel = %{version}
Provides:       libec-devel = %{version}

%description devel
Development headers and library files for developing applications
with eclib.

%prep
%autosetup -n eclib-%{version}

%build
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{lname}

%files
%license COPYING
%doc README NEWS
%{_bindir}/*
%{_mandir}/man1/mwrank.1%{?ext_man}
%{_datadir}/doc/eclib

%files -n %{lname}
%{_libdir}/libec.so.16*

%files devel
%{_includedir}/eclib
%{_libdir}/libec.so
%{_libdir}/pkgconfig/eclib.pc

%changelog
