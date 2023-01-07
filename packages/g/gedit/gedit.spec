#
# spec file for package gedit
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


%bcond_without  python_bindings
%define api_ver 44

Name:           gedit
Version:        44.1
Release:        0
Summary:        UTF-8 text editor
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            https://wiki.gnome.org/Apps/Gedit
Source0:        https://download.gnome.org/sources/gedit/44/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE gedit-desktop.patch -- Adds more MIME types.
Patch0:         gedit-desktop.patch
# PATCH-FIX-OPENSUSE gedit-plugins-python-env.patch bjorn.lie@gmail.com -- Fix python env
Patch1:         gedit-plugins-python-env.patch

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel >= 0.9.3
BuildRequires:  gtk-doc
BuildRequires:  hicolor-icon-theme
BuildRequires:  iso-codes-devel
BuildRequires:  meson >= 0.53
BuildRequires:  pkgconfig
BuildRequires:  python3-base >= 3.2.3
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(amtk-5) >= 5.6
BuildRequires:  pkgconfig(gio-2.0) >= 2.64
BuildRequires:  pkgconfig(glib-2.0) >= 2.64
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gspell-1) >= 1.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.2
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.14.1
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.14.1
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0
BuildRequires:  pkgconfig(tepl-6) >= 6.4
BuildRequires:  pkgconfig(vapigen) >= 0.25.1
BuildRequires:  pkgconfig(x11)
Requires:       python3-cairo
Requires:       python3-gobject
#bnc#910913 - plugin snippets depend on this package
Requires:       python3-gobject-cairo
Recommends:     iso-codes
Provides:       gedit2 = %{version}
Obsoletes:      gedit2 < %{version}
%if %{with python_bindings}
# See bnc#847114 - plugins generally depend on it
Requires:       python3-gedit
%endif
# Throws "Settings schema 'org.gnome.desktop.interface' is not installed"
#   in WSLg without this; see boo#1198312
Requires:       gsettings-desktop-schemas

%description
Gedit is a UTF-8 text editor for the GNOME environment.

It features a multi-document frame, syntax highlighting, autoindent
options, autosave, and plugins.

%package -n python3-gedit
Summary:        Python bindings for gedit
Group:          Development/Languages/Python
BuildArch:      noarch

%description -n python3-gedit
Gedit is a UTF-8 text editor for the GNOME
environment.

This package provides the python bindings, based on gobject-introspection.

%package devel
Summary:        Development files for the gedit text editor
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gtksourceview-devel
Provides:       gedit2-devel = %{version}
Obsoletes:      gedit2-devel < %{version}
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}
%if %{with python_bindings}
Requires:       python3-gedit
%endif

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
%{_datadir}/metainfo/org.gnome.gedit.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/org.gnome.gedit.service
# %%{_datadir}/gedit/gir-1.0/ lives in -devel
%exclude %{_datadir}/gedit/gir-1.0/
%{_datadir}/gedit/
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.externaltools.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.filebrowser.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.filebrowser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.pythonconsole.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.spell.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.time.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.gedit.plugins.time.gschema.xml
%dir %{_libdir}/gedit/
%{_libdir}/gedit/libgedit-%{api_ver}.so
%{_libdir}/gedit/girepository-1.0/
%dir %{_libdir}/gedit/plugins/
# Explicitly list plugins so we know when we miss one
%{_libdir}/gedit/plugins/docinfo.plugin
%{_libdir}/gedit/plugins/libdocinfo.so
%{_libdir}/gedit/plugins/externaltools/
%{_libdir}/gedit/plugins/externaltools.plugin
%{_libdir}/gedit/plugins/filebrowser.plugin
%{_libdir}/gedit/plugins/libfilebrowser.so
%{_libdir}/gedit/plugins/modelines.plugin
%{_libdir}/gedit/plugins/libmodelines.so
%{_libdir}/gedit/plugins/pythonconsole/
%{_libdir}/gedit/plugins/pythonconsole.plugin
%{_libdir}/gedit/plugins/quickopen/
%{_libdir}/gedit/plugins/quickopen.plugin
%{_libdir}/gedit/plugins/snippets/
%{_libdir}/gedit/plugins/snippets.plugin
%{_libdir}/gedit/plugins/sort.plugin
%{_libdir}/gedit/plugins/libsort.so
%{_libdir}/gedit/plugins/spell.plugin
%{_libdir}/gedit/plugins/libspell.so
%{_libdir}/gedit/plugins/time.plugin
%{_libdir}/gedit/plugins/libtime.so
%{_libdir}/gedit/plugins/quickhighlight.plugin
%{_libdir}/gedit/plugins/libquickhighlight.so
%{_mandir}/man1/gedit.1%{?ext_man}
%{_datadir}/icons/hicolor/*/apps/*

%if %{with python_bindings}
%files -n python3-gedit
%{python3_sitelib}/gi/
%endif

%files devel
%doc CONTRIBUTING.md
%doc %{_datadir}/gtk-doc/html/gedit/
%{_datadir}/gedit/gir-1.0/
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/vapi/gedit.deps
%{_datadir}/vala/vapi/gedit.vapi

%files lang -f %{name}.lang

%changelog
