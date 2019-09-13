#
# spec file for package krb5-auth-dialog
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           krb5-auth-dialog
Version:        3.26.1
Release:        0
Summary:        Kerberos 5 ticket monitoring tray applet
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://www.gnome.org/
Source:         http://download.gnome.org/sources/krb5-auth-dialog/3.26/%{name}-%{version}.tar.xz
BuildRequires:  intltool
BuildRequires:  krb5-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnotify) >= 0.7.0
Recommends:     %{name}-lang

%description
krb5-auth-dialog is a tray applet that monitors and refreshes your
Kerberos ticket. It pops up reminders when the ticket is about to
expire.

It features ticket autorenewal and supports pkinit.

%lang_package

%prep
%setup -q
translation-update-upstream

%build
%configure \
        --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{buildroot}%{_sysconfdir}/xdg/autostart/%{name}.desktop
# Categories in the .desktop file don't work for brp-check, unfortunately
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/%{name}.desktop GNOME GTK System Network
%find_lang %{name} %{?no_lang_C}

%files
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}*
%{_libdir}/%{name}/
%dir %{_datadir}/appdata
%{_datadir}/appdata/krb5-auth-dialog.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.KrbAuthDialog.service
%{_datadir}/GConf/gsettings/org.gnome.KrbAuthDialog.convert
%{_datadir}/glib-2.0/schemas/org.gnome.KrbAuthDialog.gschema.xml
%{_datadir}/icons/hicolor/*/status/krb*.*
%{_sysconfdir}/xdg/autostart/*.desktop
%{_mandir}/man?/*%{ext_man}

%files lang -f %{name}.lang

%changelog
