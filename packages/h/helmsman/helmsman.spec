#
# spec file for package helmsman
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


Name:           helmsman
Version:        3.17.1
Release:        0
Summary:        Helm Charts as Code
License:        MIT
URL:            https://github.com/Praqma/helmsman
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.21
Requires:       helm

%description
Helmsman is a Helm Charts (k8s applications) as Code tool which allows you to
automate the deployment/management of your Helm charts from version controlled
code.

How does it work?

Helmsman uses a simple declarative TOML file to allow you to describe a desired
state for your k8s applications as in the example toml file. Alternatively YAML
declaration is also acceptable example yaml file.

The desired state file (DSF) follows the desired state specification.

Helmsman sees what you desire, validates that your desire makes sense (e.g.
that the charts you desire are available in the repos you defined), compares it
with the current state of Helm and figures out what to do to make your desire
come true.

%prep
%autosetup -p 1 -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X main.Version=v%{version}-${BUILD_DATE}" \
   -o bin/%{name} ./cmd/%{name}/main.go

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
