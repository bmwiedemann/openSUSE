#
# spec file for package clazy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.6
Release:        0
Summary:        Qt oriented code checker based on the Clang framework
License:        LGPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://www.kdab.com/clazy-video/
Source0:        https://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Patch0:         cmake-clang-cpp.patch
BuildRequires:  clang
BuildRequires:  clang-devel >= 3.9
BuildRequires:  cmake >= 3.0
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)

%description
clazy is a compiler plugin which allows Clang to understand Qt semantics.
You get more than 50 Qt related compiler warnings, ranging from unneeded memory
allocations to misusage of API, including fix-its for automatic refactoring.

%prep
%setup -q
%patch0 -p1

%build
%define _lto_cflags %{nil}
export CXXFLAGS="`echo %{optflags} | sed 's#-fstack-clash-protection##'`"
export CFLAGS="$CXXFLAGS"

%cmake

%make_jobs

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
