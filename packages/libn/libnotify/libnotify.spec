#
# spec file for package libnotify
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.8.2
Release:        0
Summary:        Notifications Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            https://galago-project.org/
Source:         https://download.gnome.org/sources/libnotify/0.8/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gi-docgen)
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
	-Dman=true \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libnotify4

%files -n libnotify4
%license COPYING
%{_libdir}/*.so.*

%files -n typelib-1_0-Notify-0_7
%{_libdir}/girepository-1.0/Notify-0.7.typelib

%files tools
%{_bindir}/notify-send
%{_mandir}/man1/notify-send.1%{?ext_man}

%files devel
%doc AUTHORS NEWS README.md
%doc %{_datadir}/doc/libnotify-0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gir-1.0/*.gir

%changelog
