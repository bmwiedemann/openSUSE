#
# spec file for package intel-media-driver
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


%define so_ver	7

Name:           intel-media-driver
Version:        22.6.4
Release:        0
Summary:        Intel Media Driver for VAAPI
License:        BSD-3-Clause AND MIT
Group:          System/Libraries
URL:            https://github.com/intel/media-driver
Source0:        %{url}/archive/refs/tags/intel-media-%{version}.tar.gz
Source1:        generate-supplements.sh
Source2:        supplements.inc
Source3:        baselibs.conf
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.5
BuildRequires:  gmmlib-devel >= 22.2.0
BuildRequires:  pkgconfig
#Note this is NOT libva library version!
BuildRequires:  pkgconfig(libva) >= 1.14.0
BuildRequires:  pkgconfig(pciaccess)
ExclusiveArch:  x86_64 i586
%include %{S:2}

%description
The Intel Media Driver for VAAPI is a new VA-API (Video Acceleration API)
user mode driver supporting hardware accelerated decoding, encoding, and
video post processing for GEN based graphics hardware.

%package -n libigfxcmrt%{so_ver}
Summary:        Intel Graphics C for Media Runtime Library
License:        MIT
Group:          System/Libraries

%description -n libigfxcmrt%{so_ver}
cmrtlib is a runtime library for Intel GPU render engine.

%package -n libigfxcmrt-devel
Summary:        Development files for Intel Graphics C for Media Runtime Library
License:        MIT
Group:          Development/Libraries/C and C++
Requires:       libigfxcmrt%{so_ver} = %{version}

%description -n libigfxcmrt-devel
cmrtlib is a runtime library for Intel GPU render engine.

This package contains the development headers for the library found in
libigfxcmrt%{so_ver}.

%prep
%setup -q -c -a 0
mv media-driver-* media-driver
chmod -x media-driver/*.md
%define __sourcedir media-driver
#sed -i -e 's,-Werror,,' media-driver/cmrtlib/linux/CMakeLists.txt

%ifarch i586
sed -i -e 's/-m${ARCH}/-m32/' -e 's/${ARCH}/"32"/' media-driver/media_driver/cmake/linux/media_compile_flags_linux.cmake
%endif

%build
srcroot=`pwd`

%ifarch i586
export CFLAGS="%optflags -D_FILE_OFFSET_BITS=64" \
       CXXFLAGS="%optflags -D_FILE_OFFSET_BITS=64"
%endif

%cmake \
    -DBUILD_SHARED_LIBS:BOOL=OFF -DMEDIA_BUILD_FATAL_WARNINGS:BOOL=OFF
%cmake_build

%install
%cmake_install

# create a profile for exporting LIBVA_DRIVER_NAME variable
%if 0%{?suse_version} >= 1550
mkdir -p %{buildroot}%{_distconfdir}/profile.d
echo "export LIBVA_DRIVER_NAME=iHD" > %{buildroot}%{_distconfdir}/profile.d/intel-media-driver.sh
echo "setenv LIBVA_DRIVER_NAME iHD" > %{buildroot}%{_distconfdir}/profile.d/intel-media-driver.csh
%else
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
echo "export LIBVA_DRIVER_NAME=iHD" > %{buildroot}%{_sysconfdir}/profile.d/intel-media-driver.sh
echo "setenv LIBVA_DRIVER_NAME iHD" > %{buildroot}%{_sysconfdir}/profile.d/intel-media-driver.csh
%endif

%files
%doc media-driver/README.md
%license media-driver/LICENSE.md
%{_libdir}/dri
%if 0%{?suse_version} >= 1550
%dir %{_distconfdir}/profile.d
%{_distconfdir}/profile.d/*
%else
%{_sysconfdir}/profile.d/*
%endif

%files -n libigfxcmrt%{so_ver}
%{_libdir}/libigfxcmrt.so.%{so_ver}
%{_libdir}/libigfxcmrt.so.%{so_ver}.*

%files -n libigfxcmrt-devel
%doc media-driver/cmrtlib/README.md
%{_includedir}/igfxcmrt
%{_libdir}/libigfxcmrt.so
%{_libdir}/pkgconfig/igfxcmrt.pc

%changelog
