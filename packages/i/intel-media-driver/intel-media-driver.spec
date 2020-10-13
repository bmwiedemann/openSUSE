#
# spec file for package intel-media-driver
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


%define so_ver	7

Name:           intel-media-driver
Version:        20.3.0
Release:        0
Summary:        Intel Media Driver for VAAPI
License:        MIT AND BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/intel/media-driver
Source:         https://github.com/intel/media-driver/archive/intel-media-%{version}.tar.gz
Source1:        generate-supplements.sh
Patch1:         Werror-initialize-in-right-order.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  gmmlib-devel >= 20.3.2
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libva) >= 1.9.0
BuildRequires:  pkgconfig(pciaccess)
ExclusiveArch:  x86_64
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000A84sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001602sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001606sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000160Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000160Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000160Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000160Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001612sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001616sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000161Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000161Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000161Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000161Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001622sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001626sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000162Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000162Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000162Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000162Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000163Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001902sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001906sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000190Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000190Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000190Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001912sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001913sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001915sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001916sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001917sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000191Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000191Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000191Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000191Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001921sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001923sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001926sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001927sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000192Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000192Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000192Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001932sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000193Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000193Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000193Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001A84sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00001A85sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003184sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003185sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E90sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E91sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E92sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E93sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E94sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E96sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E98sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E99sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E9Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E9Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003E9Csv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA0sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA1sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA2sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA3sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA4sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA5sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA6sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA7sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA8sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00003EA9sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00004500sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00004541sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00004551sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00004571sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00004E51sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00004E61sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00004E71sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005902sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005906sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005908sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000590Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000590Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000590Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005912sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005913sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005915sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005916sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005917sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000591Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000591Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000591Csv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000591Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000591Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005921sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005923sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005926sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005927sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000592Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000592Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005932sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000593Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A41sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A42sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A44sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A49sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A4Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A50sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A51sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A52sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A54sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A59sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A5Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A5Csv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A84sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00005A85sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d000087C0sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d000087CAsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A50sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A51sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A52sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A53sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A54sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A56sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A57sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A58sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A59sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A5Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A5Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A5Csv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A5Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00008A71sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009A40sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009A49sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009A59sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009A60sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009A68sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009A70sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009A78sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009AC0sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009AC9sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009AD9sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009AF8sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009B21sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009B41sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BA0sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BA2sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BA4sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BA5sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BA8sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BAAsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BABsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BACsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BC0sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BC2sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BC4sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BC5sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BC6sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BC8sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BCAsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BCBsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BCCsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BE6sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00009BF6sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d0000FF05sv*sd*bc*sc*i*)

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
pushd media-driver
%patch1 -p1
popd
%define __sourcedir media-driver
sed -i -e 's,-Werror,,' media-driver/cmrtlib/linux/CMakeLists.txt

%build
srcroot=`pwd`
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
