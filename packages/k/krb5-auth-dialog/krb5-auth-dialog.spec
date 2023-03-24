#
# spec file for package krb5-auth-dialog
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2009 Dominique Leuenberger, Almere, The Netherlands.
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


Name:           krb5-auth-dialog
Version:        44.0.alpha1
Release:        0
Summary:        Kerberos 5 ticket monitoring tray applet
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://www.gnome.org/
Source0:        https://download.gnome.org/sources/krb5-auth-dialog/44/%{name}-%{version}.tar.xz

BuildRequires:  krb5-devel
BuildRequires:  meson >= 0.53.0
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.66
BuildRequires:  pkgconfig(gobject-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk4) >= 4.4
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2

%description
krb5-auth-dialog is a tray applet that monitors and refreshes your
Kerberos ticket. It pops up reminders when the ticket is about to
expire.

It features ticket autorenewal and supports pkinit.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}

%files
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}*
%{_libdir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.KrbAuthDialog.service
%{_datadir}/glib-2.0/schemas/org.gnome.KrbAuthDialog.gschema.xml
%{_datadir}/icons/hicolor/*/status/krb*.*
%{_datadir}/metainfo/org.gnome.KrbAuthDialog.metainfo.xml
%{_mandir}/man?/*%{ext_man}
%{_sysconfdir}/xdg/autostart/*.desktop

%files lang -f %{name}.lang

%changelog
