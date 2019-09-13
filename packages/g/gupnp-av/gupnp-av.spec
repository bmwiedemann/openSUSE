#
# spec file for package gupnp-av
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.12.11
Release:        0
Summary:        Library to ease the handling and implementation of UPnP A/V profiles
License:        LGPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gupnp.org/
Source:         http://download.gnome.org/sources/gupnp-av/0.12/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(vapigen)

%description
GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles.

%package -n libgupnp-av-1_0-2
Summary:        Library to ease the handling and implementation of UPnP A/V profiles
Group:          Development/Libraries/C and C++
Requires:       %{name} >= %{version}

%description -n libgupnp-av-1_0-2
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
Requires:       libgupnp-av-1_0-2 = %{version}
Requires:       typelib-1_0-GUPnPAV-1_0 = %{version}

%description -n libgupnp-av-devel
GUPnP A/V is a small utility library that aims to ease the handling and
implementation of UPnP A/V profiles.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgupnp-av-1_0-2 -p /sbin/ldconfig
%postun -n libgupnp-av-1_0-2 -p /sbin/ldconfig

%files
%{_datadir}/gupnp-av/

%files -n libgupnp-av-1_0-2
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/*.so.*

%files -n typelib-1_0-GUPnPAV-1_0
%{_libdir}/girepository-1.0/GUPnPAV-1.0.typelib

%files -n libgupnp-av-devel
%{_includedir}/%{name}-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/GUPnPAV-1.0.gir
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/%{name}
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gupnp-av-1.0.deps
%{_datadir}/vala/vapi/gupnp-av-1.0.vapi

%changelog
