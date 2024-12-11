#
# spec file for package wf-config
#
# Copyright (c) 2021 SUSE LLC
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

%define so_ver 0.9
%define libname libwf-config1
Name:           wf-config
Version:        0.9.0
Release:        0
Summary:        A library for managing configuration files
License:        MIT
URL:            https://wayfire.org/
Source0:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/WayfireWM/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz.sha256sum
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(doctest)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(wlroots) >= 0.17.0

%description
A library for managing configuration files, written for wayfire.

%package -n %{libname}
Summary:        A library for managing configuration files

%description -n %{libname}
A library for managing configuration files, written for wayfire.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}

%description devel
Development files for %{name}.

%prep
echo "`grep %{name}-%{version}.tar.xz %{SOURCE1} | grep -Eo '^[0-9a-f]+'`  %{SOURCE0}" | sha256sum -c
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
ln -s libwf-config.so.%{version} libwf-config.so.0

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%check
%meson_test

%files -n %{libname}
%license LICENSE
%{_libdir}/*.so.*

%files devel
%{_includedir}/wayfire
%{_libdir}/libwf-config.so
%{_libdir}/pkgconfig/wf-config.pc

%changelog
