#
# spec file for package something-for-reddit
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


%global gobject_introspection_version 1.35.9
%global gtk3_version 3.13.2
%global soup_version 2.4
Name:           something-for-reddit
Version:        0.2.2
Release:        0
Summary:        Browse Reddit from GNOME
License:        GPL-3.0-or-later
URL:            https://github.com/samdroid-apps/something-for-reddit
Source:         %{url}/archive/v%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  python3-Markdown
BuildRequires:  python3-arrow
BuildRequires:  python3-devel
BuildRequires:  sassc
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(libsoup-2.4) >= %{soup_version}
Requires:       python3-Markdown
Requires:       python3-arrow
Requires:       python3-gobject-Gdk
BuildArch:      noarch
%glib2_gsettings_schema_requires

%description
This is a Reddit client, built with Gtk+ and optimized for GNOME.

%prep
%autosetup -p1
sed -i -e "1s|#!.*|#!/usr/bin/python3|" reddit-is-gtk.in

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build

%install
%make_install
rm %{buildroot}%{python3_sitelib}/redditisgtk/Makefile # drop arch-specific file to make it a noarch package
%fdupes %{buildroot}%{_prefix}

%files
%license COPYING
%{_bindir}/reddit-is-gtk
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/
%{_datadir}/metainfo/reddit-is-gtk.appdata.xml
%dir %{_datadir}/appdata
%{_datadir}/appdata/reddit-is-gtk.appdata.xml
%{_datadir}/glib-2.0/schemas/today.sam.something-for-reddit.gschema.xml
%{_datadir}/applications/reddit-is-gtk.desktop
%{python3_sitelib}/redditisgtk

%changelog
