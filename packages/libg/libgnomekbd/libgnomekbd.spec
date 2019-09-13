#
# spec file for package libgnomekbd
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


%define sover 8
Name:           libgnomekbd
Version:        3.26.1
Release:        0
Summary:        GNOME Keyboard Library
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/libgnomekbd
Source0:        https://download.gnome.org/sources/libgnomekbd/3.26/%{name}-%{version}.tar.xz
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxklavier) >= 5.2

%description
GNOME keyboard library and utility.

%package -n gnomekbd-tools
Summary:        GNOME Keyboard tools
Group:          System/GUI/GNOME
Recommends:     %{name}-lang

%description -n gnomekbd-tools
GNOME keyboard library and utility.

This package provides various binaries and conversion tools for
libgnomekbd.

%package -n libgnomekbd%{sover}
Summary:        GNOME Keyboard Library
Group:          System/Libraries
# Make -lang package installable, and ease upgrade path
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libgnomekbd%{sover}
GNOME keyboard shared library.

This package provides the shared library of libgnomekbd.

%package -n typelib-1_0-Gkbd-3_0
Summary:        Introspection bindings for libgnomekbd
Group:          System/Libraries

%description -n typelib-1_0-Gkbd-3_0
GNOME keyboard library and utility.

This package provides the GObject Introspection bindings for
libgnomekbd.

%package devel
Summary:        GNOME Keyboard Library
Group:          Development/Libraries/GNOME
Requires:       %{name}%{sover} = %{version}
Requires:       gnomekbd-tools = %{version}
Requires:       typelib-1_0-Gkbd-3_0 = %{version}

%description devel
This package contains the header files for developing
applications that want to make use of libgnomekbd.

%lang_package

%prep
%autosetup
translation-update-upstream

%build
%configure \
	--disable-static \
	%{nil}
%make_build V=1

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%post -n libgnomekbd%{sover} -p /sbin/ldconfig
%postun -n libgnomekbd%{sover} -p /sbin/ldconfig

%files -n gnomekbd-tools
%{_bindir}/gkbd-keyboard-display
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/libgnomekbd.convert
%{_datadir}/applications/gkbd-keyboard-display.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.libgnomekbd.desktop.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.libgnomekbd.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.libgnomekbd.keyboard.gschema.xml
%{_datadir}/libgnomekbd/

%files -n libgnomekbd%{sover}
%license COPYING.LIB
%{_libdir}/*so.*

%files -n typelib-1_0-Gkbd-3_0
%{_libdir}/girepository-1.0/Gkbd-3.0.typelib

%files lang -f %{name}.lang

%files devel
%{_includedir}/libgnomekbd/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Gkbd-3.0.gir

%changelog
