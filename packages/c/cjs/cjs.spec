#
# spec file for package cjs
#
# Copyright (c) 2020 SUSE LLC
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


%define soname  libcjs
%define sover   0
%define typelib typelib-1_0-CjsPrivate-1_0
Name:           cjs
Version:        4.6.0
Release:        0
Summary:        JavaScript module used by Cinnamon
License:        MIT AND (MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later)
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cjs
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  dbus-1
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(mozjs-52)

%description
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

%package -n %{soname}%{sover}
Summary:        Shared Libraries for Cinnamon JS module
Group:          System/Libraries

%description -n %{soname}%{sover}
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package provides libraries for cjs.

%package -n %{typelib}
Summary:        Cinnamon JS module -- Introspection Bindings
Group:          System/Libraries

%description -n %{typelib}
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package provides the GObject Introspection bindings for
Cinnamon JS.

%package devel
Summary:        Development Files for Cinnamon JS module
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       %{soname}%{sover} = %{version}
Requires:       %{typelib} = %{version}

%description devel
JavaScript bindings based on GObject Introspection for the
Cinnamon Desktop.

This package contains development files for cjs.

%prep
%setup -q
# we didn't enable code-coverage tests, so "@CODE_COVERAGE_RULES@" never get filled
sed -i '$d' Makefile-test.am

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
%if 0%{?suse_version} < 1500
  --without-dbus-tests \
%endif
  --disable-static

export CFLAGS+='%{optflags}'
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files
%license COPYING*
%doc README debian/changelog
%{_bindir}/%{name}*

%files -n %{soname}%{sover}
%{_libdir}/libcjs.so.%{sover}*

%files -n %{typelib}
%dir %{_libdir}/cjs/
%dir %{_libdir}/cjs/girepository-1.0/
%{_libdir}/cjs/girepository-1.0/CjsPrivate-1.0.typelib

%files devel
%{_includedir}/%{name}-1.0/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
