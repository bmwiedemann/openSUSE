#
# spec file for package chrono
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


%define         sover 0
%define         appid io.github.alainm23.chrono
Name:           chrono
Version:        1.0.0
Release:        0
Summary:        A natural language date and time parser library for Vala/GLib applications
License:        GPL-3.0-or-later
URL:            https://github.com/alainm23/chrono
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         soversion.patch
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:  valadoc-doclet-html
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.70
BuildRequires:  pkgconfig(gobject-2.0)

%description
A natural language date and time parser library for Vala/GLib applications.

Originally developed as part of Planify.

%package devel
Summary:        A natural language date and time parser library for Vala/GLib applications
Requires:       lib%{name}%{sover} = %{version}

%description devel
A natural language date and time parser library for Vala/GLib applications.

Originally developed as part of Planify.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
%{summary}.

%prep
%autosetup -p1

%build
%meson \
  -Ddocs=true \
  -Dtests=true \
  %{nil}
%meson_build

%install
%meson_install

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}

%files devel
%license LICENSE
%doc README.md
%{_includedir}/chrono.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/metainfo/%{appid}.metainfo.xml
%{_datadir}/vala/vapi/%{name}.vapi

%changelog
