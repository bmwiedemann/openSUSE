#
# spec file for package endeavour
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2022 Bjørn Lie, Bryne, Norway.
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


Name:           endeavour
Version:        43.0
Release:        0
Summary:        Personal task manager for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/Endeavour
Source:         %{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  itstool
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.43.4
BuildRequires:  pkgconfig(glib-2.0) >= 2.58.0
BuildRequires:  pkgconfig(goa-1.0) >= 3.2.0
BuildRequires:  pkgconfig(gtk4) >= 3.92.0
BuildRequires:  pkgconfig(libadwaita-1) >= 1.2.alpha
BuildRequires:  pkgconfig(libecal-2.0) >= 3.33.2
BuildRequires:  pkgconfig(libedataserver-1.2) >= 3.32.0
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.17
BuildRequires:  pkgconfig(libportal-gtk4)
Obsoletes:      gnome-todo < %{version}
Provides:       gnome-todo = %{version}
Obsoletes:      gnome-todo-lang < %{version}

%description
A intuitive and powerful application to manage your personal tasks.
It uses GNOME technologies and has complete integration with the
GNOME desktop environment.

%package devel
Summary:        Development files for the GNOME task manager

%description devel
A intuitive and powerful application to manage your personal tasks.
It uses GNOME technologies and has complete integration with the
GNOME desktop environment.

This package contains the development files for %{name}.

%lang_package

%prep
%autosetup -p1

%build
# NOTE: We are not building introspection support as that
# introduces a dep on a private lib, last checked ver 43.0
%meson \
	-D introspection=false \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%check
%meson_test

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Todo.desktop
%{_datadir}/dbus-1/services/org.gnome.Todo.service
%{_datadir}/glib-2.0/schemas/org.gnome.todo.gschema.xml
%{_datadir}/help/C/%{name}/
%dir %{_datadir}/icons/hicolor/symbolic/actions
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/metainfo/org.gnome.Todo.appdata.xml

%files devel
%doc doc/CONTRIBUTING.md doc/HACKING.md README.md
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%files lang -f %{name}.lang

%changelog
