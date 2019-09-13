#
# spec file for package telepathy-farstream
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


Name:           telepathy-farstream
Version:        0.6.2
Release:        0
Summary:        Telepathy library to handle Call channels
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
Url:            http://telepathy.freedesktop.org/
Source0:        http://telepathy.freedesktop.org/releases/telepathy-farstream/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(telepathy-glib) >= 0.21

%description
Telepathy Farstream is a Telepathy client library that uses Farsight2
to handle Call channels.

%package -n libtelepathy-farstream3
Summary:        Telepathy library to handle Call channels
# There used to be python bindings for this library, but this now
# achieved with introspection. Since there's no guarantee the
# bindings will still work with this version, we obsolete them
Group:          System/Libraries
Obsoletes:      python-tpfarstream < %{version}

%description -n libtelepathy-farstream3
Telepathy Farstream is a Telepathy client library that uses Farsight2
to handle Call channels.

%package -n typelib-1_0-TelepathyFarstream-0_6
Summary:        Introspection bindings for the Telepathy Call channel handling library
Group:          System/Libraries

%description -n typelib-1_0-TelepathyFarstream-0_6
Telepathy Farstream is a Telepathy client library that uses Farsight2
to handle Call channels.

%package devel
Summary:        Development files for the Telepathy Call channel handling library
Group:          Development/Languages/C and C++
Requires:       libtelepathy-farstream3 = %{version}
Requires:       typelib-1_0-TelepathyFarstream-0_6 = %{version}

%description devel
Telepathy Farstream is a Telepathy client library that uses Farsight2
to handle Call channels.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libtelepathy-farstream3 -p /sbin/ldconfig
%postun -n libtelepathy-farstream3 -p /sbin/ldconfig

%files -n libtelepathy-farstream3
%license COPYING
%doc ChangeLog NEWS README
%{_libdir}/libtelepathy-farstream.so.*

%files -n typelib-1_0-TelepathyFarstream-0_6
%{_libdir}/girepository-1.0/TelepathyFarstream-0.6.typelib

%files devel
%dir %{_includedir}/telepathy-1.0
%{_includedir}/telepathy-1.0/telepathy-farstream/
%{_libdir}/pkgconfig/telepathy-farstream.pc
%{_libdir}/libtelepathy-farstream.so
%doc %{_datadir}/gtk-doc/html/telepathy-farstream/
%{_datadir}/gir-1.0/TelepathyFarstream-0.6.gir

%changelog
