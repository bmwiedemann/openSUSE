#
# spec file for package terraform-provider-openstack
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
%global project         terraform-provider-openstack
%global repo            terraform-provider-openstack
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global registry        registry.terraform.io
%global namespace       hashicorp
%global providername    openstack

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

Name:           terraform-provider-openstack
Version:        1.43.0
Release:        0
Summary:        Terraform OpenStack provider
License:        MPL-2.0
Group:          System/Management
URL:            https://github.com/terraform-provider-openstack/terraform-provider-openstack
Source:         %{repo}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source99:       terraform-provider-openstack-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?ubuntu_version}
BuildRequires:  debhelper
BuildRequires:  dh-golang
BuildRequires:  golang-go
BuildRequires:  libvirt-dev
BuildRequires:  pkg-config
BuildRequires:  xz-utils
%else
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  golang
%endif
%if 0%{?suse_version}
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.14
%endif
# Terraform is not available for 32bit platforms
ExcludeArch:    %ix86 %arm
Requires:       mkisofs
Requires:       terraform >= 0.12.0
%endif
%if 0%{?suse_version}
%{go_provides}
%endif

%description
This is a terraform provider that lets you provision servers on an OpenStack platform via Terraform.

%prep
%setup -q -n %{repo}-%{version}
%setup -q -D -T -a 1 -n %{repo}-%{version}

%build
export GO111MODULE=off
export GOPROXY=off
%if 0%{?suse_version}
%goprep %{import_path}
%gobuild
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?ubuntu_version}
mkdir -p ./_build/src/github.com/terraform-providers/
ln -s $(pwd) ./_build/src/github.com/terraform-providers/terraform-provider-openstack
export GOPATH=$(pwd)/_build
cd _build/src/github.com/terraform-providers/terraform-provider-openstack
go build .
%endif

%install
export GO111MODULE=off
export GOPROXY=off
%if 0%{?suse_version}
%goinstall
rm -rf %{buildroot}/%{_libdir}/go/contrib
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?ubuntu_version}
export GOPATH=$(pwd)/_build
mkdir -p %{buildroot}%{_bindir}
export GOBIN=%{buildroot}%{_bindir}
cd _build/src/github.com/terraform-providers/terraform-provider-openstack
go install
%endif
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}_v%{version}
install -d 755 %{buildroot}%{_datadir}/terraform/providers/%{registry}/%{namespace}/%{providername}/%{version}/linux_%{terraformarch}
ln -s %{_bindir}/%{name} %{buildroot}%{_datadir}/terraform/providers/%{registry}/%{namespace}/%{providername}/%{version}/linux_%{terraformarch}/%{name}_v%{version}

curr=$PWD
# extract the binary to be published
if [ -d %{_topdir}/OTHER ]; then
    cd %{buildroot}%{_bindir}
    tar zcf %{_topdir}/OTHER/%{name}-%{version}.%{_repository}.%{_arch}.tar.gz %{name}
fi
cd $curr

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}_v%{version}
%{_datadir}/terraform

%changelog
