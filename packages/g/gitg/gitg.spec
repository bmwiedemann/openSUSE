#
# spec file for package gitg
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gitg
Version:        3.32.1
Release:        0
Summary:        Git repository viewer
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
URL:            https://wiki.gnome.org/Apps/Gitg
Source0:        https://download.gnome.org/sources/gitg/3.32/%{name}-%{version}.tar.xz

# PATCH-FIX-OPENSUSE gitg-typelib-dependencies.patch dimstar@opensuse.org -- Change the way we add library dependencies to .typelibs. openSUSE requires a full library name, incl. version
Patch0:         gitg-typelib-dependencies.patch
# PATCH-FIX-UPSTREAM gitg-port-to-gtksourceview4.patch -- Port to gtksourceview4
Patch1:         gitg-port-to-gtksourceview4.patch

BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gladeui-2.0) >= 3.2
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.10.1
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(gtksourceview-4) >= 4.0.3
BuildRequires:  pkgconfig(gtkspell3-3.0) >= 3.0.3
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libdazzle-1.0)
BuildRequires:  pkgconfig(libgit2-glib-1.0) >= 0.27.7
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.5.0
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.5.0
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.0.0
#BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.2
# Those dependencies cannot (yet) be auto-detected, as they are actually compiled inside a binary...
# ./gitg-3.16.1/gitg/gitg-plugins-engine.vala:			repo.require("Peas", "1.0", 0);
Requires:       typelib-1_0-Peas-1_0
# ./gitg-3.16.1/gitg/gitg-plugins-engine.vala:			repo.require("PeasGtk", "1.0", 0);
Requires:       typelib-1_0-PeasGtk-1_0
Recommends:     %{name}-lang

%description
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%package -n libgitg-1_0-0
Summary:        Git repository viewer -- Library
Group:          System/Libraries

%description -n libgitg-1_0-0
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%package -n libgitg-ext-1_0-0
Summary:        Git repository viewer -- Library
Group:          System/Libraries

%description -n libgitg-ext-1_0-0
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%package -n typelib-1_0-Gitg-1_0
Summary:        Git repository viewer -- Library
Group:          System/Libraries

%description -n typelib-1_0-Gitg-1_0
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%package -n typelib-1_0-GitgExt-1_0
Summary:        Git repository viewer -- Library
Group:          System/Libraries

%description -n typelib-1_0-GitgExt-1_0
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%package -n glade-catalog-gitg
Summary:        Git repository viewer -- Catalog for Glade
Group:          Development/Tools/GUI Builders
Requires:       glade
Requires:       libgitg-1_0-0 = %{version}
Supplements:    packageand(glade:%{name}-devel)

%description -n glade-catalog-gitg
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

This package provides a catalog for Glade, to allow the use the gitg
widgets in Glade.

%package -n libgitg-devel
Summary:        Git repository viewer -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libgitg-1_0-0 = %{version}
Requires:       libgitg-ext-1_0-0 = %{version}
Requires:       python3-GitgExt = %{version}
Requires:       typelib-1_0-Gitg-1_0 = %{version}
Requires:       typelib-1_0-GitgExt-1_0 = %{version}

%description -n libgitg-devel
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%package -n python3-GitgExt
Summary:        Git repository viewer -- Python bindings
Group:          Development/Libraries/GNOME

%description -n python3-GitgExt
gitg is a GitX clone for GNOME/gtk+. It aims at being a small, fast and
convenient tool to visualize git history and actions that benefit from a
graphical presentation.

%lang_package

%prep
%autosetup -p1
sed -i 's/\[.*\]//g' po/POTFILES.in 
translation-update-upstream po gitg

%build
%meson \
	-Dglade_catalog=true \
	-Dpython=true \
	-Ddeprecations=false \
	-Ddocs=false \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -G "Git repository viewer" org.gnome.gitg RevisionControl
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%post -n libgitg-1_0-0 -p /sbin/ldconfig
%postun -n libgitg-1_0-0 -p /sbin/ldconfig
%post -n libgitg-ext-1_0-0 -p /sbin/ldconfig
%postun -n libgitg-ext-1_0-0 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README.md NEWS
%{_bindir}/gitg
%{_datadir}/metainfo/org.gnome.gitg.appdata.xml
%{_datadir}/gitg/
%{_datadir}/applications/org.gnome.gitg.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gitg.gschema.xml
%{_datadir}/icons/hicolor/
%{_libdir}/gitg/
%{_mandir}/man1/gitg.1%{?ext_man}

%files -n libgitg-1_0-0
%{_libdir}/libgitg-1.0.so.*

%files -n libgitg-ext-1_0-0
%{_libdir}/libgitg-ext-1.0.so.*

%files -n glade-catalog-gitg
%{_datadir}/glade/catalogs/gitg-glade.xml

%files -n typelib-1_0-Gitg-1_0
%{_libdir}/girepository-1.0/Gitg-1.0.typelib

%files -n typelib-1_0-GitgExt-1_0
%{_libdir}/girepository-1.0/GitgExt-1.0.typelib

%files -n libgitg-devel
%{_datadir}/gir-1.0/Gitg-1.0.gir
%{_datadir}/gir-1.0/GitgExt-1.0.gir
%{_datadir}/vala/vapi/libgitg-1.0.vapi
%{_datadir}/vala/vapi/libgitg-ext-1.0.vapi
%{_includedir}/libgitg-1.0/
%{_includedir}/libgitg-ext-1.0/
%{_libdir}/libgitg-1.0.so
%{_libdir}/libgitg-ext-1.0.so
%{_libdir}/pkgconfig/libgitg-1.0.pc
%{_libdir}/pkgconfig/libgitg-ext-1.0.pc

%files -n python3-GitgExt
%{python3_sitelib}/gi/

%files lang -f %{name}.lang

%changelog
