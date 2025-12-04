#
# spec file for package gspell
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


%define shlib lib%{name}-1-3
Name:           gspell
Version:        1.14.2
Release:        0
Summary:        A spell checker library for GTK+ applications
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://gitlab.gnome.org/GNOME/gspell
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  gtk-doc >= 1.25
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(enchant-2) >= 2.1.3
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.42.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(iso-codes) >= 0.35
%ifarch aarch64 %{ix86} x86_64 ppc ppc64 ppc64le s390x armv7l armv7hl armv6l armv6hl
BuildRequires:  pkgconfig(valgrind)
%endif
BuildRequires:  pkgconfig(vapigen)

%description
gspell provides a flexible API to implement the spell checking in a GTK+
application.

%package -n %{shlib}
Summary:        Spell checker library for GTK+
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n %{shlib}
gspell provides a flexible API to implement the spell checking in a GTK+
application.

This package provides the shared libraries for gspell.

%package -n typelib-1_0-Gspell-1
Summary:        Introspection bindings for the GTK+ spell checker library
# typelib name was wrong until version 1.7.1; obsolete to ease upgrade path
Group:          System/Libraries
Obsoletes:      typelib-1_0-Gspell-1_0 < 1.7.1

%description -n typelib-1_0-Gspell-1
gspell provides a flexible API to implement the spell checking in a GTK+
application.

This package provides the GObject Introspection bindings for gspell.

%package devel
Summary:        Development files for the GTK+ spell checker library
Group:          Development/Libraries/GNOME
Requires:       %{shlib} = %{version}
Requires:       typelib-1_0-Gspell-1 = %{version}

%description devel
gspell provides a flexible API to implement the spell checking in a GTK+
application.

This package provides the files necessary for developing software using
gspell.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

### FIXME ###
#%%check
#%%meson_test

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}-1 %{?no_lang_C}

%ldconfig_scriptlets -n %{shlib}

%files
%license LICENSES
%doc AUTHORS README.md NEWS
%{_bindir}/gspell-app1

%files -n %{shlib}
%{_libdir}/lib%{name}-1.so.*

%files -n typelib-1_0-Gspell-1
%{_libdir}/girepository-1.0/Gspell-1.typelib

%files devel
%doc %{_datadir}/gtk-doc/html/gspell-1/
%{_includedir}/gspell-1/
%{_libdir}/lib%{name}-1.so
%{_libdir}/pkgconfig/gspell-1.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gspell-1.*
%dir %{_libexecdir}/installed-tests
%dir %{_libexecdir}/installed-tests/gspell-1
%{_libexecdir}/installed-tests/gspell-1/test-checker
%{_libexecdir}/installed-tests/gspell-1/test-entry
%{_libexecdir}/installed-tests/gspell-1/test-icu
%{_libexecdir}/installed-tests/gspell-1/test-inline-checker-text-buffer
%{_libexecdir}/installed-tests/gspell-1/test-text-iter
%{_libexecdir}/installed-tests/gspell-1/test-utils
%dir %{_datadir}/installed-tests
%dir %{_datadir}/installed-tests/gspell-1
%{_datadir}/installed-tests/gspell-1/test-checker.test
%{_datadir}/installed-tests/gspell-1/test-entry.test
%{_datadir}/installed-tests/gspell-1/test-icu.test
%{_datadir}/installed-tests/gspell-1/test-inline-checker-text-buffer.test
%{_datadir}/installed-tests/gspell-1/test-text-iter.test
%{_datadir}/installed-tests/gspell-1/test-utils.test

%files lang -f %{name}-1.lang

%changelog
