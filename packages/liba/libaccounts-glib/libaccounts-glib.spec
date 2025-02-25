#
# spec file for package libaccounts-glib
#
# Copyright (c) 2022 SUSE LLC
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


%define typelib typelib-1_0-Accounts-1_0
%define sover   0
Name:           libaccounts-glib
Version:        1.27
Release:        0
Summary:        Account management library for GLib Applications
License:        LGPL-2.1-only
URL:            https://gitlab.com/accounts-sso/libaccounts-glib
Source:         https://gitlab.com/accounts-sso/libaccounts-glib/-/archive/VERSION_%{version}/libaccounts-glib-VERSION_%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.26
BuildRequires:  pkgconfig(gobject-2.0) >= 2.35.1
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3) >= 3.7.0
BuildRequires:  pkgconfig(vapigen)

%description
This package contains the shared libraries for use by applications.

%package -n libaccounts-glib%{sover}
Summary:        Account management library for GLib Applications

%description -n libaccounts-glib%{sover}
This package contains the shared libraries for use by applications.

%package -n %{typelib}
Summary:        Account management library for GLib Applications -- Introspection Bindings

%description -n %{typelib}
This package contains the GObject Introspection bindings for the
accounts-glib library.

%package devel
Summary:        Development files for libaccounts-glib
Requires:       libaccounts-glib%{sover} = %{version}
Requires:       %{typelib} = %{version}

%description devel
This package contains the development files for the accounts-glib
library.

%package docs
Summary:        Documentation for libaccounts-glib
BuildArch:      noarch

%description docs
This package contains the documentation for the accounts-glib
library.

%package tools
Summary:        Tools for libaccounts-glib
Requires:       libaccounts-glib%{sover} = %{version}

%description tools
This package contains the tools for the accounts-glib library.

%prep
%autosetup -p1 -n libaccounts-glib-VERSION_%{version}

%build
%meson

%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libaccounts-glib%{sover}

%files -n libaccounts-glib%{sover}
%doc NEWS
%license COPYING
%{_libdir}/libaccounts-glib.so.%{sover}*
%{_libdir}/libaccounts-glib.so.1.27

%files -n %{typelib}
%{_libdir}/girepository-1.0/Accounts-1.0.typelib

%files devel
%{_includedir}/libaccounts-glib/
%{_datadir}/gettext/
%{_libdir}/libaccounts-glib.so
%{_libdir}/pkgconfig/libaccounts-glib.pc
%{_datadir}/gir-1.0/Accounts-1.0.gir
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/libaccounts-glib.*

%files docs
%doc %{_datadir}/gtk-doc/html/libaccounts-glib/

%files tools
%{_bindir}/ag-backup
%{_bindir}/ag-tool
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/interfaces/
%{_datadir}/dbus-1/interfaces/com.google.code.AccountsSSO.Accounts.Manager.xml
%dir %{_datadir}/xml/accounts/
%dir %{_datadir}/xml/accounts/schema/
%dir %{_datadir}/xml/accounts/schema/dtd/
%{_datadir}/xml/accounts/schema/dtd/accounts-*.dtd

%changelog
