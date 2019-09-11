#
# spec file for package caja
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


%define lname libcaja-extension1
%define typelib typelib-1_0-Caja-2_0
%define _version 1.23
Name:           caja
Version:        1.23.1
Release:        0
Summary:        File manager for the MATE desktop
License:        GPL-2.0-only AND LGPL-2.0-only
Group:          System/GUI/Other
Url:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(exempi-2.0)
BuildRequires:  pkgconfig(gail)
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sm)
Recommends:     %{name}-lang
# mate-file-manager was last used in openSUSE 13.1.
Provides:       mate-file-manager = %{version}
Obsoletes:      mate-file-manager < %{version}
Obsoletes:      mate-file-manager-lang < %{version}

%description
Caja is the official file manager for the MATE desktop. It allows to
browse directories, preview files and launch applications associated
with them. It is also responsible for handling the icons on the MATE
desktop. It works on local and remote filesystems.

%lang_package

%package devel
Summary:        Caja development files
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       %{name} = %{version}
# mate-file-manager-devel was last used in openSUSE 13.1.
Provides:       mate-file-manager-devel = %{version}
Obsoletes:      mate-file-manager-devel < %{version}

%description devel
Caja is the official file manager for the MATE desktop. It allows to
browse directories, preview files and launch applications associated
with them. It is also responsible for handling the icons on the MATE
desktop. It works on local and remote filesystems.

%package -n %{lname}
Summary:        Caja shared libraries
Group:          System/Libraries
Requires:       %{name}-gschemas >= %{version}

%description -n %{lname}
Caja is the official file manager for the MATE desktop. It allows to
browse directories, preview files and launch applications associated
with them. It is also responsible for handling the icons on the MATE
desktop. It works on local and remote filesystems.

# Needed for using pluma as standalone from MATE.

%package gschemas
Summary:        Caja GSchemas
Group:          System/Libraries
Obsoletes:      mate-file-manager < %{version}
# caja-gsettings-schemas was last used in openSUSE Leap 42.1.
Obsoletes:      %{name}-gsettings-schemas < %{version}
Provides:       %{name}-gsettings-schemas = %{version}
%glib2_gsettings_schema_requires

%description gschemas
Caja is the official file manager for the MATE desktop. It allows to
browse directories, preview files and launch applications associated
with them. It is also responsible for handling the icons on the MATE
desktop. It works on local and remote filesystems.

This package provides the GSettings schemas for Caja.

%package -n %{typelib}
Summary:        MATE file manager typelib
Group:          System/GUI/Other

%description -n %{typelib}
Caja is the official file manager for the MATE desktop. It allows to
browse directories, preview files and launch applications associated
with them. It is also responsible for handling the icons on the MATE
desktop. It works on local and remote filesystems.

%prep
%setup -q

%build
%if 0%{?suse_version} < 1500
export CFLAGS="%{optflags} -std=gnu99"
%endif
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-update-mimedb \
  --disable-static        \
  --enable-introspection
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print
# Create extensions directories.
mkdir -p %{buildroot}%{_libdir}/caja/extensions-2.0/ \
  %{buildroot}%{_datadir}/caja/extensions/ \
  %{buildroot}%{_datadir}/caja-extensions/

%suse_update_desktop_file caja-autorun-software
%suse_update_desktop_file caja-browser
%suse_update_desktop_file caja-computer
%suse_update_desktop_file caja-file-management-properties
%suse_update_desktop_file caja-folder-handler
%suse_update_desktop_file caja-home
%suse_update_desktop_file caja
%suse_update_desktop_file mate-network-scheme

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%post gschemas
%glib2_gsettings_schema_post

%postun gschemas
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING COPYING.EXTENSIONS COPYING.LIB
%doc AUTHORS NEWS
%{_bindir}/caja
%{_bindir}/caja-autorun-software
%{_bindir}/caja-connect-server
%{_bindir}/caja-file-management-properties
%{_datadir}/caja/
%{_datadir}/dbus-1/services/org.mate.freedesktop.FileManager1.service
%{_datadir}/applications/caja-autorun-software.desktop
%{_datadir}/applications/caja-browser.desktop
%{_datadir}/applications/caja-computer.desktop
%{_datadir}/applications/caja-file-management-properties.desktop
%{_datadir}/applications/caja-folder-handler.desktop
%{_datadir}/applications/caja-home.desktop
%{_datadir}/applications/caja.desktop
%{_datadir}/applications/mate-network-scheme.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*
%{_mandir}/man?/*.?%{?ext_man}
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/caja.appdata.xml
# Own common extensions directories.
%dir %{_libdir}/caja/
%dir %{_libdir}/caja/extensions-2.0/
%dir %{_datadir}/caja/extensions/
%dir %{_datadir}/caja-extensions/

%files lang -f caja.lang

%files -n %{typelib}
%{_libdir}/girepository-1.0/Caja-2.0.typelib

%files -n %{lname}
%{_libdir}/*.so.*

%files gschemas
%{_datadir}/glib-2.0/schemas/*.xml

%files devel
%{_datadir}/gtk-doc/html/libcaja-extension/
%{_includedir}/caja/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libcaja-extension.pc
%{_datadir}/gir-1.0/Caja-2.0.gir

%changelog
