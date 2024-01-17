#
# spec file for package terraform-provider-libvirt
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


Name:           terraform-provider-libvirt
Version:        0.7.1
Release:        0
Summary:        Terraform provider for kvm hypervisors via libvirt
License:        MPL-2.0
Group:          System/Management
URL:            https://github.com/dmacvicar/terraform-provider-libvirt/
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source99:       %{name}-rpmlintrc
%if 0%{?suse_version}
%{go_nostrip}
%endif
%if 0%{?ubuntu_version}
BuildRequires:  debhelper
BuildRequires:  dh-golang
BuildRequires:  golang-go
BuildRequires:  libvirt-dev
BuildRequires:  pkg-config
BuildRequires:  xz-utils
%else
BuildRequires:  libvirt-devel
BuildRequires:  xz
Requires:       libvirt-client
%if 0%{?suse_version}
Requires:       mkisofs
%else
Requires:       genisoimage
%endif
# Terraform is not available for 32bit platforms
ExcludeArch:    %ix86 %arm
Requires:       terraform >= 0.12.0
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  golang
%endif
%if 0%{?suse_version}
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) = 1.18
%endif
%endif
%if 0%{?suse_version}
%{go_provides}
%endif

%description
This is a terraform provider that lets you provision servers on a libvirt host
via Terraform.

%prep
%setup -qa1

%build
export GOFLAGS="-mod=vendor"
%if 0%{?suse_version}
%{goprep} github.com/dmacvicar/terraform-provider-libvirt
%{gobuild}
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?ubuntu_version}
mkdir -p ./_build/src/github.com/dmacvicar
ln -s $(pwd) ./_build/src/github.com/dmacvicar/terraform-provider-libvirt
export GOPATH=$(pwd)/_build
cd _build/src/github.com/dmacvicar/terraform-provider-libvirt
go build -ldflags "-X main.version=%{version}" .
%endif

%install
export GOFLAGS="-mod=vendor"
%if 0%{?suse_version}
%{goinstall}
rm -rf %{buildroot}/%{_libdir}/go/contrib
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?ubuntu_version}
export GOPATH=$(pwd)/_build
mkdir -p %{buildroot}%{_bindir}
export GOBIN=%{buildroot}%{_bindir}
cd _build/src/github.com/dmacvicar/terraform-provider-libvirt
go install -ldflags "-X main.version=%{version}"
%endif

# take the + out of the rpm version
VERSION=$(echo "%{version}" | cut -d '+' -f 1)
PROVIDER_OS_PATH="$(go env GOOS)_$(go env GOARCH)"

# for terraform v0.13
mkdir -p %{buildroot}%{_datadir}/terraform/plugins/registry.terraform.io/dmacvicar/libvirt/${VERSION}/${PROVIDER_OS_PATH}
ln -s %{_bindir}/terraform-provider-libvirt %{buildroot}%{_datadir}/terraform/plugins/registry.terraform.io/dmacvicar/libvirt/${VERSION}/${PROVIDER_OS_PATH}/terraform-provider-libvirt

curr=$PWD
# extract the binary to be published
if [ -d %{_topdir}/OTHER ]; then
    cd %{buildroot}%{_bindir}
    tar zcf %{_topdir}/OTHER/%{name}-%{version}.%{_repository}.%{_arch}.tar.gz %{name}
fi
cd $curr

%files
%license LICENSE
%doc README.md
%{_datadir}/terraform
%{_bindir}/%{name}

%changelog
