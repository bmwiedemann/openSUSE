#
# spec file for package gjs
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


%bcond_with profiling
%global __requires_exclude typelib\\(GioWin32\\)

Name:           gjs
Version:        1.86.0
Release:        0
Summary:        JavaScript bindings based on gobject-introspection and Mozilla
License:        LGPL-2.0-or-later AND MIT
Group:          Development/Libraries/GNOME
URL:            https://wiki.gnome.org/Projects/Gjs
Source0:        %{name}-%{version}.tar.zst

# PATCH-FIX-UPSTREAM gjs-gi-Allow-optional-inout-arguments-to-be-null.patch glgo#GNOME/gjs!1047 bsc#1258964 xwang@suse.com -- Allow optional inout arguments to be null
Patch1:         gjs-gi-Allow-optional-inout-arguments-to-be-null.patch

BuildRequires:  /usr/bin/dbus-run-session
BuildRequires:  c++_compiler
BuildRequires:  meson >= 0.54.0
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
%if 0%{?sle_version} && 0%{?sle_version} <= 150500
BuildRequires:  xorg-x11-Xvfb
%else
BuildRequires:  xorg-x11-server-Xvfb
%endif
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.85.1
BuildRequires:  pkgconfig(girepository-2.0) >= 2.85.1
BuildRequires:  pkgconfig(glib-2.0) >= 2.85.1
BuildRequires:  pkgconfig(gobject-2.0) >= 2.85.1
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0) >= 2.85.1
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(mozjs-140)
%if %{with profiling}
BuildRequires:  pkgconfig(sysprof-capture-4)
%endif
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
License:        LGPL-2.0-or-later AND MIT
Group:          System/Libraries
Obsoletes:      typelib-1_0-GjsDBus-1_0 < %{version}

%description -n typelib-1_0-GjsPrivate-1_0
This module contains JavaScript bindings based on gobject-introspection and the
Mozilla SpiderMonkey JavaScript engine.

%package -n libgjs-devel
Summary:        Development files for the GJS library
License:        LGPL-2.0-or-later AND MIT
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
%meson \
 	-Dinstalled_tests=false \
	-Dprofiler=%{?with_profiling:enabled}%{!?with_profiling:disabled} \
	%{nil}
%meson_build

%install
%meson_install

%check
%ifnarch s390x
export DISPLAY=:98
Xvfb :98 >& Xvfb.log & trap "kill $! || true" EXIT
sleep 10
%meson_test
%endif

%ldconfig_scriptlets -n libgjs0

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/gjs
%{_bindir}/gjs-console

%files -n libgjs0
%license LICENSES/LGPL-2.0-or-later.txt
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
# FIXME -- nuke these
%dir %{_libexecdir}/installed-tests/gjs
%{_libexecdir}/installed-tests/gjs/GIMarshallingTests-1.0.typelib
%{_libexecdir}/installed-tests/gjs/Regress-1.0.typelib
%{_libexecdir}/installed-tests/gjs/RegressUnix-1.0.typelib
%{_libexecdir}/installed-tests/gjs/Utility-1.0.typelib
%{_libexecdir}/installed-tests/gjs/WarnLib-1.0.typelib
%{_libexecdir}/installed-tests/gjs/libgimarshallingtests.so
%{_libexecdir}/installed-tests/gjs/libregress.so
%{_libexecdir}/installed-tests/gjs/libutility.so
%{_libexecdir}/installed-tests/gjs/libwarnlib.so

%changelog
