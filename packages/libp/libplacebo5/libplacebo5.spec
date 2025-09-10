#
# spec file for package libplacebo5
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define libname libplacebo
%define sover   264
%if 0%{?suse_version} < 1600
%define py_min_ver 11
%endif
Name:           libplacebo5
Version:        5.264.1
Release:        0
Summary:        Library for GPU-accelerated video/image rendering primitives
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://code.videolan.org/videolan/libplacebo
Source0:        https://code.videolan.org/videolan/libplacebo/-/archive/v%{version}/libplacebo-v%{version}.tar.bz2
Source9:        baselibs.conf
Patch0:         https://github.com/haasn/libplacebo/commit/12509c0f.patch
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  meson >= 0.63.0
BuildRequires:  pkgconfig
BuildRequires:  python3%{?py_min_ver}-Jinja2
BuildRequires:  python3%{?py_min_ver}-glad2
BuildRequires:  pkgconfig(dav1d)
BuildRequires:  pkgconfig(dovi)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libunwind)
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
Requires:       %{libname}%{sover} = %{version}
Conflicts:      %{libname}-devel

%description    devel
The %{libname}-devel package contains libraries and header files for
developing applications that use %{libname}.

%package     -n %{libname}%{sover}
Summary:        Library for GPU-accelerated video/image rendering primitives
Group:          System/Libraries

%description -n %{libname}%{sover}
This library contains GPU-accelerated video/image rendering
primitives, as well as a standalone vulkan-based image/video
renderer. It is based on the core rendering algorithms and ideas
of mpv.

%prep
%autosetup -p1 -n %{libname}-v%{version}

%build
%if 0%{?suse_version} < 1600
export PYTHON=%{_bindir}/python3.%{py_min_ver}
%endif
%meson -Dglslang=disabled -Dd3d11=disabled -Dtests=false
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n %{libname}%{sover}

%files -n %{libname}%{sover}
%doc README.md
%license LICENSE
%{_libdir}/%{libname}.so.%{sover}

%files devel
%doc README.md demos
%license LICENSE
%{_includedir}/%{libname}
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%changelog
