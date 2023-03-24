#
# spec file for package ghex
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


%define ghex_abi   4
%define so_ver     1
%define so_ver_ext 0
%define soname libgtkhex-%{ghex_abi}-%{so_ver}

Name:           ghex
Version:        44.rc
Release:        0
Summary:        GNOME Binary Editor
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://wiki.gnome.org/Apps/Ghex
Source:         https://download.gnome.org/sources/ghex/44/%{name}-%{version}.tar.xz

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
BuildRequires:  pkgconfig(libadwaita-1)
# Obsoletes libgtkhex-4-0 can be dropped when SLED/Leap 15.5 is out of support
Obsoletes:      libgtkhex-4-0 < %{version}

%description
GHex allows the user to load data from any file and to view and edit it
in either hex or ASCII. It is a must for anyone playing games that use
a non-ASCII format for saving.

%package -n %{soname}
Summary:        GNOME Binary Editor -- Library
Group:          System/Libraries

%description -n %{soname}
GHex allows the user to load data from any file and to view and edit it
in either hex or ASCII. It is a must for anyone playing games that use
a non-ASCII format for saving.

%package devel
Summary:        GNOME Binary Editor -- Development Files
Group:          Development/Libraries/GNOME
Requires:       %{soname} = %{version}

%description devel
GHex allows the user to load data from any file and to view and edit it
in either hex or ASCII. It is a must for anyone playing games that use
a non-ASCII format for saving.

%package -n typelib-1_0-Hex-%{ghex_abi}
Summary:        Introspection bindings for ghex
Group:          System/Libraries

%description -n typelib-1_0-Hex-%{ghex_abi}
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
%find_lang %{name} ghex-%{ghex_abi}-%{so_ver}.%{so_ver_ext}.lang %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}

%ldconfig_scriptlets -n %{soname}

%files
%license COPYING
%doc README.md COPYING-DOCS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/ghex
%{_datadir}/metainfo/org.gnome.GHex.appdata.xml
%{_datadir}/applications/org.gnome.GHex.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.GHex*
# Not split out as they are private to ghex
%dir %{_libdir}/gtkhex-%{ghex_abi}.%{so_ver_ext}
%{_libdir}/gtkhex-%{ghex_abi}.%{so_ver_ext}/*.so

%files -n %{soname}
%{_libdir}/libgtkhex-%{ghex_abi}.so.*

%files -n typelib-1_0-Hex-%{ghex_abi}
%{_libdir}/girepository-1.0/Hex-%{ghex_abi}.typelib

%files devel
%{_includedir}/gtkhex-%{ghex_abi}/
%{_libdir}/libgtkhex-%{ghex_abi}.so
%{_libdir}/pkgconfig/gtkhex-%{ghex_abi}.pc
%{_datadir}/gir-1.0/Hex-%{ghex_abi}.gir

%files lang -f %{name}-%{ghex_abi}-%{so_ver}.%{so_ver_ext}.lang

%changelog
