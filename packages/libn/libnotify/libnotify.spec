#
# spec file for package libnotify
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libnotify
Version:        0.7.8
Release:        0
Summary:        Notifications Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            http://galago-project.org/
#Source0:       https://download.gnome.org/sources/libnotify/0.7/%%{name}-%%{version}.tar.xz
Source:         %{name}-%{version}.tar.xz
Source98:       libnotify-rpmlintrc
Source99:       baselibs.conf

BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
D-BUS notifications library.

%package -n libnotify4
Summary:        Notifications Library
Group:          System/Libraries
Recommends:     notification-daemon

%description -n libnotify4
D-BUS notifications library.

%package -n typelib-1_0-Notify-0_7
Summary:        Notifications Library -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Notify-0_7
D-BUS notifications library.

This package provides the GObject Introspection bindings for libnotify.

%package tools
Summary:        Notifications Library -- Tools
Group:          System/Libraries
Provides:       libnotify = %{version}
Obsoletes:      libnotify < %{version}

%description tools
D-BUS notifications library.

This package contains the notify-send tool to create notifications.

%package devel
Summary:        Notifications Library
Group:          Development/Libraries/X11
Requires:       libnotify4 = %{version}
Requires:       typelib-1_0-Notify-0_7 = %{version}
Provides:       libnotify-doc = %{version}
Obsoletes:      libnotify-doc < %{version}

%description devel
D-BUS notifications library.

%prep
%autosetup -p1

%build
%meson \
	-Dtests=false \
	-Dintrospection=enabled \
	-Dgtk_doc=true \
	-Ddocbook_docs=disabled \
	%{nil}
%meson_build

%install
%meson_install

%post -n libnotify4 -p /sbin/ldconfig
%postun -n libnotify4 -p /sbin/ldconfig

%files -n libnotify4
%license COPYING
# README is empty
%doc AUTHORS ChangeLog NEWS
%{_libdir}/*.so.*

%files -n typelib-1_0-Notify-0_7
%{_libdir}/girepository-1.0/Notify-0.7.typelib

%files tools
%{_bindir}/notify-send

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/libnotify

%changelog
