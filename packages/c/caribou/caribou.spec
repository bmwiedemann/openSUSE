#
# spec file for package caribou
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


Name:           caribou
Version:        0.4.21
Release:        0
Summary:        On-screen Keyboard for GNOME
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://live.gnome.org/Caribou
Source0:        http://download.gnome.org/sources/caribou/0.4/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM caribou-vala-build-fix.patch boo#1186617 mgorse@suse.com -- fix the build with newer valac versions.
Patch0:         caribou-vala-build-fix.patch
# PATCH-FIX-UPSTREAM caribou-CVE-2021-3567.patch boo#1186617 mgorse@suse.com -- fix segfault when attempting to use shifted characters.
Patch1:         caribou-CVE-2021-3567.patch
# PATCH-FIX-UPSTREAM caribou-stop-patching-gir.patch mgorse@suse.com -- stop patching the GIR.
Patch2:         caribou-stop-patching-gir.patch
# PATCH-FIX-UPSTREAM caribou-css-fix.patch boo#1187112 mgorse@suse.com -- fix failure to start in GNOME flashback.
Patch3:         caribou-css-fix.patch
# Needed for Patch2
BuildRequires:  libtool
# For directory ownership
BuildRequires:  dbus-1
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-gobject >= 3.18
BuildRequires:  python3-xml
BuildRequires:  vala >= 0.13
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(clutter-1.0)
BuildRequires:  pkgconfig(gdk-3.0) >= 3.0.0
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pygobject-3.0) >= 2.90.3
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
Requires:       python3-atspi
Requires:       python3-xml
%glib2_gsettings_schema_requires

%description
Caribou is a text entry and UI navigation application being developed
as an alternative to the Gnome On-screen Keyboard. The overarching goal
for Caribou is to create a usable solution for people whose primary way
of accessing a computer is a switch device.

%package gtk-module-common
Summary:        On-screen Keyboard for GNOME -- Common Files for GTK+ Modules
Group:          System/GUI/GNOME
Recommends:     %{name}-gtk2-module
Recommends:     %{name}-gtk3-module

%description gtk-module-common
Caribou is a text entry and UI navigation application being developed
as an alternative to the Gnome On-screen Keyboard. The overarching goal
for Caribou is to create a usable solution for people whose primary way
of accessing a computer is a switch device.

This package contains files common to both the GTK+ 2 and GTK+ 3
modules.

%package gtk2-module
Summary:        On-screen Keyboard for GNOME -- GTK+ 2 Module
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       %{name}-gtk-module-common = %{version}
Supplements:    packageand(%{name}:gtk2)

%description gtk2-module
Caribou is a text entry and UI navigation application being developed
as an alternative to the Gnome On-screen Keyboard. The overarching goal
for Caribou is to create a usable solution for people whose primary way
of accessing a computer is a switch device.

%package gtk3-module
Summary:        On-screen Keyboard for GNOME -- GTK+ 3 Module
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       %{name}-gtk-module-common = %{version}
Supplements:    packageand(%{name}:gtk3)

%description gtk3-module
Caribou is a text entry and UI navigation application being developed
as an alternative to the Gnome On-screen Keyboard. The overarching goal
for Caribou is to create a usable solution for people whose primary way
of accessing a computer is a switch device.

%package -n libcaribou0
Summary:        On-screen Keyboard for GNOME -- Library
Group:          System/Libraries
Requires:       %{name}-common >= %{version}

%description -n libcaribou0
Caribou is a text entry and UI navigation application being developed
as an alternative to the Gnome On-screen Keyboard. The overarching goal
for Caribou is to create a usable solution for people whose primary way
of accessing a computer is a switch device.

%package common
Summary:        On-screen Keyboard for GNOME -- Common data files
Group:          System/Libraries

%description common
Caribou is a text entry and UI navigation application being developed
as an alternative to the Gnome On-screen Keyboard. The overarching goal
for Caribou is to create a usable solution for people whose primary way
of accessing a computer is a switch device.

%package -n typelib-1_0-Caribou-1_0
Summary:        On-screen Keyboard for GNOME -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Caribou-1_0
Caribou is a text entry and UI navigation application being developed
as an alternative to the Gnome On-screen Keyboard. The overarching goal
for Caribou is to create a usable solution for people whose primary way
of accessing a computer is a switch device.

This package provides the GObject Introspection bindings for the caribou
library.

%package devel
Summary:        On-screen Keyboard for GNOME -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libcaribou0 = %{version}
Requires:       typelib-1_0-Caribou-1_0 = %{version}

%description devel
Caribou is a text entry and UI navigation application being developed
as an alternative to the Gnome On-screen Keyboard. The overarching goal
for Caribou is to create a usable solution for people whose primary way
of accessing a computer is a switch device.

%lang_package

%prep
%autosetup -p1

%build
# Needed for patch2
autoreconf -fi
export CFLAGS="$CFLAGS -Wno-error=incompatible-pointer-types"
%configure \
    --disable-static     \
    --enable-gtk3-module \
    --enable-gtk2-module PYTHON=python3
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}

%post -n libcaribou0 -p /sbin/ldconfig
%postun -n libcaribou0 -p /sbin/ldconfig

%files
%license COPYING
%doc README
%{_bindir}/caribou-preferences
%{python3_sitelib}/caribou/
%{_datadir}/antler/
%{_datadir}/dbus-1/services/org.gnome.Caribou.Antler.service
%{_datadir}/dbus-1/services/org.gnome.Caribou.Daemon.service
%{_datadir}/glib-2.0/schemas/org.gnome.antler.gschema.xml
%{_libexecdir}/antler-keyboard
%{_libexecdir}/caribou
%{_sysconfdir}/xdg/autostart/caribou-autostart.desktop

%files gtk-module-common
%dir %{_libdir}/gnome-settings-daemon-3.0
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/caribou-gtk-module.desktop

%files gtk2-module
%{_libdir}/gtk-2.0/modules/libcaribou-gtk-module.so

%files gtk3-module
%{_libdir}/gtk-3.0/modules/libcaribou-gtk-module.so

%files -n libcaribou0
%{_libdir}/libcaribou.so.*

%files common
%{_datadir}/caribou/
%{_datadir}/glib-2.0/schemas/org.gnome.caribou.gschema.xml

%files -n typelib-1_0-Caribou-1_0
%{_libdir}/girepository-1.0/Caribou-1.0.typelib

%files devel
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/caribou-1.0.*
%{_includedir}/libcaribou/
%{_libdir}/libcaribou.so
%{_libdir}/pkgconfig/caribou-1.0.pc

%files lang -f %{name}.lang

%changelog
