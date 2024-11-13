#
# spec file for package goldpinger
#
# Copyright (c) 2023 SUSE LLC
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


Name:           goldpinger
Version:        3.10.2
Release:        0
Summary:        Tests and displays connectivity between nodes in a Kubernetes cluster
License:        Apache-2.0
URL:            https://github.com/bloomberg/goldpinger
Source:         goldpinger-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.23

%description
Goldpinger makes calls between its instances to monitor your networking. It
runs as a DaemonSet on Kubernetes and produces Prometheus metrics that can be
scraped, visualised and alerted on.

Oh, and it gives you the graph below for your cluster.

%prep
%autosetup -p 1 -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.Version=v%{version} \
   -X main.Build=$BUILD_DATE" \
   -o bin/%{name} ./cmd/%{name}

%install
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
