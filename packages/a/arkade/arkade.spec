#
# spec file for package arkade
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

Name:           arkade
Version:        0.11.16
Release:        0
Summary:        Open Source Kubernetes Marketplace
License:        Apache-2.0
URL:            https://github.com/alexellis/arkade
Source:         arkade-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
arkade provides a portable marketplace for downloading your favourite devops CLIs and installing helm charts, with a single command.
You can also download CLIs like kubectl, kind, kubectx and helm faster than you can type "apt-get/brew update".

%prep
%autosetup -p1 -a 1

%build
go build \
   -mod=vendor \
   -ldflags="-X main.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
