#
# spec file for package libglib-testing
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


Name:           libglib-testing
Version:        0.1.1
Release:        0
Summary:        GLib test harness and mocking framework
License:        LGPL-2.1-or-later
URL:            https://gitlab.gnome.org/pwithnall/libglib-testing
Source:         %{url}/-/archive/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.45.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.44
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44

%description
libglib-testing is a test library providing test harnesses and mock
classes which complement the classes provided by GLib. It is
intended to be used by any project which uses GLib and which wants
to write internal unit tests.

%package -n libglib-testing-0-0
Summary:        GLib test harness and mocking framework

%description -n libglib-testing-0-0
libglib-testing is a test library providing test harnesses and mock
classes which complement the classes provided by GLib. It is
intended to be used by any project which uses GLib and which wants
to write internal unit tests.

%package devel
Summary:        GLib test harness and mocking framework
Requires:       libglib-testing-0-0 = %{version}

%description devel
libglib-testing is a test library providing test harnesses and mock
classes which complement the classes provided by GLib. It is
intended to be used by any project which uses GLib and which wants
to write internal unit tests.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%post   -n libglib-testing-0-0 -p /sbin/ldconfig
%postun -n libglib-testing-0-0 -p /sbin/ldconfig

%files -n libglib-testing-0-0
%license COPYING
%doc NEWS README
%{_libdir}/libglib-testing-0.so.*

%files devel
%{_libdir}/pkgconfig/glib-testing-0.pc
%{_includedir}/glib-testing-0
%{_datadir}/gtk-doc/html/%{name}/
%{_libdir}/libglib-testing-0.so

%changelog
