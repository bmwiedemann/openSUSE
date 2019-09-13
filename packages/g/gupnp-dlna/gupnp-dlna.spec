#
# spec file for package gupnp-dlna
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           gupnp-dlna
Version:        0.10.5
Release:        0
Summary:        A collection of helpers for building DLNA applications
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://www.gupnp.org/
Source:         http://download.gnome.org/sources/gupnp-dlna/0.10/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:  pkgconfig(vapigen)

%description
GUPnP-DLNA is a collection of helpers for building DLNA media sharing
applications using GUPnP.

%package -n libgupnp-dlna-2_0-3
Summary:        A collection of helpers for building DLNA applications
Group:          System/Libraries
Requires:       libgupnp-dlna-backend >= %{version}

%description -n libgupnp-dlna-2_0-3
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
Requires:       libgupnp-dlna-2_0-3 = %{version}
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
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgupnp-dlna-2_0-3 -p /sbin/ldconfig
%postun -n libgupnp-dlna-2_0-3 -p /sbin/ldconfig

%files -n libgupnp-dlna-2_0-3
%license COPYING
%doc AUTHORS README TODO
# This directory contains DLNA profiles, needed by the library
%{_datadir}/%{name}-2.0/
%dir %{_libdir}/gupnp-dlna
%{_libdir}/lib*.so.3*

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
%doc %{_datadir}/gtk-doc/html/%{name}/
%doc %{_datadir}/gtk-doc/html/%{name}-gst/
%doc %{_datadir}/gtk-doc/html/%{name}-metadata/

%files -n gupnp-dlna-tools
%{_bindir}/gupnp-dlna-info-2.0
%{_bindir}/gupnp-dlna-ls-profiles-2.0

%changelog
