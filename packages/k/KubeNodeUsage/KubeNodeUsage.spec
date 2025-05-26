#
# spec file for package KubeNodeUsage
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


Name:           KubeNodeUsage
Version:        3.0.4
Release:        0
Summary:        Provides insights into Kubernetes node and pod usage
License:        MIT
URL:            https://github.com/AKSarav/KubeNodeUsage
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.23
BuildRequires:  zsh

%description
KubeNodeUsage is a Terminal App designed to provide insights into Kubernetes
node and pod usage. It offers both interactive exploration and command-line
filtering options to help you analyze your cluster effectively right from your
terminal .

%prep
%autosetup -p 1 -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
