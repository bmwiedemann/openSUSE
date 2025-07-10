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


%define         sover 0_20_4
%define         cname GXml
Name:           gxml
Version:        0.20.4
Release:        0
Summary:        GXml provides a GObject API for manipulating XML
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/GNOME/gxml
Source0:        %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         versioning.patch
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
Requires:       typelib-1_0-%{cname}-%{sover} = %{version}
Recommends:     %{name}-lang = %{version}

%description devel
%{summary}.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
%{summary}.

%package -n typelib-1_0-%{cname}-%{sover}
Summary:        Typelib files for %{name}

%description -n typelib-1_0-%{cname}-%{sover}
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
%find_lang %{cname}

#%%check
#right now broken as glib-2.0 has some issue
#%%meson_test

%ldconfig_scriptlets -n lib%{name}%{sover}

%files devel
%license COPYING
%doc AUTHORS DESIGN MAINTAINERS NEWS README
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_datadir}/gir-1.0/%{cname}-%{version}.gir
%{_datadir}/vala/vapi/%{name}.{deps,vapi}
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books
%{_datadir}/devhelp/books/%{cname}

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{version}

%files -n typelib-1_0-%{cname}-%{sover}
%{_libdir}/girepository-1.0/%{cname}-%{version}.typelib

%files lang -f %{cname}.lang

%changelog
