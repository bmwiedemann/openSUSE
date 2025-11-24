#
# spec file for package mate-menus
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define soname   libmate-menu
%define sover    2
%define typelib  typelib-1_0-MateMenu-2_0
%define _version 1.28

Name:           mate-menus
Version:        1.28.0
Release:        0
Summary:        MATE Desktop Menu
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  intltool
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
Requires:       %{name}-branding
Recommends:     %{name}-lang
Obsoletes:      python-%{name} < %{version}
Obsoletes:      python2-%{name} < %{version}

%description
mate-menus contains the libmate-menu library, the layout
configuration files for the MATE menu, as well as a simple menu
editor.

The libmate-menu library implements the "Desktop Menu Specification"
from freedesktop.org.

%package branding-upstream
Summary:        Upstream menus definition for the MATE desktop menu
License:        GPL-2.0-or-later
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: This package contains set of needed .menu files in
#BRAND: /etc/xdg/menus. .directory files in
#BRAND: %%{_datadir}/desktop-directories/Multimedia.directory are part of
#BRAND: the main package. If you need custom one, simply it put there
#BRAND: and modify .menu file to refer to it.

%description branding-upstream
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:

https://freedesktop.org/Standards/menu-spec

This package provides the upstream definitions for menus.

%package -n %{soname}%{sover}
Summary:        MATE Desktop Menu
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{soname}%{sover}
The libmate-menu library implements the "Desktop Menu Specification"
from freedesktop.org.

%package -n %{typelib}
Summary:        Introspection bindings for the MATE Desktop Menu
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{typelib}
The libmate-menu library implements the "Desktop Menu Specification"
from freedesktop.org.

%package devel
Summary:        Header files for the MATE Desktop Menu
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Development/Libraries/X11
Requires:       %{soname}%{sover} = %{version}
Requires:       %{typelib} = %{version}
Requires:       pkgconfig(glib-2.0)
Obsoletes:      python2-%{name} < %{version}

%description devel
mate-menus contains the libmate-menu library, the layout configuration
files for the MATE menu, as well as a simple menu editor.

The libmate-menu library implements the "Desktop Menu Specification"
from freedesktop.org.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static \
  --disable-collection
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog README
%dir %{_sysconfdir}/xdg/menus/
# Files from branding-upstream.
%exclude %{_sysconfdir}/xdg/menus/mate-applications.menu
%exclude %{_sysconfdir}/xdg/menus/mate-preferences-categories.menu
%exclude %{_sysconfdir}/xdg/menus/mate-settings.menu
%dir %{_datadir}/mate/desktop-directories/
%{_datadir}/mate/desktop-directories/mate-*.directory
%dir %{_datadir}/mate/

%files branding-upstream
%config %{_sysconfdir}/xdg/menus/mate-applications.menu
%config %{_sysconfdir}/xdg/menus/mate-preferences-categories.menu
%config %{_sysconfdir}/xdg/menus/mate-settings.menu

%files -n %{typelib}
%{_libdir}/girepository-1.0/MateMenu-2.0.typelib

%files -n %{soname}%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files devel
%{_includedir}/mate-menus/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/MateMenu-2.0.gir
%dir %{_datadir}/mate-menus/
%{_datadir}/mate-menus/examples/

%files lang -f %{name}.lang

%changelog
