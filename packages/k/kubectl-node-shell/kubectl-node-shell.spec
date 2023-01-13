#
# spec file for package kubectl-node-shell
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


# For kubectl to find this correctly,
# the executable needs to be named kubectl-node_shell
# (with an underscore in node_shell)
%define executable_name kubectl-node_shell

Name:           kubectl-node-shell
Version:        1.6.0
Release:        0
Summary:        Exec into node via kubectl
License:        Apache-2.0
URL:            https://github.com/kvaps/kubectl-node-shell
Source:         kubectl-node-shell-%{version}.tar.gz
Requires:       bash
BuildArch:      noarch

%description
Start a root shell in the node's host OS running.
(formerly known as kubectl-enter)

%prep
%setup -q

%build

%install
sed -i '1s|^.*$|#!%{_bindir}/sh|' %{executable_name}
# Install the binary.
install -D -m 0755 %{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
