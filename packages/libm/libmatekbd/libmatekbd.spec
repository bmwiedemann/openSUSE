#
# spec file for package libmatekbd
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


%define typelib typelib-1_0-Matekbd-1_0
%define _version 1.23
%define sover   4
Name:           libmatekbd
Version:        1.23.0
Release:        0
Summary:        MATE Desktop keyboard configuration libraries
License:        LGPL-2.1-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         http://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gio-2.0) >= 2.48
BuildRequires:  pkgconfig(glib-2.0) >= 2.48
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(libxklavier) >= 5.2
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(x11)
%glib2_gsettings_schema_requires

%description
This package provides libmatekdb, an API to manage the keyboard in
MATE Desktop applications.

%package -n matekbd-common
Summary:        MATE Desktop keyboard configuration common files
Group:          System/GUI/Other

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
Obsoletes:      %{name}1

%description -n %{name}%{sover}
This package provides libmatekdb, an API to manage the keyboard in
MATE Desktop applications.

%package devel
Summary:        MATE Desktop keyboard configuration development files
Group:          Development/Libraries/Other
Requires:       %{name}%{sover} = %{version}
Requires:       matekbd-common = %{version}

%description devel
This package provides libmatekdb, an API to manage the keyboard in
MATE Desktop applications.

%package -n %{typelib}
Summary:        MATE Desktop keyboard configuration typelib
Group:          System/GUI/Other

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
make %{?_smp_mflags} V=1

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print

%if 0%{?suse_version} < 1500
%post -n matekbd-common
%glib2_gsettings_schema_post

%postun -n matekbd-common
%glib2_gsettings_schema_postun
%endif

%post -n %{name}%{sover} -p /sbin/ldconfig

%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/*.so.%{sover}*

%files -n matekbd-common
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/libmatekbd/

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
