#
# spec file for package libmatekbd
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


%define typelib  typelib-1_0-Matekbd-1_0
%define _version 1.28
%define sover    6

Name:           libmatekbd
Version:        1.28.0
Release:        0
Summary:        MATE Desktop keyboard configuration libraries
License:        LGPL-2.1-or-later
Group:          Development/Libraries/X11
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxklavier) >= 5.2
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(x11)
%glib2_gsettings_schema_requires

%description
This package provides libmatekdb, an API to manage the keyboard in
MATE Desktop applications.

%package -n matekbd-common
Summary:        MATE Desktop keyboard configuration common files
Group:          System/Libraries

%description -n matekbd-common
This package provides libmatekdb, an API to manage the keyboard in
MATE Desktop applications.

%package -n %{name}%{sover}
Summary:        MATE Desktop keyboard configuration shared libraries
Group:          System/Libraries
Requires:       matekbd-common
Recommends:     %{name}-lang
Provides:       %{name} = %{version}
# libmatekbd with a wrong sover was last used in openSUSE Leap 42.1.
Obsoletes:      %{name}1 < %{version}

%description -n %{name}%{sover}
This package provides libmatekdb, an API to manage the keyboard in
MATE Desktop applications.

%package -n %{name}ui%{sover}
Summary:        MATE Desktop keyboard configuration shared libraries
Group:          System/Libraries
Requires:       matekbd-common
Recommends:     %{name}-lang
Provides:       %{name} = %{version}
# libmatekbd with a wrong sover was last used in openSUSE Leap 42.1.

%description -n %{name}ui%{sover}
This package provides libmatekdbui, an API to manage the keyboard in
MATE Desktop applications.

%package devel
Summary:        MATE Desktop keyboard configuration development files
Group:          Development/Libraries/X11
Requires:       %{name}%{sover} = %{version}
Requires:       %{name}ui%{sover} = %{version}
Requires:       matekbd-common = %{version}

%description devel
This package provides libmatekdb, an API to manage the keyboard in
MATE Desktop applications.

%package -n %{typelib}
Summary:        MATE Desktop keyboard configuration typelib

%description -n %{typelib}
This package provides libmatekdb, an API to manage the keyboard in
MATE Desktop applications.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%post -n %{name}ui%{sover} -p /sbin/ldconfig
%postun -n %{name}ui%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/%{name}.so.*

%files -n %{name}ui%{sover}
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/%{name}ui.so.*

%files -n matekbd-common
%{_datadir}/glib-2.0/schemas/*.xml

%files -n %{typelib}
%{_libdir}/girepository-1.0/Matekbd-1.0.typelib

%files devel
%license COPYING
%doc AUTHORS ChangeLog
%{_includedir}/%{name}/
%{_datadir}/gir-1.0/Matekbd-1.0.gir
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files lang -f %{name}.lang

%changelog
