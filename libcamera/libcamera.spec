#
# spec file for package libcamera
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libcamera
%define lname   libcamera-suse0
Version:        0~14.b99da21
Release:        0
Summary:        A complex camera support library in C++
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://git.linuxtv.org/libcamera.git/
Source:         %name-%version.tar.xz
Patch1:         vers.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  c++_compiler
BuildRequires:  meson >= 0.40
BuildRequires:  pkg-config
BuildRequires:  xz

%description
libcamera is an experimental camera user-space API.

A camera may consist of multiple sensors or function blocks, and can
expose multiple kernel device nodes in /dev for different stages of
the pipeline. The libcamera API groups and exposes these pieces as
what users consider one "camera".

%package -n %lname
Summary:        A complex camera support library in C++
Group:          System/Libraries

%description -n %lname
libcamera is an experimental camera user-space API.

A camera may consist of multiple sensors or function blocks, and can
expose multiple kernel device nodes in /dev for different stages of
the pipeline. The libcamera API groups and exposes these pieces as
what users consider one "camera".

%package devel
Summary:        Development for libcamera, a camera support library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libcamera is an experimental camera user-space API.

This subpackage contains the header files.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
# Together with patch1, this makes for the "-release" feature from libtool
mv "%buildroot/%_libdir/libcamera-suse.so" "%buildroot/%_libdir/libcamera.so"
perl -i -pe 's{-lcamera-suse}{-lcamera}' "%buildroot/%_libdir/pkgconfig"/*.pc

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%defattr(-,root,root)
%_libdir/libcamera*.so.*

%files devel
%defattr(-,root,root)
%license licenses/*gpl*
%_includedir/libcamera/
%_libdir/libcamera.so
%_libdir/pkgconfig/*.pc

%changelog
