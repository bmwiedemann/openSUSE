#
# spec file for package retro-gtk
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


# Use of library versioning and name versioning macros to facilitate updatings
%define namever 0_14-0
%define libver  0.14
Name:           retro-gtk
Version:        0.16.1
Release:        0
Summary:        Toolkit to write Gtk+3-based frontends to libretro
License:        GPL-3.0-only
Group:          System/GUI/GNOME
URL:            https://git.gnome.org/browse/retro-gtk
Source0:        https://download.gnome.org/sources/retro-gtk/0.16/%{name}-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel >= 0.6.7
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(vapigen)

%description
retro-gtk wraps the libretro API for use in Gtk applications such as
GNOME Games.

%package -n libretro-gtk-%{namever}
Summary:        Toolkit to write Gtk+3-based frontends to libretro
Group:          System/Libraries

%description -n libretro-gtk-%{namever}
retro-gtk wraps the libretro API for use in Gtk applications such as
GNOME Games.
(libretro is an API specification implemented by some emulator
libraries like libretro-bsnes.)

%package -n typelib-1_0-Retro-%{namever}
Summary:        GObject introspection bindings for libretro-gtk
Group:          System/Libraries

%description -n typelib-1_0-Retro-%{namever}
retro-gtk wraps the libretro API for use in Gtk applications.
This subpackage contains the gobject bindings for the
libretro-gtk shared library.

%package devel
Summary:        Development files for retro-gtk, a Gtk+3 wrapper for libretro
Group:          Development/Languages/C and C++
Requires:       libretro-gtk-%{namever} = %{version}
Requires:       typelib-1_0-Retro-%{namever} = %{version}

%description devel
retro-gtk wraps the libretro API for use in Gtk applications.
This subpackage contains the headers to make use of the libretro-gtk
library.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
# make install copies AUTHORS, COPYING et.al to doc/%%{name}
# we capture them using the %%doc macro
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%post   -n libretro-gtk-%{namever} -p /sbin/ldconfig
%postun -n libretro-gtk-%{namever} -p /sbin/ldconfig

%files -n libretro-gtk-%{namever}
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/libretro-gtk-%{libver}.so.0

%files -n typelib-1_0-Retro-%{namever}
%{_libdir}/girepository-1.0/Retro-%{libver}.typelib

%files devel
%{_bindir}/retro-demo
%{_datadir}/gir-1.0/Retro-%{libver}.gir
%{_datadir}/vala/vapi/retro-gtk-%{libver}.deps
%{_datadir}/vala/vapi/retro-gtk-%{libver}.vapi
%{_libdir}/pkgconfig/retro-gtk-%{libver}.pc
%{_includedir}/retro-gtk/
%{_libdir}/libretro-gtk-%{libver}.so

%changelog
