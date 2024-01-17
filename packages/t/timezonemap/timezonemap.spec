#
# spec file for package timezonemap
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


Name:           timezonemap
Version:        0.4.4
Release:        0
Summary:        GTK+3 timezone map widget
License:        GPL-3.0-only
Group:          System/Libraries
URL:            https://launchpad.net/timezonemap
Source:         https://launchpad.net/timezonemap/trunk/0.4.4/+download/libtimezonemap-0.4.4.tar.xz
BuildRequires:  glib2-devel
BuildRequires:  gnome-common
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  json-glib-devel
BuildRequires:  pkgconfig(libsoup-2.4)

%description
Timezone map widget for GTK+3

%package -n libtimezonemap1
Summary:        GTK+3 timezone map widget
Group:          System/Libraries

%description -n libtimezonemap1
Timezone map widget for GTK+3.

%package devel
Summary:        Development headers for %{name}
Group:          Development/Libraries/C and C++
Requires:       libtimezonemap1 = %{version}

%description devel
Development headers for %{name}.

%package -n typelib-1_0-TimezoneMap-1_0
Summary:        GTK+3 timezone map widget - Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-TimezoneMap-1_0
This package contains the GObject Introspection bindings for
%{name} library.

%prep
%setup -q -n lib%{name}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libtimezonemap1 -p /sbin/ldconfig
%postun -n libtimezonemap1 -p /sbin/ldconfig

%files -n libtimezonemap1
%license COPYING
%doc README
%{_libdir}/libtimezonemap.so.1
%{_libdir}/libtimezonemap.so.1.0.0
%{_datadir}/libtimezonemap

%files devel
%{_includedir}/timezonemap
%{_libdir}/libtimezonemap.so
%{_libdir}/pkgconfig/timezonemap.pc
%{_datadir}/gir-1.0/TimezoneMap-1.0.gir

%files -n typelib-1_0-TimezoneMap-1_0
%{_libdir}/girepository-1.0/TimezoneMap-1.0.typelib

%changelog
