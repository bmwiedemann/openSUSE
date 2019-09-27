#
# spec file for package mate-panel
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


%define soname  libmate-panel-applet-4
%define sover   1
%define typelib typelib-1_0-MatePanelApplet-4_0
%define _version 1.23
Name:           mate-panel
Version:        1.23.0
Release:        0
Summary:        MATE Desktop Panel
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Source1:        %{name}-branding.gschema.override.in
Source2:        baselibs.conf
# PATCH-FIX-OPENSUSE mate-panel-layouts-suse.patch sor.alexei@meowr.ru -- Correct missing elements.
Patch0:         mate-panel-layouts-suse.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(NetworkManager)
BuildRequires:  pkgconfig(dconf) >= 0.13.4
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libmate-menu)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}
BuildRequires:  pkgconfig(mateweather) >= %{_version}
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr) >= 1.3
Requires:       %{name}-branding >= %{version}
Requires:       gsettings-backend-dconf
Requires:       gvfs-backends
Recommends:     %{name}-lang
# Remove old packages.
Obsoletes:      mate-panel-matecomponent-support

%description
This package contains the MATE Desktop Panel. The panel is an
interface to manage the desktop, launch applications, and organise
access to data.

%package branding-upstream
Summary:        Upstream default layout for the MATE desktop panel
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: Provides /usr/share/mate-panel/panel-default-layout.layout
#BRAND: which contains the default layout.
#BRAND: Branding package should require packages with applets in
#BRAND: the default layout.
%glib2_gsettings_schema_requires

%description branding-upstream
This package contains the MATE Desktop Panel. The panel is an
interface to manage the desktop, launch applications, and organise
access to data.

This package contains the upstream default layout for MATE Panel.

%package -n %{soname}-%{sover}
Summary:        MATE Panel Applet Library -- matecomponent-based library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{soname}-%{sover}
This package contains the MATE Desktop Panel. The panel is an
interface to manage the desktop, launch applications, and organise
access to data.

%package -n %{typelib}
Summary:        Introspection bindings for the MATE panel applet library
License:        GPL-2.0-or-later
Group:          System/GUI/Other

%description -n %{typelib}
This package contains the MATE Desktop Panel. The panel is an
interface to manage the desktop, launch applications, and organise
access to data.

%package devel
Summary:        Development files for the MATE panel applet library
License:        GPL-2.0-or-later
Group:          Development/Libraries/Other
Requires:       %{soname}-%{sover} = %{version}
Requires:       %{typelib} = %{version}

%description devel
This package contains the MATE Desktop Panel. The panel is an
interface to manage the desktop, launch applications, and organise
access to data.

%lang_package

%prep
%autosetup -p1

cp -a %{SOURCE1} zz-mate-panel-upream-branding.gschema.override

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --libexecdir=%{_libexecdir}/%{name} \
  --disable-static                    \
  --enable-introspection              \
  --disable-scrollkeeper
make %{?_smp_mflags} V=1

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/mate/
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{_datadir}/mate/
%fdupes %{buildroot}%{_datadir}/mate-panel/
%fdupes %{buildroot}%{_includedir}/
%suse_update_desktop_file %{name}

# And install schema override file to get it applied.
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas/
install -pm 0644 zz-mate-panel-upream-branding.gschema.override \
  %{buildroot}%{_datadir}/glib-2.0/schemas/

%post -n %{soname}-%{sover} -p /sbin/ldconfig

%postun -n %{soname}-%{sover} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun

%post branding-upstream
%glib2_gsettings_schema_post

%postun branding-upstream
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc ChangeLog README
%{_mandir}/man?/mate-panel.?%{?ext_man}
%{_mandir}/man?/mate-panel-test-applets.?%{?ext_man}
%{_mandir}/man?/mate-desktop-item-edit.?%{?ext_man}
%{_bindir}/mate-desktop-item-edit
%{_bindir}/mate-panel
%{_bindir}/mate-panel-test-applets
%{_libexecdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/help/C/
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/%{name}/
# Files from branding-upstream.
%exclude %{_datadir}/glib-2.0/schemas/zz-mate-panel-upream-branding.gschema.override

%files branding-upstream
%{_datadir}/glib-2.0/schemas/zz-mate-panel-upream-branding.gschema.override

%files -n %{soname}-%{sover}
%dir %{_datadir}/mate
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{typelib}
%{_libdir}/girepository-1.0/MatePanelApplet-4.0.typelib

%files devel
%{_includedir}/mate-panel-4.0/
%{_libdir}/pkgconfig/libmatepanelapplet-4.0.pc
%{_libdir}/%{soname}.so
%{_datadir}/gir-1.0/MatePanelApplet-4.0.gir
%{_datadir}/gtk-doc/html/%{name}-applet/

%files lang -f %{name}.lang
%{_datadir}/help/
%exclude %{_datadir}/help/C/

%changelog
