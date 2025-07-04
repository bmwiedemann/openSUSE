#
# spec file for package grilo
#
# Copyright (c) 2025 SUSE LLC
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


Name:           grilo
Version:        0.3.19
Release:        0
Summary:        Framework for browsing and searching media content
License:        LGPL-2.1-or-later
Group:          Productivity/Multimedia/Other
URL:            https://live.gnome.org/Grilo
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  meson >= 0.62.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0) >= 2.58
BuildRequires:  pkgconfig(glib-2.0) >= 2.58
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(oauth)
BuildRequires:  pkgconfig(totem-plparser) >= 3.4.1
BuildRequires:  pkgconfig(vapigen) >= 0.27

%description
Grilo is a framework for browsing and searching media content from
various sources using a single API.

%package -n libgrilo-0_3-0
Summary:        Framework for browsing and searching media content
# Needed for the -lang package to be installable
# Without plugins, grilo is useless
Group:          System/Libraries
Recommends:     grilo-plugins
Provides:       %{name} = %{version}

%description -n libgrilo-0_3-0
Grilo is a framework for browsing and searching media content from
various sources using a single API.

%package -n typelib-1_0-Grl-0_3
Summary:        Framework for browsing and searching media content -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Grl-0_3
Grilo is a framework for browsing and searching media content from
various sources using a single API.

This package provides the GObject Introspection bindings for the
libgrl library.

%package -n libgrlnet-0_3-0
Summary:        Framework for browsing and searching media content -- Networking Helper Library
Group:          System/Libraries

%description -n libgrlnet-0_3-0
Grilo is a framework for browsing and searching media content from
various sources using a single API.

%package -n libgrlpls-0_3-0
Summary:        Framework for browsing and searching media content -- Playlist Helper Library
Group:          System/Libraries

%description -n libgrlpls-0_3-0
Grilo is a framework for browsing and searching media content from
various sources using a single API.

%package -n typelib-1_0-GrlNet-0_3
Summary:        Introspection bindings for grilo
Group:          System/Libraries

%description -n typelib-1_0-GrlNet-0_3
Grilo is a framework for browsing and searching media content from
various sources using a single API.

This package provides the GObject Introspection bindings for the
libgrlnet library.

%package -n typelib-1_0-GrlPls-0_3
Summary:        Introspection bindings for grilo
Group:          System/Libraries

%description -n typelib-1_0-GrlPls-0_3
Grilo is a framework for browsing and searching media content from
various sources using a single API.

This package provides the GObject Introspection bindings for the
libgrlnet library.

%package tools
Summary:        Framework for browsing and searching media content -- Tools
Group:          Productivity/Multimedia/Other

%description tools
Grilo is a framework for browsing and searching media content from
various sources using a single API.

This package provides tools related to Grilo.

%package devel
Summary:        Framework for browsing and searching media content -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libgrilo-0_3-0 = %{version}
Requires:       libgrlnet-0_3-0 = %{version}
Requires:       libgrlpls-0_3-0 = %{version}
Requires:       typelib-1_0-Grl-0_3 = %{version}
Requires:       typelib-1_0-GrlNet-0_3 = %{version}
Requires:       typelib-1_0-GrlPls-0_3 = %{version}

%description devel
Grilo is a framework for browsing and searching media content from
various sources using a single API.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D soup3=true \
	-D enable-test-ui=false \
	%{nil}
%meson_build

%install
%meson_install
# No need for manpages since the binary is not built
rm -vrf %{buildroot}%{_mandir}/man1/grilo-test-ui-*
%find_lang %{name} %{?no_lang_C}
# Create directories needed for plugins
install -d %{buildroot}%{_libdir}/grilo-0.3
install -d %{buildroot}%{_datadir}/grilo-0.3/plugins
%fdupes %{buildroot}%{_datadir}

%check
%ifarch s390x
%meson_test -t 5
%else
%meson_test
%endif

%ldconfig_scriptlets -n libgrilo-0_3-0
%ldconfig_scriptlets -n libgrlnet-0_3-0
%ldconfig_scriptlets -n libgrlpls-0_3-0

%files -n libgrilo-0_3-0
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libgrilo-0.3.so.*
# Directories needed for plugins
%dir %{_libdir}/grilo-0.3

%files -n typelib-1_0-Grl-0_3
%{_libdir}/girepository-1.0/Grl-0.3.typelib

%files -n libgrlnet-0_3-0
%license COPYING

%{_libdir}/libgrlnet-0.3.so.*

%files -n libgrlpls-0_3-0
%license COPYING

%{_libdir}/libgrlpls-0.3.so.*

%files -n typelib-1_0-GrlNet-0_3
%{_libdir}/girepository-1.0/GrlNet-0.3.typelib

%files -n typelib-1_0-GrlPls-0_3
%{_libdir}/girepository-1.0/GrlPls-0.3.typelib

%files tools
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/grl-inspect-0.3
%{_bindir}/grl-launch-0.3
%{_mandir}/man1/grl-inspect-0.3.1%{?ext_man}
%{_mandir}/man1/grl-launch-0.3.1%{?ext_man}

%files devel
%doc %{_datadir}/gtk-doc/html/grilo/
%{_includedir}/grilo-0.3/
%{_libdir}/*.so
%{_libdir}/pkgconfig/grilo-0.3.pc
%{_libdir}/pkgconfig/grilo-net-0.3.pc
%{_libdir}/pkgconfig/grilo-pls-0.3.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.deps
%{_datadir}/vala/vapi/*.vapi

%files lang -f %{name}.lang

%changelog
