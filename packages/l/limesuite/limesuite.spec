#
# spec file for package limesuite
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017-2020, Martin Hauke <mardnh@gmx.de>
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


%define sover 20_10-1
%define libname libLimeSuite%{sover}
%define soapy_modver 0.7
Name:           limesuite
Version:        20.10.0
Release:        0
Summary:        Collection of software supporting LMS7-based hardware
License:        Apache-2.0
Group:          Productivity/Hamradio/Other
URL:            https://myriadrf.org/projects/lime-suite/
#Git-Clone:     https://github.com/myriadrf/LimeSuite.git
Source:         https://github.com/myriadrf/LimeSuite/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnuplot
BuildRequires:  pkgconfig
BuildRequires:  wxGTK3-devel
BuildRequires:  pkgconfig(SoapySDR) >= %{soapy_modver}
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev)

%description
Lime Suite is a collection of software supporting several hardware
platforms including the LimeSDR, drivers for the LMS7002M transceiver
RFIC, and other tools for developing with LMS7-based hardware. Lime
Suite enables many SDR applications, such as GQRX for example, to
work with supported hardware through the bundled SoapySDR support
module.

%package -n %{libname}
Summary:        Library for Lime Suite
Group:          System/Libraries
Requires:       %{name}-udev

%description -n %{libname}
Lime Suite is a collection of software supporting several hardware
platforms and other tools for developing with LMS7-based hardware.

%package udev
Summary:        Udev rules for LimeSDR
Group:          Hardware/Other

%description udev
Udev rules for Lime Suite

%package devel
Summary:        Development files for libLimeSuite
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libraries and header files for developing applications that want to make
use of libLimeSuite.

%package -n soapysdr%{soapy_modver}-module-lms7
Summary:        SoapySDR LMS7 support module
Group:          System/Libraries

%description -n soapysdr%{soapy_modver}-module-lms7
Soapy LMS7 - LimeSDR device support for Soapy SDR.
A Soapy module that supports LimeSDR devices within the Soapy API.

%prep
%setup -q -n LimeSuite-%{version}

# HACK: set udev permissions to 666
sed -i 's|MODE="660"|MODE="666"|g' udev-rules/64-limesuite.rules

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_AUTOSET_INSTALL_RPATH=FALSE \
  -DUDEV_RULES_PATH=%{_udevrulesdir} \
%ifarch x86_64
  -DENABLE_SIMD_FLAGS="SSE3" \
%else
  -DENABLE_SIMD_FLAGS="none" \
%endif
  -DLIME_SUITE_EXTVER=release
%make_jobs

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig
%postun  -n %{libname} -p /sbin/ldconfig
%post udev
%udev_rules_update

%postun udev
%udev_rules_update

%files
%license COPYING
%doc Changelog.txt README.md
%{_bindir}/LimeUtil
%{_bindir}/LimeSuiteGUI
%{_bindir}/LimeQuickTest
%dir %{_datadir}/Lime
%{_datadir}/Lime/Desktop

%files udev
%{_udevrulesdir}/64-limesuite.rules

%files -n %{libname}
%{_libdir}/libLimeSuite.so.*

%files devel
%{_libdir}/libLimeSuite.so
%{_includedir}/lime
%{_libdir}/pkgconfig/LimeSuite.pc
%{_libdir}/cmake/LimeSuite/

%files -n soapysdr%{soapy_modver}-module-lms7
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libLMS7Support.so

%changelog
