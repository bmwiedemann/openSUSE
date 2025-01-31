#
# spec file for package blis
#
# Copyright (c) 2025 SUSE LLC
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


# Config to build blis with
%ifarch x86_64
%define blis_config x86_64
%else
%ifarch %{arm64}
%define blis_config arm64
# Error when building with LTO on arm64
%define _lto_cflags %{nil}
%else
%define blis_config generic
%endif
%endif
%define sover 4
%define shlib lib%{name}%{sover}
Name:           blis
Version:        1.1
Release:        0
Summary:        BLAS-like Library Instantiation Software Framework
License:        BSD-3-Clause
URL:            https://github.com/flame/blis
Source:         %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3

%description
BLIS is a portable software framework for instantiating high-performance
BLAS-like dense linear algebra libraries. The framework was designed to isolate
essential kernels of computation that, when optimized, immediately enable
optimized implementations of most of its commonly used and computationally
intensive operations. BLIS is written in ISO C99.

%package -n %{shlib}
Summary:        Shared library for blis

%description -n %{shlib}
BLIS is a portable software framework for instantiating high-performance
BLAS-like dense linear algebra libraries. The framework was designed to isolate
essential kernels of computation that, when optimized, immediately enable
optimized implementations of most of its commonly used and computationally
intensive operations. BLIS is written in ISO C99.

This package provides the shared library for blis.

%package devel
Summary:        Headers and devel files for blis
Requires:       %{shlib} = %{version}
# Both cblas-devel and blis-devel provide a %%{_includedir}/cblas.h header file
# and the latter is a drop-in replacement for the former
Conflicts:      cblas-devel

%description devel
BLIS is a portable software framework for instantiating high-performance
BLAS-like dense linear algebra libraries. The framework was designed to isolate
essential kernels of computation that, when optimized, immediately enable
optimized implementations of most of its commonly used and computationally
intensive operations. BLIS is written in ISO C99.

This package provides the headers and devel files for %{name}.

%prep
%autosetup

%build
export CFLAGS="%{optflags}"
# Not an autotools configure script
./configure                          \
  --disable-rpath                    \
  --disable-static                   \
  --enable-verbose-make              \
  --enable-cblas                     \
  --enable-debug=opt                 \
  --prefix=%{_prefix}                \
  --libdir=%{_libdir}                \
  --enable-threading=openmp,pthreads \
%{blis_config}
%make_build
%make_build -C testsuite

%install
%make_install

# Manually remove rpath from pkgconfig file
sed -i "s/\-Wl,\-rpath.* //g" %{buildroot}%{_datadir}/pkgconfig/blis.pc

%check
pushd testsuite
./test_libblis.x

%ldconfig_scriptlets -n %{shlib}

%files -n %{shlib}
%{_libdir}/lib%{name}.so.*

%files devel
%license LICENSE
%doc CHANGELOG README.md docs/ReleaseNotes.md
%{_includedir}/*.h
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_datadir}/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
