#
# spec file for package gnome-initial-setup
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        3.32.1
Release:        0
Summary:        GNOME Initial Setup Assistant
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Url:            https://wiki.gnome.org/Design/OS/InitialSetup
Source0:        https://download.gnome.org/sources/gnome-initial-setup/3.32/%{name}-%{version}.tar.xz

# PATCH-FEATURE-SLE gnome-initial-setup-only-launch-CJK.patch FATE#321126 qzhao@suse.com -- Make gnome-initial-setup only work for CJK
Patch0:         gnome-initial-setup-only-launch-CJK.patch
# PATCH-FEATURE-SLE gnome-initial-setup-only-setup-keyboard.patch FATE#321126 yfjiang@suse.com -- Only launch the keyboard and IM setup
Patch1:         gnome-initial-setup-only-setup-keyboard.patch
# PATCH-FEATURE-SLE gnome-initial-setup-disable-dep-on-started-docs.patch FATE#321126 yfjiang@suse.com -- Disable help dialog after g-i-s system to remove the dependency of gnome-getting-started-docs
Patch2:         gnome-initial-setup-disable-dep-on-started-docs.patch
# PATCH-FIX-OPENSUSE gnome-initial-setup-mozc-engine-prioritized.patch boo#1067288 bnc#1029083 qzhao@suse.com -- Make the Mozc input engine as the 1st choice for Japanese environment.
Patch3:         gnome-initial-setup-mozc-engine-prioritized.patch

BuildRequires:  krb5-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(cheese)
BuildRequires:  pkgconfig(cheese-gtk) >= 3.3.5
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdm) >= 3.8.3
BuildRequires:  pkgconfig(geocode-glib-1.0)
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.53.0
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.7.5
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(goa-backend-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.11.3
BuildRequires:  pkgconfig(gweather-3.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4.99
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libgeoclue-2.0) >= 2.3.1
BuildRequires:  pkgconfig(libnm) >= 1.2
BuildRequires:  pkgconfig(libnma) >= 1.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(packagekit-glib2)
BuildRequires:  pkgconfig(pango) >= 1.32.5
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(rest-0.7)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Recommends:     %{name}-lang
# Remove the yelp document dependency on both sle and leap, keeping tw consistent with upstream
%if !0%{?sle_version}
Requires:       gnome-getting-started-docs
%endif

%description
Initial assistant, helping you to get the system up and running.

%lang_package

%prep
%setup -q
# Only enable keyboard/im setup feature in CJK environment on both sle and leap, keeping tw consistent with upstream
%if 0%{?sle_version} >= 120300
%patch0 -p1
%patch1 -p1
%patch2 -p1
%endif
%patch3 -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%pre
useradd -rM -d /run/gnome-initial-setup/ -s /sbin/nologin %{name} || :

%files
%license COPYING
%doc README
%dir %{_datadir}/gdm
%dir %{_datadir}/gdm/greeter
%dir %{_datadir}/gdm/greeter/applications
%{_datadir}/gdm/greeter/applications/gnome-initial-setup.desktop
%{_datadir}/gdm/greeter/applications/setup-shell.desktop
%dir %{_datadir}/gnome-session
%dir %{_datadir}/gnome-session/sessions
%{_datadir}/gnome-session/sessions/gnome-initial-setup.session
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/modes
%{_datadir}/gnome-shell/modes/initial-setup.json
%{_datadir}/polkit-1/rules.d/20-gnome-initial-setup.rules
%{_libexecdir}/gnome-initial-setup
%{_libexecdir}/gnome-initial-setup-copy-worker
%{_libexecdir}/gnome-welcome-tour
%{_sysconfdir}/xdg/autostart/gnome-initial-setup-copy-worker.desktop
%{_sysconfdir}/xdg/autostart/gnome-initial-setup-first-login.desktop
%{_sysconfdir}/xdg/autostart/gnome-welcome-tour.desktop

%files lang -f %{name}.lang

%changelog
