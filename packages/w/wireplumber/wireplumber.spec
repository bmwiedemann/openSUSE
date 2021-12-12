#
# spec file for package wireplumber
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


%define apiver 0.4
%define apiver_str 0_4
%define sover 0
%define libwireplumber libwireplumber-%{apiver_str}-%{sover}
Name:           wireplumber
Version:        0.4.5
Release:        0
Summary:        Session / policy manager implementation for PipeWire
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.freedesktop.org/pipewire/wireplumber
Source0:        wireplumber-%{version}.tar.xz
Source1:        split-config-file.py
Patch0:         0001-m-reserve-device-replace-the-hash-table-key-on-new-insert.patch
Patch1:         0002-policy-node-wait-for-nodes-when-we-become-unlinked.patch
Patch100:       reduce-meson-required-version.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  meson >= 0.54.0
BuildRequires:  pipewire >= 0.3.32
#!BuildIgnore:    pipewire-session-manager
BuildRequires:  pipewire-spa-plugins-0_2
BuildRequires:  pkgconfig
BuildRequires:  xmltoman
BuildRequires:  pkgconfig(lua5.3)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.62.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.62
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-allocators-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(jack) >= 1.9.10
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.32
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  python3-base
BuildRequires:  python3-lxml
Requires:       pipewire >= 0.3.32
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc9
BuildRequires:  gcc9-c++
%else
BuildRequires:  gcc-c++
%endif
Provides:       pipewire-session-manager

%description
WirePlumber is a modular session / policy manager for PipeWire and
a GObject-based high-level library that wraps PipeWire's API,
providing convenience for writing the daemon's modules as well as
external tools for managing PipeWire.

%package audio
Summary:        Session / policy manager implementation for PipeWire (audio support)
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{libwireplumber} = %{version}
Conflicts:      pulseaudio
Recommends:     pipewire-pulseaudio
Supplements:    (pipewire-pulseaudio and wireplumber)

%description audio
WirePlumber is a modular session / policy manager for PipeWire and
a GObject-based high-level library that wraps PipeWire's API,
providing convenience for writing the daemon's modules as well as
external tools for managing PipeWire.

This package enables the use of alsa devices in PipeWire.

%package devel
Summary:        Session / policy manager implementation for PipeWire
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{libwireplumber} = %{version}

%description devel
WirePlumber is a modular session / policy manager for PipeWire and
a GObject-based high-level library that wraps PipeWire's API,
providing convenience for writing the daemon's modules as well as
external tools for managing PipeWire.

This package provides all the necessary files for development with WirePlumber

%package -n %{libwireplumber}
Summary:        Session / policy manager implementation for PipeWire
Group:          System/Libraries

%description -n %{libwireplumber}
WirePlumber is a modular session / policy manager for PipeWire and
a GObject-based high-level library that wraps PipeWire's API,
providing convenience for writing the daemon's modules as well as
external tools for managing PipeWire.

This package provides the wireplumber shared library.

%package -n typelib-1_0-Wp-%{apiver_str}
Summary:        Introspection bindings for libwireplumber
Group:          System/Libraries

%description -n typelib-1_0-Wp-%{apiver_str}
WirePlumber is a modular session / policy manager for PipeWire and
a GObject-based high-level library that wraps PipeWire's API,
providing convenience for writing the daemon's modules as well as
external tools for managing PipeWire.

This package provides the GObject Introspection bindings for
the wireplumber shared library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if %{pkg_vcmp meson < 0.56.0}
%patch100 -p1
%endif

pushd src/config/main.lua.d
python3 %{SOURCE1} 
rm 90-enable-all.lua
popd

%build
%if %{pkg_vcmp gcc < 8}
export CC=gcc-9
%endif
%meson -Ddoc=disabled \
       -Dsystem-lua=true \
       -Delogind=disabled
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}/%{_datadir}/doc/pipewire/html

%ifnarch %ix86 ppc64
%check
export XDG_RUNTIME_DIR=/tmp
%meson_test
%endif

%pre
%systemd_user_pre wireplumber.service

%post
%systemd_user_post wireplumber.service

%preun
%systemd_user_preun wireplumber.service

%postun
%systemd_user_postun wireplumber.service

%post   -n %{libwireplumber} -p /sbin/ldconfig
%postun -n %{libwireplumber} -p /sbin/ldconfig

%files
%{_bindir}/wireplumber
%{_bindir}/wpctl
%{_bindir}/wpexec
%dir %{_libdir}/wireplumber-%{apiver}
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-default-nodes-api.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-default-nodes.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-default-profile.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-device-activation.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-file-monitor-api.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-logind.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-lua-scripting.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-metadata.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-mixer-api.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-portal-permissionstore.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-reserve-device.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-route-settings-api.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-si-audio-adapter.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-si-audio-endpoint.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-si-node.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-si-standard-link.so
%{_userunitdir}/wireplumber.service
%{_userunitdir}/wireplumber@.service
%{_datadir}/wireplumber
%exclude %{_datadir}/wireplumber/main.lua.d/90-2-1-enable-alsa.lua

%files audio
%{_datadir}/wireplumber/main.lua.d/90-2-1-enable-alsa.lua

%files devel
%{_includedir}/wireplumber-%{apiver}
%{_libdir}/libwireplumber-%{apiver}.so
%{_libdir}/pkgconfig/wireplumber-%{apiver}.pc
%{_datadir}/gir-1.0/Wp-%{apiver}.gir

%files -n typelib-1_0-Wp-%{apiver_str}
%{_libdir}/girepository-1.0/Wp-%{apiver}.typelib

%files -n %{libwireplumber}
%{_libdir}/libwireplumber-%{apiver}.so.%{sover}
%{_libdir}/libwireplumber-%{apiver}.so.%{sover}.*

%changelog
