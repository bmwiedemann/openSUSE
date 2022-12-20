#
# spec file for package xfce4-settings
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_with git

Name:           xfce4-settings
Version:        4.18.0
Release:        0
Summary:        Tools for Managing Xfce Settings
License:        GPL-2.0-only AND GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/xfce/xfce4-settings/start
Source:         https://archive.xfce.org/src/xfce/xfce4-settings/4.18/%{name}-%{version}.tar.bz2
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(exo-2)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(garcon-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.17.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.17.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.13
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xorg-libinput)
BuildRequires:  pkgconfig(xrandr)
%if 0%{?suse_version} > 1500
BuildRequires:  xorgproto-devel
%endif
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Requires:       %{name}-branding = %{version}
Recommends:     %{name}-color
Recommends:     %{name}-lang = %{version}
Provides:       xfce-mcs-manager = %{version}
Obsoletes:      xfce-mcs-manager < %{version}
Provides:       xfce-mcs-plugins = %{version}
Obsoletes:      xfce-mcs-plugins < %{version}

%description
This package provides a number of tools for managing settings in the Xfce
desktop environment.

%package branding-upstream
Summary:        Upstream Branding of xfce4-settings
Group:          System/GUI/XFCE
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
#BRAND: xsettings.xml: Determines diverse settings including the default theme
#BRAND: and anti-aliasing default settings.
#BRAND: xfce-settings-manager.menu: Configures the settings manager menu.
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for xfce4-settings.

%package color
Summary:        Subpackage providing xfce4-color-settings
BuildRequires:  sane-backends
BuildRequires:  xiccd
BuildRequires:  pkgconfig(colord) >= 0.1.24
BuildRequires:  pkgconfig(colord-gtk) >= 0.1.24
# Make sure colord and other runtime dependencies are installed boo#1173953
Requires:       colord
Requires:       %{name} = %{version}-%{release}
Requires:       sane-backends
Requires:       xiccd
Provides:       xfce4-color-settings

%description color
The Xfce Color Profile settings tool is a front-end to set up color management
for printers, scanners, and displays.

%lang_package

%prep
%autosetup

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
export CFLAGS="%{optflags} -D_FORTIFY_SOURCE=1"
%configure \
    --enable-maintainer-mode \
    --with-helper-path-prefix=%{_libexecdir} \
    --enable-sound-settings \
    --enable-colord \
    --enable-pluggable-dialogs
%else
%configure \
    --with-helper-path-prefix=%{_libexecdir} \
    --enable-sound-settings \
    --enable-colord \
    --enable-pluggable-dialogs
%endif
%make_build

%install
%make_install

%suse_update_desktop_file xfsettingsd
# add back X-XFCE for now
%suse_update_desktop_file xfce-display-settings X-XFCE
# add back X-XFCE for now
%suse_update_desktop_file xfce-keyboard-settings X-XFCE
# add back X-XFCE for now
%suse_update_desktop_file xfce-mouse-settings X-XFCE
# add back X-XFCE for now
%suse_update_desktop_file xfce-settings-manager X-XFCE
# add back X-XFCE for now
%suse_update_desktop_file xfce-ui-settings X-XFCE
# add back X-XFCE for now; this is a personal and not a system setting
%suse_update_desktop_file -r xfce4-accessibility-settings XFCE X-XFCE GTK Settings DesktopSettings X-XFCE-SettingsDialog X-XFCE-PersonalSettings
# add back X-XFCE for now; this is a personal and not a system setting
%suse_update_desktop_file -r xfce4-mime-settings XFCE X-XFCE GTK Settings DesktopSettings X-XFCE-SettingsDialog X-XFCE-PersonalSettings
# add back X-XFCE for now
%suse_update_desktop_file xfce4-settings-editor X-XFCE

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

# Fix python shebangs
sed -i 's+#!/usr/bin/env python3+#!/usr/bin/python3+g' %{buildroot}%{_libexecdir}/xfce4/xfce4-compose-mail

%find_lang %{name} %{?no_lang_C}

%files
%doc AUTHORS NEWS README.md TODO
%license COPYING
%{_bindir}/xfce4-accessibility-settings
%{_bindir}/xfce4-appearance-settings
%{_bindir}/xfce4-display-settings
%{_bindir}/xfce4-find-cursor
%{_bindir}/xfce4-keyboard-settings
%{_bindir}/xfce4-mime-helper
%{_bindir}/xfce4-mouse-settings
%{_bindir}/xfce4-settings-editor
%{_bindir}/xfce4-settings-manager
%{_bindir}/xfsettingsd
%{_bindir}/xfce4-mime-settings
%dir %{_libexecdir}/xfce4/settings/
%{_libexecdir}/xfce4/settings/appearance-install-theme
%{_libexecdir}/xfce4/xfce4-compose-mail
%dir %{_datadir}/applications/
%{_datadir}/applications/xfce-display-settings.desktop
%{_datadir}/applications/xfce-keyboard-settings.desktop
%{_datadir}/applications/xfce-mouse-settings.desktop
%{_datadir}/applications/xfce-settings-manager.desktop
%{_datadir}/applications/xfce-ui-settings.desktop
%{_datadir}/applications/xfce4-accessibility-settings.desktop
%{_datadir}/applications/xfce4-file-manager.desktop
%{_datadir}/applications/xfce4-mail-reader.desktop
%{_datadir}/applications/xfce4-mime-settings.desktop
%{_datadir}/applications/xfce4-settings-editor.desktop
%{_datadir}/applications/xfce4-terminal-emulator.desktop
%{_datadir}/applications/xfce4-web-browser.desktop
%{_sysconfdir}/xdg/autostart/xfsettingsd.desktop
%dir %{_datadir}/icons/hicolor/
%{_datadir}/icons/hicolor/*/*/org.xfce.filemanager.*
%{_datadir}/icons/hicolor/*/*/org.xfce.mailreader.*
%{_datadir}/icons/hicolor/*/*/org.xfce.settings.accessibility.*
%{_datadir}/icons/hicolor/*/*/org.xfce.settings.appearance.*
%{_datadir}/icons/hicolor/*/*/org.xfce.settings.default-applications.*
%{_datadir}/icons/hicolor/*/*/org.xfce.settings.display.*
%{_datadir}/icons/hicolor/*/*/org.xfce.settings.editor.*
%{_datadir}/icons/hicolor/*/*/org.xfce.settings.keyboard.*
%{_datadir}/icons/hicolor/*/*/org.xfce.settings.manager.*
%{_datadir}/icons/hicolor/*/*/org.xfce.settings.mouse.*
%{_datadir}/icons/hicolor/*/*/org.xfce.terminalemulator.*
%{_datadir}/icons/hicolor/*/*/org.xfce.webbrowser.*
%{_datadir}/icons/hicolor/*/*/xfce-display-extend.*
%{_datadir}/icons/hicolor/*/*/xfce-display-external.*
%{_datadir}/icons/hicolor/*/*/xfce-display-internal.*
%{_datadir}/icons/hicolor/*/*/xfce-display-mirror.*
%{_datadir}/icons/hicolor/*/*/xfce-display-profile.*
%dir %{_datadir}/xfce4/helpers
%{_datadir}/xfce4/helpers/*.desktop

%files lang -f %{name}.lang

%files branding-upstream
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xsettings.xml
%dir %{_sysconfdir}/xdg/menus
%{_sysconfdir}/xdg/menus/xfce-settings-manager.menu
%config %{_sysconfdir}/xdg/xfce4/helpers.rc

%files color
%{_bindir}/xfce4-color-settings
%dir %{_datadir}/applications/
%{_datadir}/applications/xfce4-color-settings.desktop
%dir %{_datadir}/icons/hicolor/
%{_datadir}/icons/hicolor/*/*/org.xfce.settings.color.*

%changelog
