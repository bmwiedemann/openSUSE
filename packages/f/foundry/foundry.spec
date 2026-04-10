#
# spec file for package test
#
# Copyright (c) 2025 SUSE LLC and contributors
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

Name:           foundry
Version:        1.1.1
Release:        0
Summary:        IDE library and command-line companion tool
# foundry: LGPL-2.1-or-later and GPL-3.0-or-later
# bundled eggbitset / timsort: Apache-2.0
License:        LGPL-2.1-or-later AND GPL-3.0-or-later AND Apache-2.0
URL:            https://gitlab.gnome.org/GNOME/foundry
Source:         foundry-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gtk4) >= 4.20
BuildRequires:  pkgconfig(gtksourceview-5) >= 5.18
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(jsonrpc-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcmark)
BuildRequires:  pkgconfig(libdex-1) >= 1.1.alpha
BuildRequires:  pkgconfig(libgit2)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(libpeas-2)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(template-glib-1.0)
BuildRequires:  pkgconfig(vte-2.91-gtk4) >= 0.80
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(yaml-0.1)

%description
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.

%package -n libfoundry-1-1
Summary:        IDE library and command-line companion tool

%description -n libfoundry-1-1
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.

%package -n libfoundry-gtk-1-1
Summary:        IDE library and command-line companion tool

%description -n libfoundry-gtk-1-1
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.

%package -n typelib-1_0-Foundry-1
Summary:        IDE library and command-line companion tool

%description -n typelib-1_0-Foundry-1
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.

%package -n typelib-1_0-FoundryGtk-1
Summary:        IDE library and command-line companion tool

%description -n typelib-1_0-FoundryGtk-1
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.

%package        devel
Summary:        IDE library and command-line companion tool (development files)
Requires:       libfoundry-1-1 = %{version}
Requires:       libfoundry-gtk-1-1 = %{version}
Requires:       typelib-1_0-Foundry-1 = %{version}
Requires:       typelib-1_0-FoundryGtk-1 = %{version}

%description    devel
This tool aims to extract much of what makes GNOME Builder an IDE into a
library and companion command-line tool.

This package contains the development headers.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%ifnarch %{ix86} %{arm} s390x
%check
%meson_test
%endif

%files -f %{name}.lang
%doc README.md
%doc NEWS
%license COPYING
%{_bindir}/foundry
%{_datadir}/bash-completion/completions/foundry
%{_datadir}/foundry/
#%{_datadir}/glib-2.0/schemas/app.devsuite.foundry{,.*}.gschema.xml
%{_datadir}/metainfo/org.gnome.Foundry.metainfo.xml
%{_mandir}/man1/foundry.1%{?ext_man}
%{_datadir}/glib-2.0/schemas/org.gnome.foundry*.xml

%files -n libfoundry-1-1
%{_libdir}/libfoundry-1.so.1{,.0.0}

%files -n libfoundry-gtk-1-1
%{_libdir}/libfoundry-gtk-1.so.1{,.0.0}
%{_libdir}/libfoundry-adw-1.so.1{,.0.0}

%files -n typelib-1_0-Foundry-1
%{_libdir}/girepository-1.0/Foundry-1.typelib

%files -n typelib-1_0-FoundryGtk-1
%{_libdir}/girepository-1.0/FoundryAdw-1.typelib
%{_libdir}/girepository-1.0/FoundryGtk-1.typelib

%files devel
%{_datadir}/gir-1.0/Foundry{,Adw,Gtk}-1.gir
%{_includedir}/libfoundry-1/
%{_includedir}/libfoundry-gtk-1/
%{_includedir}/libfoundry-adw-1/
%dir %{_libdir}/libfoundry-1
%dir %{_libdir}/libfoundry-1/include
%{_libdir}/libfoundry-1/include/libfoundry-config.h
%{_libdir}/libfoundry{,-adw,-gtk}-1.so
%{_libdir}/pkgconfig/libfoundry{,-adw,-gtk}-1.pc

%changelog
