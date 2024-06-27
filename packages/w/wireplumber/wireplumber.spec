#
# spec file for package wireplumber
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


%define pipewire_minimum_version 1.0.2
%define apiver 0.5
%define apiver_str 0_5
%define sover 0
%define libwireplumber libwireplumber-%{apiver_str}-%{sover}
Name:           wireplumber
Version:        0.5.3+git11.4868b3c
Release:        0
Summary:        Session / policy manager implementation for PipeWire
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.freedesktop.org/pipewire/wireplumber
Source0:        wireplumber-%{version}.tar.xz
Source1:        split-config-file.py
# docs
BuildRequires:  doxygen
BuildRequires:  graphviz
# /docs
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  meson >= 0.59.0
BuildRequires:  pipewire >= %{pipewire_minimum_version}
BuildRequires:  pipewire-spa-plugins-0_2 >= %{pipewire_minimum_version}
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-lxml
BuildRequires:  xmltoman
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.62.0
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.62
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libpipewire-0.3) >= %{pipewire_minimum_version}
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-Sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-breathe
#!BuildIgnore:  pipewire-session-manager
# Setup ALSA devices if PipeWire handles PulseAudio or JACK connections.
Requires:       (%{name}-audio if (pipewire-pulseaudio or pipewire-jack))
Requires:       pipewire >= %{pipewire_minimum_version}
Provides:       pipewire-session-manager
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc9
BuildRequires:  gcc9-c++
%else
BuildRequires:  c++_compiler
%endif
%{?systemd_ordering}


%description
WirePlumber is a modular session / policy manager for PipeWire and
a GObject-based high-level library that wraps PipeWire's API,
providing convenience for writing the daemon's modules as well as
external tools for managing PipeWire.

%lang_package

%package doc
Summary:        Wireplumber Session / policy manager documentation
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description doc
This package contains documentation for the WirePlumber
session/policy manager for PipeWire.

%package audio
Summary:        Enable audio support in PipeWire / WirePlumber
Group:          Development/Libraries/C and C++
Requires:       %{libwireplumber} = %{version}
Requires:       %{name} = %{version}
Recommends:     pipewire-jack
Recommends:     pipewire-pulseaudio
Conflicts:      pulseaudio
BuildArch:      noarch

%description audio
WirePlumber is a modular session / policy manager for PipeWire and
a GObject-based high-level library that wraps PipeWire's API,
providing convenience for writing the daemon's modules as well as
external tools for managing PipeWire.

This package enables the use of alsa devices in PipeWire.

%package devel
Summary:        Session / policy manager implementation for PipeWire
Group:          Development/Libraries/C and C++
Requires:       %{libwireplumber} = %{version}
Requires:       %{name} = %{version}

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

%package zsh-completion
Summary:        Wireplumber zsh completion
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (wireplumber and zsh)

%description zsh-completion
Optional dependency offering zsh completion for various wpctl parameters.

%prep
%autosetup -p1

pushd src/config
python3 %{SOURCE1}
popd

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-9
export CXX=g++-9
%endif
%meson -Ddoc=enabled \
       -Dsystem-lua=true \
       -Delogind=disabled
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}/%{_datadir}/doc/pipewire/html
%find_lang %{name} %{?no_lang_C}

%ifnarch %ix86 ppc64
%check
export XDG_RUNTIME_DIR=/tmp
%meson_test
%endif

%pre
%systemd_user_pre wireplumber.service

%post
%systemd_user_post wireplumber.service

%if 0%{?suse_version} <= 1500
# If the pipewire.socket user unit is not enabled and the workaround
# for boo#1186561 has never been executed, we need to execute it now
if [ ! -L %{_sysconfdir}/systemd/user/pipewire.service.wants/wireplumber.service \
    -a ! -f %{_localstatedir}/lib/pipewire/wireplumber_post_workaround \
    -a -x %{_bindir}/systemctl ]; then
    for service in wireplumber.service ; do
        %{_bindir}/systemctl --global preset "$service" || :
    done

    mkdir -p %{_localstatedir}/lib/pipewire
    cat << EOF > %{_localstatedir}/lib/pipewire/wireplumber_post_workaround
# The existence of this file means that the wireplumber user services were
# enabled at least once. Please don't remove this file as that would
# make the services to be enabled again in the next package update.
#
# Check the following bugs for more information:
# https://bugzilla.opensuse.org/show_bug.cgi?id=1200485
EOF
fi
%endif


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
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-dbus-connection.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-default-nodes-api.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-file-monitor-api.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-log-settings.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-logind.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-lua-scripting.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-mixer-api.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-portal-permissionstore.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-reserve-device.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-settings.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-si-audio-adapter.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-si-audio-virtual.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-si-node.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-si-standard-link.so
%{_libdir}/wireplumber-%{apiver}/libwireplumber-module-standard-event-source.so

%{_userunitdir}/wireplumber.service
%{_userunitdir}/wireplumber@.service
%{_datadir}/wireplumber
%dir %{_datadir}/doc/wireplumber
%dir %{_datadir}/doc/wireplumber/examples
%{_datadir}/doc/wireplumber/examples/wireplumber.conf.d
%{_datadir}/wireplumber/wireplumber.conf
%dir %{_datadir}/wireplumber/wireplumber.conf.d
%exclude %{_datadir}/wireplumber/wireplumber.conf.d/00-device-monitors.conf
%exclude %{_datadir}/wireplumber/wireplumber.conf.d/01-require-audio-in-main-profile.conf
%{_datadir}/wireplumber/wireplumber.conf.d/alsa-vm.conf

%files lang -f %{name}.lang

%files audio
%{_datadir}/wireplumber/wireplumber.conf.d/00-device-monitors.conf
%{_datadir}/wireplumber/wireplumber.conf.d/01-require-audio-in-main-profile.conf

%files devel
%{_includedir}/wireplumber-%{apiver}
%{_libdir}/libwireplumber-%{apiver}.so
%{_libdir}/pkgconfig/wireplumber-%{apiver}.pc
%{_datadir}/gir-1.0/Wp-%{apiver}.gir

%files doc
%{_datadir}/doc/wireplumber/html/
%exclude %{_datadir}/doc/wireplumber/examples

%files -n typelib-1_0-Wp-%{apiver_str}
%{_libdir}/girepository-1.0/Wp-%{apiver}.typelib

%files -n %{libwireplumber}
%{_libdir}/libwireplumber-%{apiver}.so.%{sover}
%{_libdir}/libwireplumber-%{apiver}.so.%{sover}.*

%files zsh-completion
%dir %{_datarootdir}/zsh
%dir %{_datarootdir}/zsh/site-functions/
%{_datarootdir}/zsh/site-functions/_wpctl

%changelog
