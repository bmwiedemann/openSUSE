#
# spec file for package libaccounts-glib
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


%define typelib typelib-1_0-Accounts-1_0
%define sover   0
%define _version VERSION_1.23-8d14b10652b2fe6c25d8ad8334e2d5023d254313
Name:           libaccounts-glib
Version:        1.23
Release:        0
Summary:        Account management library for GLib Applications
License:        LGPL-2.1
Group:          System/Libraries
Url:            https://gitlab.com/accounts-sso/libaccounts-glib
Source:         https://gitlab.com/accounts-sso/%{name}/repository/VERSION_%{version}/archive.tar.gz#/%{name}-%{_version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  autoconf >= 2.64
BuildRequires:  automake
BuildRequires:  gtk-doc
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(check) >= 0.9.4
BuildRequires:  pkgconfig(gio-2.0) >= 2.36
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.26
BuildRequires:  pkgconfig(gobject-2.0) >= 2.35.1
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python2)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3) >= 3.7.0

%description
This package contains the shared libraries for use by applications.

%package -n %{name}%{sover}
Summary:        Account management library for GLib Applications
Group:          System/Libraries

%description -n %{name}%{sover}
This package contains the shared libraries for use by applications.

%package -n python-libaccounts
Summary:        Python bindings for the Account management library
Group:          Development/Languages/Python

%description -n python-libaccounts
This package contains the python bindings for the account
management library.

%package -n python3-libaccounts
Summary:        Python bindings for the Account management library
Group:          Development/Languages/Python

%description -n python3-libaccounts
This package contains the python bindings for the account
management library.

%package -n %{typelib}
Summary:        Account management library for GLib Applications -- Introspection Bindings
Group:          System/Libraries

%description -n %{typelib}
This package contains the GObject Introspection bindings for the
accounts-glib library.

%package devel
Summary:        Development files for libaccounts-glib
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       %{typelib} = %{version}
Requires:       python-libaccounts = %{version}
Requires:       python3-libaccounts = %{version}

%description devel
This package contains the development files for the accounts-glib
library.

%package docs
Summary:        Documentation for libaccounts-glib
Group:          Documentation/HTML
BuildArch:      noarch

%description docs
This package contains the documentation for the accounts-glib
library.

%package tools
Summary:        Tools for libaccounts-glib
Group:          Development/Tools/Other
Requires:       %{name}%{sover} = %{version}

%description tools
This package contains the tools for the accounts-glib library.

%prep
%setup -q -n %{name}-%{_version}

%build
gtkdocize --copy --flavour no-tmpl
autoreconf -fi
%global _configure ../configure
for python in python2 python3; do
    mkdir -p build-$python
    pushd build-$python
    export PYTHON=$python
    %configure \
      --disable-static \
      --enable-gtk-doc
    make %{?_smp_mflags}
    popd
done

%install
%make_install -C build-python2
%make_install -C build-python3/pygobject
find %{buildroot} -type f -name "*.la" -delete -print

# Remove a Mer specific file.
rm -f %{buildroot}%{_datadir}/backup-framework/applications/accounts.conf

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS
%{_libdir}/%{name}.so.%{sover}*

%files -n %{typelib}
%defattr(-,root,root)
%{_libdir}/girepository-1.0/Accounts-1.0.typelib

%files -n python-libaccounts
%defattr(-,root,root)
%{python_sitearch}/gi/overrides/

%files -n python3-libaccounts
%defattr(-,root,root)
%{python3_sitearch}/gi/overrides/

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Accounts-1.0.gir
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/%{name}.*

%files docs
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/%{name}/

%files tools
%defattr(-,root,root)
%{_bindir}/ag-backup
%{_bindir}/ag-tool
%{_mandir}/man1/ag-backup.1%{?ext_man}
%{_mandir}/man1/ag-tool.1%{?ext_man}
%dir %{_datadir}/dbus-1/
%dir %{_datadir}/dbus-1/interfaces/
%{_datadir}/dbus-1/interfaces/com.google.code.AccountsSSO.Accounts.Manager.xml
%dir %{_datadir}/xml/accounts/
%dir %{_datadir}/xml/accounts/schema/
%dir %{_datadir}/xml/accounts/schema/dtd/
%{_datadir}/xml/accounts/schema/dtd/accounts-*.dtd

%changelog
