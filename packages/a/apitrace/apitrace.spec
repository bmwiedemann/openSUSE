#
# spec file for package apitrace
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


Name:           apitrace
Version:        10.0
Release:        0
Summary:        Tools for tracing OpenGL
License:        MIT
URL:            https://apitrace.github.io/
Source0:        https://github.com/apitrace/apitrace/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# https://github.com/apitrace/apitrace/issues/756
Patch0:         apitrace-fix-glibc-2.34.patch
BuildRequires:  cmake >= 2.8.11
BuildRequires:  gcc-c++ >= 4.9
BuildRequires:  libdwarf-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libprocps)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  pkgconfig(waffle-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-wrappers
Requires:       python3-Pillow
Requires:       python3-curses
Requires:       python3-numpy

%description
apitrace consists of a set of tools to:
- trace OpenGL, OpenGL ES, Direct3D, and DirectDraw APIs calls to a file;
- replay the recorded calls from a file, on any machine and, for OpenGL and OpenGL ES, on any operating system;
- inspect state at any call while replaying;
- view framebuffers and textures;
- view call data;
- edit trace files;
- profile performance of traces;

%package wrappers
Summary:        Tools for tracing OpenGL

%description wrappers
This package contains libs that are preloaded into traced programs.

%prep
%autosetup -p1

# Apitrace uses glibc private symbols
# and author claims they have good reasons to do so:
# https://github.com/apitrace/apitrace/issues/258
# Hack find_requires to filter-out GLIBC_PRIVATE.
cat >my_find_requires <<EOF
#!/bin/sh
%{__find_requires} "$@" | grep -v GLIBC_PRIVATE
EOF
chmod +x my_find_requires
%global _use_internal_dependency_generator 0
%global __find_requires %{_builddir}/%{name}-%{version}/my_find_requires

%build
%cmake -DENABLE_GUI=yes
%cmake_build

%install
%cmake_install
sed -i 's|#!%{_bindir}/env python3|#!%{_bindir}/python3|' %{buildroot}%{_libdir}/%{name}/scripts/*.py
chmod -x %{buildroot}%{_libdir}/%{name}/scripts/highlight.py
# We're packaging docs in files section
rm -r %{buildroot}%{_datadir}/doc/%{name}/

%check
%ctest

%files
%license LICENSE
%doc README.markdown docs/BUGS.markdown docs/NEWS.markdown docs/USAGE.markdown
%{_bindir}/apitrace
%{_bindir}/eglretrace
%{_bindir}/glretrace
%{_bindir}/gltrim
%{_bindir}/qapitrace
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/scripts/

%files wrappers
%{_libdir}/%{name}/wrappers/

%changelog
