#
# spec file for package certstrap
#
# Copyright (c) 2020 SUSE LLC
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


Name:           certstrap
Version:        1.2.0+git20200507.7cda9d4
Release:        0
Summary:        Tool for bootstrapping CAs, certificate requests, and signed certificates
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/square/certstrap
Source:         %{name}-%{version}.tar.xz
BuildRequires:  golang(API) >= 1.14
ExcludeArch:    s390

%description
Certstrap is a certificate manager for bootstrapping one's own
certificate authority and public key infrastructure.
certstrap can be used if you do not feel like dealing with openssl,
its myriad of options or config files.

%prep
%setup -q

%build
export GOPATH=$HOME/go
go build -v -buildmode=pie -mod vendor

%install
install -d -p %{buildroot}%{_bindir}
install -p -m 0755 certstrap %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/certstrap

%changelog
