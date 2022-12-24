#
# spec file for package xfce4-session
#
# Copyright (c) 2020-2022 SUSE LLC
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
Name:           xfce4-session
Version:        4.18.0
Release:        0
Summary:        Xfce Session Manager
License:        GPL-2.0-only
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/xfce/xfce4-session/start
Source0:        https://archive.xfce.org/src/xfce/xfce4-session/4.18/%{name}-%{version}.tar.bz2
%if %{with git}
# PATCH-FIX-OPENSUSE xfce4-session-adapt-session-scripts-git.patch bnc#789057 maurizio.galli@gmail.com-- Adapt upstream sessions script to openSUSE.
Patch0:         xfce4-session-adapt-session-scripts-git.patch
# PATCH-FIX-OPENSUSE add-light-locker-support.patch  maurizio.galli@gmail.com -- add light-locker to xflock4 script.
%else
# PATCH-FIX-OPENSUSE xfce4-session-adapt-session-scripts.patch bnc#789057 gber@opensuse.org -- Adapt upstream sessions script to openSUSE.
Patch1:         xfce4-session-adapt-session-scripts.patch
# PATCH-FIX-OPENSUSE add-light-locker-support.patch  -- add light-locker to xflock4 script.
%endif
BuildRequires:  fdupes
BuildRequires:  iceauth
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.10
BuildRequires:  pkgconfig(libxfce4panel-2.0)
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.15.1
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.15.2
BuildRequires:  pkgconfig(libxfconf-0) >= 4.12.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.102
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
Requires:       %{name}-branding = %{version}
Requires:       systemd
Requires:       xfce4-settings
Requires:       xfconf
# bnc#845264
Requires:       iceauth
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name}-doc = %{version}
Recommends:     %{name}-lang = %{version}
# minimal packages for an Xfce session
Recommends:     xfwm4
Recommends:     xfdesktop
Recommends:     thunar
Recommends:     xfce4-panel
# xfce4-about needs to be dragged at a low level
Recommends:     libxfce4ui-tools
Obsoletes:      libxfsm-4_6-0 < %{version}
Obsoletes:      xfce4-session-devel < %{version}

%description
xfce4-session is the session manager for the Xfce desktop environment.

%package branding-upstream
Summary:        Upstream Branding of xfce4-session
Group:          System/GUI/XFCE
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
# BRAND: xfce4-session.xml: Control session parameters such as the tools and
# BRAND: applications started by default or the splash theme.
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for the Xfce Session Manager.

%lang_package

%prep
%autosetup -p1

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --disable-static
%else
%configure \
    --disable-static
%endif
%make_build

%install
%make_install

%fdupes -s %{buildroot}%{_datadir}/icons/hicolor/*

chmod 755 %{buildroot}%{_sysconfdir}/xdg/xfce4/xinitrc

install -d -m 755 %{buildroot}%{_datadir}/xfce/applications

# add back X-XFCE for now; this is a personal and not a system setting
%suse_update_desktop_file -r xfce-session-settings XFCE X-XFCE GTK Settings DesktopSettings X-XFCE-SettingsDialog X-XFCE-PersonalSettings
%suse_update_desktop_file xfce4-session-logout

%find_lang %{name}

find %{buildroot} -type f -name "*.la" -delete -print
# not needed, shutdown/reboot happens via systemd
rm %{buildroot}%{_datadir}/polkit-1/actions/org.xfce.session.policy \
    %{buildroot}%{_libdir}/xfce4/session/xfsm-shutdown-helper

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

# remove xscreensaver desktop file. We use xfce4-screensaver instead.
rm %{buildroot}%{_sysconfdir}/xdg/autostart/xscreensaver.desktop

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/xfce.desktop 20

%postun
[ -f %{_datadir}/xsessions/xfce.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/xfce.desktop

%files
%license COPYING
%doc AUTHORS BUGS NEWS README.md TODO
%config %{_sysconfdir}/xdg/xfce4/Xft.xrdb
%{_sysconfdir}/xdg/xfce4/xinitrc
%{_bindir}/xfce4-session
%{_bindir}/xfce4-session-logout
%{_bindir}/xfce4-session-settings
%{_bindir}/xflock4
%{_bindir}/startxfce4
%{_datadir}/xsessions/xfce.desktop
%{_datadir}/xsessions/default.desktop
%ghost %{_sysconfdir}/alternatives/default.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*/*/*
%doc %{_mandir}/man1/xfce4-session*.1*

%files lang -f %{name}.lang

%files branding-upstream
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-session.xml

%changelog
