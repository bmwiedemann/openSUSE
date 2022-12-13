#
# spec file for package mutter
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without profiler

%define api_major 11
%define api_minor 0
%define libmutter libmutter-%{api_major}-%{api_minor}
Name:           mutter
Version:        43.2
Release:        0
Summary:        Window and compositing manager based on Clutter
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
# Source url disabled, using git checkout via source service
#Source0:        https://download.gnome.org/sources/mutter/42/%%{name}-%%{version}.tar.xz
Source0:        %{name}-%{version}.tar.xz

# PATCH-FIX-OPENSUSE mutter-Lower-HIDPI_LIMIT-to-144.patch fate#326682, bsc#1125467 qkzhu@suse.com -- Lower HIDPI_LIMIT to 144
Patch0:         mutter-Lower-HIDPI_LIMIT-to-144.patch
# PATCH-FIX-UPSTREAM mutter-disable-cvt-s390x.patch bsc#1158128 fcrozat@suse.com -- Do not search for cvt on s390x, it doesn't exist there
Patch1:         mutter-disable-cvt-s390x.patch
# PATCH-FIX-OPENSUSE mutter-window-actor-Special-case-shaped-Java-windows.patch -- window-actor: Special-case shaped Java windows
Patch2:         mutter-window-actor-Special-case-shaped-Java-windows.patch
# PATCH-FIX-UPSTREAM mutter-crash-meta_context_terminate.patch bsc#1199382 glgo#GNOME/mutter#2267 xwang@suse.com -- Fix SIGSEGV in meta_context_terminate
Patch3:         mutter-crash-meta_context_terminate.patch

## SLE-only patches start at 1000
# PATCH-FEATURE-SLE mutter-SLE-bell.patch FATE#316042 bnc#889218 idonmez@suse.com -- make audible bell work out of the box.
Patch1000:      mutter-SLE-bell.patch
# PATCH-FIX-SLE mutter-SLE-relax-some-constraints-on-CSD-windows.patch bnc#883491 cxiong@suse.com -- Relax some constraints on window positioning for CSD windows s.t. they can be placed at the very top of the monitor.
Patch1001:      mutter-SLE-relax-some-constraints-on-CSD-windows.patch
# PATCH-FIX-SLE mutter-SLE-bsc984738-grab-display.patch bsc#984738 bgo#769387 hpj@suse.com -- Revert a upstream commit to avoid X11 race condition that results in wrong dialog sizes.
Patch1002:      mutter-SLE-bsc984738-grab-display.patch

BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  fdupes
%ifnarch s390x
BuildRequires:  (libxcvt if xorg-x11-server > 21)
%endif
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig
BuildRequires:  xorg-x11-server
BuildRequires:  xvfb-run
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(colord) >= 1.4.5
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fribidi) >= 1.0.0
BuildRequires:  pkgconfig(gbm) >= 17.3
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.69.0
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.69.0
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.37.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.8
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.12.0
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:  pkgconfig(libdrm) >= 2.4.83
BuildRequires:  pkgconfig(libinput) >= 1.15.0
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.21
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.7
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 136
BuildRequires:  pkgconfig(libwacom) >= 0.13
BuildRequires:  pkgconfig(pango) >= 1.2.0
BuildRequires:  pkgconfig(sm)
%if %{with profiler}
BuildRequires:  pkgconfig(sysprof-4)
BuildRequires:  pkgconfig(sysprof-capture-4) >= 3.37.3
%endif
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.21
BuildRequires:  pkgconfig(wayland-server) >= 1.13.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcomposite) >= 0.4
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes) >= 3
BuildRequires:  pkgconfig(xi) >= 1.7.4
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.3
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xrandr) >= 1.5.0
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xwayland)
Requires:       gnome-settings-daemon
Provides:       windowmanager
# Obsolete the now private typelib.
Obsoletes:      typelib-1_0-Meta-3_0
# libmutter-<n>-0 and mutter-data were folded into the main package after GNOME 40
# The library is not realy usable decoupled from the mutter version, and offering to
# parallel install it only gives a false sense of capability. A full GNOME Stack
# has a matching gnome-shell, mutter, libmutter version.
Obsoletes:      libmutter-8-0 <= %{version}
# mutter-data was essentilly hard-required at the same version, as mutter requires
# libmutter-<n>-0 (which has a soname bump at every major version change), libmutter
# required mutter-data >= %%{version} and mutter-data required mutter=%%{version}.
Obsoletes:      mutter-data <= %{version}

%description
Mutter is a window and compositing manager based on Clutter, forked
from Metacity.

%package devel
Summary:        Development files for mutter, a window and compositing manager
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of the mutter library.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# SLE-only patches and translations.
%if 0%{?sle_version}
%patch1000 -p1
%patch1001 -p1
%patch1002 -p1
%endif

%build
%meson \
	-Degl_device=true \
	-Dwayland_eglstream=true \
	-Dcogl_tests=false \
	-Dclutter_tests=false \
	-Dtests=false \
	-Dinstalled_tests=false \
	-Dxwayland_initfd=auto \
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

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_mandir}/man1/mutter.1%{?ext_man}
%{_bindir}/mutter
%{_libexecdir}/mutter-restart-helper
%{_datadir}/applications/mutter.desktop
%{_udevrulesdir}/61-mutter.rules

# These so files are not split out since they are private to mutter
%{_libdir}/mutter-%{api_major}/libmutter-clutter-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/libmutter-cogl-pango-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/libmutter-cogl-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/plugins/libdefault.so

# These typelibs are not split out since they are private to mutter
%{_libdir}/mutter-%{api_major}/Cally-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Clutter-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Cogl-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/CoglPango-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Meta-%{api_major}.typelib

%{_libdir}/libmutter-%{api_major}.so.*
%dir %{_libdir}/mutter-%{api_major}/
# users of libmutter need this directory
%dir %{_libdir}/mutter-%{api_major}/plugins/

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
%{_libdir}/mutter-%{api_major}/Cogl-%{api_major}.gir
%{_libdir}/mutter-%{api_major}/CoglPango-%{api_major}.gir
%{_libdir}/mutter-%{api_major}/libmutter-clutter-%{api_major}.so
%{_libdir}/mutter-%{api_major}/libmutter-cogl-pango-%{api_major}.so
%{_libdir}/mutter-%{api_major}/libmutter-cogl-%{api_major}.so
%{_libdir}/libmutter-%{api_major}.so
%{_libdir}/pkgconfig/libmutter-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-clutter-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-cogl-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-cogl-pango-%{api_major}.pc

%files lang -f %{name}.lang

%changelog
