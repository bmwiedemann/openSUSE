#
# spec file for package muffin
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


%define soname  libmuffin
%define sover   0
%define typelib typelib-1_0-Muffin-0_0
%define _lto_cflags %{nil}
Name:           muffin
Version:        6.4.1
Release:        0
Summary:        Cinnamon Desktop default window manager
License:        GPL-2.0-or-later AND MIT
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/muffin
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  fdupes
BuildRequires:  libxcvt
BuildRequires:  meson
BuildRequires:  mutter-devel
BuildRequires:  zenity
BuildRequires:  pkgconfig(cinnamon-desktop) >= 4.0.0
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xwayland)
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

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}
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
%doc NEWS README* debian/changelog
%{_bindir}/muffin
%{_libdir}/%{name}/
%{_libexecdir}/muffin-restart-helper
%exclude %{_libdir}/%{name}/*.typelib
%exclude %{_libdir}/%{name}/*.gir
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/muffin.1.*
%{_datadir}/glib-2.0/schemas/*.gschema.xml

%files lang -f %{name}.lang

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files -n typelib-1_0-Muffin-0_0
%{_libdir}/%{name}/*.typelib

%files devel
%{_includedir}/muffin/
%{_libdir}/libmuffin.so
%{_libdir}/muffin/*.gir
%{_libdir}/pkgconfig/*

%changelog
