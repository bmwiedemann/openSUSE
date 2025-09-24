#
# spec file for package libnice
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


Name:           libnice
Version:        0.1.22+7
Release:        0
Summary:        Interactive Connectivity Establishment implementation
License:        LGPL-2.1-only OR MPL-1.1
Group:          Development/Libraries/GNOME
URL:            https://nice.freedesktop.org/
Source:         %{name}-%{version}.tar.zst
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM libnice-port-gupnp-igd-bump.patch -- Port to new gupnp-igd
Patch1:         libnice-port-gupnp-igd-bump.patch

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gnutls) >= 2.12.0
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0) >= 0.11.91
BuildRequires:  pkgconfig(gstreamer-base-1.0) >= 0.11.91
BuildRequires:  pkgconfig(gupnp-igd-1.6)

%description
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE).

%package -n libnice10
Summary:        Interactive Connectivity Establishment implementation
Group:          System/Libraries

%description -n libnice10
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE).

%package -n gstreamer-libnice
Summary:        GStreamer plugin for the Interactive Connectivity Establishment
Group:          System/Libraries
Supplements:    (libnice10 and gstreamer)

%description -n gstreamer-libnice
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE).

%package devel
Summary:        Development files for libnice, an implemtation of ICE
Group:          Development/Libraries/C and C++
Requires:       libnice10 = %{version}
Requires:       typelib-1_0-Nice-0_1 = %{version}
Provides:       libnice-doc = %{version}
Obsoletes:      libnice-doc < %{version}

%description devel
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE).

%package -n typelib-1_0-Nice-0_1
Summary:        Introspection bindings for libnice
Group:          System/Libraries

%description -n typelib-1_0-Nice-0_1
libnice is an implementation of the IETF's draft Interactive
Connectivity Establishment standard (ICE).

This package provides the GObject Introspection bindings for libnice.

%prep
%autosetup -p1

# Disable tests that don't work in the build service
sed -e 's/^  '\''test-set-port-range'\''/#&/'  -i tests/meson.build

%build
%meson
%meson_build

%install
%meson_install

%check
%ifarch s390x
%meson_test -t 5
%else
%meson_test
%endif

%ldconfig_scriptlets -n libnice10

%files
%{_bindir}/stunbdc
%{_bindir}/stund

%files -n libnice10
%{_libdir}/*.so.*

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/nice/
%{_includedir}/stun/
%{_datadir}/gir-1.0/Nice-0.1.gir

%files -n gstreamer-libnice
%{_libdir}/gstreamer-1.0/libgstnice.so

%files -n typelib-1_0-Nice-0_1
%{_libdir}/girepository-1.0/Nice-0.1.typelib

%changelog
