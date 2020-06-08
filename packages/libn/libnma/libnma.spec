#
# spec file for package libnma
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


%define sover 0
%define base_ver 1.8

Name:           libnma
Version:        1.8.28
Release:        0
Summary:        Shared library for NetworkManager-applet
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libnma
Source0:        https://download.gnome.org/sources/%{name}/%{base_ver}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM libnma-fix-segment-fault.patch bsc#1168347 glgo#GNOME/libnma#7 sckang@suse.com -- nma-ws: properly dispose wireless security objects.
Patch0:         libnma-fix-segment-fault.patch

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gck-1) >= 3.14
BuildRequires:  pkgconfig(gcr-3) >= 3.14
BuildRequires:  pkgconfig(gio-2.0) >= 2.38
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
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
Requires:       mobile-broadband-provider-info

%description -n %{name}%{sover}
Shared library for NetworkManager-applet.

%package -n     typelib-1_0-NMA-1_0
Summary:        Introspection bindings for %{name}

%description -n typelib-1_0-NMA-1_0
Introspection bindings for %{name}.

%package        devel
Summary:        Development Files for %{name}
Requires:       %{name}%{sover} = %{version}
Requires:       typelib-1_0-NMA-1_0 = %{version}

%description    devel
Development Files for %{name}.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc NEWS
%{_libdir}/%{name}.so.*
%{_datadir}/glib-2.0/schemas/org.gnome.nm-applet.gschema.xml

%files -n typelib-1_0-NMA-1_0
%{_libdir}/girepository-1.0/NMA-1.0.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/%{name}/
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/NMA-1.0.gir
%{_datadir}/vala/vapi/libnma.deps
%{_datadir}/vala/vapi/libnma.vapi

%files lang -f %{name}.lang

%changelog
