#
# spec file for package libplacebo
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


%{?sle15_python_module_pythons}
%define sover   349
Name:           libplacebo
Version:        7.349.0
Release:        0
Summary:        Library for GPU-accelerated video/image rendering primitives
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://code.videolan.org/videolan/libplacebo
Source0:        https://code.videolan.org/videolan/libplacebo/-/archive/v%{version}/libplacebo-v%{version}.tar.bz2
Source1:        https://github.com/Immediate-Mode-UI/Nuklear/raw/c512ac886425f6b6b6c816d67f4cb1385cd4cc53/nuklear.h
Source9:        baselibs.conf
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
BuildRequires:  gcc13
BuildRequires:  gcc13-c++
%else
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
%endif
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module glad2}
BuildRequires:  meson >= 0.63.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(dovi)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(libxxhash)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(shaderc)
BuildRequires:  pkgconfig(vulkan)

%description
This library contains GPU-accelerated video/image rendering
primitives, as well as a standalone vulkan-based image/video
renderer. It is based on the core rendering algorithms and ideas
of mpv.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n %{name}%{sover}
Summary:        Library for GPU-accelerated video/image rendering primitives
Group:          System/Libraries

%description -n %{name}%{sover}
This library contains GPU-accelerated video/image rendering
primitives, as well as a standalone vulkan-based image/video
renderer. It is based on the core rendering algorithms and ideas
of mpv.

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} > 150400
%package     -n plplay
Summary:        Example video player based on %{name}
Group:          Productivity/Multimedia/Video/Players

%description -n plplay
A small example video player based on %{name} and FFmpeg. This provides little
more than the ability to display video files, and rather serves as a tool to
help understand and demonstrate the various options provided by %{name}.
%endif

%prep
%setup -q -n %{name}-v%{version}
cp %{SOURCE1} ./demos/3rdparty/nuklear/

%build
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150200
export CC=gcc-13
export CXX=g++-13
%endif
%meson -Dglslang=disabled -Dd3d11=disabled -Dtests=true \
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} > 150400
       -Ddemos=true \
%else
       -Ddemos=false \
%endif

%meson_build

%install
%meson_install

%check
%meson_test

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%doc README.md
%license LICENSE
%{_libdir}/%{name}.so.%{sover}

%files devel
%doc README.md demos
%license LICENSE
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} > 150400
%files -n plplay
%{_bindir}/plplay
%endif

%changelog
