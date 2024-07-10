#
# spec file for package libva
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


%define flavor @BUILD_FLAVOR@%nil

%define build_gl 0
%define sover 2

%if "%flavor" == "gl"
%define build_gl 1
%define name_suffix -%{flavor}
%else
%define name_suffix %{nil}
%endif

Name:           libva%{name_suffix}
%define _name   libva
Version:        2.22.0
Release:        0
Summary:        Video Acceleration (VA) API
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://01.org/linuxmedia
Source0:        https://github.com/intel/libva/archive/%{version}.tar.gz#/libva-%{version}.tar.gz
Source2:        baselibs.conf
Patch0:         propagate-dpy.patch

BuildRequires:  c++_compiler
BuildRequires:  meson
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client) >= 1.11.0
BuildRequires:  pkgconfig(wayland-scanner) >= 1.11.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xv)
%if %{build_gl}
BuildRequires:  pkgconfig(gl)
%endif

%description
The libva library implements the Video Acceleration API.
The library loads a hardware dependendent driver.

%package -n libva-glx%{sover}
Summary:        GLX backend for the Video Acceleration API
Group:          System/Libraries
Supplements:    libva%{sover}

%description -n libva-glx%{sover}
The libva library implements the Video Acceleration API.
The library loads a hardware dependendent driver.

This is the VA/GLX runtime library.

%package -n libva-wayland%{sover}
Summary:        Wayland backend for the Video Acceleration API
Group:          System/Libraries

%description -n libva-wayland%{sover}
The libva library implements the Video Acceleration API.
The library loads a hardware dependendent driver.

%package devel
Summary:        Development files for the Video Acceleration API
Group:          Development/Languages/C and C++
%if 0%{?build_gl}
BuildRequires:  libva-devel = %{version}
Requires:       libva-glx%{sover} = %{version}
Requires:       pkgconfig(gl)
%else
Requires:       libva%{sover} = %{version}
Requires:       libva-drm%{sover} = %{version}
Requires:       libva-wayland%{sover} = %{version}
Requires:       libva-x11-%{sover} = %{version}
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xfixes)
Recommends:     libva-gl-devel
%endif

%description devel
The libva library implements the Video Acceleration API.
The library loads a hardware dependendent driver.

%if 0%{?build_gl}
This package provides the development environment for libva gl packages.
%else
This package provides the development environment for libva packages.
%endif

%package -n libva%{sover}
Summary:        Video Acceleration API
Group:          System/Libraries

%description -n libva%{sover}
The libva library implements the Video Acceleration API.
The library loads a hardware dependendent driver.

This is the core runtime library.

%package -n libva-drm%{sover}
Summary:        DRM backend for the Video Acceleration API
Group:          System/Libraries
Supplements:    libva%{sover}

%description -n libva-drm%{sover}
The libva library implements the Video Acceleration API.
The library loads a hardware dependendent driver.

This is the VA/DRM runtime library.

%package -n libva-x11-%{sover}
Summary:        X11 backend for the Video Acceleration API
Group:          System/Libraries
Supplements:    libva%{sover}

%description -n libva-x11-%{sover}
The libva library implements the Video Acceleration API.
The library loads a hardware dependendent driver.

This is the VA/X11 runtime library.

%prep
%autosetup -n %{_name}-%{version} -p1

%build
%meson \
	-D driverdir=%{_libdir}/dri \
%if %{build_gl}
	-D with_glx=yes \
	-D with_x11=yes \
	-D disable_drm=true \
	-D with_wayland=no \
	-D with_win32=no \
%else
	-D with_glx=no \
%endif
	%{nil}
%meson_build

%install
%meson_install

%if %{build_gl}
# remove all files packaged during without gl mode
rm -rf `find %{buildroot}%{_includedir}/va/* | grep -v "glx"`
rm -rf `find %{buildroot}%{_libdir}/libva* | grep -v "glx"`
rm -rf `find %{buildroot}%{_libdir}/pkgconfig/libva*.pc | grep -v "glx"`
%endif

%ldconfig_scriptlets -n libva-glx%{sover}
%ldconfig_scriptlets -n libva-wayland%{sover}
%ldconfig_scriptlets -n libva%{sover}
%ldconfig_scriptlets -n libva-drm%{sover}
%ldconfig_scriptlets -n libva-x11-%{sover}

%if %{build_gl}
%files -n libva-glx%{sover}
%{_libdir}/libva-glx.so.%{sover}*

%files devel
%{_libdir}/libva-glx.so
%{_includedir}/va/va_glx.h
%{_includedir}/va/va_backend_glx.h
%{_libdir}/pkgconfig/libva-glx.pc
%else

%files -n libva%{sover}
%license COPYING
%{_libdir}/libva.so.*

%files -n libva-x11-%{sover}
%{_libdir}/libva-x11.so.*

%files -n libva-drm%{sover}
%{_libdir}/libva-drm.so.*

%files -n libva-wayland%{sover}
%{_libdir}/libva-wayland.so.%{sover}*

%files devel
%{_libdir}/libva.so
%{_libdir}/libva-x11.so
%{_libdir}/libva-drm.so
%{_libdir}/libva-wayland.so
%{_includedir}/va
%{_libdir}/pkgconfig/libva-drm.pc
%{_libdir}/pkgconfig/libva-x11.pc
%{_libdir}/pkgconfig/libva-wayland.pc
%{_libdir}/pkgconfig/libva.pc
%endif

%changelog
