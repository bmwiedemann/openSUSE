#
# spec file for package mutter
#
# Copyright (c) 2024 SUSE LLC
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


%bcond_with profiler

%define api_major 14
%define api_minor 0
%define libmutter libmutter-%{api_major}-%{api_minor}
Name:           mutter
Version:        46.3
Release:        0
Summary:        Window and compositing manager based on Clutter
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
Source0:        %{name}-%{version}.tar.zst

# PATCH-FIX-UPSTREAM mutter-disable-cvt-s390x.patch bsc#1158128 fcrozat@suse.com -- Do not search for cvt on s390x, it doesn't exist there
Patch1:         mutter-disable-cvt-s390x.patch
# PATCH-FIX-OPENSUSE mutter-window-actor-Special-case-shaped-Java-windows.patch -- window-actor: Special-case shaped Java windows
Patch2:         mutter-window-actor-Special-case-shaped-Java-windows.patch
# PATCH-FIX-UPSTREAM mutter-fix-x11-restart.patch glgo#GNOME/gnome-shell#7050 glgo#GNOME/mutter!3329 alynx.zhou@suse.com -- Fix crash on restarting mutter under x11
Patch3:         mutter-fix-x11-restart.patch
# PATCH-FIX-OPENSUSE 0001-Revert-clutter-actor-Cache-stage-relative-instead-of.patch glgo#GNOME/mutter#3302 bsc#1219546 alynx.zhou@suse.com -- Fix partial update on VT switch
Patch4:         0001-Revert-clutter-actor-Cache-stage-relative-instead-of.patch
#PATCH-FEATURE-OPENSUSE mutter-implement-text-input-v1.patch glgo#GNOME/mutter!3751 bsc#1219505 alynx.zhou@suse.com -- Allow input method to work in Wayland Chromium
Patch5:         mutter-implement-text-input-v1.patch

## SLE-only patches start at 1000
# PATCH-FEATURE-SLE mutter-SLE-bell.patch FATE#316042 bnc#889218 idonmez@suse.com -- make audible bell work out of the box.
Patch1000:      mutter-SLE-bell.patch
# PATCH-FIX-SLE mutter-SLE-relax-some-constraints-on-CSD-windows.patch bnc#883491 cxiong@suse.com -- Relax some constraints on window positioning for CSD windows s.t. they can be placed at the very top of the monitor.
Patch1001:      mutter-SLE-relax-some-constraints-on-CSD-windows.patch

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
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.37.2
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0) >= 232
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm) >= 2.4.118
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libinput) >= 1.15.0
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.21
BuildRequires:  pkgconfig(libstartup-notification-1.0) >= 0.7
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev) >= 136
BuildRequires:  pkgconfig(libwacom) >= 0.13
BuildRequires:  pkgconfig(pango) >= 1.2.0
BuildRequires:  pkgconfig(pixman-1) >= 0.42
BuildRequires:  pkgconfig(sm)
%if %{with profiler}
BuildRequires:  pkgconfig(sysprof-6)
BuildRequires:  pkgconfig(sysprof-capture-4) >= 3.37.2
%endif
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.33
BuildRequires:  pkgconfig(wayland-server) >= 1.22
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
%autosetup -N
%if !0%{?sle_version}
%autopatch -p1 -M 999
%else
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%endif
# SLE-only patches and translations.
%if 0%{?sle_version}
%patch -P 1000 -p1
%patch -P 1001 -p1
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
	-Dlibdisplay_info=true \
%if %{with profiler}
	-Dprofiler=true \
%else
	-Dprofiler=false \
%endif
	%{nil}
%meson_build

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
%{_libexecdir}/mutter-x11-frames
%{_udevrulesdir}/61-mutter.rules

# These so files are not split out since they are private to mutter
%{_libdir}/mutter-%{api_major}/libmutter-clutter-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/libmutter-cogl-pango-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/libmutter-cogl-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/libmutter-mtk-%{api_major}.so.*
%{_libdir}/mutter-%{api_major}/plugins/libdefault.so

# These typelibs are not split out since they are private to mutter
%{_libdir}/mutter-%{api_major}/Cally-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Clutter-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Cogl-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/CoglPango-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Meta-%{api_major}.typelib
%{_libdir}/mutter-%{api_major}/Mtk-%{api_major}.typelib

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
%{_libdir}/mutter-%{api_major}/Mtk-%{api_major}.gir
%{_libdir}/mutter-%{api_major}/libmutter-clutter-%{api_major}.so
%{_libdir}/mutter-%{api_major}/libmutter-cogl-pango-%{api_major}.so
%{_libdir}/mutter-%{api_major}/libmutter-cogl-%{api_major}.so
%{_libdir}/mutter-%{api_major}/libmutter-mtk-%{api_major}.so
%{_libdir}/libmutter-%{api_major}.so
%{_libdir}/pkgconfig/libmutter-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-clutter-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-cogl-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-cogl-pango-%{api_major}.pc
%{_libdir}/pkgconfig/mutter-mtk-%{api_major}.pc

%files lang -f %{name}.lang

%changelog
