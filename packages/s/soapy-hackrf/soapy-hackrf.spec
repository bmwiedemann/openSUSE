#
# spec file for package soapy-hackrf
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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


%define soapy_modver 0.8
%define soapy_modname soapysdr%{soapy_modver}-module-hackrf
Name:           soapy-hackrf
Version:        0.3.4
Release:        0
Summary:        SoapySDR HackRF module
License:        MIT
Group:          Hardware/Other
URL:            https://github.com/pothosware/SoapyHackRF/wiki
#Git-Clone:     https://github.com/pothosware/SoapyHackRF.git
Source:         https://github.com/pothosware/SoapyHackRF/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(libhackrf)

%description
Soapy HackRF - HackRF device support for Soapy SDR.
A Soapy module that supports HackRF devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        SoapySDR HackRF module
Group:          System/Libraries

%description -n %{soapy_modname}
Soapy HackRF - HackRF device support for Soapy SDR.
A Soapy module that supports HackRF devices within the Soapy API.

%prep
%setup -q -n SoapyHackRF-%{name}-%{version}

%build
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install

%files -n %{soapy_modname}
%license LICENSE
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libHackRFSupport.so

%changelog
