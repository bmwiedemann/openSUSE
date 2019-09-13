#
# spec file for package gfbgraph
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


%define APIversion 0.2
Name:           gfbgraph
Version:        0.2.3
Release:        0
Summary:        Facebook Graph API access library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Url:            https://github.com/alvaropg/gfbgraph
Source:         http://download.gnome.org/sources/gfbgraph/0.2/%{name}-%{version}.tar.xz
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(rest-0.7)

%description
A GObject library for Facebook Graph API

%package -n libgfbgraph-0_2-0
Summary:        Facebook Graph API access library
Group:          System/Libraries

%description -n libgfbgraph-0_2-0
A GObject library for Facebook Graph API

%package -n typelib-1_0-GFBGraph-0_2
Summary:        Introspection bindings for the Facebook Graph API access library
Group:          System/Libraries

%description -n typelib-1_0-GFBGraph-0_2
A GObject library for Facebook Graph API

%package devel
Summary:        Development files for the Facebook Graph API access library
Group:          Development/Languages/C and C++
Requires:       libgfbgraph-0_2-0 = %{version}
Requires:       typelib-1_0-GFBGraph-0_2 = %{version}

%description devel
A GObject library for Facebook Graph API

This package contains header and linker information.

%prep
%setup -q

%build
%configure \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# This should not be installed by make install - we package them as %%doc
rm -rf %{buildroot}/%{_prefix}/doc/libgfbgraph/

%post -n libgfbgraph-0_2-0 -p /sbin/ldconfig
%postun -n libgfbgraph-0_2-0 -p /sbin/ldconfig

%files -n libgfbgraph-0_2-0
%license COPYING
%doc AUTHORS NEWS ChangeLog README
%{_libdir}/libgfbgraph-%{APIversion}.so.*

%files -n typelib-1_0-GFBGraph-0_2
%{_libdir}/girepository-1.0/GFBGraph-0.2.typelib

%files devel
%{_datadir}/gir-1.0/GFBGraph-0.2.gir
%{_datadir}/gtk-doc/html/gfbgraph-0.2/
%{_includedir}/gfbgraph-%{APIversion}/
%{_libdir}/libgfbgraph-%{APIversion}.so
%{_libdir}/pkgconfig/libgfbgraph-%{APIversion}.pc

%changelog
