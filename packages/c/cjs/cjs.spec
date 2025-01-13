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


%define         sover   0
%define         typelib typelib-1_0-CjsPrivate-1_0
Name:           cjs
Version:        6.4.0
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
BuildRequires:  pkgconfig(mozjs-115)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(readline)
%else
BuildRequires:  readline-devel
%endif
BuildRequires:  pkgconfig(sysprof-6)
BuildRequires:  pkgconfig(sysprof-capture-4)

%description
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

%package -n lib%{name}%{sover}
Summary:        Shared Libraries for Cinnamon JS module

%description -n lib%{name}%{sover}
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package provides libraries for cjs.

%package -n typelib-1_0-CjsPrivate-1_0
Summary:        Cinnamon JS module -- Introspection Bindings

%description -n typelib-1_0-CjsPrivate-1_0
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package provides the GObject Introspection bindings for
Cinnamon JS.

%package devel
Summary:        Development Files for Cinnamon JS module
Requires:       %{name} = %{version}
Requires:       lib%{name}%{sover} = %{version}
Requires:       typelib-1_0-CjsPrivate-1_0 = %{version}

%description devel
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package contains development files for cjs.

%prep
%autosetup

%build
%meson \
  -Dcairo=enabled \
  -Dreadline=enabled \
  -Dprofiler=enabled \
  --libexecdir=%{_libdir}/%{name}/
%meson_build

%install
%meson_install
%fdupes -s %{buildroot}

%ldconfig_scriptlets -n lib%{name}%{sover}

%files
%license COPYING
%doc README.md NEWS
%{_bindir}/%{name}*

%files -n lib%{name}%{sover}
%{_libdir}/libcjs.so.%{sover}*

%files -n typelib-1_0-CjsPrivate-1_0
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/girepository-1.0/
%{_libdir}/%{name}/girepository-1.0/CjsPrivate-1.0.typelib

%files devel
%{_includedir}/%{name}-1.0/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_datadir}/%{name}-1.0/

%changelog
