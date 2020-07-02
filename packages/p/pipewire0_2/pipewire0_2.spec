#
# spec file for package pipewire0_2
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


%define libpipewire libpipewire-0_2-1
%define apiver 0.2
Name:           pipewire0_2
Version:        0.2.7
Release:        0
Summary:        Old version of pipewire, an audio and video server, for WebRTC compatibility
License:        LGPL-2.1-or-later
URL:            https://pipewire.org/
Source0:        https://github.com/PipeWire/pipewire/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pipewire0_2-bluez5-declare-as-extern.patch badshah400@gmail.com -- Declare the object spa_a2dp_sink_factory as extern to avoid conflict with a previous declaration; patch taken from fedora
Patch0:         pipewire0_2-bluez5-declare-as-extern.patch
# PATCH-FIX-UPSTREAM pipewire0_2-link-a2dp-codecs.patch badshah400@gmail.com -- Actually link against a2dp-codecs.o to prevent undefined references
Patch1:         pipewire0_2-link-a2dp-codecs.patch
BuildRequires:  meson >= 0.47.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(sbc)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(x11)

%description
PipeWire is a server and user space API to deal with multimedia pipelines.
 
This is the old version 0.2 of pipewire, maintained only to provide
compatibility with apps supporting WebRTC in Wayland that have not yet been
ported to use pipewire >= 0.3, e.g. google-chrome.

%package -n %{libpipewire}
Summary:        Shared libraries for outdated version of pipewire for compatibility with WebRTC

%description -n %{libpipewire}
PipeWire is a server and user space API to deal with multimedia pipelines.

This package provides the shared library for version 0.2 of pipewire.

%package compat
Summary:        Modules for oudated version of pipewire, for compatibility with WebRTC
Requires:       %{libpipewire} = %{version}

%description compat
PipeWire is a server and user space API to deal with multimedia pipelines.

This package provides all the modules and plugins for pipewire 0.2 to allow
screen-sharing support via WebRTC in Wayland sessions for apps not ported to
pipewire >= 0.3.

%prep
%autosetup -p1 -n pipewire-%{version}

%build
%meson \
	-Dgstreamer=disabled \
	-Dsystemd=false \
        --includedir=%{_includedir}/%{name} \
	%{nil}
%meson_build

%install
%meson_install

# WE ONLY REALLY NEED THE LIBS AND MODULES TO SUPPORT WEBRTC SCREEN-SHARING
rm -rf %{buildroot}%{_bindir}/*
rm -rf %{buildroot}%{_sysconfdir}/*
rm -rf %{buildroot}%{_libdir}/libpipewire-%{apiver}.so
rm -rf %{buildroot}%{_includedir}/%{name}/
rm -rf %{buildroot}%{_libdir}/pkgconfig

%post   -n %{libpipewire} -p /sbin/ldconfig
%postun -n %{libpipewire} -p /sbin/ldconfig

%files -n %{libpipewire}
%{_libdir}/libpipewire-%{apiver}.so.*

%files compat
%{_libdir}/pipewire-%{apiver}/
%{_libdir}/spa/

%changelog
