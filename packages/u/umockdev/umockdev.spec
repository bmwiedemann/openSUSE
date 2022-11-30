#
# spec file for package umockdev
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


%define shlib libumockdev0
%define shlibpre libumockdev-preload0
Name:           umockdev
Version:        0.17.15
Release:        0
Summary:        Mock hardware devices for creating unit tests and bug reporting
License:        LGPL-2.1-or-later
URL:            https://github.com/martinpitt/umockdev/
Source:         https://github.com/martinpitt/umockdev/releases/download/%{version}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  vala
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
# Disable to avoid build cycle with gudev (it is recommended but not required here)
# BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(libudev)
# For tests
BuildRequires:  pkgconfig(udev)

%description
umockdev mocks Linux devices for creating integration tests for hardware
related libraries and programs. It also provides tools to record the properties
and behaviour of particular devices, and to run a program or test suite under a
test bed with the previously recorded devices loaded.

%package -n %{shlib}
Summary:        Shared library for umockdev

%description -n %{shlib}
umockdev mocks Linux devices for creating integration tests for hardware
related libraries and programs.

This package provides the shared library for %{name}.

%package -n %{shlibpre}
Summary:        Shared library for umockdev-preload

%description -n %{shlibpre}
umockdev mocks Linux devices for creating integration tests for hardware
related libraries and programs.

This package provides the shared library for umockdev-preload.

%package devel
Summary:        Headers and sources for developing apps with umockdev
Requires:       %{name} = %{version}
Requires:       %{shlibpre} = %{version}
Requires:       %{shlib} = %{version}
Requires:       typelib-1_0-UMockdev-1_0 = %{version}

%description devel
umockdev mocks Linux devices for creating integration tests for hardware
related libraries and programs.

This package provides the headers and sources needed to build software against
umockdev.

%package -n typelib-1_0-UMockdev-1_0
Summary:        Introspection bindings for umockdev -- a hardware mocking tool

%description -n typelib-1_0-UMockdev-1_0
umockdev mocks Linux devices for creating integration tests for hardware
related libraries and programs.

This package provides the GObject Introspection bindings for the library
umockdev.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig
%post -n %{shlibpre} -p /sbin/ldconfig
%postun -n %{shlibpre} -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/*

%files -n %{shlib}
%license COPYING
%{_libdir}/libumockdev.so.*

%files -n %{shlibpre}
%license COPYING
%{_libdir}/libumockdev-preload.so.*

%files devel
%license COPYING
%{_includedir}/umockdev-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi

%files -n typelib-1_0-UMockdev-1_0
%{_libdir}/girepository-1.0/UMockdev-1.0.typelib

%changelog
