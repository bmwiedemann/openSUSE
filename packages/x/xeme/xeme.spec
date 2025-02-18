#
# spec file for package xeme
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
Name:           xeme
Version:        0+53
Release:        0
Summary:        High level XMPP parsing library
License:        LGPL-2.1-or-later
URL:            https://keep.imfreedom.org/xeme/xeme
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gi-docgen
BuildRequires:  pkgconfig(birb)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
Its goal is to handle all of the marshaling and unmarshaling for you and give
you high level XMPP stanza objects to work with.

%package devel
Summary:        Development files for %{name}
Requires:       typelib-1_0-Xeme-1_0 = %{version}

%description devel
%{summary}.

%package -n typelib-1_0-Xeme-1_0
Summary:        Library files for %{name}

%description -n typelib-1_0-Xeme-1_0
%{summary}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%package -n lib%{name}%{sover}
Summary:        Library files for %{name}

%description -n lib%{name}%{sover}
%{summary}.

%description doc
%{summary}.

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

%check
%meson_test

%files devel
%license LICENSE
%doc README.md
%{_includedir}/xeme-1.0
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Xeme-1.0.gir

%files doc
%{_datadir}/doc/%{name}

%files -n typelib-1_0-Xeme-1_0
%{_libdir}/girepository-1.0/Xeme-1.0.typelib

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.%{sover}
%{_libdir}/lib%{name}.so.%{sover}.*

%changelog
