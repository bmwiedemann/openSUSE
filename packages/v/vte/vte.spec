#
# spec file for package vte
#
# Copyright (c) 2020 SUSE LLC
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


%define _sover -2_91-0
%define _apiver 2.91
%define _binver 2.91
%define _gtkver 3.0
%define _name   vte

Name:           vte
Version:        0.60.3
Release:        0
Summary:        Terminal Emulator Library
License:        LGPL-2.0-only AND LGPL-3.0-only AND GPL-3.0-or-later
Group:          Development/Libraries/GNOME
URL:            https://gitlab.gnome.org/GNOME/vte
Source:         %{_name}-%{version}.tar.xz

BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(fribidi) >= 1.0.0
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gnutls) >= 3.2.7
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16.0
BuildRequires:  pkgconfig(libpcre2-8) >= 10.21
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pango) >= 1.22.0
BuildRequires:  pkgconfig(vapigen) >= 0.24
BuildRequires:  pkgconfig(zlib)

%description
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

%package -n libvte%{_sover}
Summary:        Terminal Emulator Library
# Needed to make lang package installable (and because we used to
# have a vte package earlier).
License:        LGPL-2.0-only
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libvte%{_sover}
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

%package -n typelib-1_0-Vte-%{?_binver}
Summary:        Introspection bindings for the VTE terminal emulator library
License:        LGPL-2.0-only
Group:          System/Libraries

%description -n typelib-1_0-Vte-%{?_binver}
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides the GObject Introspection bindings for VTE.

%package tools
Summary:        Tools from the VTE terminal emulator package
License:        LGPL-2.0-only
Group:          System/Libraries

%description tools
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package provides tools using VTE.

%package devel
Summary:        Development files for the VTE terminal emulator library
License:        LGPL-2.0-only
Group:          Development/Libraries/GNOME
Requires:       libvte%{_sover} = %{version}
Requires:       typelib-1_0-Vte-%{?_binver} = %{version}
Provides:       vte-doc = %{version}
Obsoletes:      vte-doc < %{version}

%description devel
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

This package contains the files needed for building applications using
VTE.

%lang_package

%prep
%autosetup -n %{_name}-%{version} -p1
translation-update-upstream po vte-%{_apiver}

%build
%meson \
	-Ddocs=true \
	%{nil}
%meson_build

%install
%meson_install

%find_lang vte-%{_apiver}
%fdupes %{buildroot}/%{_prefix}

%post -n libvte%{_sover} -p /sbin/ldconfig
%postun -n libvte%{_sover} -p /sbin/ldconfig

%files -n libvte%{_sover}
%license COPYING.GPL3 COPYING.LGPL2 COPYING.LGPL3
%{_libdir}/*.so.*
%config %{_sysconfdir}/profile.d/vte.sh
%config %{_sysconfdir}/profile.d/vte.csh
%dir %{_userunitdir}/vte-spawn-.scope.d
%{_userunitdir}/vte-spawn-.scope.d/defaults.conf
%{_libexecdir}/vte-urlencode-cwd

%files -n typelib-1_0-Vte-%{?_binver}
%{_libdir}/girepository-1.0/Vte-%{_apiver}.typelib

%files tools
%{_bindir}/vte-%{?_binver}

%files devel
%doc AUTHORS NEWS
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/vte-%{_apiver}/
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gtk-doc/html/vte-%{_apiver}/
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/vte-2.91.vapi
%{_datadir}/vala/vapi/vte-2.91.deps

%files lang -f vte-%{_apiver}.lang

%changelog
