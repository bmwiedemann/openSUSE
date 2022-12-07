#
# spec file for package evolution
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


# _version needs to be %{version} stripped to major.minor.micro only...
%define _version %(echo %{version} | grep -E -o '[0-9]+\.[0-9]+\.[0-9]+')

Name:           evolution
Version:        3.46.2
Release:        0
# FIXME: check if note on license is still valid (comment before license)
Summary:        The Integrated GNOME Mail, Calendar, and Address Book Suite
# NOTE: Some files are currently GPL-2.0 but pending relicensing, see bnc#749859
License:        CC-BY-SA-3.0 AND LGPL-2.0-only AND LGPL-3.0-only AND OLDAP-2.8 AND GFDL-1.1-only AND GFDL-1.3-only
Group:          Productivity/Networking/Email/Clients
URL:            https://wiki.gnome.org/Apps/Evolution/
Source0:        https://download.gnome.org/sources/evolution/3.46/%{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  bogofilter
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
# don't you ever enable this! It's experimental and insecure (bnc#609013)
#BuildRequires:  libytnef-devel
BuildRequires:  psmisc
BuildRequires:  spamassassin
BuildRequires:  sqlite3-devel
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(camel-1.2) >= %{_version}
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gail-3.0) >= 3.2.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.24.0
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-2.0) >= 2.56.0
BuildRequires:  pkgconfig(gladeui-2.0) >= 3.10.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.40.0
BuildRequires:  pkgconfig(gnome-autoar-0) >= 0.1.1
BuildRequires:  pkgconfig(gnome-autoar-gtk-0) >= 0.1.1
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 2.91.3
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
# NOTE when bumping this BR, bump the req in devel pac below
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.8.0
# /NOTE
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtkspell3-3.0)
# NOTE when bumping this BR, bump the req in devel pac below
BuildRequires:  pkgconfig(gweather4)
# /NOTE
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libebackend-1.2) >= %{_version}
BuildRequires:  pkgconfig(libebook-1.2) >= %{_version}
BuildRequires:  pkgconfig(libecal-2.0) >= %{_version}
BuildRequires:  pkgconfig(libedataserver-1.2) >= %{_version}
BuildRequires:  pkgconfig(libedataserverui-1.2) >= %{_version}
BuildRequires:  pkgconfig(libnotify) >= 0.7
# /NOTE
BuildRequires:  pkgconfig(libpst) >= 0.6.54
# NOTE when bumping this BR, bump the req in devel pac below
BuildRequires:  pkgconfig(libsoup-3.0)
# /NOTE
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.3
BuildRequires:  pkgconfig(nspr)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(shared-mime-info) >= 0.22
BuildRequires:  pkgconfig(webkit2gtk-4.1)
Requires:       evolution-data-server >= %{_version}
# Mono and python plugins were available until evo 3.5.x
Obsoletes:      evolution-mono-plugins < %{version}
Obsoletes:      evolution-plugin-rss < %{version}
Obsoletes:      evolution-python-plugins < %{version}

%description
Evolution consists of modular components (at the moment: mailer,
calendar, and address book) that should make daily life easier. Because
of the modular design, it is possible to plug new components into
Evolution or embed the existing ones in other applications.

%package -n glade-catalog-evolution
Summary:        Glade catalog for the Evolution groupware library
Group:          Development/Tools/GUI Builders
Requires:       %{name} = %{version}
Requires:       glade
Supplements:    (glade and %{name}-devel)

%description -n glade-catalog-evolution
Evolution consists of modular components (at the moment: mailer,
calendar, and address book) that should make daily life easier. Because
of the modular design, it is possible to plug new components into
Evolution or embed the existing ones in other applications.

This package provides a catalog for Glade, to allow the use of Evolution
widgets in Glade.

%package -n evolution-plugin-bogofilter
Summary:        Bogofilter plugin for the Evolution groupware suite
Group:          Productivity/Networking/Email/Clients
Requires:       %{name}
Requires:       bogofilter
Enhances:       %{name}
Supplements:    (%{name} and bogofilter)

%description -n evolution-plugin-bogofilter
Adds support for junk-mail filtering via bogofilter.

%package -n evolution-plugin-pst-import
Summary:        Outlook PST importer plugin for the Evolution groupware suite
Group:          Productivity/Networking/Email/Clients
Requires:       %{name}
Enhances:       %{name}

%description -n evolution-plugin-pst-import
Adds support to import messages from Outlook PST files.

%package -n evolution-plugin-spamassassin
Summary:        SpamAssassin plugin for the Evolution groupware suite
Group:          Productivity/Networking/Email/Clients
Requires:       %{name}
Requires:       spamassassin
Enhances:       %{name}
Supplements:    (%{name} and spamassassin)

%description -n evolution-plugin-spamassassin
Adds support for junk-mail filtering via spamassassin.

%package -n evolution-plugin-text-highlight
Summary:        Text highlight plugin for the Evolution groupware suite
Group:          Productivity/Networking/Email/Clients
BuildRequires:  highlight
Requires:       %{name}
Requires:       highlight
Enhances:       %{name}
Supplements:    (%{name} and highlight)

%description -n evolution-plugin-text-highlight
Adds support to highlight syntax of mails and their attachments.

%package devel
Summary:        Development files for the Evolution groupware suite
Group:          Development/Libraries/C and C++
Requires:       evolution = %{version}
Requires:       evolution-data-server-devel >= %{version}
Requires:       pkgconfig(enchant-2)
Requires:       pkgconfig(gtk+-3.0) >= 3.8.0
Requires:       pkgconfig(gtkspell3-3.0)
Requires:       pkgconfig(gweather4)
Requires:       pkgconfig(libsoup-3.0)
Requires:       pkgconfig(libxml-2.0)
Provides:       evolution2-devel = %{version}
Obsoletes:      evolution2-devel < %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%autosetup -p1

%build
%cmake \
  -DLIBEXEC_INSTALL_DIR=%{_libexecdir} \
  -DENABLE_YTNEF=OFF \
  -DWITH_GLADE_CATALOG=ON \
  -DENABLE_GTK_DOC=ON \
  -DCMAKE_SKIP_INSTALL_RPATH=OFF
%cmake_build

%install
%cmake_install
%suse_update_desktop_file -r -G "Mail and Calendar" org.gnome.Evolution GNOME GTK Network Email Calendar ContactManagement
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%files
%license COPYING COPYING-DOCS COPYING-DOCS.CCBYSA COPYING-DOCS.GFDL
%doc AUTHORS NEWS
%doc %{_datadir}/help/C/%{name}/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/*
%{_datadir}/GConf/gsettings/evolution.convert
%{_datadir}/applications/*.desktop
%{_datadir}/evolution
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.importer.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.shell.gschema.xml
# Should not be installed as the plugin is not installed (bgo#666613)
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.external-editor.gschema.xml
# despite the plugins being split in their own packages, the schema must be present in any case
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.bogofilter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.sender-validator.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.spamassassin.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/evolution.svg
%{_datadir}/icons/hicolor/*/apps/evolution-symbolic.svg
%{_datadir}/metainfo/org.gnome.Evolution.appdata.xml
%dir %{_libdir}/evolution/
%{_libdir}/evolution/*.so
%dir %{_libdir}/evolution/modules
%{_libdir}/evolution/modules/module-addressbook.so
%{_libdir}/evolution/modules/module-backup-restore.so
%{_libdir}/evolution/modules/module-book-config-carddav.so
%{_libdir}/evolution/modules/module-book-config-google.so
%{_libdir}/evolution/modules/module-book-config-ldap.so
%{_libdir}/evolution/modules/module-book-config-local.so
%{_libdir}/evolution/modules/module-cal-config-caldav.so
%{_libdir}/evolution/modules/module-cal-config-contacts.so
%{_libdir}/evolution/modules/module-cal-config-google.so
%{_libdir}/evolution/modules/module-cal-config-local.so
%{_libdir}/evolution/modules/module-cal-config-weather.so
%{_libdir}/evolution/modules/module-cal-config-webdav-notes.so
%{_libdir}/evolution/modules/module-cal-config-webcal.so
%{_libdir}/evolution/modules/module-calendar.so
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.calendar.gschema.xml
%{_libdir}/evolution/modules/module-composer-autosave.so
%{_libdir}/evolution/modules/module-composer-to-meeting.so
%{_libdir}/evolution/modules/module-contact-photos.so
%{_libdir}/evolution/modules/module-gravatar.so
%{_libdir}/evolution/modules/module-itip-formatter.so
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.itip.gschema.xml
%{_libdir}/evolution/modules/module-mail-config.so
%{_libdir}/evolution/modules/module-mail.so
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.mail.gschema.xml
%{_libdir}/evolution/modules/module-accounts-window.so
%{_libdir}/evolution/modules/module-config-lookup.so
%{_libdir}/evolution/modules/module-mailto-handler.so
%{_libdir}/evolution/modules/module-mdn.so
%{_libdir}/evolution/modules/module-offline-alert.so
%{_libdir}/evolution/modules/module-plugin-lib.so
%{_libdir}/evolution/modules/module-plugin-manager.so
%{_libdir}/evolution/modules/module-prefer-plain.so
%{_libdir}/evolution/modules/module-settings.so
%{_libdir}/evolution/modules/module-startup-wizard.so
%{_libdir}/evolution/modules/module-vcard-inline.so
%{_libdir}/evolution/modules/module-webkit-editor.so
%{_libdir}/evolution/modules/module-webkit-inspector.so
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.addressbook.gschema.xml
%dir %{_libdir}/evolution/plugins
%{_libdir}/evolution/plugins/*-email-custom-header.*
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.email-custom-header.gschema.xml
%{_libdir}/evolution/plugins/*-evolution-attachment-reminder.*
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.attachment-reminder.gschema.xml
%{_libdir}/evolution/plugins/*-evolution-bbdb.*
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.autocontacts.gschema.xml
%{_libdir}/evolution/plugins/*-gnome-dbx-import.*
%{_libdir}/evolution/plugins/*-gnome-face.*
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.face-picture.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.publish-calendar.gschema.xml
%{_libdir}/evolution/plugins/liborg-gnome-external-editor.so
%{_libdir}/evolution/plugins/org-gnome-external-editor.eplug
%{_libdir}/evolution/plugins/*-mailing-list-actions.*
%{_libdir}/evolution/plugins/*-mail-notification.*
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.mail-notification.gschema.xml
%{_libdir}/evolution/plugins/*-mail-to-task.*
%{_libdir}/evolution/plugins/*-prefer-plain.*
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.prefer-plain.gschema.xml
%{_libdir}/evolution/plugins/*-publish-calendar.*
%{_libdir}/evolution/plugins/liborg-gnome-evolution-sender-validation.so
%{_libdir}/evolution/plugins/org-gnome-evolution-sender-validation.eplug
%{_libdir}/evolution/plugins/*-save-calendar.*
%{_libdir}/evolution/plugins/*-templates.*
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.templates.gschema.xml
%dir %{_libexecdir}/evolution
%{_libexecdir}/evolution/evolution-backup
%{_libexecdir}/evolution/killev
%dir %{_libdir}/evolution/web-extensions
%{_libdir}/evolution/web-extensions/libewebextension.so
%dir %{_libdir}/evolution/web-extensions/webkit-editor
%{_libdir}/evolution/web-extensions/webkit-editor/module-webkit-editor-webextension.so
%dir %{_libdir}/evolution-data-server/ui-modules
%{_libdir}/evolution-data-server/ui-modules/module-evolution-alarm-notify.so
%{_libdir}/evolution-data-server/camel-providers/libcamelrss.so
%{_libdir}/evolution-data-server/camel-providers/libcamelrss.urls
%{_libdir}/evolution/modules/module-rss.so

%files -n glade-catalog-evolution
%{_libdir}/glade/modules/libgladeevolution.so
%{_datadir}/glade/catalogs/evolution.xml

%files -n evolution-plugin-bogofilter
%{_datadir}/metainfo/org.gnome.Evolution-bogofilter.metainfo.xml
%{_libdir}/evolution/modules/module-bogofilter.so

%files -n evolution-plugin-spamassassin
%{_datadir}/metainfo/org.gnome.Evolution-spamassassin.metainfo.xml
%{_libdir}/evolution/modules/module-spamassassin.so

%files -n evolution-plugin-pst-import
%{_libdir}/evolution/plugins/*-pst-import.*
%{_datadir}/metainfo/org.gnome.Evolution-pst.metainfo.xml

%files -n evolution-plugin-text-highlight
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.text-highlight.gschema.xml
%{_libdir}/evolution/modules/module-text-highlight.so

%files devel
%doc ChangeLog HACKING MAINTAINERS NEWS-1.0
%doc %{_datadir}/gtk-doc/html/evolution-*/
%{_includedir}/evolution*
%{_libdir}/pkgconfig/evolution-calendar-3.0.pc
%{_libdir}/pkgconfig/evolution-mail-3.0.pc
%{_libdir}/pkgconfig/evolution-shell-3.0.pc
%{_libdir}/pkgconfig/libemail-engine.pc

%files lang -f evolution.lang

%changelog
