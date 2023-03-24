#
# spec file for package gnome-shell-extensions
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2011 Dominique Leuenberger, Amsterdam, The Netherlands
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


%global __requires_exclude typelib\\(Meta\\)
Name:           gnome-shell-extensions
Version:        44.0
Release:        0
Summary:        A collection of extensions for GNOME Shell
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GnomeShell/Extensions
Source0:        https://download.gnome.org/sources/gnome-shell-extensions/44/%{name}-%{version}.tar.xz
Source1:        README.SUSE

# PATCH-FEATURE-OPENSUSE gnome-shell-add-app-to-desktop.patch bnc#870580 dliang@suse.com --  allow adding app shortcut to desktop easily.
Patch1:         gnome-shell-add-app-to-desktop.patch

## NOTE keep SLE Classic patch at the bottom
BuildRequires:  fdupes
# Needed for directory ownership
BuildRequires:  gnome-shell
# gobject-introspection is needed for the typelib() rpm magic.
BuildRequires:  gobject-introspection
BuildRequires:  meson >= 0.53.0
BuildRequires:  sassc

%description
GNOME Shell Extensions is a collection of extensions providing
additional and optional functionality to GNOME Shell.

%package common
Summary:        Common files for GNOME Shell extensions
Group:          System/GUI/GNOME
Requires:       gnome-shell
# Obsoletes for metapackage and extensions from gnome-shell-extensions that we used to package
Obsoletes:      gnome-shell-extension-alternate-tab < %{version}
Obsoletes:      gnome-shell-extension-apps-menu < %{version}
Obsoletes:      gnome-shell-extension-auto-move-windows < %{version}
Obsoletes:      gnome-shell-extension-dock < %{version}
Obsoletes:      gnome-shell-extension-drive-menu < %{version}
Obsoletes:      gnome-shell-extension-gajim < %{version}
Obsoletes:      gnome-shell-extension-native-window-placement < %{version}
Obsoletes:      gnome-shell-extension-places-menu < %{version}
Obsoletes:      gnome-shell-extension-systemMonitor < %{version}
Obsoletes:      gnome-shell-extension-windows-navigator < %{version}
Obsoletes:      gnome-shell-extension-workspace-indicator < %{version}
Obsoletes:      gnome-shell-extension-xrandr-indicator < %{version}
Obsoletes:      gnome-shell-extensions < %{version}
BuildArch:      noarch

%description common
This package provides files common to several GNOME Shell Extensions

%package -n gnome-shell-classic
Summary:        A collection of extensions for Gnome-shell classic
Group:          System/GUI/GNOME
Requires:       gnome-shell-extension-desktop-icons
Requires:       gnome-shell-extensions-common
Obsoletes:      gnome-shell-classic-session < %{versoin}
BuildArch:      noarch

%description -n gnome-shell-classic
This GNOME Shell extension adds a power off item in the status
menu, and provides the ability to hibernate.

This package provides the extensions required to switch to
gnome-shell classic.

%package -n gnome-shell-extension-user-theme
Summary:        Allow the user to change GNOME Shell Themes
Group:          System/GUI/GNOME
BuildArch:      noarch

%description -n gnome-shell-extension-user-theme
This extension allows the user to switch to different themes. It's possible
to pick system installed themes or even themes installed in the user's home.

%lang_package -n %{name}-common

%prep
%setup -q
%patch1 -p1

# In openSUSE GNOME, we don't launch gnome-session directly, but wrap this through a shell script, /usr/bin/gnome
sed -i "s:Exec=gnome-session:Exec=gnome:g" data/gnome-classic.desktop.in
cp %{SOURCE1} .
%if 0%{?sle_version}
sed -i -e 's/openSUSE/SUSE Linux Enterprise/g' README.SUSE
%endif

%build
%meson \
    -D classic_mode=true \
    -D extension_set=classic \
    -D enable_extensions="apps-menu,places-menu,launch-new-instance,window-list,workspace-indicator,user-theme"
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%if 0%{?sle_version}
# Prepare for 'default.desktop' being update-alternative handled, boo#1039756
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop
touch %{buildroot}%{_sysconfdir}/alternatives/default-waylandsession.desktop
install -d -m755 %{buildroot}%{_datadir}/wayland-sessions
ln -s %{_sysconfdir}/alternatives/default-waylandsession.desktop %{buildroot}%{_datadir}/wayland-sessions/default.desktop
%endif

%files common
%license COPYING
%doc README.SUSE HACKING.md NEWS README.md

%files -n gnome-shell-classic
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.extensions.classic.gschema.override
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.apps-menu.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml
%dir %{_datadir}/gnome-shell/extensions
%{_datadir}/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/modes/classic.json
%dir %{_datadir}/gnome-shell/theme/
%{_datadir}/gnome-shell/theme/classic-process-working.svg
%{_datadir}/gnome-shell/theme/gnome-classic-high-contrast.css
%{_datadir}/gnome-shell/theme/gnome-classic.css
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/gnome-classic-wayland.desktop
%{_datadir}/wayland-sessions/gnome-classic.desktop
%{_datadir}/xsessions/gnome-classic-xorg.desktop
%{_datadir}/xsessions/gnome-classic.desktop
%if 0%{?sle_version}
%dir %{_datadir}/wayland-sessions
%{_datadir}/xsessions/default.desktop
%{_datadir}/wayland-sessions/default.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %{_sysconfdir}/alternatives/default-waylandsession.desktop
%endif

%files -n gnome-shell-extension-user-theme
%license COPYING
%{_datadir}/gnome-shell/extensions/user-theme@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml

%files common-lang -f %{name}.lang

%changelog
