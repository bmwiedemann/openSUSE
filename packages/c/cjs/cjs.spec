#
# spec file for package cjs
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define         sover   0
%global __requires_exclude typelib\\(GIMarshallingTests!|GIMarshallingTests)|Gio!|Gio)|Regress!|Regress)|WarnLib!|WarnLib)\\)

Name:           cjs
Version:        140.0
Release:        0
Summary:        JavaScript module used by Cinnamon
License:        (GPL-2.0-or-later OR MPL-1.1 OR LGPL-2.1-or-later) AND MIT
URL:            https://github.com/linuxmint/cjs
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(mozjs-140)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(readline)
%else
BuildRequires:  readline-devel
%endif
BuildRequires:  pkgconfig(sysprof-6)
BuildRequires:  pkgconfig(sysprof-capture-4)
Conflicts:      gjs

%description
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

%package -n lib%{name}%{sover}
Summary:        Shared Libraries for Cinnamon JS module

%description -n lib%{name}%{sover}
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package provides libraries for cjs.

%package devel
Summary:        Development Files for Cinnamon JS module
Requires:       %{name} = %{version}
Requires:       lib%{name}%{sover} = %{version}

%description devel
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package contains development files for cjs.

%package tests
Summary:        Tests for the cjs package
Requires:       %{name} = %{version}

%description tests
The cjs-tests package contains tests that can be used to verify
the functionality of the installed cjs package.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}%{_prefix}

%ldconfig_scriptlets -n lib%{name}%{sover}

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/%{name}*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/girepository-1.0
%{_libdir}/%{name}/girepository-1.0/GjsPrivate-1.0.typelib

%files -n lib%{name}%{sover}
%{_libdir}/libcjs.so.%{sover}*

%files devel
%{_includedir}/%{name}-1.0/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/%{name}-1.0/

%files tests
%{_libexecdir}/installed-tests/
%{_datadir}/installed-tests/
%{_datadir}/glib-2.0/schemas/org.cinnamon.CjsTest.gschema.xml

%changelog
