#
# spec file for package terraform-provider-aws
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


Name:           terraform-provider-aws
Version:        2.59.0
Release:        0
Summary:        Terraform provider for Amazon Web Services (AWS)
License:        MPL-2.0
Group:          System/Management
URL:            https://github.com/terraform-providers/terraform-provider-aws
Source:         %{name}-%{version}.tar.xz
%if 0%{?suse_version}
%{go_nostrip}
%endif
%if 0%{?ubuntu_version}
BuildRequires:  debhelper
BuildRequires:  dh-golang
BuildRequires:  golang-go
BuildRequires:  libvirt-dev
BuildRequires:  pkgconfig
BuildRequires:  xz-utils
%else
Requires:       terraform >= 0.12.0
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  golang
%endif
%if 0%{?suse_version}
BuildRequires:  golang(API) >= 1.14
BuildRequires:  golang-packaging
BuildRequires:  xz
%endif
%endif
%if 0%{?suse_version}
%{go_provides}
%endif

%description
This is a terraform provider that lets you provision servers on Amazon Web
Services via Terraform.

%prep
%setup -q

%build
%{goprep} github.com/terraform-providers/terraform-provider-aws
%{gobuild} -mod=vendor ""
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}_v%{version}

%install
%{goinstall}

%files
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}_v%{version}

%changelog
