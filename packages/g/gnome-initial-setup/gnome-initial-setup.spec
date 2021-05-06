#
# spec file for package gnome-initial-setup
#
# Copyright (c) 2021 SUSE LLC
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
Version:        40.1
Release:        0
Summary:        GNOME Initial Setup Assistant
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Design/OS/InitialSetup
Source0:        https://download.gnome.org/sources/gnome-initial-setup/40/%{name}-%{version}.tar.xz
# PATCH-FEATURE-SLE gnome-initial-setup-smarter.patch FATE#325763 FATE#321126 boo#1067288 bnc#1029083 qzhao@suse.com -- Investigate gnome-initial-setup, and make a Smarter gnome initial configuration.
Patch0:         gnome-initial-setup-smarter.patch

BuildRequires:  krb5-devel
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese) >= 3.28
BuildRequires:  pkgconfig(cheese-gtk) >= 3.3.5
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdm) >= 3.8.3
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.53.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.7.5
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 3.37.1
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.3
BuildRequires:  pkgconfig(gweather-3.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4.99
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.3.1
BuildRequires:  pkgconfig(libnm) >= 1.2
BuildRequires:  pkgconfig(libnma) >= 1.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.18.8
BuildRequires:  pkgconfig(pango) >= 1.32.5
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(systemd) >= 242
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.26.0
# Remove the yelp document dependency on both sle and leap, keeping tw consistent with upstream
%if !0%{?sle_version}
Requires:       gnome-getting-started-docs
%endif

%description
Initial assistant, helping you to get the system up and running.

%lang_package

%prep
%setup -q
%if 0%{?sle_version} >= 150200
%patch0 -p1
%endif

%build
%meson \
        -Dparental_controls=disabled \
%if 0%{?sle_version} && 0%{?sle_version} < 160000
        -Dsystemd=false \
%endif
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%pre
useradd -rM -d /run/gnome-initial-setup/ -s /sbin/nologin %{name} || :

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
%{_sysconfdir}/xdg/autostart/gnome-initial-setup-copy-worker.desktop
%{_sysconfdir}/xdg/autostart/gnome-initial-setup-first-login.desktop
%if !0%{?sle_version} || 0%{?sle_version} >= 160000
%{_userunitdir}/gnome-initial-setup-copy-worker.service
%{_userunitdir}/gnome-initial-setup-first-login.service
%dir %{_userunitdir}/gnome-session@gnome-initial-setup.target.d
%{_userunitdir}/gnome-session@gnome-initial-setup.target.d/session.conf
%dir %{_userunitdir}/gnome-session.target.wants
%{_userunitdir}/gnome-session.target.wants/gnome-initial-setup-copy-worker.service
%{_userunitdir}/gnome-session.target.wants/gnome-initial-setup-first-login.service
%endif

%files lang -f %{name}.lang

%changelog
