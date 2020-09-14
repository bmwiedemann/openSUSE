#
# spec file for package mutter
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


# don't enable sysprof support by default
%bcond_with profiler

%define api_major 6
%define api_minor 0
%define libmutter libmutter-%{api_major}-%{api_minor}
Name:           mutter
Version:        3.36.6+2
Release:        0
Summary:        Window and compositing manager based on Clutter
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
Source:         %{name}-%{version}.tar.xz

# PATCH-FIX-OPENSUSE mutter-Lower-HIDPI_LIMIT-to-144.patch fate#326682, bsc#1125467 qkzhu@suse.com -- Lower HIDPI_LIMIT to 144
Patch3:         mutter-Lower-HIDPI_LIMIT-to-144.patch
# PATCH-FIX-UPSTREAM mutter-disable-cvt-s390x.patch bsc#1158128 fcrozat@suse.com -- Do not search for cvt on s390x, it doesn't exist there
Patch4:         mutter-disable-cvt-s390x.patch

## SLE-only patches start at 1000
# PATCH-FEATURE-SLE mutter-SLE-bell.patch FATE#316042 bnc#889218 idonmez@suse.com -- make audible bell work out of the box.
Patch1000:      mutter-SLE-bell.patch
# PATCH-FIX-SLE mutter-SLE-relax-some-constraints-on-CSD-windows.patch bnc#883491 cxiong@suse.com -- Relax some constraints on window positioning for CSD windows s.t. they can be placed at the very top of the monitor.
Patch1001:      mutter-SLE-relax-some-constraints-on-CSD-windows.patch
# PATCH-NEEDS-REBASE mutter-SLE-bsc984738-grab-display.patch bsc#984738 bgo#769387 hpj@suse.com -- Revert a upstream commit to avoid X11 race condition that results in wrong dialog sizes.
Patch1002:      mutter-SLE-bsc984738-grab-display.patch

BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  xorg-x11-server
BuildRequires:  xorg-x11-server-wayland
BuildRequires:  zenity
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gbm) >= 17.1
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.61.1
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.61.1
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.33.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.7
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libdrm) >= 2.4.83
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.0
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 136
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(pango) >= 1.2.0
BuildRequires:  pkgconfig(sm)
%if %{with profiler}
BuildRequires:  pkgconfig(sysprof-3)
BuildRequires:  pkgconfig(sysprof-capture-3) >= 3.35.2
%endif
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.18
BuildRequires:  pkgconfig(wayland-server) >= 1.13.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcomposite) >= 0.2
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.3
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xrandr) >= 1.5.0
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
Requires:       zenity
Provides:       windowmanager
# Obsolete the now private typelib.
Obsoletes:      typelib-1_0-Meta-3_0

%description
Mutter is a window and compositing manager based on Clutter, forked
from Metacity.

%package -n %{libmutter}
Summary:        Window and compositing manager based on Clutter
# we need the gsettings schema; hopefully, they'll stay backwards compatible
# (since we can't require = version, to not break SLPP)
Group:          System/Libraries
Requires:       %{name}-data >= %{version}
# We need to obsolete the old mutter libs, as otherwise upgrading is impossible
# This makes me believe we should probably fold libmutter into the main package
# with the next update (3.30)
Obsoletes:      libmutter-1-0
Obsoletes:      libmutter0

%description -n %{libmutter}
Mutter is a window and compositing manager based on Clutter, forked
from Metacity.

This package contains a library for shared features.

%package data
Summary:        Data files for mutter, a window and compositing manager based on Clutter
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}

%description data
Mutter is a window and compositing manager based on Clutter, forked
from Metacity.

This package contains data files needed by mutter and its library.

%package devel
Summary:        Development files for mutter, a window and compositing manager
Group:          Development/Libraries/GNOME
Requires:       %{libmutter} = %{version}
Requires:       %{name} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of the mutter library.

%lang_package

%prep
%setup -q
%patch3 -p1
%patch4 -p1

# SLE-only patches and translations.
translation-update-upstream po mutter
%if 0%{?sle_version}
%patch1000 -p1
%patch1001 -p1
# %patch1002 -p1
%endif

%build
%meson \
	-Degl_device=true \
	-Dcogl_tests=false \
	-Dclutter_tests=false \
	-Dtests=false \
	-Dinstalled_tests=false \
	-Dxwayland_initfd=disabled \
%if %{with profiler}
	-Dprofiler=true \
%else
	-Dprofiler=false \
%endif
	%{nil}
%meson_build

#%%check
#%%meson_test

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%post -n %{libmutter} -p /sbin/ldconfig
%postun -n %{libmutter} -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS
%{_mandir}/man1/mutter.1%{?ext_man}
%{_bindir}/mutter
%{_libexecdir}/mutter-restart-helper
%{_datadir}/applications/mutter.desktop

# These so files are not split out since they are private to mutter
%{_libdir}/mutter-%{api_major}/libmutter-clutter-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/libmutter-cogl-pango-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/libmutter-cogl-path-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/libmutter-cogl-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/plugins/libdefault.so

# These typelibs are not split out since they are private to mutter
%{_libdir}/mutter-%{api_major}/Cally-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Clutter-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/ClutterX11-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Cogl-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/CoglPango-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Meta-%{api_major}.typelib

%files -n %{libmutter}
%{_libdir}/libmutter-%{api_major}.so.*
%dir %{_libdir}/mutter-%{api_major}/
# users of libmutter need this directory
%dir %{_libdir}/mutter-%{api_major}/plugins/

%files data
# Do not depend on g-c-c just for a directory
%dir %{_datadir}/gnome-control-center
%dir %{_datadir}/gnome-control-center/keybindings
%{_datadir}/gnome-control-center/keybindings/50-mutter-windows.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-navigation.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-system.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-wayland.xml
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml

%files devel
%{_includedir}/mutter-%{api_major}/
%{_libdir}/mutter-%{api_major}/Meta-%{api_major}.gir
%{_libdir}/mutter-%{api_major}/Cally-%{api_major}.gir
%{_libdir}/mutter-%{api_major}/Clutter-%{api_major}.gir
%{_libdir}/mutter-%{api_major}/ClutterX11-%{api_major}.gir
%{_libdir}/mutter-%{api_major}/Cogl-%{api_major}.gir
%{_libdir}/mutter-%{api_major}/CoglPango-%{api_major}.gir
%{_libdir}/mutter-%{api_major}/libmutter-clutter-%{api_major}.so
%{_libdir}/mutter-%{api_major}/libmutter-cogl-pango-%{api_major}.so
%{_libdir}/mutter-%{api_major}/libmutter-cogl-path-%{api_major}.so
%{_libdir}/mutter-%{api_major}/libmutter-cogl-%{api_major}.so
%{_libdir}/libmutter-%{api_major}.so
%{_libdir}/pkgconfig/libmutter-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-clutter-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-clutter-x11-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-cogl-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-cogl-pango-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-cogl-path-%{api_major}.pc

%files lang -f %{name}.lang

%changelog
