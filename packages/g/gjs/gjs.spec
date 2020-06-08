#
# spec file for package gjs
#
# Copyright (c) 2020 SUSE LLC
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


Name:           gjs
Version:        1.64.3
Release:        0
Summary:        JavaScript bindings based on gobject-introspection and Mozilla
License:        MIT AND LGPL-2.0-or-later
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/Gjs
Source0:        https://download.gnome.org/sources/gjs/1.64/%{name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  git
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  readline-devel
BuildRequires:  systemtap-sdt-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.58.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.53.4
BuildRequires:  pkgconfig(gthread-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(mozjs-68)
# Hack - fix sysprof static devel requires instead
BuildRequires:  pkgconfig(sysprof-3)
BuildRequires:  pkgconfig(sysprof-capture-3)
Requires:       libgjs0 = %{version}
ExcludeArch:    s390

%description
This module contains JavaScript bindings based on gobject-introspection and the
Mozilla SpiderMonkey JavaScript engine.

%package -n libgjs0
Summary:        JavaScript bindings based on gobject-introspection and Mozilla
License:        LGPL-2.0-or-later
Group:          System/Libraries
Provides:       libgjs-0 = %{version}
Obsoletes:      libgjs-0 < %{version}

%description -n libgjs0
This module contains JavaScript bindings based on gobject-introspection and the
Mozilla SpiderMonkey JavaScript engine.

%package -n typelib-1_0-GjsPrivate-1_0
Summary:        Introspection bindings for the GJS library
# The tyeplib was renamed in gnome 3.6, to reflect it is a private lib.
License:        MIT AND LGPL-2.0-or-later
Group:          System/Libraries
Obsoletes:      typelib-1_0-GjsDBus-1_0 < %{version}

%description -n typelib-1_0-GjsPrivate-1_0
This module contains JavaScript bindings based on gobject-introspection and the
Mozilla SpiderMonkey JavaScript engine.

%package -n libgjs-devel
Summary:        Development files for the GJS library
License:        MIT AND LGPL-2.0-or-later
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       libgjs0 = %{version}
Requires:       typelib-1_0-GjsPrivate-1_0 = %{version}
# Just a helper provides
Provides:       gjs-devel = %{version}

%description -n libgjs-devel
This module contains JavaScript bindings based on gobject-introspection and the
Mozilla SpiderMonkey JavaScript engine.

%prep
%autosetup -p1

%build
# FIXME # Doesn't play well with systemtap -- lets test this during 3.37 unstable round, do we still needed?
%global _lto_cflags %{nil}

%meson \
	-Ddtrace=true \
	-Dsystemtap=true \
	-Dinstalled_tests=false \
	%{nil}
%meson_build

%install
%meson_install

# FIXME # Try again on next versionbump
#%%check
#%%meson_test

%post -n libgjs0 -p /sbin/ldconfig
%postun -n libgjs0 -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/gjs
%{_bindir}/gjs-console

%files -n libgjs0
%license COPYING.LGPL
%{_libdir}/*.so.*

%files -n typelib-1_0-GjsPrivate-1_0
%dir %{_libdir}/gjs
%dir %{_libdir}/gjs/girepository-1.0/
%{_libdir}/gjs/girepository-1.0/GjsPrivate-1.0.typelib

%files -n libgjs-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/%{name}-1.0/
%{_datadir}/systemtap/tapset/*.stp

%changelog
