#
# spec file for package empathy
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


%define with_geocode 1

Name:           empathy
Version:        3.12.14
Release:        0
Summary:        Instant Messenger Client for GNOME, based on Telepathy
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            http://live.gnome.org/Empathy
Source:         http://download.gnome.org/sources/empathy/3.12/%{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM empathy-fix-gettext-domain.patch zaitor@opensuse.org -- gschema: Fix gettext-domain
Patch0:         empathy-fix-gettext-domain.patch

BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  python3-xml
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(champlain-gtk-0.12) >= 0.12.1
BuildRequires:  pkgconfig(cheese-gtk) >= 3.4.0
BuildRequires:  pkgconfig(clutter-1.0) >= 1.10.0
BuildRequires:  pkgconfig(clutter-gst-3.0)
BuildRequires:  pkgconfig(clutter-gtk-1.0) >= 1.1.2
BuildRequires:  pkgconfig(cogl-1.0) >= 1.14
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(folks) >= 0.9.5
BuildRequires:  pkgconfig(folks-telepathy) >= 0.9.5
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(goa-1.0) >= 3.5.1
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.4
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1) >= 0.5
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(mission-control-plugins) >= 5.13.1
BuildRequires:  pkgconfig(telepathy-farstream) >= 0.6.0
BuildRequires:  pkgconfig(telepathy-glib) >= 0.23.2
BuildRequires:  pkgconfig(telepathy-logger-0.2) >= 0.8.0
BuildRequires:  pkgconfig(webkit2gtk-4.0)
# Not strictly required but empathy now relies on gnome-contacts to
# display contacts' details and link contacts together.
Requires:       gnome-contacts
Requires:       iso-codes
Requires:       telepathy-gabble
Requires:       telepathy-logger
Requires:       telepathy-mission-control
Recommends:     %{name}-lang
Recommends:     geoclue2
Recommends:     telepathy-haze
Recommends:     telepathy-idle
# The applets and the libraries have been removed
Obsoletes:      empathy-devel < 2.29.1
Obsoletes:      gnome-applets-empathy < 2.29.1
Obsoletes:      python-empathy < 2.29.1
# Nautilus-sendto was completely stripped down in version 3.7.92 and only does mail now; no more headers available.
Obsoletes:      nautilus-sendto-plugin-empathy <= 3.7.92
%glib2_gsettings_schema_requires
%if %{with_geocode}
BuildRequires:  pkgconfig(geoclue-2.0) >= 1.99.3
BuildRequires:  pkgconfig(geocode-glib-1.0) >= 0.99.1
%endif

%description
Empathy is a messaging program which supports text, voice, and video
chat and file transfers over many different protocols. You can tell it
about your accounts on all those services and do all your chatting
within one application.

Empathy uses Telepathy for protocol support and has a user interface
based on Gossip. Empathy is the default chat client in current
versions of GNOME, making it easier for other GNOME applications to
integrate collaboration functionality using Telepathy.

%package -n telepathy-mission-control-plugin-goa
Summary:        Telepathy Mission Control Plugin to use data from GNOME Online Accounts
Group:          Productivity/Networking/Instant Messenger
Requires:       gnome-online-accounts
Requires:       telepathy-mission-control
Supplements:    packageand(telepathy-mission-control:gnome-online-accounts)

%description -n telepathy-mission-control-plugin-goa
This plugin for Mission Control provides integration with the GNOME
Online Accounts service. Mission Control will automatically create a
Telepathy account for GNOME Online Accounts configured with the "Chat"
feature enabled.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
export LANG=C.UTF-8
export PYTHON=%{_bindir}/python3
%configure \
	--disable-static \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Even though %%suse_update_desktop_file is useless on >= 12.2, we keep it for now for backports to 12.1
%suse_update_desktop_file empathy
%find_lang %{name} %{?no_lang_C}
# TelePathy Account Widget has it's own language files.
%find_lang %{name}-tpaw %{name}.lang %{no_lang_C}
# create symlinks for man pages
%fdupes -s %{buildroot}%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}

%if 0%{?suse_version} < 1330
%post
%glib2_gsettings_schema_post
%desktop_database_post
%icon_theme_cache_post

%postun
%glib2_gsettings_schema_postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc README TODO
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/empathy
%{_bindir}/empathy-accounts
%{_bindir}/empathy-debugger
%{_datadir}/adium/
%{_datadir}/icons/hicolor/*/apps/empathy*
%dir %{_datadir}/appdata
%{_datadir}/appdata/empathy.appdata.xml
%{_datadir}/applications/empathy.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/empathy/
%{_datadir}/GConf/gsettings/empathy.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Empathy.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.telepathy-account-widgets.gschema.xml
%{_datadir}/telepathy/clients/*.client
%{_libdir}/%{name}/
%{_libexecdir}/empathy-auth-client
%{_libexecdir}/empathy-call
%{_libexecdir}/empathy-chat
%{_mandir}/man1/empathy.1%{?ext_man}
%{_mandir}/man1/empathy-accounts.1%{?ext_man}
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/clients

%files -n telepathy-mission-control-plugin-goa
%{_libdir}/mission-control-plugins.0/mcp-account-manager-goa.so

%files lang -f %{name}.lang

%changelog
