#
# spec file for package ansible-terraform-inventory
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

%define executable_name terraform-inventory

Name:           ansible-terraform-inventory
Version:        0.10
Release:        0
Summary:        Generate a dynamic Ansible inventory from a Terraform state file
License:        MIT
URL:            https://github.com/adammck/terraform-inventory
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22
Provides:       %{executable_name} = %{version}

%description
This is a little Go app which generates a dynamic Ansible inventory from a
Terraform state file. It allows one to spawn a bunch of instances with
Terraform, then (re-)provision them with Ansible.

The following providers are supported:

* AWS
* CloudStack
* DigitalOcean
* Docker
* Exoscale
* Google Compute Engine
* Hetzner Cloud
* libvirt
* Linode
* OpenStack
* Packet
* ProfitBricks
* Scaleway
* SoftLayer
* VMware
* Nutanix
* Open Telekom Cloud
* Yandex.Cloud
* Telmate/Proxmox

It's very simple to add support for new providers. See pull requests with the
provider label for examples.

%prep
%autosetup -p 1 -a 1

%build
%ifarch i586 riscv64
CGO_ENABLED=1 go build \
%else
CGO_ENABLED=0 go build \
%endif
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.build_version=v%{version}" \
   -o bin/%{executable_name}

%install
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%check
%{buildroot}/%{_bindir}/%{executable_name} --version | grep v%{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
