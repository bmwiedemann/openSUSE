#
# spec file for package gnome-initial-setup
#
# Copyright (c) 2024 SUSE LLC
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


Name:           gnome-initial-setup
Version:        46.3
Release:        0
Summary:        GNOME Initial Setup Assistant
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Design/OS/InitialSetup
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  krb5-devel
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  vala
BuildRequires:  (pkgconfig(webkit2gtk-5.0) or pkgconfig(webkitgtk-6.0))
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdm) >= 3.8.3
BuildRequires:  pkgconfig(geocode-glib-2.0) >= 2.6.0
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.53.0
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.37.1
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.10
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4.99
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2.alpha
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.3.1
BuildRequires:  pkgconfig(libnm) >= 1.2
BuildRequires:  pkgconfig(libnma-gtk4) >= 1.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18.8
BuildRequires:  pkgconfig(pango) >= 1.32.5
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(rest-1.0)
BuildRequires:  pkgconfig(systemd) >= 242
# Remove the yelp document dependency on both sle and leap, keeping tw consistent with upstream
%if !0%{?sle_version}
Requires:       gnome-getting-started-docs
%endif
%sysusers_requires

%description
Initial assistant, helping you to get the system up and running.

%lang_package

%prep
%autosetup -p1

%build
%sysusers_generate_pre data/%{name}.conf %{name} %{name}.conf
%meson \
	-D parental_controls=disabled \
%if 0%{?sle_version} && 0%{?sle_version} < 160000
	-D systemd=false \
%endif
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%if !0%{?sle_version}
# Move autostart file to /usr/etc
 mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
 mv %{buildroot}%{_sysconfdir}/xdg/autostart/gnome-initial-setup-copy-worker.desktop %{buildroot}%{_distconfdir}/xdg/autostart/gnome-initial-setup-copy-worker.desktop
 mv %{buildroot}%{_sysconfdir}/xdg/autostart/gnome-initial-setup-first-login.desktop %{buildroot}%{_distconfdir}/xdg/autostart/gnome-initial-setup-first-login.desktop
%endif

%pre -f %{name}.pre

%files
%license COPYING
%doc README.md
%{_datadir}/applications/gnome-initial-setup.desktop
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%{_datadir}/gnome-session/sessions/gnome-initial-setup.session
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/modes/initial-setup.json
%{_datadir}/polkit-1/rules.d/20-gnome-initial-setup.rules
%{_libexecdir}/gnome-initial-setup
%{_libexecdir}/gnome-initial-setup-copy-worker

%dir %{_datadir}/dconf
%dir %{_datadir}/dconf/profile
%{_datadir}/dconf/profile/gnome-initial-setup
%dir %{_datadir}/gnome-initial-setup
%{_datadir}/gnome-initial-setup/initial-setup-dconf-defaults
%if !0%{?sle_version}
%{_distconfdir}/xdg/autostart/gnome-initial-setup-copy-worker.desktop
%{_distconfdir}/xdg/autostart/gnome-initial-setup-first-login.desktop
%else
%{_sysconfdir}/xdg/autostart/gnome-initial-setup-copy-worker.desktop
%{_sysconfdir}/xdg/autostart/gnome-initial-setup-first-login.desktop
%endif
%if !0%{?sle_version} || 0%{?sle_version} >= 160000
%{_userunitdir}/gnome-initial-setup-copy-worker.service
%{_userunitdir}/gnome-initial-setup-first-login.service
%dir %{_userunitdir}/gnome-session@gnome-initial-setup.target.d
%{_userunitdir}/gnome-session@gnome-initial-setup.target.d/session.conf
%dir %{_userunitdir}/basic.target.wants
%dir %{_userunitdir}/gnome-session.target.wants
%{_userunitdir}/basic.target.wants/gnome-initial-setup-copy-worker.service
%{_userunitdir}/gnome-session.target.wants/gnome-initial-setup-first-login.service
%{_sysusersdir}/gnome-initial-setup.conf
%endif

%files lang -f %{name}.lang

%changelog
