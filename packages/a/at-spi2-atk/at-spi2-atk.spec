#
# spec file for package at-spi2-atk
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


Name:           at-spi2-atk
Version:        2.34.1
Release:        0
Summary:        GTK+ module for the Assistive Technology Service Provider Interface
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://gitlab.gnome.org/GNOME/at-spi2-atk
Source0:        https://download.gnome.org/sources/at-spi2-atk/2.34/%{name}-%{version}.tar.xz
Source98:       baselibs.conf
Source99:       %{name}-rpmlintrc

BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atk) >= 2.33.3
BuildRequires:  pkgconfig(atspi-2) >= 2.33.2
BuildRequires:  pkgconfig(dbus-1) >= 1.5
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.0.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.0.0
BuildRequires:  pkgconfig(libxml-2.0)

%description
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

%package common
Summary:        Comon files for the AT-SPI GTK+ module
# The GTK+ module is useful only if the at-spi registry is running. But it's
# not a strict runtime dependency.
Group:          System/Libraries
Recommends:     at-spi2-core
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
# The library that was shipped with at-spi2-atk was removed.
Obsoletes:      libcspi-devel <= 0.1.1
Obsoletes:      libcspi0 <= 0.1.1
# With version 2.5.91, the gtk3 module was dropped.
Obsoletes:      %{name}-gtk3 < 2.5.91
# With versiom 2.5.92, the lang pack was dropped.
Obsoletes:      %{name}-lang < 2.5.92

%description common
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

This package contains files common to the GTK+ 2 and GTK+ 3 modules
for at-spi.

%package gtk2
Summary:        GTK+2 module for the Assistive Technology Service Provider Interface
Group:          System/Libraries
Requires:       %{name}-common = %{version}
# We want to have this package installed if the user has gtk2 and the at-spi
# stack already installed
Supplements:    packageand(at-spi2-core:gtk2)

%description gtk2
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

This package contains the GTK+ 2 module for at-spi, based on ATK.

%package -n libatk-bridge-2_0-0
Summary:        ATK/D-Bus bridging library
Group:          System/Libraries
Requires:       at-spi2-core

%description -n libatk-bridge-2_0-0
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

The package contains a ATK/D-Bus bridge library.

%package devel
Summary:        Development files for the Assistive Technology Service Provider Interface
Group:          Development/Languages/C and C++
Requires:       libatk-bridge-2_0-0 = %{version}

%description devel
AT-SPI is a general interface for applications to make use of the
accessibility toolkit. This version is based on dbus.

%prep
%autosetup

%build
%meson \
	-Ddisable_p2p=false \
	%{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libatk-bridge-2_0-0 -p /sbin/ldconfig
%postun -n libatk-bridge-2_0-0 -p /sbin/ldconfig

%files common
%dir %{_libdir}/gnome-settings-daemon-3.0
%dir %{_libdir}/gnome-settings-daemon-3.0/gtk-modules
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop

%files gtk2
%license COPYING

%dir %{_libdir}/gtk-2.0
%dir %{_libdir}/gtk-2.0/modules
%{_libdir}/gtk-2.0/modules/libatk-bridge.so

%files -n libatk-bridge-2_0-0
%{_libdir}/libatk-bridge-2.0.so.*

%files devel
%doc AUTHORS README
%{_includedir}/at-spi2-atk/
%{_libdir}/libatk-bridge-2.0.so
%{_libdir}/pkgconfig/atk-bridge-2.0.pc

%changelog
