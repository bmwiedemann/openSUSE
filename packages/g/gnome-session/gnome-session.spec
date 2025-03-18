#
# spec file for package gnome-session
#
# Copyright (c) 2025 SUSE LLC
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


%define basever 47

Name:           gnome-session
Version:        47.0.1
Release:        0
Summary:        Session Tools for the GNOME Desktop
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://www.gnome.org
#Source0:        https://download.gnome.org/sources/gnome-session/44/%%{name}-%%{version}.tar.xz
Source0:        %{name}-%{version}.tar.zst
Source1:        gnome
Source2:        gnome.desktop
# PATCH-FIX-UPSTREAM gnome-session-better-handle-empty-xdg_session_type.patch bsc#1084756 bgo#794256 yfjiang@suse.com -- solution provided by msrb@suse.com using a more reasonable way to handle gpu acceleration check
Patch0:         gnome-session-better-handle-empty-xdg_session_type.patch
# PATCH-FIX-OPENSUSE gnome-session-s390-not-require-g-s-d_wacom.patch bsc#1129412 yfjiang@suse.com -- Remove the runtime requirement of g-s-d Wacom plugin
Patch2:         gnome-session-s390-not-require-g-s-d_wacom.patch

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
BuildRequires:  pkgconfig(glib-2.0) >= 2.46.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.24.2
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.10
BuildRequires:  pkgconfig(libsystemd) >= 209
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(systemd) >= 242
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xtrans)
Requires:       %{name}-core = %{version}
Requires:       (gnome-session-wayland or gnome-session-xsession)
Suggests:       gnome-session-wayland
# gnome-session-default-session merged into gnome-session; the alternative - fallback-session - disappeared
# with GNOME 3.8
Provides:       %{name}-default-session = %{version}
Obsoletes:      %{name}-default-session <= %{version}

%description
This package provides the basic session tools, like session management
functionality, for the GNOME Desktop.

%package wayland
Summary:        Wayland support for the GNOME Session Manager
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Requires:       gnome-settings-daemon
Requires:       xorg-x11-server-wayland

%description wayland
This package contains the definition of the default GNOME session on Wayland.

%package core
Summary:        Minimal version of the GNOME Session Manager
Group:          System/GUI/GNOME
Requires:       /usr/bin/dbus-launch
Requires:       gsettings-desktop-schemas >= 0.1.7
Requires:       hicolor-icon-theme

%description core
This package contains a minimal version of gnome-session, that can be
used for specific cases. The gnome-session package is needed for a fully
functional GNOME desktop.

%package xsession
Summary:        Desktop file for X11 GNOME Session
Provides:       gnome-session:%{_datadir}/xsessions/gnome.desktop
Requires:       %{name} = %{version}
Requires:       gnome-shell
Requires:       xorg-x11-server

%description xsession
Desktop file to add GNOME (X11) to display manager session menu.

%lang_package

%prep
%setup -q
%patch -P 0 -p1
%ifarch s390 s390x
%patch -P 2 -p1
%endif

%build
%meson \
	-D docbook=false \
	-D systemduserunitdir=%{_userunitdir} \
	%{nil}
%meson_build

%install
%meson_install
# install startup script and xsession file
install -d -m755 %{buildroot}%{_bindir}
install -m755 %{SOURCE1} %{buildroot}%{_bindir}/gnome
install -d -m755 %{buildroot}%{_datadir}/xsessions
install -m644 %{SOURCE2} %{buildroot}%{_datadir}/xsessions/gnome.desktop
%find_lang %{name}-%{basever} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

# Prepare for 'default.desktop' being update-alternative handled, boo#1039756
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop
touch %{buildroot}%{_sysconfdir}/alternatives/default-waylandsession.desktop
ln -s %{_sysconfdir}/alternatives/default-waylandsession.desktop %{buildroot}%{_datadir}/wayland-sessions/default.desktop

%post xsession
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/gnome.desktop 25

%postun xsession
[ -f %{_datadir}/xsessions/gnome.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/gnome.desktop

%files
%{_bindir}/gnome
%{_datadir}/gnome-session/sessions/gnome.session
%{_datadir}/gnome-session/sessions/gnome-dummy.session

%files xsession
%{_datadir}/xsessions/default.desktop
%{_datadir}/xsessions/gnome.desktop
%{_datadir}/xsessions/gnome-xorg.desktop
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop

%post wayland
%{_sbindir}/update-alternatives --install %{_datadir}/wayland-sessions/default.desktop \
  default-waylandsession.desktop %{_datadir}/wayland-sessions/gnome.desktop 25

%postun wayland
[ -f %{_datadir}/wayland-sessions/gnome.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-waylandsession.desktop %{_datadir}/wayland-sessions/gnome.desktop

%files wayland
%dir %{_datadir}/wayland-sessions
%{_datadir}/wayland-sessions/default.desktop
%{_datadir}/wayland-sessions/gnome.desktop
%{_datadir}/wayland-sessions/gnome-wayland.desktop
%ghost %{_sysconfdir}/alternatives/default-waylandsession.desktop
# Disabled as wayland is now the default session again.
#{_datadir}/wayland-sessions/gnome-wayland.desktop

%files core
%license COPYING
%doc AUTHORS ChangeLog NEWS README
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
%{_libexecdir}/gnome-session-binary
# Helper for the session definitions, to know if hardware is accelerated
%{_libexecdir}/gnome-session-check-accelerated
%{_libexecdir}/gnome-session-check-accelerated-gl-helper
%{_libexecdir}/gnome-session-check-accelerated-gles-helper
%{_libexecdir}/gnome-session-ctl
%{_libexecdir}/gnome-session-failed
%{_datadir}/gnome-session/hardware-compatibility
%dir %{_userunitdir}/gnome-launched-.scope.d
%{_userunitdir}/gnome-launched-.scope.d/override.conf
%{_userunitdir}/gnome-session-failed.service
%{_userunitdir}/gnome-session-failed.target
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
%{_userunitdir}/gnome-session-x11.target
%{_userunitdir}/gnome-session-x11@.target
%{_userunitdir}/gnome-session.target
%{_userunitdir}/gnome-session@.target
%dir %{_userunitdir}/gnome-session@gnome.target.d
%{_userunitdir}/gnome-session@gnome.target.d/gnome.session.conf

%files lang -f %{name}-%{basever}.lang

%changelog
