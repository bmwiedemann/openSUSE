#
# spec file for package gucharmap
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


%define api_version 2.90
%define so_api _2_90
%define so_gucharmap 7
%define pc_api 2.90
Name:           gucharmap
Version:        15.0.2
Release:        0
Summary:        A Featureful Unicode Character Map
License:        GPL-3.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Gucharmap
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  appdata-tools
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel >= 0.9.0
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel >= 3.4.0
BuildRequires:  intltool
BuildRequires:  meson >= 0.50.0
BuildRequires:  pkgconfig
BuildRequires:  unicode-ucd >= 14.0
BuildRequires:  unicode-ucd-unihan
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0) >= 2.32.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
Recommends:     %{name}-doc

%description
Gucharmap is a featureful unicode character map.

%package -n libgucharmap%{so_api}-%{so_gucharmap}
Summary:        A Featureful Unicode Character Map -- Library
Group:          System/GUI/GNOME

%description -n libgucharmap%{so_api}-%{so_gucharmap}
Gucharmap is a featureful unicode character map.

This package contains a library to use the character map.

%package -n typelib-1_0-Gucharmap-2_90
Summary:        A Featureful Unicode Character Map -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-Gucharmap-2_90
Gucharmap is a featureful unicode character map.

This package provides the GObject Introspection bindings for the
gucharmap library.

%package devel
Summary:        A Featureful Unicode Character Map -- Development Files
Group:          Development/Libraries/GNOME
Requires:       libgucharmap%{so_api}-%{so_gucharmap} = %{version}
Requires:       typelib-1_0-Gucharmap-2_90 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%lang_package

%prep
%autosetup -p1

%build
export LIBS="-ldl"
%meson \
    -Ducd_path=%{_datadir}/unicode/ucd \
    %{nil}
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
# We need X-SuSE-Editor to avoid an error for the categories check. We don't
# want TextEditor, since that's too wide.
%suse_update_desktop_file -N "GNOME Character Map" -G "Character Map" %{name} X-SuSE-Editor
%fdupes -s %{buildroot}%{_datadir}

%post -n libgucharmap%{so_api}-%{so_gucharmap} -p /sbin/ldconfig
%postun -n libgucharmap%{so_api}-%{so_gucharmap} -p /sbin/ldconfig

%files
%license COPYING COPYING.GFDL COPYING.UNICODE
%doc README.md
%{_bindir}/gucharmap
%{_datadir}/applications/gucharmap.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Charmap.gschema.xml
%doc %{_datadir}/help/C/gucharmap/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/gucharmap.metainfo.xml

%files -n libgucharmap%{so_api}-%{so_gucharmap}
%{_libdir}/libgucharmap%{so_api}.so.%{so_gucharmap}*

%files -n typelib-1_0-Gucharmap-2_90
%{_libdir}/girepository-1.0/Gucharmap-2.90.typelib

%files lang -f %{name}.lang

%files devel
%{_includedir}/gucharmap-%{pc_api}/
%{_libdir}/libgucharmap%{so_api}.so
%{_libdir}/pkgconfig/gucharmap-%{pc_api}.pc
%{_datadir}/gir-1.0/Gucharmap-%{pc_api}.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gucharmap-2.90.deps
%{_datadir}/vala/vapi/gucharmap-2.90.vapi
%doc %{_datadir}/gtk-doc/html/gucharmap-%{pc_api}/

%changelog
