#
# spec file for package deja-dup
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        49.3
Release:        0
Summary:        Simple backup tool and frontend for duplicity
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
URL:            https://wiki.gnome.org/Apps/DejaDup
Source0:        %{name}-%{version}.tar.zst
#PATCH-FIX-OPENSUSE deja-dup-49.2-loosen_pkit_filters.patch boo#1212486
Patch0:         deja-dup-49.2-loosen_pkit_filters.patch
BuildRequires:  appstream-glib
BuildRequires:  blueprint-compiler
BuildRequires:  dbus-1
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  glib2-tools
BuildRequires:  meson >= 1.1
BuildRequires:  pkgconfig
BuildRequires:  restic
BuildRequires:  vala >= 0.16.0
BuildRequires:  xdg-user-dirs
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.80
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gtk4) >= 4.18
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1) >= 1.8
BuildRequires:  pkgconfig(libnotify) >= 0.7
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(packagekit-glib2) >= 1.2
Requires:       duplicity >= 0.8.21
Requires:       python3-oauthlib
Recommends:     restic
Obsoletes:      nautilus-deja-dup <= 42.4

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
%meson \
	-D enable_restic=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
%ifarch x86_64
%meson_test
%endif

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
%{_libexecdir}/deja-dup/deja-dup-find-fusermount
%{_libexecdir}/deja-dup/fusermount
%{_libexecdir}/deja-dup/fusermount3
%{_datadir}/applications/org.gnome.DejaDup.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.DejaDup.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.DejaDup*
%dir %{_libdir}/deja-dup
%{_libdir}/deja-dup/libdeja.so
%{_datadir}/metainfo/org.gnome.DejaDup.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.DejaDup.service

%files lang -f %{name}.lang

%changelog
