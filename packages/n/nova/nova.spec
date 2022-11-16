#
# spec file for package nova
#
# Copyright (c) 2022 SUSE LLC
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

Name:           nova
Version:        3.4.1
Release:        0
Summary:        Find outdated or deprecated Helm charts running in your cluster
License:        Apache-2.0
URL:            https://github.com/FairwindsOps/nova
Source:         nova-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.17

# found conflict of nova-3.4.0-1.1.x86_64 with python3-novaclient-17.6.0-1.2.noarch
#   /usr/bin/nova
Conflicts:      python3-novaclient

%description
Nova scans your cluster for installed Helm charts, then cross-checks them against all known Helm repositories. If it finds an updated version of the chart you're using, or notices your current version is deprecated, it will let you know.

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
