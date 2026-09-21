#
# spec file for package apitrace
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


Name:           apitrace
Version:        14.0
Release:        0
Summary:        Tools for tracing OpenGL
License:        BSD-3-Clause AND MIT
URL:            https://apitrace.github.io/
Source0:        https://github.com/apitrace/apitrace/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# contrib seekable format is not shipped by libzstd
Source2:        https://github.com/facebook/zstd/releases/download/v1.5.7/zstd-1.5.7.tar.gz
# PATCH-FIX-OPENSUSE 001-no-submodules.patch mpluskal@suse.com -- github archive has no git submodules; use system deps
Patch0:         001-no-submodules.patch
# PATCH-FIX-OPENSUSE 002-no-static-libbacktrace.patch mpluskal@suse.com -- link system libbacktrace
Patch1:         002-no-static-libbacktrace.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.15
BuildRequires:  libbacktrace-devel
BuildRequires:  libdwarf-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libbrotlidec) >= 1.0.7
BuildRequires:  pkgconfig(libbrotlienc) >= 1.0.7
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libproc2)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libzstd) >= 1.4.0
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  pkgconfig(waffle-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib) >= 1.2.6
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
# seekable format lives in zstd contrib, not in libzstd
tar -C thirdparty/zstd --strip-components=1 -xf %{SOURCE2}

%build
export CXXFLAGS="%{optflags} -Wno-error=return-type"
%cmake -DENABLE_STATIC_SNAPPY=OFF -DENABLE_QT6=ON
%cmake_build

%install
%cmake_install
# We're packaging docs in files section
rm -r %{buildroot}%{_datadir}/doc/%{name}

# fix env
%python3_fix_shebang_path %{buildroot}%{_libdir}/%{name}/scripts/*.py

%check
%ctest

%files
%license LICENSE thirdparty/zstd/LICENSE
%doc README.markdown docs/BUGS.markdown docs/NEWS.markdown docs/USAGE.markdown
%dir %{_libdir}/%{name}
%{_bindir}/apitrace
%{_bindir}/eglretrace
%{_bindir}/glretrace
%{_bindir}/gltrim
%{_bindir}/qapitrace
%{_libdir}/%{name}/scripts/

%files wrappers
%{_libdir}/%{name}/wrappers/

%changelog
