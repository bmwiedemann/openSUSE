#
# spec file for package cjs
#
# Copyright (c) 2024 SUSE LLC
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


%define soname  libcjs
%define sover   0
%define typelib typelib-1_0-CjsPrivate-1_0
%define __requires_exclude_from ^.*installed-tests.*$
Name:           cjs
Version:        6.0.0
Release:        0
Summary:        JavaScript module used by Cinnamon
License:        (GPL-2.0-or-later OR MPL-1.1 OR LGPL-2.1-or-later) AND MIT
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cjs
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  dbus-1
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  sysprof-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(mozjs-102)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(readline)
%else
BuildRequires:  readline-devel
%endif
BuildRequires:  pkgconfig(sysprof-capture-4)

%description
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

%package -n %{soname}%{sover}
Summary:        Shared Libraries for Cinnamon JS module
Group:          System/Libraries

%description -n %{soname}%{sover}
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package provides libraries for cjs.

%package -n %{typelib}
Summary:        Cinnamon JS module -- Introspection Bindings
Group:          System/Libraries

%description -n %{typelib}
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package provides the GObject Introspection bindings for
Cinnamon JS.

%package devel
Summary:        Development Files for Cinnamon JS module
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       %{soname}%{sover} = %{version}
Requires:       %{typelib} = %{version}

%description devel
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package contains development files for cjs.

%prep
%setup -q

%build
%meson --libexecdir=%{_libdir}/%{name}/
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes -s %{buildroot}%{_libdir}/%{name}/installed-tests/

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING*
%doc README.md debian/changelog
%{_bindir}/%{name}*

%files -n %{soname}%{sover}
%{_libdir}/libcjs.so.%{sover}*

%files -n %{typelib}
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/girepository-1.0/
%{_libdir}/%{name}/girepository-1.0/CjsPrivate-1.0.typelib

%files devel
%{_includedir}/%{name}-1.0/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/%{name}-1.0/

%changelog
