#
# spec file for package gplugin
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


%define         sover 0
Name:           gplugin
Version:        0.44.2
Release:        0
Summary:        GObject based library that implements a reusable plugin system
License:        LGPL-2.0-or-later
URL:            https://keep.imfreedom.org/gplugin/gplugin
Source0:        https://sourceforge.net/projects/pidgin/files/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1:        https://sourceforge.net/projects/pidgin/files/%{name}/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x40de1dc7288fe3f50ab938c548f66affd9bdb729#/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  lua-lgi
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-gi-docgen >= 2021.1
BuildRequires:  python3-gobject
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.76
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3)

%description
GPlugin is a GObject based library that implements a reusable plugin system.
It supports loading plugins in multiple other languages via loaders.  It relies
heavily on [GObjectIntrospection](https://gi.readthedocs.io/) to expose its API
to the other languages.

It has a simple API which makes it very easy to use in your application.
For more information on using GPlugin in your application, please see the
[embedding](https://docs.pidgin.im/gplugin/latest/chapter-embedding.html) page.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       lib%{name}%{sover} = %{version}
Requires:       lib%{name}-gtk4-%{sover} = %{version}
Requires:       typelib-1_0-GPlugin-1_0 = %{version}
Requires:       typelib-1_0-GPluginGtk4-1_0 = %{version}

%description devel
%{summary}.

%package -n lib%{name}%{sover}
Summary:        Library of %{name}

%description -n lib%{name}%{sover}
%{summary}.

%package -n typelib-1_0-GPlugin-1_0
Summary:        Typelib for %{name}

%description -n typelib-1_0-GPlugin-1_0
%{summary}.

%package -n typelib-1_0-GPluginGtk4-1_0
Summary:        Gtk4 Typelib for %{name}

%description -n typelib-1_0-GPluginGtk4-1_0
%{summary}.

%package -n lib%{name}-gtk4-%{sover}
Summary:        Gtk4 libs for %{name}

%description -n lib%{name}-gtk4-%{sover}
%{summary}.

%prep
%autosetup

%build
%meson \
  -Ddoc=true \
  -Dgplugin-introspection=false \
  -Dintrospection=true \
  -Dgtk4=enabled \
  -Dhelp2man=true \
  -Dinstall-gplugin-gtk4-viewer=true \
  -Dinstall-gplugin-query=true \
  -Dlua=true \
  -Dnls=true \
  -Dpython3=true \
  -Dvapi=true
%meson_build

%install
%meson_install
%fdupes %{buildroot}

%check
%meson_test

%ldconfig_scriptlets -n lib%{name}%{sover}
%ldconfig_scriptlets -n lib%{name}-gtk4-%{sover}

%files
%license COPYING
%doc README.md COPYRIGHT ChangeLog HACKING.md HISTORY.md
%{_bindir}/%{name}-gtk4-viewer
%{_bindir}/%{name}-query
%{_datadir}/%{name}
%{_mandir}/man?/%{name}-gtk4-viewer.?%{ext_man}
%{_mandir}/man?/%{name}-query.?%{ext_man}

%files devel
%{_includedir}/%{name}-1.0
%{_includedir}/%{name}-gtk4-1.0
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-gtk4.so
%{_libdir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-gtk4.pc
%{_datadir}/gir-1.0/GPlugin-1.0.gir
%{_datadir}/gir-1.0/GPluginGtk4-1.0.gir
%dir %{_datadir}/{vala,vala/vapi}
%{_datadir}/vala/vapi/%{name}.{deps,vapi}
%{_datadir}/vala/vapi/%{name}-gtk4.{deps,vapi}

%files doc
%{_datadir}/doc/%{name}
%{_datadir}/doc/%{name}-gtk4

%files -n typelib-1_0-GPlugin-1_0
%{_libdir}/girepository-1.0/GPlugin-1.0.typelib

%files -n typelib-1_0-GPluginGtk4-1_0
%{_libdir}/girepository-1.0/GPluginGtk4-1.0.typelib

%files -n lib%{name}%{sover}
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-gtk4-%{sover}
%{_libdir}/lib%{name}-gtk4.so.*

%changelog
