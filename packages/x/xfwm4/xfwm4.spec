#
# spec file for package xfwm4
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
Name:           xfwm4
Version:        4.18.0
Release:        0
Summary:        Default Window Manager for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/xfce/xfwm4/start
Source0:        https://archive.xfce.org/src/xfce/xfwm4/4.18/%{name}-%{version}.tar.bz2
Source1:        xfwm4.xml
BuildRequires:  exo-tools
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.14
BuildRequires:  pkgconfig(libxfce4kbd-private-3) >= 4.18.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.18.0
BuildRequires:  pkgconfig(libxfce4util-1.0)
BuildRequires:  pkgconfig(libxfconf-0) >= 4.18.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpresent)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
Recommends:     %{name}-lang = %{version}
Suggests:       xfwm4-themes
Provides:       xfwm4-doc = %{version}
Obsoletes:      xfwm4-doc <= 4.8.3
Provides:       windowmanager

%description
xfwm4 is the default Xfce window manager which manages the placement of
application windows on the screen, provides beautiful window decorations,
manages workspaces or virtual desktops and natively supports multiscreen mode.
It provides its own compositing manager for true transparency and shadows. The
Xfce window manager also includes a keyboard shorcuts editor for user specific
commands and basic windows manipulations and provides a preferences dialog for
advanced tweaks.

%package branding-upstream
Summary:        Upstream Branding of xfwm4
Group:          System/GUI/XFCE
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
#BRAND: xfce4.xml: Determines a number of window manager settings including the
#BRAND: default theme and title bar font.
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for the xfwm4 window manager.

%lang_package

%prep
%autosetup

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --enable-compositor \
    --enable-xpresent
%else
%configure \
    --enable-compositor \
    --enable-xpresent
%endif
%make_build

%install
%make_install

install -D -p -m 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml

%suse_update_desktop_file xfce-wm-settings
%suse_update_desktop_file xfce-wmtweaks-settings
%suse_update_desktop_file xfce-workspaces-settings

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%if %{with git}
%doc example.gtkrc-2.0 AUTHORS COMPOSITOR NEWS NOTES TODO
%else
%doc example.gtkrc-2.0 AUTHORS COMPOSITOR NEWS TODO README.md
%endif
%license COPYING*
%{_bindir}/xfwm4
%{_bindir}/xfwm4-settings
%{_bindir}/xfwm4-tweaks-settings
%{_bindir}/xfwm4-workspace-settings
%dir %{_libdir}/xfce4/xfwm4
%{_libdir}/xfce4/xfwm4/helper-dialog
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/themes/*
%{_datadir}/xfwm4

%files lang -f %{name}.lang

%files branding-upstream
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfwm4.xml

%changelog
