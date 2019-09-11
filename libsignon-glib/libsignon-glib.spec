#
# spec file for package libsignon-glib
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version VERSION_1.14-e90302e342bfd27bc8c9132ab9d0ea3d8723fd03

Name:           libsignon-glib
Version:        1.14
Release:        0
Summary:        Library for signond
License:        LGPL-2.1
Group:          System/Libraries
Url:            https://gitlab.com/accounts-sso/libsignon-glib
Source:         https://gitlab.com/accounts-sso/%{name}/repository/VERSION_%{version}/archive.tar.bz2#/%{name}-%{_version}.tar.bz2
BuildRequires:  gtk-doc
BuildRequires:  libtool >= 2.2
BuildRequires:  python-devel
BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0) >= 2.35.1
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(signond) >= 8.40
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GLib-based client library for applications handling account
authentication through the Online Accounts Single Sign-On service

%package -n libsignon-glib1
Summary:        Library for signond
Group:          System/Libraries

%description -n libsignon-glib1
GLib-based client library for applications handling account
authentication through the Online Accounts Single Sign-On service

This package provides shared libraries for libsignon-glib

%package devel
Summary:        Development headers for libsignon-glib
Group:          Development/Libraries/C and C++
Requires:       libsignon-glib1 = %{version}

%description devel
GLib-based client library for applications handling account
authentication through the Online Accounts Single Sign-On service

This package provides development headers for libsignon-glib.

%package -n typelib-1_0-Signon-1_0
Summary:        Library for signond -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Signon-1_0
GLib-based client library for applications handling account
authentication through the Online Accounts Single Sign-On service

This package provides the GObject Introspection bindings for
libsignon-glib library.

%prep
%setup -q -n %{name}-%{_version}
NOCONFIGURE=1 ./autogen.sh

%build
%configure
make -j1

%install
make install DESTDIR=%{buildroot} %{?_smp_mflags}
find %{buildroot}%{_libdir} -name "*.la" -delete

%post -n libsignon-glib1 -p /sbin/ldconfig

%postun -n libsignon-glib1 -p /sbin/ldconfig

%files -n libsignon-glib1
%defattr(-,root,root)
%doc AUTHORS README.md NEWS COPYING
%{_libdir}/libsignon-glib.so.1
%{_libdir}/libsignon-glib.so.1.0.0

%files devel
%defattr(-,root,root)
%{_includedir}/libsignon-glib
%{_libdir}/libsignon-glib.so
%{_libdir}/pkgconfig/libsignon-glib.pc
%{_datadir}/gir-1.0/Signon-1.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/signon.vapi

%files -n typelib-1_0-Signon-1_0
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Signon-1.0.typelib

%changelog
