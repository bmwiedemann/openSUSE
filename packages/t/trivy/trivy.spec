#
# spec file for package trivy
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


Name:           trivy
Version:        0.52.1
Release:        0
Summary:        A Simple and Comprehensive Vulnerability Scanner for Containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/aquasecurity/trivy
Source:         %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  golang(API) = 1.22
BuildRequires:  golang-packaging
BuildRequires:  zstd
Requires:       ca-certificates
Requires:       git-core
Requires:       rpm

%description
Trivy (`tri` pronounced like trigger, `vy` pronounced like envy) is a simple and
comprehensive vulnerability scanner for containers and other artifacts. A
software vulnerability is a glitch, flaw, or weakness present in the software or
in an Operating System. Trivy detects vulnerabilities of OS packages (Alpine,
RHEL, CentOS, etc.) and application dependencies (Bundler, Composer, npm, yarn,
etc.). Trivy is easy to use. Just install the binary and you're ready to
scan. All you need to do for scanning is to specify a target such as an image
name of the container.

%prep
%autosetup -p1 -a1

%build
export CGO_ENABLED=1
go build -o trivy -mod=vendor -buildmode=pie -trimpath -ldflags "-s -w -X=main.version=%{version}" cmd/trivy/main.go

%install
install -D -m 755 trivy %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%doc NOTICE README.md
%{_bindir}/%{name}

%changelog
