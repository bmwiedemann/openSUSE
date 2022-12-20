#
# spec file for package libxfce4util
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


%bcond_with git
%define libname libxfce4util7
Name:           libxfce4util
Version:        4.18.0
Release:        0
Summary:        Utility Library for the Xfce Desktop Environment
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://www.xfce.org/
Source0:        https://archive.xfce.org/src/xfce/libxfce4util/4.18/%{name}-%{version}.tar.bz2
Source100:      %{name}-rpmlintrc
BuildRequires:  intltool
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif

%description
libxfce4util is a general-purpose utility library with core application support
for the Xfce Desktop Environment.

%package tools
Summary:        Tools for libxfce4util
Group:          System/Libraries
Provides:       libxfce4util:%{_sbindir}/xfce4-kiosk-query

%description tools
This package contains tools for libxfce4util.

%package -n %{libname}
Summary:        Utility Library for the Xfce Desktop Environment
Group:          System/Libraries
Recommends:     %{name}-lang = %{version}
Provides:       libxfce4util = %{version}
Obsoletes:      libxfce4util <= 4.8.2

%description -n %{libname}
libxfce4util is a general-purpose utility library with core application support
for the Xfce Desktop Environment.

%package -n typelib-1_0-Libxfce4util-1_0
Summary:        Utility Library for the Xfce Desktop Environment
Group:          System/Libraries
Provides:       typelib-1_0-libxfce4util-1_0 = %{version}
Obsoletes:      typelib-1_0-libxfce4util-1_0 < %{version}

%description -n typelib-1_0-Libxfce4util-1_0
libxfce4util is a general-purpose utility library with core application support
for the Xfce Desktop Environment.

%package devel
Summary:        Development Files for libxfce4util
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name}-tools = %{version}
Requires:       typelib-1_0-Libxfce4util-1_0 = %{version}

%description devel
This package contains the API documentation and development files needed for
developing applications based on libxfce4util.

%lang_package

%prep
%autosetup

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --enable-vala=yes \
    --disable-static \
    --enable-gtk-doc
%else
%configure \
    --enable-vala=yes \
    --disable-static
%endif

%make_build

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,ur_PK,tl_PH}

%find_lang %{name} %{?no_lang_C}

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files tools
%{_sbindir}/xfce4-kiosk-query

%files lang -f %{name}.lang

%files -n %{libname}
%doc AUTHORS NEWS TODO README.Kiosk README.md
%license COPYING
%{_libdir}/libxfce4util.so.*

%files -n typelib-1_0-Libxfce4util-1_0
%{_libdir}/girepository-1.0/Libxfce4util-1.0.typelib

%files devel
%{_libdir}/pkgconfig/libxfce4util-*.pc
%{_libdir}/libxfce4util.so
%dir %{_includedir}/xfce4
%{_includedir}/xfce4/libxfce4util/
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/libxfce4util
%{_datadir}/gir-1.0/Libxfce4util-1.0.gir
%{_datadir}/vala/vapi/

%changelog
