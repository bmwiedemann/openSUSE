#
# spec file for package clazy
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


%define release_ver v1.17
Name:           clazy
Version:        1.17
Release:        0
Summary:        Qt oriented code checker based on the Clang framework
License:        LGPL-2.0-or-later
URL:            https://apps.kde.org/clazy/
Source0:        https://download.kde.org/stable/clazy/%{version}/src/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/clazy/%{version}/src/%{name}-%{version}.tar.xz.sig
# https://invent.kde.org/sysadmin/release-keyring/-/blob/master/keys/alex@key1.asc?ref_type=heads
Source2:        clazy.keyring
BuildRequires:  clang
BuildRequires:  clang-devel >= 19.0
BuildRequires:  cmake >= 3.13
%if 0%{?suse_version} == 1500
BuildRequires:  gcc14-PIE
BuildRequires:  gcc14-c++
%endif
BuildRequires:  libstdc++-devel
Requires:       clang
%requires_eq    libclang%{_libclang_sonum}
%requires_eq    libLLVM%{_llvm_sonum}
%requires_eq    libclang-cpp%{_llvm_sonum}

%description
clazy is a compiler plugin which allows Clang to understand Qt semantics.
You get more than 50 Qt related compiler warnings, ranging from unneeded memory
allocations to misusage of API, including fix-its for automatic refactoring.

%prep
%autosetup -p1 -n %{name}-%{release_ver}

# When exporting CXX=clazy, the executable matching libraries used to build clazy must be used
# NOTE: 'readlink -f' can't be used, or the result won't be 'clang++-xx' but 'clang-xx', which will cause linker errors
sed -i "s#CLANGXX:-clang++#CLANGXX:-clang++-%{_llvm_sonum}#" clazy.cmake

%build
%define _lto_cflags %{nil}

%if 0%{?suse_version} == 1500
export CXX=g++-14
%endif

# The clang-tidy plugin must be built without '-Wl,--no-undefined'
%cmake \
  -DCMAKE_INSTALL_DOCDIR=%{_datadir}/doc/clazy \
  -DCMAKE_EXE_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now" -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed -Wl,-z,now"

%cmake_build

%install
%cmake_install

sed -i 's#%{_bindir}/env sh$#/bin/sh#' %{buildroot}%{_bindir}/clazy

%files
%license LICENSES/*
%doc %{_datadir}/doc/clazy
%doc README.md HOWTO.md Changelog
%{_bindir}/clazy
%{_bindir}/clazy-standalone
%{_datadir}/metainfo/org.kde.clazy.metainfo.xml
%{_libdir}/ClazyPlugin.so
%{_libdir}/ClazyClangTidy.so
%{_mandir}/man1/clazy.1%{?ext_man}

%changelog
