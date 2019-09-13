#
# spec file for package something-for-reddit
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global gobject_introspection_version 1.35.9
%global gtk3_version 3.13.2
%global soup_version 2.4
Name:           something-for-reddit
Version:        0.2
Release:        0
Summary:        Browse Reddit from GNOME
License:        GPL-3.0+
Url:            https://github.com/samdroid-apps/something-for-reddit
Source:         https://github.com/samdroid-apps/something-for-reddit/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/samdroid-apps/something-for-reddit/pull/44
Patch0:         desktop.patch
BuildRequires:  desktop-file-utils
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  python3-arrow
BuildRequires:  python3-devel
BuildRequires:  python3-Markdown
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= %{gobject_introspection_version}
BuildRequires:  pkgconfig(gtk+-3.0) >= %{gtk3_version}
BuildRequires:  pkgconfig(libsoup-2.4) >= %{soup_version}
BuildRequires:  update-desktop-files
BuildRequires:  rubygem(sass)
BuildRequires:  fdupes
Requires:       python3-arrow
Requires:       python3-gobject-Gdk
Requires:       python3-Markdown
BuildArch:      noarch
%glib2_gsettings_schema_requires

%description
This is a Reddit client, built with Gtk+ and optimized for GNOME.

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{python3_sitelib}/redditisgtk/Makefile # drop arch-specific file to make it a noarch package
%fdupes %{buildroot}%{_prefix}

%post
%desktop_database_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%glib2_gsettings_schema_postun

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/reddit-is-gtk
%{_datadir}/%{name}
%{_datadir}/pixmaps/*
%dir %{_datadir}/appdata/
%{_datadir}/appdata/reddit-is-gtk.appdata.xml
%{_datadir}/glib-2.0/schemas/today.sam.something-for-reddit.gschema.xml
%{_datadir}/applications/reddit-is-gtk.desktop
%{python3_sitelib}/redditisgtk

%changelog
