#
# spec file for package soapy-remote
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define soapy_modver 0.7
%define soapy_modname soapysdr%{soapy_modver}-module-remote

Name:           soapy-remote
Version:        0.5.1
Release:        0
Summary:        Remote device support for Soapy SDR
License:        BSL-1.0
Group:          Productivity/Hamradio/Other
Url:            https://github.com/pothosware/SoapyRemote/wiki
#Git-Clone:     https://github.com/pothosware/SoapyRemote.git
Source:         https://github.com/pothosware/SoapyRemote/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(SoapySDR)

%description
A Soapy module that supports remote devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        Remote device support for Soapy SDR
Group:          System/Libraries

%description -n %{soapy_modname}
A Soapy module that supports remote devices within the Soapy API.

%prep
%setup -q -n SoapyRemote-%{name}-%{version}

%build
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install
# FIXME: should be handled - disabled for now
rm %{buildroot}//usr/lib/sysctl.d/SoapySDRServer.conf
rm %{buildroot}//usr/lib/systemd/system/SoapySDRServer.service

%files -n %{soapy_modname}
%license LICENSE_1_0.txt
%doc Changelog.txt README.md
%{_bindir}/SoapySDRServer
%{_mandir}/man1/SoapySDRServer.1%{ext_man}
%dir %{_libdir}/SoapySDR/
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libremoteSupport.so

%changelog
