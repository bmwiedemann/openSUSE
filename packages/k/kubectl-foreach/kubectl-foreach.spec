#
# spec file for package kubectl-foreach
#
# Copyright (c) 2021 SUSE LLC
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

Name:           kubectl-foreach
Version:        0.2.1
Release:        0
Summary:        Run kubectl commands in all/some contexts in parallel
License:        Apache-2.0
URL:            https://github.com/ahmetb/kubectl-foreach
Source:         kubectl-foreach-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.18

%description
Run a kubectl command in one or more contexts (clusters) in parallel (similar to GNU parallel/xargs).

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   --buildmode=pie

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
