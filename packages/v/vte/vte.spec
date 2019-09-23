#
# spec file for package vte
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.56.3
Release:        0
Summary:        Terminal Emulator Library
License:        LGPL-2.0-only AND LGPL-3.0-only AND GPL-3.0-or-later
Group:          Development/Libraries/GNOME
URL:            http://www.gnome.org
# Switched to sourceservice, as upstream have a tendency to not release tarballs on time.
#Source:         http://download.gnome.org/sources/vte/0.45/%%{_name}-%%{version}.tar.xz
Source:         %{_name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gcc-c++
#
# Needed due to using sourceservice and we need to bootstrap tarball
BuildRequires:  gnome-common
#
BuildRequires:  gobject-introspection-devel
BuildRequires:  gperf
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gnutls) >= 3.2.7
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(pango) >= 1.22.0
BuildRequires:  pkgconfig(vapigen) >= 0.24
BuildRequires:  pkgconfig(zlib)

%description
VTE is a terminal emulator library that provides a terminal widget for
use with GTK+ as well as handling of child process and terminal
emulation settings.

%package -n libvte%{_sover}
Summary:        Terminal Emulator Library
License:        LGPL-2.0-only
Group:          System/Libraries
Recommends:     %{name}-lang
# Needed to make lang package installable (and because we used to
# have a vte package earlier).
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
translation-update-upstream

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--with-gtk=%{_gtkver}\
	--disable-static \
	--disable-glade-catalogue \
	--enable-introspection \
	--enable-gtk-doc \
	%{nil}
%make_build

%install
%make_install

%find_lang vte-%{_apiver}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_prefix}

%post -n libvte%{_sover} -p /sbin/ldconfig
%postun -n libvte%{_sover} -p /sbin/ldconfig

%files -n libvte%{_sover}
%license COPYING.GPL3 COPYING.LGPL2 COPYING.LGPL3

%{_libdir}/*.so.*
%config %{_sysconfdir}/profile.d/vte.sh

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

%files lang -f vte-%{_apiver}.lang

%changelog
