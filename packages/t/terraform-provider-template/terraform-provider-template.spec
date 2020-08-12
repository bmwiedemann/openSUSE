#
# spec file for package terraform-provider-template
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


Name:           terraform-provider-template
Version:        2.1.2
Release:        0
Summary:        Terraform template-provider
License:        MPL-2.0
Group:          System/Management
URL:            https://github.com/terraform-providers/terraform-provider-template
Source:         %{name}-%{version}.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.8
Requires:       terraform >= 0.12.0
# Make sure that the binary is not getting stripped.
%if 0%{?suse_version}
%{go_nostrip}
%endif
%if 0%{?suse_version}
%{go_provides}
%endif

%description
This is a terraform provider that lets you use template files

%prep
%setup -q

%build
%if 0%{?suse_version}
%{goprep} github.com/terraform-providers/%{name}
%{gobuild} -mod=vendor ""
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?ubuntu_version}
mkdir -p ./_build/src/github.com/terraform-providers
ln -s $(pwd) ./_build/src/github.com/terraform-providers/terraform-provider-template
export GOPATH=$(pwd)/_build
cd _build/src/github.com/terraform-providers/terraform-provider-template
go build -ldflags "-X main.version=%{version}" .
%endif

%install
%if 0%{?suse_version}
%{goinstall}
rm -rf %{buildroot}/%{_libdir}/go/contrib
%endif
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?ubuntu_version}
export GOPATH=$(pwd)/_build
mkdir -p %{buildroot}%{_bindir}
export GOBIN=%{buildroot}%{_bindir}
cd _build/src/github.com/terraform-providers/terraform-provider-template
go install -ldflags "-X main.version=%{version}"
%endif
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}_v%{version}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}_v%{version}

%changelog
