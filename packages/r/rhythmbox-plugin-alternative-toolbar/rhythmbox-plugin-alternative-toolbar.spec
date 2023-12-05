#
# spec file for package rhythmbox-plugin-alternative-toolbar
#
# Copyright (c) 2023 SUSE LLC
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


# Exclude auto generated unversioned Requires symbols in order to manually
# require the right version.
%define __requires_exclude typelib\\((GLib|GObject|G[dt]k|Gio|Gtk|Pango)\\)
%define glib_version 2.0
%define gtk_version  3.0
%define peas_version 1.0

Name:           rhythmbox-plugin-alternative-toolbar
Version:        0.20.4
Release:        0
Summary:        Modern, minimal and music-focused interface for Rhythmbox
License:        GPL-3.0-only
URL:            https://github.com/fossfreedom/alternative-toolbar
Source:         alternative-toolbar-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool
BuildRequires:  python3-gobject
BuildRequires:  typelib(GLib) = %{glib_version}
BuildRequires:  typelib(GObject) = %{glib_version}
BuildRequires:  typelib(Gdk) = %{gtk_version}
BuildRequires:  typelib(Gio) = %{glib_version}
BuildRequires:  typelib(Gtk) = %{gtk_version}
BuildRequires:  typelib(Pango) = 1.0
BuildRequires:  typelib(Peas) = %{peas_version}
BuildRequires:  typelib(PeasGtk) = %{peas_version}
BuildRequires:  typelib(RB) = 3.0

# Manually require the right version (see __requires_exclude definition above).
Requires:       typelib(GLib) = %{glib_version}
Requires:       typelib(GObject) = %{glib_version}
Requires:       typelib(Gdk) = %{gtk_version}
Requires:       typelib(Gio) = %{glib_version}
Requires:       typelib(Gtk) = %{gtk_version}
Requires:       typelib(Pango) = 1.0

%description
Alternative Toolbar replaces the Rhythmbox large toolbar with a Client-Side
Decorated or Compact toolbar which can be hidden.

%lang_package

%prep
%autosetup -n alternative-toolbar-%{version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%find_lang alternative-toolbar

%files
%license LICENSE
%doc GENERAL README.md TRANSLATE_README DISTRO_PACKAGING readme.html
%dir %{_libdir}/rhythmbox/plugins/alternative-toolbar
%{_libdir}/rhythmbox/plugins/alternative-toolbar
%dir %{_datadir}/rhythmbox/plugins/alternative-toolbar
%{_datadir}/rhythmbox/plugins/alternative-toolbar/*
%{_datadir}/glib-2.0/schemas/org.gnome.rhythmbox.plugins.alternative_toolbar.gschema.xml
%{_datadir}/metainfo/org.gnome.rhythmbox.alternative-toolbar.addon.appdata.xml

%files lang -f alternative-toolbar.lang

%changelog
