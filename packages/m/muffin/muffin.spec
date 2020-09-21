#
# spec file for package muffin
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


%define soname  libmuffin
%define sover   0
%define typelib typelib-1_0-Muffin-0_0
%define _lto_cflags %{nil}
Name:           muffin
Version:        4.6.3
Release:        0
Summary:        Cinnamon Desktop default window manager
License:        GPL-2.0-or-later AND MIT
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/muffin
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE muffin-svid-default-source.patch marguerite@opensuse.org -- Change _SVID_SOURCE to _DEFAULT_SOURCE.
Patch0:         %{name}-svid-default-source.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  mutter-devel
BuildRequires:  update-desktop-files
BuildRequires:  zenity
BuildRequires:  pkgconfig(cinnamon-desktop) >= 4.0.0
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xtst)
Requires:       cinnamon-gschemas
Requires:       zenity
Recommends:     %{name}-lang
Provides:       windowmanager
%glib2_gsettings_schema_requires

%description
Cinnamon Desktop default window manager.
Muffin uses GTK+ and Clutter to do everything.

%lang_package

%package -n %{soname}%{sover}
Summary:        Muffin shared libraries
Group:          System/Libraries

%description -n %{soname}%{sover}
Cinnamon Desktop default window manager.
Muffin uses GTK+ and Clutter to do everything.

This package provides Muffin's shared libraries.

%package -n %{typelib}
Summary:        Muffin Introspection bindings
Group:          System/Libraries

%description -n %{typelib}
Cinnamon Desktop default window manager.
Muffin uses GTK+ and Clutter to do everything.

This package provides the GObject Introspection bindings for muffin.

%package devel
Summary:        Muffin development files
Group:          Development/Libraries/Other
Requires:       %{soname}%{sover} = %{version}
Requires:       %{typelib} = %{version}

%description devel
Cinnamon Desktop default window manager.
Muffin uses GTK+ and Clutter to do everything.

This package provides the development files.

%prep
%autosetup -p1

NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static \
           --enable-compile-warnings=minimum \
           --disable-wayland-egl-platform \
           --disable-wayland-egl-server \
           --disable-kms-egl-platform \
           --disable-wayland \
           --disable-native-backend \
           --disable-clutter-doc

%make_build V=1

%install
%make_install
%find_lang %{name}
%suse_update_desktop_file %{name}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%if 0%{?suse_version} < 1500
%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun
%endif

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README README* rationales.txt debian/changelog
%{_bindir}/muffin
%{_libdir}/%{name}/
%{_libexecdir}/muffin-restart-helper
%exclude %{_libdir}/%{name}/*.typelib
%exclude %{_libdir}/%{name}/*.gir
%dir %{_datadir}/muffin/
%{_datadir}/muffin/theme/
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/muffin.1.*
%{_datadir}/glib-2.0/schemas/*.gschema.xml

%files lang -f %{name}.lang

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*
%{_libdir}/%{soname}-clutter-%{sover}.so
%{_libdir}/%{soname}-cogl-%{sover}.so
%{_libdir}/%{soname}-cogl-pango-%{sover}.so
%{_libdir}/%{soname}-cogl-path-%{sover}.so

%files -n typelib-1_0-Muffin-0_0
%{_libdir}/%{name}/*.typelib

%files devel
%{_bindir}/muffin-message
%{_bindir}/muffin-theme-viewer
%{_bindir}/muffin-window-demo
%{_datadir}/muffin/icons/
%{_datadir}/gtk-doc/html/muffin/
%{_includedir}/muffin/
%{_libdir}/libmuffin.so
%{_libdir}/muffin/*.gir
%{_libdir}/pkgconfig/*
%{_mandir}/man1/muffin-*

%changelog
