#
# spec file for package brisk-menu
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


Name:           brisk-menu
Version:        0.5.0
Release:        0
Summary:        Modern, efficient menu for MATE
License:        GPL-2.0-or-later AND CC-BY-SA-4.0
Group:          System/GUI/Other
Url:            https://github.com/solus-project/brisk-menu
Source:         https://github.com/solus-project/brisk-menu/releases/download/v%{version}/%{name}-v%{version}.tar.xz
Source1:        https://github.com/solus-project/brisk-menu/releases/download/v%{version}/%{name}-v%{version}.tar.xz.asc
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM brisk-menu-mate-menus-1.22.patch -- https://github.com/solus-project/brisk-menu/pull/103
Patch0:         brisk-menu-mate-menus-1.22.patch
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libmate-menu) >= 1.21
BuildRequires:  pkgconfig(libmatepanelapplet-4.0) >= 1.21
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(x11)
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires

%description
Modern, efficient menu for the MATE Desktop Environment.

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1

%lang_package

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files
%license LICENSE*
%{_libexecdir}/brisk-menu
%dir %{_datadir}/mate-panel/
%dir %{_datadir}/mate-panel/applets/
%{_datadir}/mate-panel/applets/*brisk*.mate-panel-applet
%{_datadir}/icons/hicolor/scalable/actions/brisk*.*
%{_datadir}/glib-2.0/schemas/*%{name}.gschema.xml
%{_datadir}/dbus-1/services/org.mate.panel.applet.BriskMenuFactory.service

%files lang -f %{name}.lang

%changelog
