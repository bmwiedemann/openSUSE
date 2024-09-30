#
# spec file for package kubectl-np-viewer
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

%define executable_name kubectl-np_viewer

Name:           kubectl-np-viewer
Version:        1.0.8
Release:        0
Summary:        Kubectl plugin to visualize network policies rules
License:        Apache-2.0
URL:            https://github.com/runoncloud/kubectl-np-viewer
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.14

%description
A kubectl plugin to visualize network policies rules.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{executable_name} github.com/runoncloud/kubectl-np-viewer/cmd/plugin

%install
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
