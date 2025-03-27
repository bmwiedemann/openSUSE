#
# spec file for package coeurl
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

%global libname libcoeurl0_3
Name:           coeurl
Version:        0.3.1
Release:        0
Summary:        A simple async wrapper around CURL for C++
License:        MIT
URL:            https://nheko.im/nheko-reborn/coeurl
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
BuildRequires:  meson
%if 0%{?suse_version} < 1600
BuildRequires: gcc12
BuildRequires: gcc12-c++
%else
BuildRequires: gcc
BuildRequires: gcc-c++
%endif
BuildRequires:  cmake >= 3.12
BuildRequires:  meson >= 0.55
BuildRequires:  pkgconfig(fmt) >= 10.0.0
BuildRequires:  pkgconfig(libcurl) >= 7.77.0
BuildRequires:  pkgconfig(libevent) >= 2.1.12
BuildRequires:  pkgconfig(spdlog) >= 1.14.0

%description
Simple library to do http requests asynchronously via CURL in C++. (Eventually
as coroutines, once all the compilers I need to support support them.)
This is based on the CURL-libevent
example.

%package -n %{libname}
Summary:        Libraries for %name

%description -n %{libname}
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}

%description devel
%{summary}.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
%meson
%meson_build

%install
%meson_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files devel
%license LICENSE
%doc README.md
%{_libdir}/libcoeurl.so
%dir %{_includedir}/coeurl
%{_includedir}/coeurl/*.hpp
%{_libdir}/pkgconfig/coeurl.pc

%files -n %{libname}
%{_libdir}/libcoeurl.so.*

%changelog

