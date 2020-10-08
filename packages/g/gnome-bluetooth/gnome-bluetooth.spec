#
# spec file for package gnome-bluetooth
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


%define _udevdir %(pkg-config --variable udevdir udev)
Name:           gnome-bluetooth
Version:        3.34.3
Release:        0
Summary:        GNOME Bluetooth graphical utilities
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GnomeBluetooth
Source0:        https://download.gnome.org/sources/gnome-bluetooth/3.34/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.12.0
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
BuildRequires:  pkgconfig(libudev)
# Require bluez (mandatory, as per readme, bnc#622946)
Requires:       bluez >= 5

%description
A set of graphical utilities to setup, monitor and use Bluetooth devices.

This package provides the utilities, data files and manuals for GNOME Bluetooth.

%package -n libgnome-bluetooth13
Summary:        GNOME Bluetooth's Shared Libraries
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libgnome-bluetooth13
A set of graphical utilities to setup, monitor and use Bluetooth devices.

This package provides the GNOME Bluetooth's shared library.

%package -n typelib-1_0-GnomeBluetooth-1_0
Summary:        Introspection bindings for the GNOME Bluetooth libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n typelib-1_0-GnomeBluetooth-1_0
A set of graphical utilities to setup, monitor and use Bluetooth devices.

This package provides the GObject Introspection bindings for the GNOME Bluetooth's
libraries.

%package devel
Summary:        Development files for the GNOME Bluetooth libraries
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Requires:       %{name} = %{version}
Requires:       typelib-1_0-GnomeBluetooth-1_0 = %{version}

%description devel
A set of graphical utilities to setup, monitor and use Bluetooth devices.

This package provides the necessary files for development with GNOME Bluetooth.

%lang_package

%prep
%autosetup -p1
translation-update-upstream po gnome-bluetooth2

%build
%meson \
	-D gtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name}2 %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%post -n libgnome-bluetooth13 -p /sbin/ldconfig
%postun -n libgnome-bluetooth13 -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/bluetooth-*
%{_datadir}/applications/bluetooth-sendto.desktop
%{_datadir}/gnome-bluetooth/
%{_datadir}/icons/hicolor/*/*/*bluetooth*
%{_mandir}/man1/bluetooth-*

%files -n libgnome-bluetooth13
%license COPYING.LIB
%{_libdir}/libgnome-bluetooth.so.*

%files -n typelib-1_0-GnomeBluetooth-1_0
%{_libdir}/girepository-1.0/GnomeBluetooth-1.0.typelib

%files devel
%doc AUTHORS ChangeLog.README MAINTAINERS
%doc %{_datadir}/gtk-doc/html/gnome-bluetooth
%{_includedir}/gnome-bluetooth
%{_libdir}/libgnome-bluetooth.so
%{_libdir}/pkgconfig/gnome-bluetooth-1.0.pc
%{_datadir}/gir-1.0/*.gir

%files lang -f %{name}2.lang

%changelog
