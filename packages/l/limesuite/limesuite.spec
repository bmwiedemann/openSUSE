#
# spec file for package limesuite
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2017-2023, Martin Hauke <mardnh@gmx.de>
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


# Upstream sets SOVERSION to "<major>.<minor>-1" (LIME_SUITE_SOVER in
# CMakeLists.txt), so the shipped SONAME is libLimeSuite.so.23.11-1.
# Keep both spellings in sync: sonamever is the SONAME as it appears in
# the file name, sover the same value as it appears in the package name.
%define sonamever 23.11-1
%define sover 23_11-1
%define libname libLimeSuite%{sover}
%define soapy_modver 0.8-3
Name:           limesuite
Version:        23.11.0
Release:        0
Summary:        Collection of software supporting LMS7-based hardware
License:        Apache-2.0
URL:            https://myriadrf.org/projects/lime-suite/
#Git-Clone:     https://github.com/myriadrf/LimeSuite.git
Source:         https://github.com/myriadrf/LimeSuite/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
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
Requires:       %{name}-udev
# Until now this library was packaged as libLimeSuite23_11-0, a name that
# did not match the SONAME it ships. Both names own the same library
# paths, so the rename needs an explicit replacement. The Obsoletes is
# deliberately unversioned: the released libLimeSuite23_11-0 carries a
# higher release number than a fresh build of the renamed package, so a
# "< %%{version}-%%{release}" form would never match it. No matching
# Provides is added: every consumer outside this source package binds to
# the SONAME libLimeSuite.so.23.11-1 rather than to the package name,
# and a Provides would only trade rpmlint's obsolete-not-provided for
# its self-obsoletion.
Obsoletes:      libLimeSuite23_11-0

%description -n %{libname}
Lime Suite is a collection of software supporting several hardware
platforms and other tools for developing with LMS7-based hardware.

%package udev
Summary:        Udev rules for LimeSDR
BuildArch:      noarch

%description udev
Udev rules for Lime Suite

%package devel
Summary:        Development files for libLimeSuite
Requires:       %{libname} = %{version}

%description devel
Libraries and header files for developing applications that want to make
use of libLimeSuite.

%package -n soapysdr%{soapy_modver}-module-lms7
Summary:        SoapySDR LMS7 support module

%description -n soapysdr%{soapy_modver}-module-lms7
Soapy LMS7 - LimeSDR device support for Soapy SDR.
A Soapy module that supports LimeSDR devices within the Soapy API.

%prep
%autosetup -n LimeSuite-%{version}

# HACK: set udev permissions to 666
sed -i 's|MODE="660"|MODE="666"|g' udev-rules/64-limesuite.rules

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DCMAKE_AUTOSET_INSTALL_RPATH=FALSE \
  -DUDEV_RULES_PATH=%{_udevrulesdir} \
  -DCMAKE_C_STANDARD=17 \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
%ifarch x86_64
  -DENABLE_SIMD_FLAGS="SSE3" \
%else
  -DENABLE_SIMD_FLAGS="none" \
%endif
  -DLIME_SUITE_EXTVER=release
%cmake_build

%install
%cmake_install

# Upstream sets both VERSION and SOVERSION on the library, so cmake
# installs the real file under the version-suffixed name
# libLimeSuite.so.23.11.0 and leaves the SONAME libLimeSuite.so.23.11-1
# as a symlink to it. A versioned path that is not the SONAME
# file-conflicts between package versions, so make the SONAME the real
# file and keep it the only versioned path this package ships.
rm %{buildroot}%{_libdir}/libLimeSuite.so.%{sonamever}
mv %{buildroot}%{_libdir}/libLimeSuite.so.%{version} \
   %{buildroot}%{_libdir}/libLimeSuite.so.%{sonamever}

%ldconfig_scriptlets -n %{libname}

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
%{_libdir}/libLimeSuite.so.%{sonamever}

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
