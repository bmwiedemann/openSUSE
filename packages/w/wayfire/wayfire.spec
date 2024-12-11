#
# spec file for package wayfire
#
# Copyright (c) 2023 SUSE LLC
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

%define major_ver 0.9
%define minor_ver 0
%define libname libwf-utils0
Name:           wayfire
Version:        %{major_ver}.%{minor_ver}
Release:        0
Summary:        3D wayland compositor
License:        MIT
URL:            https://wayfire.org/
Source0:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.sha256sum
# PATCH-FIX-OPENSUSE wayland.patch openSUSE uses non-standard header file locations/
Patch0:         wayland.patch
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
BuildRequires:  hwdata
BuildRequires:  inotify-tools-devel
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(doctest)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 1.7.0
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.12
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wf-config) >= %{major_ver}
BuildRequires:  pkgconfig(wlroots) >= 0.17.0
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
Recommends:     wayfire-config-manager
Recommends:     wayfire-plugins-extra
Recommends:     wcm
Recommends:     wf-shell

%description
Wayfire is a wayland compositor based on wlroots. It aims to create a customizable, extendable and lightweight environment without sacrificing its appearance. If you want to gain a better impression at what it can do, see the demo videos on youtube: https://www.youtube.com/playlist?list=PLb7YRKEhWEBUIoT-a29UoJW9mhfzjpNle

%package -n %{libname}
Summary:        Library for %{name}

%description -n %{libname}
%{summary}.

%package        devel
Summary:        Devel files for %{name}
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}

%description    devel
Development files for %{name}.

%prep
echo "`grep %{name}-%{version}.tar.xz %{SOURCE1} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%autosetup -p1

%build
%meson \
 -Duse_system_wlroots=enabled \
 -Duse_system_wfconfig=enabled \
 -Dxwayland=enabled
%meson_build

%install
%meson_install
rm -rf %{buildroot}/%{_prefix}/man/wayfire.1
install -Dpm0644 wayfire.desktop %{buildroot}%{_datadir}/wayland-sessions/%{name}.desktop
find %{buildroot} -type f -name "*.a" -delete -print0

%fdupes %{buildroot}/%{_prefix}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
%meson_test

%files
%license LICENSE
%doc README.md wayfire.ini
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/*.desktop
%{_mandir}/man1/wayfire.1%{?ext_man}

%files -n %{libname}
%{_libdir}/*.so.*
%{_libdir}/libwayfire-blur-base.so
%{_libdir}/%{name}/

%files devel
%{_libdir}/libwf-utils.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/%{name}

%changelog
