#
# spec file for package libliftoff
#
# Copyright (c) 2023 SUSE LLC
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


%define libname libliftoff0

Name:           libliftoff
Version:        0.4.1
Release:        0
Summary:        KMS plane library
Group:          Development/Libraries/C and C++
License:        MIT
URL:            https://gitlab.freedesktop.org/emersion/libliftoff
Source0:        https://gitlab.freedesktop.org/emersion/libliftoff/-/archive/v%{version}/libliftoff-v%{version}.tar.gz
BuildRequires:  meson >= 0.52.0
BuildRequires:  pkgconfig(libdrm) >= 2.4.108

%description
libliftoff offers using KMS planes from userspace. Users create
"virtual planes" called layers, set KMS properties on them, and
libliftoff will pick hardware planes for these layers if possible.

%package -n %{libname}
Summary:        Lightweight KMS plane library
Group:          System/Libraries

%description -n %{libname}
libliftoff offers using KMS planes from userspace. Users create
"virtual planes" called layers, set KMS properties on them, and
libliftoff will pick hardware planes for these layers if possible.

%package devel
Summary:        Development files for libliftoff
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-v%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/libliftoff.so.*

%files devel
%{_libdir}/libliftoff.so
%{_libdir}/pkgconfig/libliftoff.pc
%{_includedir}/libliftoff.h

%changelog
