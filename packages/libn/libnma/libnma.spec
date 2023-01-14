#
# spec file for package libnma
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


%define sover 0
%define base_ver 1.10

Name:           libnma
Version:        1.10.6
Release:        0
Summary:        Shared library for NetworkManager-applet
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libnma
Source0:        https://download.gnome.org/sources/%{name}/%{base_ver}/%{name}-%{version}.tar.xz

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gck-1) >= 3.14
BuildRequires:  pkgconfig(gck-2)
BuildRequires:  pkgconfig(gcr-3) >= 3.14
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gio-2.0) >= 2.38
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12
BuildRequires:  pkgconfig(gtk4) >= 4.0
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libnm) >= 1.7
BuildRequires:  pkgconfig(mobile-broadband-provider-info)
BuildRequires:  pkgconfig(vapigen)

%description
Shared library for NetworkManager-applet.

%package -n     %{name}%{sover}
Summary:        Shared library for NetworkManager-applet
# Make lang package installable.
Provides:       %{name}
# Since version 1.8.28
Obsoletes:      nma-data < %{version}
Provides:       nma-data = %{version}
Obsoletes:      libnma-data < %{version}
Provides:       libnma-data = %{version}
Requires:       %{name}-glib-schema >= %{version}
Requires:       mobile-broadband-provider-info

%description -n %{name}%{sover}
Shared library for NetworkManager-applet.

%package glib-schema
Summary:        GLib-schema org.gnome.nm-applet.eap
BuildArch:      noarch

%description glib-schema
The glib-schema allows libnma to be configured wia dconf

It is required by libnma

%package -n     %{name}-gtk4-%{sover}
Summary:        Shared library for NetworkManager-applet. Gtk4 version
Requires:       mobile-broadband-provider-info

%description -n %{name}-gtk4-%{sover}
Shared library for NetworkManager-applet. Gtk4 version.

%package -n     typelib-1_0-NMA-1_0
Summary:        Introspection bindings for %{name}

%description -n typelib-1_0-NMA-1_0
Introspection bindings for %{name}.

%package -n     typelib-1_0-NMA4-1_0
Summary:        Introspection bindings for %{name}

%description -n typelib-1_0-NMA4-1_0
Introspection bindings for %{name}.

%package        devel
Summary:        Development Files for %{name}
Requires:       %{name}%{sover} = %{version}
Requires:       typelib-1_0-NMA-1_0 = %{version}

%description    devel
Development Files for %{name}.

%package        gtk4-devel
Summary:        Development Files for %{name}-gtk4
# Depend on main devel package for the shared header files.
Requires:       %{name}-devel = %{version}
Requires:       %{name}-gtk4-%{sover} = %{version}
Requires:       typelib-1_0-NMA4-1_0 = %{version}

%description    gtk4-devel
Development Files for %{name}-gtk4.

%package        docs
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    docs
Documentation files for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D b_lto=true \
	-D libnma_gtk4=true \
	-D gcr=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
# this file lives in NetworkManager-applet since 1.30.0
rm %{buildroot}%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml

%ldconfig_scriptlets -n %{name}%{sover}
%ldconfig_scriptlets -n %{name}-gtk4-%{sover}

%files -n %{name}%{sover}
%license COPYING
%doc NEWS
%{_libdir}/%{name}.so.*

%files glib-schema
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.eap.gschema.xml

%files -n %{name}-gtk4-%{sover}
%{_libdir}/%{name}-gtk4.so.*

%files -n typelib-1_0-NMA-1_0
%{_libdir}/girepository-1.0/NMA-1.0.typelib

%files -n typelib-1_0-NMA4-1_0
%{_libdir}/girepository-1.0/NMA4-1.0.typelib

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/NMA-1.0.gir
%{_datadir}/vala/vapi/%{name}.deps
%{_datadir}/vala/vapi/%{name}.vapi

%files gtk4-devel
%{_libdir}/%{name}-gtk4.so
%{_libdir}/pkgconfig/%{name}-gtk4.pc
%{_datadir}/gir-1.0/NMA4-1.0.gir
%{_datadir}/vala/vapi/%{name}-gtk4.deps
%{_datadir}/vala/vapi/%{name}-gtk4.vapi

%files docs
%doc %{_datadir}/gtk-doc/html/%{name}/

%files lang -f %{name}.lang

%changelog
