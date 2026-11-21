#
# spec file for package libmatheval
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 1
Name:           libmatheval
Version:        1.1.12
Release:        0
Summary:        Library for evaluating mathematical expressions
License:        GPL-3.0-or-later
URL:            https://www.gnu.org/software/libmatheval/
Source:         https://ftp.gnu.org/gnu/libmatheval/%{name}-%{version}.tar.gz
Source2:        https://ftp.gnu.org/gnu/libmatheval/%{name}-%{version}.tar.gz.sig
# https://savannah.gnu.org/project/release-gpgkeys.php?group=libmatheval
Source3:        %{name}.keyring

%description
GNU libmatheval is a library (callable from C and Fortran) to parse and
evaluate symbolic expressions input as text. It supports expressions in any
number of variables of arbitrary names, decimal and symbolic constants, basic
unary and binary operators, and elementary mathematical functions. In addition
to parsing and evaluation, libmatheval can also compute symbolic derivatives
and output expressions to strings.

%package -n %{name}%{sover}
Summary:        Library for evaluating mathematical expressions

%description -n %{name}%{sover}
GNU libmatheval is a library (callable from C and Fortran) to parse and
evaluate symbolic expressions input as text. It supports expressions in any
number of variables of arbitrary names, decimal and symbolic constants, basic
unary and binary operators, and elementary mathematical functions. In addition
to parsing and evaluation, libmatheval can also compute symbolic derivatives
and output expressions to strings.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}

%description devel
GNU libmatheval is a library (callable from C and Fortran) to parse and
evaluate symbolic expressions input as text. It supports expressions in any
number of variables of arbitrary names, decimal and symbolic constants, basic
unary and binary operators, and elementary mathematical functions. In addition
to parsing and evaluation, libmatheval can also compute symbolic derivatives
and output expressions to strings.

This package contains the files required to build using %{name}.

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{name}%{sover}

%files -n %{name}%{sover}
%license COPYING
%doc NEWS AUTHORS README THANKS
%{_libdir}/libmatheval.so.%{sover}{,.*}

%files devel
%license COPYING
%{_includedir}/matheval.h
%{_libdir}/libmatheval.so
%{_libdir}/pkgconfig/libmatheval.pc
%{_infodir}/libmatheval.info%{?ext_info}

%changelog
