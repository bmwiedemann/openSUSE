#
# spec file for package gnome-todo
#
# Copyright (c) 2022 SUSE LLC
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
Version:        41.0+72
Release:        0
Summary:        Personal task manager for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Text/Editors
URL:            https://wiki.gnome.org/Apps/Todo
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM e128140d08c1faadc21ba42b81eefd451092f162.patch -- Do not build doc for flatpak builds
Patch0:         https://gitlab.gnome.org/GNOME/gnome-todo/-/commit/e128140d08c1faadc21ba42b81eefd451092f162.patch
# PATCH-FIX-UPSTREAM 3e1f4da8c0e536c09ffaf3b43fe2eb5dc17cc23e.patch -- Adjust to libportal changes
Patch1:         https://gitlab.gnome.org/GNOME/gnome-todo/-/commit/3e1f4da8c0e536c09ffaf3b43fe2eb5dc17cc23e.patch

BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-2.0) >= 2.43.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.58.0
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(goa-1.0) >= 3.2.0
BuildRequires:  pkgconfig(gtk4) >= 3.92.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.92
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.17.1
BuildRequires:  pkgconfig(libedataserverui-1.2) >= 3.17.1
BuildRequires:  pkgconfig(libical) >= 3.0.5
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.17
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(rest-0.7)

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
%setup
%patch0 -R -p1
%patch1 -R -p1

%build
# NOTE: We are not building introspection support as that introduces a dep on a private lib, last checked ver 41.0
%meson \
	-Dintrospection=false \
	%{nil}
%meson_build

%install
%meson_install
%suse_update_desktop_file -r org.gnome.Todo Office ProjectManagement
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Todo.desktop
%{_datadir}/dbus-1/services/org.gnome.Todo.service
%{_datadir}/glib-2.0/schemas/org.gnome.todo.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.todo.gschema.xml
%{_datadir}/help/C/%{name}/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Todo*
%{_datadir}/icons/hicolor/symbolic/actions/
%{_datadir}/metainfo/org.gnome.Todo.appdata.xml

%files devel
%doc doc/CONTRIBUTING.md doc/HACKING.md README.md
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/gnome-todo.pc

%files lang -f %{name}.lang

%changelog
