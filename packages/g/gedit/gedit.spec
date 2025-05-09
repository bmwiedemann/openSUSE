#
# spec file for package gedit
#
# Copyright (c) 2025 SUSE LLC
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


%define api_ver 48.2

Name:           gedit
Version:        48.2
Release:        0
Summary:        UTF-8 text editor
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            https://gedit-text-editor.org
Source0:        %{name}-%{version}.tar.zst
# PATCH-FIX-OPENSUSE gedit-desktop.patch -- Adds more MIME types.
Patch0:         gedit-desktop.patch

BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel >= 0.9.3
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  iso-codes-devel
BuildRequires:  meson >= 0.53
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gio-2.0) >= 2.76
BuildRequires:  pkgconfig(glib-2.0) >= 2.64
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gspell-1) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libgedit-amtk-5)
BuildRequires:  pkgconfig(libgedit-gtksourceview-300)
BuildRequires:  pkgconfig(libgedit-tepl-6) >= 6.11
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.14.1
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.14.1
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0
BuildRequires:  pkgconfig(vapigen) >= 0.25.1
BuildRequires:  pkgconfig(x11)
Recommends:     iso-codes
Provides:       gedit2 = %{version}
Obsoletes:      gedit2 < %{version}
# Throws "Settings schema 'org.gnome.desktop.interface' is not installed"
#   in WSLg without this; see boo#1198312
Requires:       gsettings-desktop-schemas
Obsoletes:      python3-gedit < 48.2

%description
Gedit is a UTF-8 text editor for the GNOME environment.

It features a multi-document frame, syntax highlighting, autoindent
options, autosave, and plugins.

%package devel
Summary:        Development files for the gedit text editor
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Provides:       gedit2-devel = %{version}
Obsoletes:      gedit2-devel < %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description devel
Gedit is a UTF-8 text editor for the GNOME
environment.

This subpackage contains the header files for creating gedit plugins.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-D gtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_prefix}

%files
%license COPYING
%doc NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gedit
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.gedit.service
# %%{_datadir}/gedit/gir-1.0/ lives in -devel
%exclude %{_datadir}/gedit/gir-1.0/
%{_datadir}/gedit/
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.filebrowser.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.spell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.time.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.time.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/metainfo/org.gnome.gedit.metainfo.xml
%dir %{_libdir}/gedit/
%{_libdir}/gedit/libgedit-%{api_ver}.so
%{_libdir}/gedit/girepository-1.0/
%dir %{_libdir}/gedit/plugins/
# Explicitly list plugins so we know when we miss one
%{_libdir}/gedit/plugins/docinfo.plugin
%{_libdir}/gedit/plugins/libdocinfo.so
%{_libdir}/gedit/plugins/filebrowser.plugin
%{_libdir}/gedit/plugins/libfilebrowser.so
%{_libdir}/gedit/plugins/modelines.plugin
%{_libdir}/gedit/plugins/libmodelines.so
%{_libdir}/gedit/plugins/libtextsize.so
%{_libdir}/gedit/plugins/textsize.plugin
%{_libdir}/gedit/plugins/sort.plugin
%{_libdir}/gedit/plugins/libsort.so
%{_libdir}/gedit/plugins/spell.plugin
%{_libdir}/gedit/plugins/libspell.so
%{_libdir}/gedit/plugins/time.plugin
%{_libdir}/gedit/plugins/libtime.so
%{_libdir}/gedit/plugins/quickhighlight.plugin

%{_libdir}/gedit/plugins/libquickhighlight.so
%{_mandir}/man1/gedit.1%{?ext_man}

%files devel
%doc CONTRIBUTING.md
%doc %{_datadir}/gtk-doc/html/gedit/
%{_datadir}/gedit/gir-1.0/
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%files lang -f %{name}.lang

%changelog
