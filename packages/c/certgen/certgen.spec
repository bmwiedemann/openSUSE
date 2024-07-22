#
# spec file for package certgen
#
# Copyright (c) 2024 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           certgen
Version:        1.3.0
Release:        0
Summary:        A dead simple tool to generate self signed certificates
License:        Apache-2.0
URL:            https://github.com/minio/certgen
Source:         %{name}-%{version}.tar.gz
BuildRequires:  go >= 1.22

%description
certgen is a simple tool to generate self-signed certificates, and provides SAN
certificates with DNS and IP entries.

%prep
%autosetup

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -trimpath \
   --tags=kqueue \
   -ldflags=" \
   -X main.version=v%{version}" \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
