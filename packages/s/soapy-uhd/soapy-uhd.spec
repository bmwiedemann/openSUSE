#
# spec file for package soapy-uhd
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define soapy_modver 0.8-3
%define soapy_modname soapysdr%{soapy_modver}-module-uhd
Name:           soapy-uhd
Version:        0.4.1git20261004
Release:        0
Summary:        Soapy SDR plugins for UHD supported SDR devices
# The three built sources carry the deprecated SPDX id GPL-3.0, which maps
# to GPL-3.0-only. Upstream set that id deliberately in commit ac3ce7f ("The
# intended license is GPL-3 to match libuhd license"); the files were
# BSL-1.0 before it. The only or-later wording in the tree is GNU Radio's,
# inherited into CMakeLists.txt, which is neither built nor shipped.
License:        GPL-3.0-only
URL:            https://github.com/pothosware/SoapyUHD/wiki
#Git-Clone:     https://github.com/pothosware/SoapyUHD.git
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
# upstream dropped BOOST_REQUIRED_COMPONENTS; only the headers are used now
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
# CMakeLists.txt: find_package(SoapySDR "0.7" NO_MODULE REQUIRED)
BuildRequires:  pkgconfig(SoapySDR) >= 0.7
# SoapyUHD#72 dropped all UHD < 4.0 code paths
BuildRequires:  pkgconfig(uhd) >= 4.0

%description
Soapy UHD - Soapy SDR devices for UHD.
A UHD module that supports Soapy devices within the UHD API.

%package -n %{soapy_modname}
Summary:        Soapy SDR plugins for UHD supported SDR devices
# The soname deps only pull libSoapySDR0_8-3; the soapy-sdr package
# (SoapySDRUtil) is never pulled in automatically
Requires:       soapy-sdr
# soapysdr0.7-module-uhd needs to be force dropped
Conflicts:      soapysdr0.7-module-uhd
# Add 'Provides/Obsoletes' entries for future updates
Provides:       soapy-uhd-module = %{soapy_modver}
Obsoletes:      soapy-uhd-module < %{soapy_modver}

%description -n %{soapy_modname}
Soapy UHD - Soapy SDR devices for UHD.
A UHD module that supports Soapy devices within the UHD API.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake
%cmake_build

%check
%ctest

%install
%cmake_install

%files -n %{soapy_modname}
%license COPYING
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libuhdSupport.so
%dir %{_libdir}/uhd
%dir %{_libdir}/uhd/modules
%{_libdir}/uhd/modules/libsoapySupport.so

%changelog
