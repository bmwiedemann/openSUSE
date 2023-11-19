#
# spec file for package cuarzo-srm
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


Name:           cuarzo-srm
Version:        0.3.2.1
%define sillyver 0.3.2-1
%define lname	libSRM-suse0
Release:        0
Summary:        Rendering manager for the Louvre library
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/CuarzoSoftware/SRM/
Source:         https://github.com/CuarzoSoftware/SRM/archive/refs/tags/v%sillyver.tar.gz
Patch1:         0001-build-heed-results-from-pkg-config.patch
Patch2:         0001-build-import-gl-dependency.patch
Patch3:         0001-versioning.patch
BuildRequires:  c_compiler
BuildRequires:  meson
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)

%description
A C library to aid in the development of Linux DRM/KMS applications.

%package -n %lname
Summary:        Rendering Manager for the Louvre library
Group:          System/Libraries

%description -n %lname
A C library to aid in the development of Linux DRM/KMS applications.
SRM allows for using multiple GPUs simultaneously. It offers
functions for creating OpenGL textures which are automatically shared
among GPUs.

%package devel
Summary:        Headers for the Simple Rendering Manager library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
A C library to aid in the development of Linux DRM/KMS applications.
SRM allows for using multiple GPUs simultaneously. It offers
functions for creating OpenGL textures which are automatically shared
among GPUs.

This package contains headers and development utilities for libSRM.

%prep
%autosetup -p1 -n SRM-%sillyver

%build
pushd src/
%meson
%meson_build
popd

%install
ln -fs /bin/true scripts/ld.sh
pushd src/
%meson_install
popd

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libSRM.so.suse0

%files devel
%license LICENSE
%_bindir/srm-*
%_includedir/SRM/
%_libdir/libSRM.so

%changelog
