#
# spec file for package gcab
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


Name:           gcab
Version:        1.2
Release:        0
Summary:        Cabinet file library and tool
License:        LGPL-2.1-or-later
Group:          Productivity/Archiving/Compression
Url:            http://ftp.gnome.org/pub/GNOME/sources/gcab
Source0:        http://download.gnome.org/sources/gcab/1.2/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.14
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.4
Recommends:     %{name}-lang

%description
gcab is a tool and library for manipulating cabinet files.

It uses the GObject API and provides GIR bindings.
It supports creation of archives with simple MSZIP compression.

This package provides gcab tool and its manuals.

%package -n libgcab-1_0-0
Summary:        Cabinet file library
Group:          System/Libraries

%description -n libgcab-1_0-0
gcab is a tool and library for manipulating cabinet files.

It uses the GObject API and provides GIR bindings.
It supports creation of archives with simple MSZIP compression.

This package provides a system library to access cab files

%package -n typelib-1_0-GCab-1_0
Summary:        Introspection bindings for the gcab cabinet file library
Group:          System/Libraries

%description -n typelib-1_0-GCab-1_0
gcab is a tool and library for manipulating cabinet files.

It uses the GObject API and provides GIR bindings.
It supports creation of archives with simple MSZIP compression.

This package contains the introspection files.

%package devel
Summary:        Development files for the gcab cabinet file library
Group:          Development/Languages/C and C++
Requires:       libgcab-1_0-0 = %{version}

%description devel
gcab is a tool and library for manipulating cabinet files.

It uses the GObject API and provides GIR bindings.
It supports creation of archives with simple MSZIP compression.

This package provides development files to build code against
libgcab.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D docs=true \
	-D introspection=true \
	-D tests=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}

%post -n libgcab-1_0-0 -p /sbin/ldconfig
%postun -n libgcab-1_0-0 -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}

%files -n libgcab-1_0-0
%{_libdir}/libgcab-1.0.so.*

%files -n typelib-1_0-GCab-1_0
%{_libdir}/girepository-1.0/GCab-1.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/libgcab-1.0/
%{_libdir}/libgcab-1.0.so
%{_libdir}/pkgconfig/libgcab-1.0.pc
%{_datadir}/gir-1.0/GCab-1.0.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgcab-1.0.*

%files lang -f %{name}.lang

%changelog
