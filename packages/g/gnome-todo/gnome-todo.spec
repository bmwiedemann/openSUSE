#
# spec file for package gnome-todo
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Bjørn Lie, Bryne, Norway.
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


Name:           gnome-todo
Version:        3.28.1
Release:        0
Summary:        Personal task manager for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://wiki.gnome.org/Apps/Todo
Source0:        http://download.gnome.org/sources/gnome-todo/3.28/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-todo-autoptr-fix.patch -- Fix build with new glib
Patch0:         gnome-todo-autoptr-fix.patch

BuildRequires:  gobject-introspection-devel >= 1.42.0
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0) >= 2.43.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.43.4
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(goa-1.0) >= 3.2.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libecal-1.2) >= 3.13.90
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.17.1
BuildRequires:  pkgconfig(libedataserverui-1.2) >= 3.17.1
BuildRequires:  pkgconfig(libical) >= 0.43
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.17
BuildRequires:  pkgconfig(rest-0.7)
Recommends:     %{name}-lang

%description
GNOME To Do is a application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%package -n typelib-1_0-Gtd-1_0
Summary:        Introspection bindings for gnome-todo's library
Group:          System/Libraries

%description -n typelib-1_0-Gtd-1_0
GNOME To Do is a application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%package devel
Summary:        Development files for the GNOME task manager
Group:          Development/Languages/C and C++

%description devel
GNOME To Do is a application to manage your personal tasks. It
uses GNOME technologies, and so it has complete integration with the
GNOME desktop environment.

%lang_package

%prep
%autosetup -p1

%build
%meson \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -r org.gnome.Todo Office ProjectManagement
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.gnome.Todo.appdata.xml
%{_datadir}/applications/org.gnome.Todo.desktop
%{_datadir}/dbus-1/services/org.gnome.Todo.service
%{_datadir}/glib-2.0/schemas/org.gnome.todo.enums.xml
%{_datadir}/glib-2.0/schemas/org.gnome.todo.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.todo.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.todo.txt.gschema.xml
%dir %{_datadir}/%{name}
%{_datadir}/gnome-todo/org.gnome.Todo.Autostart.desktop
%{_datadir}/icons/hicolor/*/apps/org.gnome.Todo*
%{_libdir}/gnome-todo/

%files -n typelib-1_0-Gtd-1_0
%{_libdir}/girepository-1.0/Gtd-1.0.typelib

%files devel
%doc CONTRIBUTING.md HACKING.md README.md
%doc %{_datadir}/gtk-doc/html/gnome-todo/
%{_datadir}/gir-1.0/Gtd-1.0.gir
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/gnome-todo.pc

%files lang -f %{name}.lang

%changelog
