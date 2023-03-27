#
# spec file for package mate-desktop
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


%define soname  libmate-desktop-2
%define sover   17
%define typelib typelib-1_0-MateDesktop-2_0
%define _version 1.26
Name:           mate-desktop
Version:        1.26.1
Release:        0
Summary:        Library with common API for various MATE modules
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Source1:        user-dirs-update-mate.desktop
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  rsvg-convert
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dconf) >= 0.13.4
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.7
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xrandr) >= 1.3
Requires:       xdg-user-dirs
Recommends:     mate-user-guide

%description
This package contains the library with common API for various
MATE modules.

%lang_package

%package -n %{soname}-%{sover}
Summary:        Library with common API for various MATE modules
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Requires:       %{name}-gschemas >= %{version}

%description -n %{soname}-%{sover}
This package contains the library with common API for various
MATE modules.


# Separate shared schemas to make MATE desktop applications usable standalone.

%package -n %{typelib}
Summary:        Common API for various MATE modules typelib
License:        GPL-2.0-or-later

%description -n %{typelib}
This package contains the library with common API for various
MATE modules.

%package gschemas
Summary:        MATE Desktop GSchemas
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Requires:       %{name}-gschemas-branding >= %{_version}
# mate-desktop-gsettings-schemas was last used in openSUSE Leap 42.1.
Obsoletes:      %{name}-gsettings-schemas < %{version}
Provides:       %{name}-gsettings-schemas = %{version}
%glib2_gsettings_schema_requires

%description gschemas
This package provides the GSettings schemas for
MATE Desktop Environment.

%package gschemas-branding-upstream
Summary:        MATE Desktop GSchemas -- Upstream default settings
License:        GPL-2.0-or-later
Requires:       %{name}-gschemas = %{version}
Supplements:    (%{name}-gschemas and branding-upstream)
Conflicts:      %{name}-gschemas-branding
Provides:       %{name}-gschemas-branding = %{version}
BuildArch:      noarch
%glib2_gsettings_schema_requires

%description gschemas-branding-upstream
This package contains the upstream default settings for
MATE Desktop GSchemas.

%package devel
Summary:        MATE module API library development files
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
Group:          Development/Libraries/X11
Requires:       %{soname}-%{sover} = %{version}

%description devel
This package contains the library with common API for various MATE modules.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

install -Dpm 0644 %{SOURCE1} \
  %{buildroot}%{_sysconfdir}/xdg/autostart/user-dirs-update-mate.desktop
%suse_update_desktop_file mate-about
%suse_update_desktop_file mate-color-select

%post -n %{soname}-%{sover} -p /sbin/ldconfig

%postun -n %{soname}-%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS
%dir %{_datadir}/mate-about
%{_sysconfdir}/xdg/autostart/user-dirs-update-mate.desktop
%{_bindir}/mate-about
%{_bindir}/mate-color-select
%{_datadir}/applications/mate-about.desktop
%{_datadir}/applications/mate-color-select.desktop
%{_datadir}/lib%{name}/
%{_datadir}/mate-about/mate-version.xml
%{_datadir}/icons/hicolor/*/apps/mate*
%{_mandir}/man?/*.?%{?ext_man}

%files lang -f %{name}.lang

%files -n %{soname}-%{sover}
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{typelib}
%{_libdir}/girepository-1.0/MateDesktop-2.0.typelib

%files gschemas
%{_datadir}/glib-2.0/schemas/*.xml

%files gschemas-branding-upstream

%files devel
%{_datadir}/gtk-doc/html/%{name}/
%{_includedir}/%{name}-2.0/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}-2.0.pc
%{_datadir}/gir-1.0/MateDesktop-2.0.gir

%changelog
