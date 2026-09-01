#
# spec file for package soapy-plutosdr
#
# Copyright (c) 2026 SUSE LLC
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
%define soapy_modname soapysdr%{soapy_modver}-module-plutosdr
Name:           soapy-plutosdr
Version:        0.2.2
Release:        0
Summary:        SoapySDR PlutoSDR module
# Legal-Review-Notice: LGPL-2.1-only is deliberate. Upstream ships the bare
# LGPL-2.1 text with no "or later" grant in any source file, README.md or
# debian/copyright; the "any later version" strings in LICENSE are section 13
# and the "How to Apply These Terms" appendix, neither of which is a grant.
License:        LGPL-2.1-only
URL:            https://github.com/pothosware/SoapyPlutoSDR/wiki
#Git-Clone:     https://github.com/pothosware/SoapyPlutoSDR.git
Source:         https://github.com/pothosware/SoapyPlutoSDR/archive/%{name}-%{version}.tar.gz#/SoapyPlutoSDR-%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(libad9361)
BuildRequires:  pkgconfig(libiio) >= 0.9
BuildRequires:  pkgconfig(libusb-1.0)

%description
Soapy PlutoSDR - PlutoSDR device support for Soapy SDR.
A Soapy module that supports PlutoSDR devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        SoapySDR PlutoSDR module
# soname dep pulls only libSoapySDR, which is what dlopens the module;
# require the package too so SoapySDRUtil is there to probe and use it
Requires:       soapy-sdr

%description -n %{soapy_modname}
Soapy PlutoSDR - PlutoSDR device support for Soapy SDR.
A Soapy module that supports PlutoSDR devices within the Soapy API.

%prep
%autosetup -n SoapyPlutoSDR-%{name}-%{version}
# upstream ships README.md with CRLF
sed -i 's/\r$//' README.md

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n %{soapy_modname}
%license LICENSE
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libPlutoSDRSupport.so

%changelog
