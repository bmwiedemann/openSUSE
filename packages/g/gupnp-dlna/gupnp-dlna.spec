#
# spec file for package gupnp-dlna
#
# Copyright (c) 2021 SUSE LLC
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


Name:           gupnp-dlna
Version:        0.12.0
Release:        0
Summary:        A collection of helpers for building DLNA applications
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gupnp.org/
Source:         https://download.gnome.org/sources/gupnp-dlna/0.12/%{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:  pkgconfig(vapigen)
# libgupnp-dlna-2_0-3 violated shared library packaging policy
Conflicts:      libgupnp-dlna-2_0-3

%description
GUPnP-DLNA is a collection of helpers for building DLNA media sharing
applications using GUPnP.

%package -n libgupnp-dlna-2_0-4
Summary:        A collection of helpers for building DLNA applications
Group:          System/Libraries
Requires:       %{name} => %{version}
Requires:       libgupnp-dlna-backend >= %{version}

%description -n libgupnp-dlna-2_0-4
GUPnP-DLNA is a collection of helpers for building DLNA media sharing
applications using GUPnP.

%package -n libgupnp-dlna-backend-gstreamer
Summary:        GUPnP-DLNA GStreamer meta-extraction backend
Group:          System/Libraries
Provides:       libgupnp-dlna-backend = %{version}

%description -n libgupnp-dlna-backend-gstreamer
GUPnP-DLNA is a collection of helpers for building DLNA media sharing
applications using GUPnP.

This package contains the meta-data extraction based on GStreamer

%package -n typelib-1_0-GUPnPDLNA-2_0
Summary:        Collection of helpers for building DLNA applications - Introspection bindings
Group:          Development/Libraries/C and C++

%description -n typelib-1_0-GUPnPDLNA-2_0
GUPnP-DLNA is a collection of helpers for building DLNA media sharing
applications using GUPnP.

This package provides the GObject Introspection bindings for GUPnP-DLNA.

%package -n typelib-1_0-GUPnPDLNAGst-2_0
Summary:        Collection of helpers for building DLNA applications - Introspection bindings
Group:          Development/Libraries/C and C++

%description -n typelib-1_0-GUPnPDLNAGst-2_0
GUPnP-DLNA is a collection of helpers for building DLNA media sharing
applications using GUPnP.

This package provides the GObject Introspection bindings for GUPnP-DLNA.

%package -n libgupnp-dlna-devel
Summary:        A collection of helpers for building DLNA applications - Development Files
Group:          Development/Libraries/C and C++
Requires:       libgupnp-dlna-2_0-4 = %{version}
Requires:       typelib-1_0-GUPnPDLNA-2_0 = %{version}
Requires:       typelib-1_0-GUPnPDLNAGst-2_0 = %{version}

%description -n libgupnp-dlna-devel
GUPnP-DLNA is a collection of helpers for building DLNA media sharing
applications using GUPnP.

%package -n gupnp-dlna-tools
Summary:        A collection of helpers for building DLNA applications
Group:          Development/Tools/Other

%description -n gupnp-dlna-tools
GUPnP-DLNA is a collection of helpers for building DLNA media sharing
applications using GUPnP.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post -n libgupnp-dlna-2_0-4 -p /sbin/ldconfig
%postun -n libgupnp-dlna-2_0-4 -p /sbin/ldconfig

%files
%{_datadir}/%{name}-2.0/

%files -n libgupnp-dlna-2_0-4
%license COPYING
%doc AUTHORS TODO
%dir %{_libdir}/gupnp-dlna
%{_libdir}/lib*.so.4*

%files -n libgupnp-dlna-backend-gstreamer
%{_libdir}/gupnp-dlna/libgstreamer.so

%files -n typelib-1_0-GUPnPDLNA-2_0
%{_libdir}/girepository-1.0/GUPnPDLNA-2.0.typelib

%files -n typelib-1_0-GUPnPDLNAGst-2_0
%{_libdir}/girepository-1.0/GUPnPDLNAGst-2.0.typelib

%files -n libgupnp-dlna-devel
%{_includedir}/%{name}-2.0/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/gupnp-dlna-2.0.pc
%{_libdir}/pkgconfig/gupnp-dlna-gst-2.0.pc
%{_libdir}/pkgconfig/gupnp-dlna-metadata-2.0.pc
%{_datadir}/gir-1.0/GUPnPDLNA-2.0.gir
%{_datadir}/gir-1.0/GUPnPDLNAGst-2.0.gir
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/*

%files -n gupnp-dlna-tools
%{_bindir}/gupnp-dlna-info-2.0
%{_bindir}/gupnp-dlna-ls-profiles-2.0

%changelog
