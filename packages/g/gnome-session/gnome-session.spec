#
# spec file for package gnome-session
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


%define basever 49

Name:           gnome-session
Version:        49.1
Release:        0
Summary:        Session Tools for the GNOME Desktop
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
Source0:        %{name}-%{version}.tar.zst
Source1:        gnome
Source2:        gnome.desktop

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gio-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.82.0
BuildRequires:  pkgconfig(gnome-desktop-4) >= 3.24.2
BuildRequires:  pkgconfig(gtk4) >= 3.22.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.10
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(systemd) >= 242
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xtrans)
Requires:       dbus-service
Requires:       gnome-settings-daemon
Requires:       gsettings-desktop-schemas >= 0.1.7
Requires:       hicolor-icon-theme
Requires:       xorg-x11-server-wayland
Requires(post): update-alternatives
Requires(postun): update-alternatives
# gnome-session-default-session merged into gnome-session; the alternative - fallback-session - disappeared
# with GNOME 3.8
Provides:       %{name}-default-session = %{version}
Obsoletes:      %{name}-default-session < %{version}
# With the change to GNOME 49, the XSession is no longer a thing
Obsoletes:      gnome-session-xsession < 49
# With the change to GNOME 49, core and wayland session are merged into the main package
Obsoletes:      gnome-session-core    < 49.1
Provides:       gnome-session-core    = %{version}
Obsoletes:      gnome-session-wayland < 49.1
Provides:       gnome-session-wayland = %{version}

%description
This package provides the basic session tools, like session management
functionality, for the GNOME Desktop.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D docbook=false \
	-D systemduserunitdir=%{_userunitdir} \
	-D mimeapps=false \
	%{nil}
%meson_build

%install
%meson_install
# install startup script and xsession file
install -d -m755 %{buildroot}%{_bindir}
install -m755 %{SOURCE1} %{buildroot}%{_bindir}/gnome
%find_lang %{name}-%{basever} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

# Prepare for 'default.desktop' being update-alternative handled, boo#1039756
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-waylandsession.desktop
ln -s %{_sysconfdir}/alternatives/default-waylandsession.desktop %{buildroot}%{_datadir}/wayland-sessions/default.desktop

%post
%{_sbindir}/update-alternatives --install %{_datadir}/wayland-sessions/default.desktop \
  default-waylandsession.desktop %{_datadir}/wayland-sessions/gnome.desktop 25

%postun
[ -f %{_datadir}/wayland-sessions/gnome.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-waylandsession.desktop %{_datadir}/wayland-sessions/gnome.desktop

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/gnome
%{_datadir}/gnome-session/sessions/gnome.session
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/default.desktop
%{_datadir}/wayland-sessions/gnome.desktop
%{_datadir}/wayland-sessions/gnome-wayland.desktop
%ghost %{_sysconfdir}/alternatives/default-waylandsession.desktop
# Disabled as wayland is now the default session again.
#{_datadir}/wayland-sessions/gnome-wayland.desktop
%{_bindir}/gnome-session
%{_bindir}/gnome-session-inhibit
%{_bindir}/gnome-session-quit
%{_datadir}/glib-2.0/schemas/org.gnome.SessionManager.gschema.xml
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/gnome-portals.conf
%{_mandir}/man1/gnome-session.1%{?ext_man}
%{_mandir}/man1/gnome-session-inhibit.1%{?ext_man}
%{_mandir}/man1/gnome-session-quit.1%{?ext_man}
%{_libexecdir}/gnome-session-ctl
%{_libexecdir}/gnome-session-init-worker
%{_libexecdir}/gnome-session-service
%{_userunitdir}/gnome-session-initialized.target
%{_userunitdir}/gnome-session-manager.target
%{_userunitdir}/gnome-session-manager@.service
%{_userunitdir}/gnome-session-monitor.service
%{_userunitdir}/gnome-session-pre.target
%{_userunitdir}/gnome-session-restart-dbus.service
%{_userunitdir}/gnome-session-shutdown.target
%{_userunitdir}/gnome-session-signal-init.service
%{_userunitdir}/gnome-session-wayland.target
%{_userunitdir}/gnome-session-wayland@.target
%{_userunitdir}/gnome-session-x11-services-ready.target
%{_userunitdir}/gnome-session-x11-services.target
%{_userunitdir}/gnome-session.target
%{_userunitdir}/gnome-session@.target
%dir %{_userunitdir}/app-flatpak-.scope.d
%{_userunitdir}/app-flatpak-.scope.d/override.conf
%dir %{_userunitdir}/app-gnome-.scope.d
%{_userunitdir}/app-gnome-.scope.d/override.conf
%{_userunitdir}/gnome-session-basic-services.target
%dir %{_userunitdir}/gnome-session@gnome.target.d
%{_userunitdir}/gnome-session@gnome.target.d/gnome.session.conf

%files lang -f %{name}-%{basever}.lang

%changelog
