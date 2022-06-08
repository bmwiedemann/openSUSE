#
# spec file for package ca-certificates-cacert
#
# Copyright (c) 2022 SUSE LLC
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


%define					certdir %{_datadir}/pki/trust/anchors
Name:           ca-certificates-cacert
Version:        1
Release:        0
Summary:        CAcert root certificates
License:        SUSE-CacertRoot
Group:          Productivity/Networking/Security
URL:            https://www.cacert.org/
# TEMP - source validator rejects validation because root cert expired
# Source:         https://www.cacert.org/class3.crt#/CAcert_class3.pem
# Source1:        https://www.cacert.org/certs/root.crt#/CAcert.pem
Source:         http://www.cacert.org/certs/CAcert_Class3Root_x14E228.crt#/CAcert_class3.pem
# http://www.cacert.org/certs/root_X0F.crt
Source1:        http://www.cacert.org/certs/root_X0F.crt#/CAcert_class1.pem
# from http://www.cacert.org/policy/RootDistributionLicense.html
Source2:        LICENSE.cacert
BuildRequires:  ca-certificates
BuildRequires:  openssl
BuildRequires:  p11-kit-devel
Requires(post): ca-certificates
Requires(postun):ca-certificates
BuildArch:      noarch

%description
This package contains the root certificates from cacert.org

%prep
%setup -qcT
cp %{SOURCE2} LICENSE

%build

%install
install -d -m 755 %{buildroot}/%{certdir}
for i in %{SOURCE0} %{SOURCE1}; do openssl x509 -in $i -out \
	%{buildroot}%{certdir}/${i##*/}; done

%post
update-ca-certificates || true

%postun
update-ca-certificates || true

%files
%license LICENSE
%{certdir}

%changelog
