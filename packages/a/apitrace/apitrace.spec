#
# spec file for package apitrace
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


Name:           apitrace
Version:        13.0
Release:        0
Summary:        Tools for tracing OpenGL
License:        MIT
URL:            https://apitrace.github.io/
Source0:        https://github.com/apitrace/apitrace/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         001-no-submodules.patch
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
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libproc2)
BuildRequires:  pkgconfig(libunwind)
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
%license LICENSE
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
