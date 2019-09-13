#
# spec file for package intel-media-driver
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


%define so_ver	7

Name:           intel-media-driver
Version:        19.2.1
Release:        0
Summary:        Intel Media Driver for VAAPI
License:        MIT AND BSD-3-Clause
Group:          System/Libraries
URL:            https://github.com/intel/media-driver
Source:         https://github.com/intel/media-driver/archive/intel-media-%{version}.tar.gz
Source1:        generate-supplements.sh
Patch0:         Werror-implicit-function-not-valid-for-C++.patch
Patch1:         Werror-initialize-in-right-order.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(igdgmm)
BuildRequires:  pkgconfig(libva) >= 1.4.1
BuildRequires:  pkgconfig(pciaccess)
ExclusiveArch:  x86_64
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1602sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1606sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X160Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X160Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X160Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X160Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1612sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1616sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X161Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X161Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X161Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X161Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1622sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1626sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X162Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X162Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X162Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X162Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X163Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1902sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1906sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X190Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X190Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X190Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1912sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1913sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1915sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1916sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1917sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X191Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X191Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X191Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X191Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1921sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1923sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1926sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1927sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X192Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X192Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X192Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1932sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X193Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X193Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X193Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1A84sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X1A85sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3184sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3185sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E90sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E91sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E92sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E93sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E94sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E96sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E98sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E99sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E9Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E9Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3E9Csv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA0sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA1sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA2sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA3sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA4sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA5sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA6sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA7sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA8sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X3EA9sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5902sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5906sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5908sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X590Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X590Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X590Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5912sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5913sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5915sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5916sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5917sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X591Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X591Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X591Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X591Esv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5921sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5923sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5926sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5927sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X592Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X592Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5932sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X593Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A41sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A42sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A44sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A49sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A4Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A50sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A51sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A52sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A54sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A59sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A5Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A5Csv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A84sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X5A85sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A50sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A51sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A52sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A53sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A56sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A57sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A58sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A59sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A5Asv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A5Bsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A5Csv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A5Dsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X8A71sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9B21sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9B41sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BA0sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BA2sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BA4sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BA5sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BA8sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BABsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BACsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BC0sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BC2sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BC4sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BC5sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BC8sv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BCAsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BCBsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BCCsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000X9BAAsv*sd*bc*sc*i*)
Supplements:    modalias(xorg-x11-server:pci:v00008086d00000XFF05sv*sd*bc*sc*i*)

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
%patch0 -p1
%patch1 -p1
popd

%define __sourcedir media-driver

%build
srcroot=`pwd`
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%make_jobs

%install
%cmake_install

# create a profile for exporting LIBVA_DRIVER_NAME variable
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
echo "export LIBVA_DRIVER_NAME=iHD" > %{buildroot}%{_sysconfdir}/profile.d/intel-media-driver.sh
echo "setenv LIBVA_DRIVER_NAME iHD" > %{buildroot}%{_sysconfdir}/profile.d/intel-media-driver.csh

%files
%doc media-driver/README.md
%license media-driver/LICENSE.md
%{_libdir}/dri
%{_sysconfdir}/profile.d/*

%files -n libigfxcmrt%{so_ver}
%{_libdir}/libigfxcmrt.so.%{so_ver}
%{_libdir}/libigfxcmrt.so.%{so_ver}.*

%files -n libigfxcmrt-devel
%doc media-driver/cmrtlib/README.md
%{_includedir}/igfxcmrt
%{_libdir}/libigfxcmrt.so
%{_libdir}/pkgconfig/igfxcmrt.pc

%changelog
