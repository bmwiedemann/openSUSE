#
# spec file for package ccache
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


# Build with hiredis by default only on TW
%if %{?suse_version} > 1600
%bcond_without hiredis
%else
%bcond_with hiredis
%endif
Name:           ccache
Version:        4.10.1
Release:        0
Summary:        A Fast C/C++ Compiler Cache
License:        GPL-3.0-or-later
URL:            https://ccache.dev/
Source0:        https://github.com/ccache/ccache/releases/download/v%{version}/ccache-%{version}.tar.xz
Source1:        https://github.com/ccache/ccache/releases/download/v%{version}/ccache-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  fmt-devel
%if %{?suse_version} > 1600
BuildRequires:  gcc
BuildRequires:  gcc-c++
# SLE requires gcc11 for std::filesystem
%else
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%endif
BuildRequires:  libzstd-devel
BuildRequires:  pkgconfig
BuildRequires:  xxhash-devel
BuildRequires:  pkgconfig(libzstd) >= 1.1.2
BuildRequires:  rubygem(asciidoctor)
Provides:       distcc:%{_bindir}/ccache
%ifnarch %{ix86} %{arm}
%endif
%if %{with hiredis}
BuildRequires:  pkgconfig(hiredis) >= 0.13.3
%endif

%description
ccache is a compiler cache. It speeds up recompilation by caching the
result of previous compilations and detecting when the same compilation is
being done again. Supported languages are C, C++, Objective-C and
Objective-C++.

%prep
%autosetup -p1

%build
%if %{?suse_version} < 1600
export CC=gcc-11 CXX=g++-11
%endif
%cmake \
  -DFETCHCONTENT_FULLY_DISCONNECTED=ON \
%if !%{with hiredis}
  -DREDIS_STORAGE_BACKEND=OFF \
%endif
%{nil}
%cmake_build
%make_build doc

%install
%cmake_install

# create the compat symlinks into /usr/libdir/ccache
mkdir -p %{buildroot}/%{_libdir}/%{name}
cd %{buildroot}/%{_libdir}/%{name}
ln -sf ../../bin/%{name} gcc
ln -sf ../../bin/%{name} g++
ln -sf ../../bin/%{name} gcc-objc
ln -sf ../../bin/%{name} gfortran
# do the same for clang
ln -sf ../../bin/%{name} clang
ln -sf ../../bin/%{name} clang++
# and regular cc
ln -sf ../../bin/%{name} cc
ln -sf ../../bin/%{name} c++
# and for nvidia cuda
ln -sf ../../bin/%{name} nvcc

%check
# running the test with multiple threads will make tests fail
%{__ctest} --output-on-failure --force-new-ctest-process -j1

%files
%license LICENSE.* GPL-3.0.txt
%doc doc/AUTHORS.* doc/MANUAL.* doc/NEWS.* README.*
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
