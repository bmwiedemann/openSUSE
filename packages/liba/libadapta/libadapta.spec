#
# spec file for package libadapta
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         sover 0
Name:           libadapta
Version:        1.5.0
Release:        0
Summary:        LibAdwaita with theme support and a few extras
License:        LGPL-2.1-or-later
URL:            https://github.com/xapp-project/libadapta
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson >= 0.59.0
BuildRequires:  python3-gi-docgen
BuildRequires:  sassc
BuildRequires:  vala
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.13.4

%description
libAdapta is libAdwaita with theme support and a few extras.

It provides the same features and the same look as libAdwaita by default.

In desktop environments which provide theme selection, libAdapta apps follow
the theme and use the proper window controls.

libAdapta also provides a compatibility header which makes it easy for
developers to switch between libAdwaita and libAdapta without requiring code
changes.

%lang_package

%package -n typelib-1_0-Adap-1
Summary:        Typelib for %{name}

%description -n typelib-1_0-Adap-1
%{summary}.

%package devel
Summary:        Development files for %{name}

%description devel
%{summary}.

%package docs
Summary:        Documentation for %{name}
BuildArch:      noarch

%description docs
%{summary}.

%package 1-%{sover}
Summary:        Library for %{name}
Provides:       %{name} = %{version}

%description 1-%{sover}
%{summary}.

%prep
%autosetup

%build
%meson \
  -Dexamples=false \
  -Dgtk_doc=true \
  -Dintrospection=enabled \
  -Dtests=true \
  -Dvapi=true \
  %{nil}
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}

%ldconfig_scriptlets 1-%{sover}

%files devel
%license COPYING
%doc AUTHORS HACKING.md NEWS README.md
%{_datadir}/gir-1.0/Adap-1.gir
%{_datadir}/vala/vapi/%{name}-1.deps
%{_datadir}/vala/vapi/%{name}-1.vapi
%{_includedir}/%{name}-1
%{_libdir}/%{name}-1.so
%{_libdir}/pkgconfig/%{name}-1.pc

%files docs
%{_datadir}/doc/%{name}-1
%{_datadir}/themes/LibAdapta-Example

%files 1-%{sover}
%{_libdir}/%{name}-1.so.%{sover}

%files -n typelib-1_0-Adap-1
%{_libdir}/girepository-1.0/Adap-1.typelib

%files lang -f %{name}.lang

%changelog
