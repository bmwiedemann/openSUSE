#
# spec file for package clazy
#
# Copyright (c) 2021 SUSE LLC
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


Name:           clazy
Version:        1.11
Release:        0
Summary:        Qt oriented code checker based on the Clang framework
License:        LGPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://www.kdab.com/clazy-video/
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        clazy.keyring
# Upstream changes on top of clazy 1.11
Patch0:         0001-Limit-the-clang-AST-crash-workaround-to-clang-7.0.patch
Patch1:         0001-Fix-crash-when-Q_PROPERTY-contents-is-empty.patch
Patch2:         0001-Allow-passing-no-check-in-plugin-arg-clazy-commandli.patch
Patch3:         0001-Build-fixes-for-LLVM-Clang-15.0.0.patch
Patch4:         0001-Adapt-to-API-changes-in-clang-llvm-16.patch
BuildRequires:  clang
BuildRequires:  clang-devel >= 8.0
BuildRequires:  cmake >= 3.7
%if 0%{?suse_version} == 1500
# C++17 is required
BuildRequires:  gcc10-c++
%else
BuildRequires:  libstdc++-devel
%endif
%requires_eq    clang%{_llvm_sonum}

%description
clazy is a compiler plugin which allows Clang to understand Qt semantics.
You get more than 50 Qt related compiler warnings, ranging from unneeded memory
allocations to misusage of API, including fix-its for automatic refactoring.

%prep
%autosetup -p1

%build
%define _lto_cflags %{nil}

%cmake

%cmake_build

%install
%cmake_install

sed -i 's#%{_bindir}/env sh#/bin/sh#' %{buildroot}%{_bindir}/clazy

%files
%license COPYING-LGPL2.txt
%doc %{_datadir}/doc/clazy
%doc README.md HOWTO Changelog
%{_bindir}/clazy
%{_bindir}/clazy-standalone
%{_datadir}/metainfo/org.kde.clazy.metainfo.xml
%{_libdir}/ClazyPlugin.so
%{_mandir}/man1/clazy.1%{?ext_man}

%changelog
