#
# spec file for package certinfo
#
# Copyright (c) 2025 SUSE LLC
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

Name:           certinfo
Version:        1.0.37+git20250707.e2340ba
Release:        0
Summary:        Print x509 certificate info
License:        MIT
URL:            https://github.com/pete911/%{name}
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
### Temporary until go1.22 is default
#BuildRequires:  golang-packaging
BuildRequires:  go >= 1.24
#####
BuildRequires:  pkgconfig(x11)

%description
Similar to openssl x509 -in <file> -text command, but handles chains, multiple files and TCP addresses. TLS/SSL version prints as well when using TCP address argument.

%prep
%setup -q -a 1

%build
go build \
  -mod=vendor \
  -buildmode=pie \
  -ldflags "-X main.Version=%{version}"

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog

