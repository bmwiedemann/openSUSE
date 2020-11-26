#
# spec file for package easy-rsa
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2015 Stefan Jakobs.
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


%define pname   EasyRSA

Name:           easy-rsa
Version:        3.0.8
Release:        0
Summary:        CLI utility to build and manage a PKI CA
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://github.com/OpenVPN/easy-rsa
Source:         https://github.com/OpenVPN/%{name}/releases/download/v%{version}/%{pname}-%{version}.tgz
Source1:        https://github.com/OpenVPN/%{name}/releases/download/v%{version}/%{pname}-%{version}.tgz.sig
# https://github.com/OpenVPN/easy-rsa/tree/master/release-keys
Source2:        %{name}.keyring
Patch100:       suse-packaging.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
easy-rsa is a CLI utility to build and manage a Public Key Infrastructure
(PKI). Once the Certificate Authority (CA) is created, you can request and sign
certificates, including sub-CAs, and create Certificate Revokation Lists (CRL).

%prep
%setup -q -n %{pname}-%{version}
%patch100

%build

%install
install -dm0755 %{buildroot}/%{_sysconfdir}/%{name}/
install -dm0755 %{buildroot}/%{_sysconfdir}/%{name}/x509-types
install -Dm0644 vars.example %{buildroot}/%{_sysconfdir}/%{name}/
install -Dm0644 openssl-easyrsa.cnf %{buildroot}/%{_sysconfdir}/%{name}/
install -Dm0644 x509-types/* %{buildroot}/%{_sysconfdir}/%{name}/x509-types/
install -Dm0755 easyrsa %{buildroot}/%{_bindir}/easyrsa

%files
%defattr(-,root,root)
%doc ChangeLog README.md README.quickstart.md
%doc doc/*
%if 0%{?sle_version} == 11 || 0%{?sle_version} <= 120400
%doc COPYING.md gpl-2.0.txt
%else
%license COPYING.md gpl-2.0.txt
%endif
%{_bindir}/easyrsa
%config(noreplace) %{_sysconfdir}/%{name}

%changelog
