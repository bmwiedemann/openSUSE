#
# spec file for package pluto
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

Name:           pluto
Version:        5.3.4
Release:        0
Summary:        A cli tool to help discover deprecated apiVersions in Kubernetes
License:        Apache-2.0
URL:            https://github.com/FairwindsOps/pluto
Source:         pluto-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.16

%description
Pluto is a utility to help users find deprecated Kubernetes apiVersions in their code repositories and their helm releases.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -ldflags="-X main.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
