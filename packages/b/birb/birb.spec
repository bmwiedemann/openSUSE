#
# spec file for package birb
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
Name:           birb
Version:        0.3.1
Release:        0
Summary:        A library of utilities for GLib based apps
License:        LGPL-2.1-or-later
URL:            https://keep.imfreedom.org/birb/birb
Source0:        https://sourceforge.net/projects/pidgin/files/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://sourceforge.net/projects/pidgin/files/%{name}/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x40de1dc7288fe3f50ab938c548f66affd9bdb729#/%{name}.keyring
Source3:        lgpl-2.1.txt
BuildRequires:  meson >= 1.0.0
BuildRequires:  pkgconfig
BuildRequires:  python3-gi-docgen >= 2024.1
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)  >= 2.76
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
Description is in development
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}
Requires:       typelib-1_0-Birb-1_0 = %{version}

%description devel
%{summary}.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
%{summary}.

%package -n typelib-1_0-Birb-1_0
Summary:        Typelib

%description -n typelib-1_0-Birb-1_0
%{summary}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%prep
%autosetup
cp %{SOURCE3} .

%build
%meson \
  -Ddoc=true \
  -Dintrospection=true \
  -Dnls=true
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%license lgpl-2.1.txt
%doc AUTHORS ChangeLog README.md
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}-1.0
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Birb-1.0.gir

%files -n typelib-1_0-Birb-1_0
%{_libdir}/girepository-1.0/Birb-1.0.typelib

%files doc
%doc AUTHORS ChangeLog README.md
%{_datadir}/doc/%{name}

%changelog
