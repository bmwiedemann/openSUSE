#
# spec file for package libzapojit
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


Name:           libzapojit
Version:        0.0.3
Release:        0
Summary:        Library for the SkyDrive and Hotmail REST APIs
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            http://download.gnome.org/sources/libzapojit
Source:         http://download.gnome.org/sources/libzapojit/0.0/%{name}-%{version}.tar.xz
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(gtk-doc) >= 1.11
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.38
BuildRequires:  pkgconfig(rest-0.7)

%description
libzapojit is a GLib/GObject wrapper for the SkyDrive and Hotmail
REST APIs.

%package -n libzapojit-0_0-0
Summary:        Library for the SkyDrive and Hotmail REST APIs
Group:          System/Libraries

%description -n libzapojit-0_0-0
libzapojit is a GLib/GObject wrapper for the SkyDrive and Hotmail
REST APIs.

%package -n typelib-1_0-Zpj-0_0
Summary:        Library for the SkyDrive and Hotmail REST APIs -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Zpj-0_0
libzapojit is a GLib/GObject wrapper for the SkyDrive and Hotmail
REST APIs.

This package provides the introspection bindings for libzapojit.

%package -n libzapojit-devel
Summary:        Library for the SkyDrive and Hotmail REST APIs -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libzapojit-0_0-0 = %{version}
Requires:       typelib-1_0-Zpj-0_0

%description -n libzapojit-devel
This package provides the files necessary for developing applications
using libzapojit.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Remove files already packaged in docdir correctly
rm %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,ChangeLog,COPYING,INSTALL,NEWS,README}

%post -n libzapojit-0_0-0 -p /sbin/ldconfig
%postun -n libzapojit-0_0-0 -p /sbin/ldconfig

%files -n libzapojit-0_0-0
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libzapojit-0.0.so.0*

%files -n typelib-1_0-Zpj-0_0
%{_libdir}/girepository-1.0/Zpj-0.0.typelib

%files -n libzapojit-devel
%{_includedir}/%{name}-0.0/
%{_datadir}/gtk-doc/html/libzapojit-0.0/
%{_datadir}/gir-1.0/Zpj-0.0.gir
%{_libdir}/libzapojit-0.0.so
%{_libdir}/pkgconfig/zapojit-0.0.pc

%changelog
