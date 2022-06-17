#
# spec file for package ghex
#
# Copyright (c) 2022 SUSE LLC
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


%define so_ver 4

Name:           ghex
Version:        42.3
Release:        0
Summary:        GNOME Binary Editor
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Ghex
Source:         https://download.gnome.org/sources/ghex/42/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(atk) >= 1.0.0
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gio-2.0) >= 2.31.10
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)

%description
GHex allows the user to load data from any file and to view and edit it
in either hex or ASCII. It is a must for anyone playing games that use
a non-ASCII format for saving.

%package -n libgtkhex-%{so_ver}-0
Summary:        GNOME Binary Editor -- Library
Group:          System/Libraries

%description -n libgtkhex-%{so_ver}-0
GHex allows the user to load data from any file and to view and edit it
in either hex or ASCII. It is a must for anyone playing games that use
a non-ASCII format for saving.

%package devel
Summary:        GNOME Binary Editor -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libgtkhex-%{so_ver}-0 = %{version}

%description devel
GHex allows the user to load data from any file and to view and edit it
in either hex or ASCII. It is a must for anyone playing games that use
a non-ASCII format for saving.

%package -n typelib-1_0-Hex-%{so_ver}
Summary:        Introspection bindings for ghex
Group:          System/Libraries

%description -n typelib-1_0-Hex-%{so_ver}
This package provides introspection bindings for ghex.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%suse_update_desktop_file -r org.gnome.GHex GNOME Utility Editor
%find_lang %{name} ghex-%{so_ver}.0.lang %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}

%ldconfig_scriptlets -n libgtkhex-%{so_ver}-0

%files
%license COPYING
%doc README.md COPYING-DOCS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/ghex
%{_datadir}/metainfo/org.gnome.GHex.appdata.xml
%{_datadir}/applications/org.gnome.GHex.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.GHex*

%files -n libgtkhex-%{so_ver}-0
%dir %{_libdir}/gtkhex-4.0
%{_libdir}/libgtkhex-%{so_ver}.so.*
%{_libdir}/gtkhex-4.0/*.so

%files -n typelib-1_0-Hex-%{so_ver}
%{_libdir}/girepository-1.0/Hex-%{so_ver}.typelib

%files devel
%{_includedir}/gtkhex-%{so_ver}/
%{_libdir}/libgtkhex-%{so_ver}.so
%{_libdir}/pkgconfig/gtkhex-%{so_ver}.pc
%{_datadir}/gir-1.0/Hex-%{so_ver}.gir

%files lang -f %{name}-%{so_ver}.0.lang

%changelog
