#
# spec file for package stp
#
# Copyright (c) 2024 SUSE LLC
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


%define sover 2_3
Name:           stp
Version:        2.3.4+20240611
Release:        0
Summary:        Constraint Solver
License:        MIT
URL:            https://github.com/stp/stp/wiki
Source0:        %{name}-%{version}.tar.xz
Patch0:         py3.patch
Patch1:         CMakeLists-use-absolute-libdir-in-rpath-handling.patch
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  minisat-devel
BuildRequires:  ninja
BuildRequires:  python3-base
BuildRequires:  xz

%description
STP is an efficient decision procedure for the validity (or satisfiability) of
formulas from a quantifier-free many-sorted theory of fixed-width bitvectors
and (non-extensional) one-dimensional arrays. The functions in STP's input
language include concatenation, extraction, left/right shift, sign-extension,
unary minus, addition, multiplication, (signed) modulo/division, bitwise
Boolean operations, if-then-else terms, and array reads and writes. The
predicates in the language include equality and (signed) comparators between
bitvector terms.

%package -n libstp%{sover}
Summary:        Constraint Solver

%description -n libstp%{sover}
STP is an efficient decision procedure for the validity (or satisfiability) of
formulas from a quantifier-free many-sorted theory of fixed-width bitvectors
and (non-extensional) one-dimensional arrays. The functions in STP's input
language include concatenation, extraction, left/right shift, sign-extension,
unary minus, addition, multiplication, (signed) modulo/division, bitwise
Boolean operations, if-then-else terms, and array reads and writes. The
predicates in the language include equality and (signed) comparators between
bitvector terms.

%package devel
Summary:        Devel files for stp
Requires:       %{name} = %{version}
Requires:       libstp%{sover} = %{version}
Requires:       minisat-devel
%if 0%{?suse_version} > 1320
Requires:       libboost_program_options-devel
%else
Requires:       boost-devel
%endif

%description devel
Developmnet files for stp library.

%package -n python3-stp
Summary:        Python bindings for stp
Requires:       libstp%{sover} = %{version}
BuildArch:      noarch

%description -n python3-stp
Python bindings for stp library.

%prep
%autosetup -p1

%build
%define __builder ninja
%cmake \
	-DPython_ADDITIONAL_VERSIONS=3 \
	-DALSO_BUILD_STATIC_LIB:BOOL="off" \
	-DSTP_TIMESTAMPS:BOOL="off"
%cmake_build

%install
%cmake_install

install -d %{buildroot}/%{_docdir}/%{name}/example
install -m 644 -t %{buildroot}/%{_docdir}/%{name}/example examples/simple/*

%post -n libstp%{sover} -p /sbin/ldconfig
%postun -n libstp%{sover} -p /sbin/ldconfig

%files
%doc AUTHORS README.markdown
%license LICENSE
%{_bindir}/stp*
%exclude %{_docdir}/%{name}/example/

%files -n libstp%{sover}
%{_libdir}/libstp.so.*

%files devel
%dir %{_includedir}/stp/
%{_includedir}/stp/*.h
%dir %{_libdir}/cmake/
%{_libdir}/libstp.so
%{_libdir}/cmake/STP/
%{_docdir}/%{name}/example/

%files -n python3-stp
%{python3_sitelib}/*

%changelog
