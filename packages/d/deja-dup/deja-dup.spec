#
# spec file for package deja-dup
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


Name:           deja-dup
Version:        42.7
Release:        0
Summary:        Simple backup tool and frontend for duplicity
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
URL:            https://wiki.gnome.org/Apps/DejaDup
Source0:        https://gitlab.gnome.org/World/deja-dup/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  appstream-glib
BuildRequires:  cmake
BuildRequires:  dbus-1
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  glib2-tools
BuildRequires:  libgpg-error-devel
BuildRequires:  libhandy-devel
BuildRequires:  meson >= 0.47
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.16.0
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.46
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.64.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(packagekit-glib2) >= 0.6.5
Recommends:     duplicity >= 0.6.25

%description
Déjà  Dup is a simple backup tool. It hides the complexity of doing
backups the 'right way' (encrypted, off-site, and regular) and uses
duplicity as the backend.

Features:
 * Support for local or remote backup locations, including Amazon S3
 * Securely encrypts and compresses your data
 * Incrementally backs up, letting you restore from any particular backup
 * Schedules regular backups
 * Integrates well into your GNOME desktop

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
%meson_test

%files
%license LICENSES/GPL-3.0-or-later.md
%doc NEWS.md README.md CONTRIBUTING.md
%doc %{_datadir}/help/C/deja-dup/
%{_bindir}/deja-dup
%{_mandir}/man1/deja-dup.1%{?ext_man}
%{_sysconfdir}/xdg/autostart/org.gnome.DejaDup.Monitor.desktop
# We explicitly list the content of %%{_libexecdir}/deja-dup to make sure we
# put the files in the right subpackage
%dir %{_libexecdir}/deja-dup
%{_libexecdir}/deja-dup/deja-dup-monitor
%{_datadir}/applications/org.gnome.DejaDup.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.DejaDup.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.DejaDup*
%dir %{_libdir}/deja-dup
%{_libdir}/deja-dup/libdeja.so
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.DejaDup.appdata.xml
%{_datadir}/dbus-1/services/org.gnome.DejaDup.service

%files lang -f %{name}.lang

%changelog
