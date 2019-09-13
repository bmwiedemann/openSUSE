#
# spec file for package libmanette
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


%define binary_version 0.2
%define package_version 0_2-0

Name:           libmanette
Version:        0.2.2
Release:        0
Summary:        A simple GObject game controller library
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://gitlab.gnome.org/aplazas/libmanette/
Source:         http://download.gnome.org/sources/libmanette/0.2/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel >= 0.6.7
BuildRequires:  meson >= 0.43.0
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gudev-1.0) >= 1.0
BuildRequires:  pkgconfig(libevdev) >= 1.4.5
BuildRequires:  pkgconfig(vapigen)

%description
libmanette allows easy access to game controllers.

%package -n libmanette-%{package_version}
Summary:        A simple GObject game controller library
Group:          System/Libraries

%description -n libmanette-%{package_version}
libmanette allows easy access to game controllers.

%package -n typelib-1_0-Manette-%{package_version}
Summary:        GObject introspection bindings for liblibmanette
Group:          System/Libraries

%description -n typelib-1_0-Manette-%{package_version}
libmanette allows easy access to game controllers.
This subpackage contains the gobject bindings for the liblibmanette
shared library.

%package devel
Summary:        Development files for the libmanette library
Group:          Development/Languages/C and C++
Requires:       libmanette-%{package_version} = %{version}

%description devel
libmanette allows easy access to game controllers.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%post -n libmanette-%{package_version} -p /sbin/ldconfig
%postun -n libmanette-%{package_version} -p /sbin/ldconfig

%files -n libmanette-%{package_version}
%license COPYING
%{_libdir}/libmanette-%{binary_version}.so.*

%files -n typelib-1_0-Manette-%{package_version}
%{_libdir}/girepository-1.0/Manette-%{binary_version}.typelib

%files devel
%{_bindir}/manette-test
%{_datadir}/gir-1.0/Manette-%{binary_version}.gir
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/manette-%{binary_version}.deps
%{_datadir}/vala/vapi/manette-%{binary_version}.vapi
%{_includedir}/libmanette/
%{_libdir}/libmanette-%{binary_version}.so
%{_libdir}/pkgconfig/manette-%{binary_version}.pc

%changelog
