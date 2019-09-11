#
# spec file for package eom
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


%define typelib typelib-1_0-Eom-1_0
%define _version 1.23
Name:           eom
Version:        1.23.0
Release:        0
Summary:        MATE Desktop graphics viewer
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpeas-gtk-1.0) >= 1.8.0
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}
Requires:       mate-desktop-gsettings-schemas >= %{_version}
Recommends:     %{name}-lang
# mate-image-viewer was last used in openSUSE 13.1.
Provides:       mate-image-viewer = %{version}
Obsoletes:      mate-image-viewer < %{version}
Obsoletes:      mate-image-viewer-lang < %{version}
%glib2_gsettings_schema_requires

%description
The Eye of MATE is a simple graphics viewer for the MATE Desktop
which uses the gdk-pixbuf library. It can deal with large images,
and zoom and scroll with constant memory usage. Its goals are
simplicity and standards compliance.

%lang_package

%package devel
Summary:        MATE Desktop graphics viewer development files
Group:          Development/Tools/Other
Requires:       %{name} = %{version}
# mate-image-viewer-devel was last used in openSUSE 13.1.
Provides:       mate-image-viewer-devel = %{version}
Obsoletes:      mate-image-viewer-devel < %{version}

%description devel
The Eye of MATE is a simple graphics viewer for the MATE Desktop
which uses the gdk-pixbuf library. It can deal with large images,
and zoom and scroll with constant memory usage. Its goals are
simplicity and standards compliance.

%package -n %{typelib}
Summary:        MATE Desktop graphics viewer typelib
Group:          System/Libraries

%description -n %{typelib}
The Eye of MATE is a simple graphics viewer for the MATE Desktop
which uses the gdk-pixbuf library. It can deal with large images,
and zoom and scroll with constant memory usage. Its goals are
simplicity and standards compliance.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --libexecdir=%{_libexecdir}/%{name}
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{name}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%glib2_gsettings_schema_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/%{name}
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/*.xml
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_datadir}/help/C/%{name}/

%files lang -f %{name}.lang

%files devel
%{_includedir}/%{name}-2.20/
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gir-1.0/Eom-1.0.gir
%{_datadir}/gtk-doc/html/%{name}/

%files -n %{typelib}
%{_libdir}/girepository-1.0/Eom-1.0.typelib

%changelog
