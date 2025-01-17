#
# spec file for package gupnp-av
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


Name:           gupnp-av
Version:        0.14.3
Release:        0
Summary:        Library to ease the handling and implementation of UPnP A/V profiles
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gupnp.org/
Source:         %{name}-%{version}.tar.zst

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0) >= 2.58
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(vapigen)

%description
GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles.

%package -n libgupnp-av-1_0-3
Summary:        Library to ease the handling and implementation of UPnP A/V profiles
Group:          Development/Libraries/C and C++
Requires:       %{name} >= %{version}
# Version 0.13 0.14 wrongly provided libgupnp-av-1.0.so.3 in libgupnp-av-1_0-2
Conflicts:      libgupnp-av-1_0-2 > 0.13

%description -n libgupnp-av-1_0-3
GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles.

%package -n typelib-1_0-GUPnPAV-1_0
Summary:        Library to ease the handling and implementation of UPnP A/V profiles -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GUPnPAV-1_0
GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles.

This package provides the GObject Introspection bindings for GUPnP A/V.

%package -n libgupnp-av-devel
Summary:        Library to ease the handling and implementation of UPnP A/V profiles - Development Files
Group:          Development/Libraries/C and C++
Requires:       libgupnp-av-1_0-3 = %{version}
Requires:       typelib-1_0-GUPnPAV-1_0 = %{version}

%description -n libgupnp-av-devel
GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles.

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libgupnp-av-1_0-3

%check
%meson_test

%files
%{_datadir}/gupnp-av/

%files -n libgupnp-av-1_0-3
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/*.so.*

%files -n typelib-1_0-GUPnPAV-1_0
%{_libdir}/girepository-1.0/GUPnPAV-1.0.typelib

%files -n libgupnp-av-devel
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GUPnPAV-1.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gupnp-av-1.0.deps
%{_datadir}/vala/vapi/gupnp-av-1.0.vapi

%changelog
