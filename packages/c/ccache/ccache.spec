#
# spec file for package ccache
#
# Copyright (c) 2020 SUSE LLC
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


Name:           ccache
Version:        3.7.9
Release:        0
Summary:        A Fast C/C++ Compiler Cache
License:        GPL-3.0-or-later
URL:            https://ccache.dev/
Source0:        https://github.com/ccache/ccache/releases/download/v%{version}/ccache-%{version}.tar.xz#/%{name}-%{version}.tar.xz
Source1:        https://github.com/ccache/ccache/releases/download/v%{version}/ccache-%{version}.tar.xz.asc#/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# PATCH-FEATURE-UPSTREAM 0001-Add-another-cleanup-mechanism-evict-older-than.patch https://github.com/ccache/ccache/pull/605
Patch0:         0001-Add-another-cleanup-mechanism-evict-older-than.patch
BuildRequires:  zlib-devel
Provides:       distcc:%{_bindir}/ccache

%description
ccache is a compiler cache. It speeds up recompilation by caching the
result of previous compilations and detecting when the same compilation is
being done again. Supported languages are C, C++, Objective-C and
Objective-C++.

%prep
%setup -q
%patch0 -p1

%build
%configure \
  --without-bundled-zlib
%make_build

%install
%make_install

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

%ifnarch %{ix86}
# Testsuite fails on i586
%check
%make_build check
%endif

%files
%license LICENSE.* GPL-3.0.txt
%doc doc/AUTHORS.* doc/MANUAL.* doc/NEWS.* README.*
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
