#
# spec file for package terraform-provider-vsphere
#
# Copyright (c) 2020 SUSE LLC
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


# Make sure that the binary is not getting stripped.
%if 0%{?suse_version}
%{go_nostrip}
%endif

Name:           terraform-provider-vsphere
Version:        1.18.3
Release:        0
Summary:        Terraform vSphere provider
License:        MPL-2.0
Group:          System/Management
URL:            https://github.com/terraform-providers/terraform-provider-vsphere
Source:         %{name}-%{version}.tar.xz
%if 0%{?suse_version}
BuildRequires:  golang-packaging
BuildRequires:  xz
BuildRequires:  golang(API) >= 1.8
%endif
Requires:       mkisofs
Requires:       terraform >= 0.10.0
BuildRequires:  git
BuildRequires:  xz
%if 0%{?suse_version}
%{go_provides}
%endif

%description
This is a terraform provider that lets you provision servers on a VMWare vSphere server.

%prep
%setup -q

%build
export GOFLAGS=-mod=vendor
%{goprep} github.com/terraform-providers/terraform-provider-vsphere
%{gobuild} .

%install
export GOFLAGS=-mod=vendor
%{goinstall}

curr=$PWD
# extract the binary to be published
if [ -d %{_topdir}/OTHER ]; then
    cd %{buildroot}%{_bindir}
    tar zcf %{_topdir}/OTHER/%{name}-%{version}.%{_repository}.%{_arch}.tar.gz %{name}
fi
cd $curr

%check
export GOFLAGS=-mod=vendor
%{gotest} github.com/terraform-providers/terraform-provider-vsphere/...

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
