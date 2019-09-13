#
# spec file for package ca-certificates-cacert
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define					certdir %{_datadir}/pki/trust/anchors
Name:           ca-certificates-cacert
Version:        1
Release:        0
Summary:        CAcert root certificates
License:        SUSE-CacertRoot
Group:          Productivity/Networking/Security
Url:            http://www.cacert.org
Source:         http://www.cacert.org/certs/class3.crt#/CAcert_class3.pem
Source1:        http://www.cacert.org/certs/root.crt#/CAcert.pem
Source2:        LICENSE.cacert
BuildRequires:  ca-certificates
BuildRequires:  openssl
BuildRequires:  p11-kit-devel
Requires(post): ca-certificates
Requires(postun): ca-certificates
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
%defattr(-, root, root)
%doc LICENSE
%{certdir}

%changelog
