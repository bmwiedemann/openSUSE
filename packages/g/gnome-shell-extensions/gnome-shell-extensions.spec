#
# spec file for package gnome-shell-extensions
#
# Copyright (c) 2019 SUSE LLC
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
Version:        3.34.1
Release:        0
Summary:        A collection of extensions for GNOME Shell
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Projects/GnomeShell/Extensions
Source0:        https://download.gnome.org/sources/gnome-shell-extensions/3.34/%{name}-%{version}.tar.xz
Source1:        README.SUSE
Source2:        sle-classic.desktop
Source3:        SLE-theme.tar.gz
Source5:        sle-classic.json
Source6:        sle-classic@suse.com.tar.gz
Source7:        00_org.gnome.shell.extensions.sle-classic.gschema.override
# PATCH-FEATURE-OPENSUSE gnome-shell-add-app-to-desktop.patch bnc#870580 dliang@suse.com --  allow adding app shortcut to desktop easily.
Patch1:         gnome-shell-add-app-to-desktop.patch
# PATCH-FIX-OPENSUSE gnome-classic-s390-not-require-g-s-d_wacom.patch bsc#1129412 yfjiang@suse.com -- Remove the runtime requirement of g-s-d Wacom plugin
Patch2:         gnome-classic-s390-not-require-g-s-d_wacom.patch

## NOTE keep SLE Classic patch at the bottom
# PATCH-FIX-SLE gse-sle-classic-ext.patch Fate#318572 cxiong@suse.com -- add sle classic support
Patch1000:      gse-sle-classic-ext.patch
# PATCH-FEATURE-SLE sle-classic-lock-screen-background.patch bsc#1007468 xwang@suse.com -- add SUSE logo on lock screen when auth is requested
Patch1001:      sle-classic-lock-screen-background.patch
BuildRequires:  fdupes
BuildRequires:  gnome-patch-translation
# Needed for directory ownership
BuildRequires:  gnome-shell
# gobject-introspection is needed for the typelib() rpm magic.
BuildRequires:  gobject-introspection
BuildRequires:  meson >= 0.44.0
BuildRequires:  sassc
BuildRequires:  translation-update-upstream

%description
GNOME Shell Extensions is a collection of extensions providing
additional and optional functionality to GNOME Shell.

%package common
Summary:        Common files for GNOME Shell extensions
Group:          System/GUI/GNOME
Requires:       gnome-shell
Recommends:     %{name}-common-lang
# Obsoletes for metapackage and extensions from gnome-shell-extensions that we used to package
Obsoletes:      gnome-shell-extension-alternate-tab < %{version}
Obsoletes:      gnome-shell-extension-apps-menu < %{version}
Obsoletes:      gnome-shell-extension-auto-move-windows < %{version}
Obsoletes:      gnome-shell-extension-dock
Obsoletes:      gnome-shell-extension-drive-menu < %{version}
Obsoletes:      gnome-shell-extension-gajim < %{version}
Obsoletes:      gnome-shell-extension-native-window-placement < %{version}
Obsoletes:      gnome-shell-extension-places-menu < %{version}
Obsoletes:      gnome-shell-extension-systemMonitor < %{version}
Obsoletes:      gnome-shell-extension-user-theme < %{version}
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
Requires:       gnome-shell-classic-session
Requires:       gnome-shell-extension-desktop-icons
Recommends:     %{name}-common-lang
BuildArch:      noarch

%description -n gnome-shell-classic
This GNOME Shell extension adds a power off item in the status
menu, and provides the ability to hibernate.

This package provides the extensions required to switch to
gnome-shell classic.

%package -n gnome-shell-classic-session
Summary:        A collection of extensions for Gnome-shell classic
Group:          System/GUI/GNOME

%description -n gnome-shell-classic-session
This packages provides architecture dependent session files to
gnome-shell classic.

%lang_package -n %{name}-common

%prep
%setup -q
%patch1 -p1
%ifarch s390 s390x
%patch2 -p1
%endif
translation-update-upstream po %{name}
gnome-patch-translation-prepare po %{name}

%patch1000 -p1
%if !0%{?is_opensuse}
%patch1001 -p1
%endif
# In openSUSE GNOME, we don't launch gnome-session directly, but wrap this through a shell script, /usr/bin/gnome
sed -i "s:Exec=gnome-session:Exec=gnome:g" data/gnome-classic.desktop.in
cp %{SOURCE1} .
%if !0%{?is_opensuse}
sed -i -e 's/openSUSE/SUSE Linux Enterprise/g' README.SUSE
%endif

%build
%meson \
    -D classic_mode=true \
    -D extension_set=classic \
    -D enable_extensions="apps-menu,places-menu,launch-new-instance,window-list,workspace-indicator, horizontal-workspaces"
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
#Install SLE theme
#Install sle-classic@suse.com extension
install -m0644 %{SOURCE2} %{buildroot}/%{_datadir}/xsessions/sle-classic.desktop
cp %{_builddir}/%{name}-%{version}/extensions/window-list/sle-classic.css \
%{buildroot}/%{_datadir}/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/sle-classic.css
install -m0644 %{SOURCE5} %{buildroot}/%{_datadir}/gnome-shell/modes/sle-classic.json
tar -xzvf %{SOURCE6}
install -d %{buildroot}/%{_datadir}/gnome-shell/extensions/sle-classic@suse.com
cp sle-classic@suse.com/*  %{buildroot}/%{_datadir}/gnome-shell/extensions/sle-classic@suse.com
install -m0644 %{SOURCE7} %{buildroot}/%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.extensions.sle-classic.gschema.override
%if !0%{?is_opensuse}
tar -xzvf %{SOURCE3}
install -d %{buildroot}%{_datadir}/gnome-shell/theme
cp SLE-theme/theme/*  %{buildroot}%{_datadir}/gnome-shell/theme
%endif
%fdupes %{buildroot}%{_datadir}

%if !0%{?is_opensuse}
# Prepare for 'default.desktop' being update-alternative handled, boo#1039756
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop
touch %{buildroot}%{_sysconfdir}/alternatives/default-waylandsession.desktop
install -d -m755 %{buildroot}%{_datadir}/wayland-sessions
ln -s %{_sysconfdir}/alternatives/default-waylandsession.desktop %{buildroot}%{_datadir}/wayland-sessions/default.desktop
%endif

%if !0%{?is_opensuse}
%post -n gnome-shell-classic
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/sle-classic.desktop 20

%postun -n gnome-shell-classic
[ -f %{_datadir}/xsessions/sle-classic.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/sle-classic.desktop
%endif

%files common
%license COPYING
%doc README.SUSE HACKING.md NEWS README.md

%files -n gnome-shell-classic
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.auto-move-windows.gschema.xml
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.extensions.classic.gschema.override
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.native-window-placement.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.screenshot-window-sizer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.user-theme.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.window-list.gschema.xml
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.extensions.sle-classic.gschema.override
%dir %{_datadir}/gnome-shell/extensions
%{_datadir}/gnome-shell/extensions/apps-menu@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/gnome-shell/extensions/launch-new-instance@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/gnome-shell/extensions/places-menu@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/gnome-shell/extensions/workspace-indicator@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/
%{_datadir}/gnome-shell/extensions/horizontal-workspaces@gnome-shell-extensions.gcampax.github.com/
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/modes/classic.json
%dir %{_datadir}/gnome-shell/theme/
%{_datadir}/gnome-shell/theme/calendar-today.svg
%{_datadir}/gnome-shell/theme/classic-process-working.svg
%{_datadir}/gnome-shell/theme/classic-toggle-off-intl.svg
%{_datadir}/gnome-shell/theme/classic-toggle-off-us.svg
%{_datadir}/gnome-shell/theme/classic-toggle-on-intl.svg
%{_datadir}/gnome-shell/theme/classic-toggle-on-us.svg
%{_datadir}/gnome-shell/theme/gnome-classic.css
%{_datadir}/gnome-shell/theme/gnome-classic-high-contrast.css
%{_datadir}/xsessions/gnome-classic.desktop
%{_datadir}/xsessions/sle-classic.desktop
%{_datadir}/gnome-shell/extensions/window-list@gnome-shell-extensions.gcampax.github.com/sle-classic.css
%{_datadir}/gnome-shell/modes/sle-classic.json
%{_datadir}/gnome-shell/extensions/sle-classic@suse.com/
%if !0%{?is_opensuse}
%dir %{_datadir}/wayland-sessions
%{_datadir}/gnome-shell/theme/sle-background.png
%{_datadir}/xsessions/default.desktop
%{_datadir}/wayland-sessions/default.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %{_sysconfdir}/alternatives/default-waylandsession.desktop
%endif

%files -n gnome-shell-classic-session
%defattr(-,root,root)
%license COPYING
%{_datadir}/gnome-session/sessions/gnome-classic.session

%files common-lang -f %{name}.lang

%changelog
