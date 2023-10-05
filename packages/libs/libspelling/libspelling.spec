#
# spec file for package libspelling
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


Name:           libspelling
Version:        0.2.0
Release:        0
Summary:        A spellcheck library for GTK 4
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/chergert/libspelling
Source:         https://download.gnome.org/sources/libspelling/0.2/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 6d26ffd30c78b7f255b1665fac3fb88960ea01ba.patch -- egg: fix license to be LGPLv2.1+
Patch:          %{url}/-/commit/6d26ffd30c78b7f255b1665fac3fb88960ea01ba.patch

BuildRequires:  pkgconfig
BuildRequires:  c_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(gi-docgen)

%description
A spellcheck library for GTK 4.
This library is heavily based upon GNOME Text Editor and GNOME
Builder's spellcheck implementation. However, it is licensed
LGPL-2.1-or-later

%package -n libspelling1-1
Summary:        Shared libraries for %{name}

%description -n libspelling1-1
Shared libraries for %{name}.

%package -n typelib-1_0-Spelling-1
Summary:        Introspection file for %{name}

%description -n typelib-1_0-Spelling-1
Introspection file for %{name}.

%package devel
Summary:        Development files for %{name}
Requires:       libspelling1-1 = %{version}
Requires:       typelib-1_0-Spelling-1 = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n libspelling1-1

%files -n libspelling1-1
%license COPYING
%doc NEWS README.md
%{_libdir}/libspelling-1.so.1*

%files -n typelib-1_0-Spelling-1
%{_libdir}/girepository-1.0/Spelling-1.typelib

%files devel
%doc %{_datadir}/doc/libspelling-1/
%{_includedir}/libspelling-1
%{_libdir}/libspelling-1.so
%{_libdir}/pkgconfig/libspelling-1.pc
%{_datadir}/gir-1.0/Spelling-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libspelling-1.deps
%{_datadir}/vala/vapi/libspelling-1.vapi

%changelog

