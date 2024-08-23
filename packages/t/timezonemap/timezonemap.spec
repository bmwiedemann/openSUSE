#
# spec file for package timezonemap
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.4.6
Release:        0
Summary:        GTK+3 timezone map widget
License:        GPL-3.0-only
URL:            https://launchpad.net/timezonemap
Source:         https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/libtimezonemap/0.4.6-7/libtimezonemap_0.4.6.orig.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gnome-common
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)

%description
Timezone map widget for GTK+3

%package -n libtimezonemap1
Summary:        GTK+3 timezone map widget

%description -n libtimezonemap1
Timezone map widget for GTK+3.

%package devel
Summary:        Development headers for %{name}
Requires:       libtimezonemap1 = %{version}

%description devel
Development headers for %{name}.

%package -n typelib-1_0-TimezoneMap-1_0
Summary:        GTK+3 timezone map widget - Introspection bindings

%description -n typelib-1_0-TimezoneMap-1_0
This package contains the GObject Introspection bindings for
%{name} library.

%prep
%autosetup -n lib%{name}-%{version}
NOCONFIGURE=1 ./autogen.sh

%build
%configure \
  --with-gtk=3 \
  --disable-static \
  --enable-introspection
%make_build

%install
%make_install

# remove .la files
rm -f %{buildroot}%{_libdir}/libtimezonemap.la

%ldconfig_scriptlets -n libtimezonemap1

%files -n libtimezonemap1
%license COPYING
%doc README debian/changelog
%{_libdir}/libtimezonemap.so.*
%{_datadir}/libtimezonemap

%files devel
%{_includedir}/timezonemap
%{_libdir}/libtimezonemap.so
%{_libdir}/pkgconfig/timezonemap.pc
%{_datadir}/gir-1.0/TimezoneMap-1.0.gir

%files -n typelib-1_0-TimezoneMap-1_0
%{_libdir}/girepository-1.0/TimezoneMap-1.0.typelib

%changelog
