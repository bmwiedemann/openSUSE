#
# spec file for package vmaf
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


Name:           vmaf
%define lname   libvmaf0
Version:        1.5.3
Release:        0
Summary:        Perceptual video quality assessment algorithm
License:        BSD-2-Clause-Patent AND BSD-3-Clause
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://github.com/Netflix/vmaf
Source:         https://github.com/Netflix/vmaf/archive/v%version.tar.gz
Source9:        baselibs.conf
Patch1:         0001-build-unbreak-x86-builds.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.47
BuildRequires:  nasm
BuildRequires:  pkg-config
Provides:       bundled(libsvm) = 3.18

%description
VMAF is a perceptual video quality assessment algorithm.

%package -n %lname
Summary:        Perceptual video quality assessment algorithm
Group:          System/Libraries
Recommends:     %name-data

%description -n %lname
VMAF is a perceptual video quality assessment algorithm.

%package data
Summary:        Models for Video Multi-Method Assessment Fusion
Group:          Productivity/Multimedia/Video/Editors and Convertors
BuildArch:      noarch

%description data
This package contains a number of trained VMAF models to be used in
different scenarios. Besides the default VMAF model which predicts
the quality of a video displayed on a HDTV in a living-room viewing
condition, a number of additional models are included, covering
mobile phone and 4KTV viewing conditions.

%package devel
Summary:        Development tools for Video Multi-Method Assessment Fusion
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release

%description devel
VMAF is a perceptual video quality assessment algorithm developed by
Netflix.
This package contains the library API definitions.

%prep
%autosetup -p1

%build
rm -rf third_party
pushd libvmaf/
%meson
%meson_build
popd

%install
pushd libvmaf/
%meson_install
popd
rm -f "%buildroot/%_libdir"/*.a
%fdupes %buildroot/%_prefix

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libvmaf.so.0*

%files data
%_datadir/model/

%files devel
%_bindir/vmaf*
%_includedir/libvmaf/
%_libdir/libvmaf.so
%_libdir/pkgconfig/*.pc
%license LICENSE
%doc FAQ.md README.md

%changelog
