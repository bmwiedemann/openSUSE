#
# spec file for package magpie
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

%define api_major 0
%bcond_with profiler
Name:           magpie
Version:        0.9.3+0
Release:        0
Summary:        Magpie is a softish fork of Mutter
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/BuddiesOfBudgie/magpie
Source0:        %{name}-%{version}.tar.xz
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
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.12.0
BuildRequires:  pkgconfig(lcms2) >= 2.6
BuildRequires:  pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:  pkgconfig(libdrm) >= 2.4.83
BuildRequires:  pkgconfig(libeis-1.0)
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
# needs the configuration files from mutter still
Requires:       mutter >= 44.0

%description
Magpie is a soft-fork of GNOME's mutter
at version 43 tailored to the requirements
of the Budgie Desktop 10 series (from v10.8 and later). 

%package devel
Summary:        Development files for magpie, a window and compositing manager
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of the magpie library.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Degl_device=true \
%if %{with profiler}
	-Dprofiler=true \
%else
	-Dprofiler=false \
%endif
%meson_build

%install
%meson_install
%find_lang %{name}

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS

# These so files are not split out since they are private to magpie
%{_libdir}/magpie-%{api_major}/libmagpie-clutter-%{api_major}.so.*
%{_libdir}/magpie-%{api_major}/libmagpie-cogl-pango-%{api_major}.so.*
%{_libdir}/magpie-%{api_major}/libmagpie-cogl-%{api_major}.so.*

# These typelibs are not split out since they are private to magpie
%{_libdir}/magpie-%{api_major}/Cally-%{api_major}.typelib
%{_libdir}/magpie-%{api_major}/Clutter-%{api_major}.typelib
%{_libdir}/magpie-%{api_major}/Cogl-%{api_major}.typelib
%{_libdir}/magpie-%{api_major}/CoglPango-%{api_major}.typelib
%{_libdir}/magpie-%{api_major}/Meta-%{api_major}.typelib

%{_libdir}/libmagpie-%{api_major}.so.*
%dir %{_libdir}/magpie-%{api_major}/

%files devel
%{_includedir}/magpie-%{api_major}/
%{_libdir}/magpie-%{api_major}/Meta-%{api_major}.gir
%{_libdir}/magpie-%{api_major}/Cally-%{api_major}.gir
%{_libdir}/magpie-%{api_major}/Clutter-%{api_major}.gir
%{_libdir}/magpie-%{api_major}/Cogl-%{api_major}.gir
%{_libdir}/magpie-%{api_major}/CoglPango-%{api_major}.gir
%{_libdir}/magpie-%{api_major}/libmagpie-clutter-%{api_major}.so
%{_libdir}/magpie-%{api_major}/libmagpie-cogl-pango-%{api_major}.so
%{_libdir}/magpie-%{api_major}/libmagpie-cogl-%{api_major}.so
%{_libdir}/libmagpie-%{api_major}.so
%{_libdir}/pkgconfig/libmagpie-%{api_major}.pc
%{_libdir}/pkgconfig/magpie-clutter-%{api_major}.pc
%{_libdir}/pkgconfig/magpie-cogl-%{api_major}.pc
%{_libdir}/pkgconfig/magpie-cogl-pango-%{api_major}.pc

%files lang -f %{name}.lang

%changelog
