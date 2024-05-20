#
# spec file for package telemetrygen
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

Name:           telemetrygen
Version:        0.98.0
Release:        0
Summary:        Telemetry generator for OpenTelemetry
License:        Apache-2.0
URL:            https://github.com/open-telemetry/opentelemetry-collector-contrib
Source0:        opentelemetry-collector-contrib-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        LICENSE
BuildRequires:  go >= 1.22

%description
This utility simulates a client generating traces, metrics, and logs. It is useful for testing and demonstration purposes.

%prep
%autosetup -p 1 -n opentelemetry-collector-contrib-%{version}
%setup -a 1 -n opentelemetry-collector-contrib-%{version}/cmd/telemetrygen/

cp %{SOURCE2} .

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{name} .

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
