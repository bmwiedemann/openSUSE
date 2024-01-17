#
# spec file for package terraform-provider-azurerm
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


%global provider        github
%global provider_tld    com
%global project         terraform-providers
%global repo            terraform-provider-azurerm
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global registry        registry.terraform.io
%global namespace       hashicorp
%global import_path     %{provider}.%{provider_tld}/%{namespace}/%{repo}
%global providername    azurerm

%ifarch aarch64
%define terraformarch   amd64
%endif
%ifarch ppc64
%define terraformarch   ppc64
%endif
%ifarch ppc64le
%define terraformarch   ppc64le
%endif
%ifarch s390x
%define terraformarch   s390x
%endif
%ifarch %{ix86}
%define terraformarch   i386
%endif
%ifarch x86_64
%define terraformarch   amd64
%endif

%if 0%{?suse_version}
%{go_nostrip}
%endif

Name:           terraform-provider-azurerm
Version:        3.35.0
Release:        0
Summary:        Terraform provider for Azure Resource Manager (AzureRM)
License:        MPL-2.0
Group:          System/Management
URL:            https://github.com/terraform-providers/terraform-provider-azurerm
Source:         %{repo}-%{version}.tar.xz
Source99:       terraform-provider-azurerm-rpmlintrc
%if 0%{?ubuntu_version}
BuildRequires:  debhelper
BuildRequires:  dh-golang
BuildRequires:  golang-go
BuildRequires:  libvirt-dev
BuildRequires:  pkgconfig
BuildRequires:  xz-utils
%else
# Terraform is not available for 32bit platforms
ExcludeArch:    %ix86 %arm
Requires:       terraform >= 1.0.0
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  golang
%endif
%if 0%{?suse_version}
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.12
%endif
%endif
%if 0%{?suse_version}
%{go_provides}
%endif

%description
This is a terraform provider that lets you provision servers on Azure Resource
Manager via Terraform.

%prep
%setup -q

%build
%{goprep} %{import_path}
%{gobuild} -mod=vendor ""

%install
%{goinstall}
rm -rf %{buildroot}/%{_libdir}/go/contrib
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}_v%{version}
ln -s %{_bindir}/%{name}_v%{version} %{buildroot}%{_bindir}/%{name}
install -d 755 %{buildroot}%{_datadir}/terraform/providers/%{registry}/%{namespace}/%{providername}/%{version}/linux_%{terraformarch}
ln -s %{_bindir}/%{name} %{buildroot}%{_datadir}/terraform/providers/%{registry}/%{namespace}/%{providername}/%{version}/linux_%{terraformarch}/%{name}_v%{version}

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}_v%{version}
%{_datadir}/terraform

%changelog
