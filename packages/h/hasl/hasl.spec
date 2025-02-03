#
# spec file for package hasl
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
Name:           hasl
Version:        0.4.0
Release:        0
Summary:        Hassle-free Authentication and Security Layer
License:        LGPL-2.1-or-later
URL:            https://keep.imfreedom.org/hasl/hasl
Source0:        https://sourceforge.net/projects/pidgin/files/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://sourceforge.net/projects/pidgin/files/%{name}/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x40de1dc7288fe3f50ab938c548f66affd9bdb729#/%{name}.keyring
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gi-docgen
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gobject-2.0) >= 2.76
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libidn) >= 1.38

%description
The Hassle-free Authentication and Security Layer client library

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}
Requires:       typelib-1_0-Hasl-1_0 = %{version}

%description devel
%{summary}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%package -n typelib-1_0-Hasl-1_0
Summary:        Typelib for %{name}

%description -n typelib-1_0-Hasl-1_0
%{summary}.

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}
Recommends:     %{name}-lang = %{version}
Provides:       %{name} = %{version}

%description -n lib%{name}%{sover}
%{summary}.

%lang_package

%prep
%autosetup

%build
%meson \
  -Ddoc=true \
  -Dintrospection=true \
  -Dnls=true
%meson_build

%install
%meson_install
%find_lang %{name}

%check
%meson_test

%ldconfig_scriptlets -n lib%{name}%{sover}

%files devel
%license LICENSE
%doc README.md ChangeLog
%{_includedir}/%{name}-1.0
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Hasl-1.0.gir

%files doc
%doc README.md ChangeLog
%{_datadir}/doc/%{name}

%files -n typelib-1_0-Hasl-1_0
%license LICENSE
%doc README.md ChangeLog
%{_libdir}/girepository-1.0/Hasl-1.0.typelib

%files -n lib%{name}%{sover}
%license LICENSE
%doc README.md ChangeLog
%{_libdir}/lib%{name}.so.*

%files lang -f %{name}.lang

%changelog
