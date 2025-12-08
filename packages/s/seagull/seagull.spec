#
# spec file for package seagull
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


%define         sover 0
Name:           seagull
Version:        0.6.0
Release:        0
Summary:        A SQLite helper library
License:        LGPL-2.1-or-later
URL:            https://keep.imfreedom.org/seagull/seagull
Source0:        https://downloads.sf.net/pidgin/%{name}-%{version}.tar.xz
Source1:        https://downloads.sf.net/pidgin/%{name}-%{version}.tar.xz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x40de1dc7288fe3f50ab938c548f66affd9bdb729#/%{name}.keyring
BuildRequires:  meson >= 1.1.0
BuildRequires:  pkgconfig
BuildRequires:  python3-gi-docgen >= 2024.1
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.76.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(sqlite3) >= 3.27.0

%description
%{summary}.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
%{summary}.

%package -n typelib-1_0-Seagull-1_0
Summary:        Introspection file for %{name}

%description -n typelib-1_0-Seagull-1_0
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}
Requires:       typelib-1_0-Seagull-1_0 = %{version}

%description devel
%{summary}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup

%build
%meson \
  -Ddoc=true \
  -Dintrospection=true \
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%files -n typelib-1_0-Seagull-1_0
%{_libdir}/girepository-1.0/Seagull-1.0.typelib

%files devel
%license LICENSE
%doc README.md
%{_datadir}/gir-1.0/Seagull-1.0.gir
%{_includedir}/%{name}-1.0
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%{_datadir}/doc/%{name}

%changelog
