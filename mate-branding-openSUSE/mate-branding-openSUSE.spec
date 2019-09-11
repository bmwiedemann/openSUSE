#
# spec file for package mate-branding-openSUSE
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define mate_control_center_version %(rpm -q --queryformat '%%{VERSION}' mate-control-center)
%define mate_desktop_gschemas_version %(rpm -q --queryformat '%%{VERSION}' mate-desktop-gschemas)
%define mate_menus_version %(rpm -q --queryformat '%%{VERSION}' mate-menus)
%define mate_panel_version %(rpm -q --queryformat '%%{VERSION}' mate-panel)
%define mate_session_manager_version %(rpm -q --queryformat '%%{VERSION}' mate-session-manager)
Name:           mate-branding-openSUSE
Version:        42.1
Release:        0
Summary:        openSUSE Branding of the MATE Desktop Environment
License:        MIT
Group:          System/GUI/Other
Url:            http://mate-desktop.org/
Source1:        mate-session-branding-openSUSE-mate_defaults.conf
Source2:        mate-session-branding.gschema.override.in
Source3:        mate-panel-branding.gschema.override.in
Source4:        mate-desktop-branding.gschema.override.in
# Exactly the same as Xfce branding icons.
Source5:        openSUSE-MATE-icons.tar.xz
# PATCH-FIX-OPENSUSE mate-control-center-branding-add-YaST.patch
Patch0:         mate-control-center-branding-add-YaST.patch
# PATCH-FIX-OPENSUSE mate-menus-branding-remove-X-SuSE-ControlCenter.patch vuntz@opensuse.org -- Remove the desktop files with X-SuSE-YaST category from the Applications menu and explicitly add YaST launcher.
Patch1:         mate-menus-branding-remove-X-SuSE-ControlCenter.patch
BuildRequires:  fdupes
BuildRequires:  mate-control-center-branding-upstream
BuildRequires:  mate-desktop-gschemas-branding-upstream
BuildRequires:  mate-menus-branding-upstream
BuildRequires:  mate-panel-branding-upstream
BuildRequires:  mate-session-manager-branding-upstream
BuildRequires:  wallpaper-branding-openSUSE
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

%description
This package provides the openSUSE look and feel for the MATE desktop environment.

%package -n mate-control-center-branding-openSUSE
Summary:        openSUSE Branding of mate-control-center
License:        GPL-2.0+
Group:          System/GUI/Other
Requires:       mate-control-center = %{mate_control_center_version}
Supplements:    packageand(mate-control-center:branding-openSUSE)
Conflicts:      otherproviders(mate-control-center-branding)
Provides:       mate-control-center-branding = %{mate_control_center_version}

%description -n mate-control-center-branding-openSUSE
This package provides the openSUSE definition of what appears in the
control centre.

%package -n mate-desktop-gschemas-branding-openSUSE
Summary:        openSUSE Branding of mate-desktop
License:        GPL-2.0+
Group:          System/GUI/Other
Requires:       adwaita-icon-theme
Requires:       mate-desktop-gschemas = %{mate_desktop_gschemas_version}
Supplements:    packageand(mate-desktop-gschemas:branding-openSUSE)
Conflicts:      otherproviders(mate-desktop-gschemas-branding)
Provides:       mate-desktop-gschemas-branding = %{mate_desktop_gschemas_version}

%description -n mate-desktop-gschemas-branding-openSUSE
This package provides the openSUSE definition for MATE Desktop GSchemas.

%package -n mate-panel-branding-openSUSE
Summary:        openSUSE Branding of mate-panel
License:        GPL-2.0+
Group:          System/GUI/Other
Requires:       mate-applet-softupd
Requires:       mate-applets
Requires:       mate-menu
Requires:       mate-panel = %{mate_panel_version}
Supplements:    packageand(mate-panel:branding-openSUSE)
Conflicts:      otherproviders(mate-panel-branding)
Provides:       mate-panel-branding = %{mate_panel_version}
%glib2_gsettings_schema_requires

%description -n mate-panel-branding-openSUSE
This package provides the openSUSE look and feel for the MATE Panel.

%package -n mate-menus-branding-openSUSE
Summary:        openSUSE Branding of mate-menus
License:        GPL-2.0+
Group:          System/GUI/Other
Requires:       mate-menus = %{mate_menus_version}
Supplements:    packageand(mate-menus:branding-openSUSE)
Conflicts:      otherproviders(mate-menus-branding)
Provides:       mate-menus-branding = %{mate_menus_version}

%description -n mate-menus-branding-openSUSE
This package provides the openSUSE definitions for menus.

%package -n mate-session-manager-branding-openSUSE
Summary:        openSUSE Branding of mate-session-manager
License:        GPL-2.0+
Group:          System/GUI/Other
Requires:       mate-icon-theme
Requires:       mate-session-manager = %{mate_session_manager_version}
Requires:       metatheme-numix-common
Requires:       wallpaper-branding-openSUSE
Recommends:     mate-themes
Supplements:    packageand(mate-session-manager:branding-openSUSE)
Conflicts:      otherproviders(mate-session-manager-branding)
Provides:       mate-session-manager-branding = %{mate_session_manager_version}
%glib2_gsettings_schema_requires

%description -n mate-session-manager-branding-openSUSE
This package provides the openSUSE look and feel for the MATE Session Manager.

%prep
# MATE Control Center branding part.
# We will base the shell content on upstream content:
cp -a %{_sysconfdir}/xdg/menus/*.menu .
%patch0 -p1
# MATE Menus branding part.
%patch1 -p1
# MATE Session Manager branding part.
cp -a %{SOURCE1} mate_defaults.conf
cp -a %{SOURCE2} mate-session-branding.gschema.override.in
# MATE Panel branding part.
cp -a %{SOURCE3} zz-mate-panel-openSUSE-branding.gschema.override
# MATE Desktop GSchemas branding part.
cp -a %{SOURCE4} zz-mate-desktop-openSUSE-branding.gschema.override
tar -xvf %{SOURCE5}

%build
# MATE session manager branding part.
[ -f %{_datadir}/wallpapers/openSUSE-default.xml ]
sed -e 's|@@WALLPAPER_URI@@|%{_datadir}/wallpapers/openSUSE-default.xml|' mate-session-branding.gschema.override.in > mate-session-branding.gschema.override
# For sound theme.
cat mate-session-branding.gschema.override | sed -e 's|@@IF_openSUSE@@||g;/^@@IF_/d' > zz-mate-session-openSUSE-branding.gschema.override

%install
# MATE Control Centre branding part.
mkdir -p %{buildroot}%{_sysconfdir}/xdg/menus/
install -m 0644 *.menu %{buildroot}%{_sysconfdir}/xdg/menus/
# MATE Desktop GSchemas branding part.
install -Dm 0644 zz-mate-desktop-openSUSE-branding.gschema.override \
  %{buildroot}%{_datadir}/glib-2.0/schemas/zz-mate-desktop-openSUSE-branding.gschema.override
# MATE Panel branding part.
install -Dm 0644 zz-mate-panel-openSUSE-branding.gschema.override \
  %{buildroot}%{_datadir}/glib-2.0/schemas/zz-mate-panel-openSUSE-branding.gschema.override
mkdir -p %{buildroot}%{_datadir}/pixmaps/
install -m 0644 mate-*.png %{buildroot}%{_datadir}/pixmaps/
# MATE Session Manager branding part.
install -Dm 0644 mate_defaults.conf %{buildroot}%{_sysconfdir}/mate_defaults.conf
install -Dm 0644 zz-mate-session-openSUSE-branding.gschema.override \
  %{buildroot}%{_datadir}/glib-2.0/schemas/zz-mate-session-openSUSE-branding.gschema.override
# Remove unwanted menu file.
rm -f %{buildroot}%{_sysconfdir}/xdg/menus/mate-{settings,preferences-categories}.menu

%post -n mate-desktop-gschemas-branding-openSUSE
%glib2_gsettings_schema_post

%postun -n mate-desktop-gschemas-branding-openSUSE
%glib2_gsettings_schema_postun

%post -n mate-panel-branding-openSUSE
%glib2_gsettings_schema_post

%postun -n mate-panel-branding-openSUSE
%glib2_gsettings_schema_postun

%post -n mate-session-manager-branding-openSUSE
%glib2_gsettings_schema_post

%postun -n mate-session-manager-branding-openSUSE
%glib2_gsettings_schema_postun

%files -n mate-desktop-gschemas-branding-openSUSE
%defattr(-,root,root)
%{_datadir}/glib-2.0/schemas/zz-mate-desktop-openSUSE-branding.gschema.override

%files -n mate-control-center-branding-openSUSE
%defattr (-,root,root)
%config %{_sysconfdir}/xdg/menus/matecc.menu

%files -n mate-menus-branding-openSUSE
%defattr(-,root,root)
%config %{_sysconfdir}/xdg/menus/mate-applications.menu

%files -n mate-panel-branding-openSUSE
%defattr(-,root,root)
%{_datadir}/glib-2.0/schemas/zz-mate-panel-openSUSE-branding.gschema.override
%{_datadir}/pixmaps/mate-*.png

%files -n mate-session-manager-branding-openSUSE
%defattr(-,root,root)
%config (noreplace) %{_sysconfdir}/mate_defaults.conf
%{_datadir}/glib-2.0/schemas/zz-mate-session-openSUSE-branding.gschema.override

%changelog
