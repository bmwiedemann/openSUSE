#
# spec file for package gxml
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


%global         GXmlAPI 0.20
%global         GXmlAPI_RPM 0_20
%define         sover -%{GXmlAPI_RPM}-2_0_2
%define         cname GXml
Name:           gxml
Version:        0.20.4
Release:        0
Summary:        GXml provides a GObject API for manipulating XML
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gxml
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         gxml-typelib-so-linking.patch
Patch1:         fix-formatting.patch
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  valadoc-doclet-devhelp
BuildRequires:  pkgconfig(gee-0.8) >= 0.20.5
BuildRequires:  pkgconfig(gio-2.0) >= 2.72
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.13

%description
GXml provides a GObject API for manipulating XML. Most functionality
is provided through libxml2. Currently, GXml provides the DOM Level 1
Core API.

%package doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%package lang
Summary:        Translations for %{name}
BuildArch:      noarch

%description lang
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}
Requires:       typelib-1_0-%{cname}-%{GXmlAPI_RPM} = %{version}

%description devel
%{summary}.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
%{summary}.

%package -n typelib-1_0-%{cname}-%{GXmlAPI_RPM}
Summary:        Typelib files for %{name}
Obsoletes:      typelib-1_0-%{cname}-%{sover} <= %{version}

%description -n typelib-1_0-%{cname}-%{GXmlAPI_RPM}
%{summary}.

%prep
%autosetup -p1

%build
%meson \
  -Ddocs=true \
  -Dexperimental=true \
  -Dintrospection=true
%meson_build

%install
%meson_install
%find_lang %{cname}-%{GXmlAPI}

#%%check
#right now broken as glib-2.0 has some issue
#%%meson_test

%ldconfig_scriptlets -n lib%{name}%{sover}

%files devel
%license COPYING
%doc AUTHORS DESIGN MAINTAINERS NEWS README
%{_datadir}/gir-1.0/%{cname}-%{GXmlAPI}.gir
%{_datadir}/vala/vapi/%{name}-%{GXmlAPI}.{deps,vapi}
%{_includedir}/%{name}-%{GXmlAPI}/
%{_libdir}/lib%{name}-%{GXmlAPI}.so
%{_libdir}/pkgconfig/%{name}-%{GXmlAPI}.pc

%files doc
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books
%{_datadir}/devhelp/books/%{cname}-%{GXmlAPI}

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}-%{GXmlAPI}.so.2*

%files -n typelib-1_0-%{cname}-%{GXmlAPI_RPM}
%{_libdir}/girepository-1.0/%{cname}-%{GXmlAPI}.typelib

%files lang -f %{cname}-%{GXmlAPI}.lang

%changelog
