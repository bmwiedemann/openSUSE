#
# spec file for package fdo-client
#
# Copyright (c) 2021 SUSE LLC
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


Name:           fdo-client
Version:        1.1.4+git20221209.c8ef757
Release:        0
Summary:        FIDO Device Onboard Client
License:        Apache-2.0
Group:          System/Base
URL:            https://github.com/intel/safestringlib/tree/v1.0.0
Source0:        fdo-client-%{version}.tar.xz
Source1:        safestringlib-1.0.0+git20171208.5da1bad.tar.xz
Source2:        tinycbor-1.0.0+git20191022.755f9ef.tar.xz
Source3:        fdo-client-service
Source4:        fdoclient.service
Source5:        README
Patch0:         build.patch
Patch1:         gcc.patch
Requires:       openssl
BuildRequires:  cmake
BuildRequires:  vim
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  libcurl-devel
%{?systemd_ordering}

%description
FDO-Client is a portable implementation of the FIDO Device Onboard Spec.
This component is portable across multiple environments,
including to various microprocessors (MPUs) and microcontrollers (MCUs).

%package devel
Summary:        FIDO Device Onboard Client SDK
Group:          Development/Libraries/C and C++
Requires:       libopenssl-1_1-devel

%description devel
This is a production-ready implementation of the Device component defined
in FIDO Device Onboard Spec published by the FIDO Alliance.
Appropriate security measures should be taken for storing the device
credentials while porting this to different platforms.

%prep
%setup -q
%setup -q -D -a 1
%setup -q -D -a 2
%patch0 -p1
%patch1 -p1

%build
pushd .
cd safestringlib*
mkdir obj
make
popd
cd tinycbor*
make
cd %{_builddir}/%{name}*
export SAFESTRING_ROOT=%{_builddir}/%{name}-%{version}/safestringlib-1.0.0+git20171208.5da1bad
export TINYCBOR_ROOT=%{_builddir}/%{name}-%{version}/tinycbor-1.0.0+git20191022.755f9ef
export BLOB_PATH=%{_sharedstatedir}/%{name}
export RO_BLOB_PATH=%{_datadir}/%{name}
cmake .
make
bash utils/keys_gen.sh .

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_docdir}/%{name}
mkdir -p %{buildroot}/%{_includedir}
mkdir -p %{buildroot}/%{_datadir}/%{name}/data
mkdir -p %{buildroot}/%{_sharedstatedir}/%{name}/data

%{__install} -m 0755 build/linux-client %{buildroot}/%{_bindir}/%{name}
%{__install} -m 0755 %{SOURCE3} %{buildroot}/%{_bindir}/fdo-client-service
%{__install} -D -m 644 %{SOURCE4} %{buildroot}/%{_unitdir}/fdoclient.service
%{__install} -m 0644 %{SOURCE5} %{buildroot}/%{_docdir}/%{name}/README
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcfdoclient

%{__install} -m 644 build/*.a %{buildroot}/%{_libdir}
%{__install} -m 644 include/*.h %{buildroot}/%{_includedir}

%{__install} data/ecdsa* %{buildroot}/%{_datadir}/%{name}/data
%{__install} data/manufacturer_addr.bin %{buildroot}/%{_datadir}/%{name}/data
%{__install} data/max_serviceinfo_sz.bin %{buildroot}/%{_datadir}/%{name}/data
%{__install} data/mfg_proxy.dat %{buildroot}/%{_datadir}/%{name}/data
%{__install} data/owner_proxy.dat %{buildroot}/%{_datadir}/%{name}/data
%{__install} data/raw.blob %{buildroot}/%{_datadir}/%{name}/data
%{__install} data/rv_proxy.dat %{buildroot}/%{_datadir}/%{name}/data

%{__install} data/Normal.blob %{buildroot}/%{_sharedstatedir}/%{name}/data
%{__install} data/platform_aes_key.bin %{buildroot}/%{_sharedstatedir}/%{name}/data
%{__install} data/platform_hmac_key.bin %{buildroot}/%{_sharedstatedir}/%{name}/data
%{__install} data/platform_iv.bin %{buildroot}/%{_sharedstatedir}/%{name}/data
%{__install} data/Secure.blob %{buildroot}/%{_sharedstatedir}/%{name}/data

%pre
%service_add_pre fdoclient.service

%preun
%service_del_preun fdoclient.service

%post
%service_add_post fdoclient.service

%postun
%service_del_postun fdoclient.service

%files
%license LICENSE
%doc README
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/data
%dir %{_sharedstatedir}/%{name}
%dir %{_sharedstatedir}/%{name}/data/
%{_bindir}/%{name}
%{_bindir}/fdo-client-service
%{_datadir}/%{name}/data/*
%{_sharedstatedir}/%{name}/data/*
%{_unitdir}/fdoclient.service
%{_sbindir}/rcfdoclient

%files devel
%license LICENSE
%{_includedir}/*.h
%{_libdir}/*.a

%changelog
