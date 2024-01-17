#
# spec file for package ucpp
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


%define libname libucpp13
Name:           ucpp
Version:        1.3.5
Release:        0
Summary:        A preprocessor compliant to C99
License:        BSD-3-Clause
Group:          Development/Tools/Building
URL:            https://gitlab.com/scarabeusiv/ucpp/
Source:         https://gitlab.com/scarabeusiv/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
ucpp is a preprocessor for C source code, specifically code compliant to the
ISO standard 9899:1999, also known as C99. A preprocessor is responsible for
macro replacement, conditional compilation and inclusion of header files.

ucpp operates in two modes:
-- lexer mode: ucpp is linked to some other code and outputs a stream of
tokens (each call to the lex() function will yield one token)
-- non-lexer mode: ucpp preprocesses text and outputs the resulting text
to a file descriptor; if linked to some other code, the cpp() function
must be called repeatedly, otherwise ucpp is a stand-alone binary.

%package -n %{libname}
Summary:        A Mixed Integer Linear Programming (MILP) Solver Library
Group:          Development/Libraries/Other

%description -n %{libname}
ucpp is a preprocessor for C source code, specifically code compliant to the
ISO standard 9899:1999, also known as C99. A preprocessor is responsible for
macro replacement, conditional compilation and inclusion of header files.

ucpp, built as a library, outputs tokens, one at a time, on demand,
as an integrated lexer.

%package devel
Summary:        Files for Developing with ucpp
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Includes and definitions for developing with the ucpp library.

%prep
%setup -q

%build
autoreconf -fvi
%configure \
    --disable-silent-rules \
    --disable-werror \
    --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/*
%{_mandir}/man1/ucpp.1%{?ext_man}

%files -n %{libname}
%license COPYING
%{_libdir}/*.so.1*

%files devel
%{_includedir}/lib%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib%{name}*.pc

%changelog
