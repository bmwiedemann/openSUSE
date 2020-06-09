#
# spec file for package terraform-provider-null
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# Make sure that the binary is not getting stripped.
%if 0%{?suse_version}
%{go_nostrip}
%endif

Name:           terraform-provider-null
Version:        2.1.2
Release:        0
License:        MPL-2.0
Summary:        Terraform null-provider
Url:            https://github.com/terraform-providers/terraform-provider-null
Group:          System/Management
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?ubuntu_version}
BuildRequires:  debhelper
BuildRequires:  dh-golang
BuildRequires:  xz-utils
BuildRequires:  golang-go
BuildRequires:  pkg-config
BuildRequires:  libvirt-dev
%else
%if 0%{?fedora} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  golang
%endif
%if 0%{?suse_version}
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.12
BuildRequires:  xz
%endif
Requires:       terraform >= 0.12.0
%endif
%if 0%{?suse_version}
%{go_provides}
%endif

%description
This is a terraform provider that lets you use null files

%prep
%setup -q -n %{name}-%{version}

%build
%goprep github.com/terraform-providers/%{name}
%gobuild -mod=vendor ""
ln -s %{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}_v%{version}

%install
%goinstall
rm -rf %{buildroot}/%{_libdir}/go/contrib

%files
%defattr(-,root,root,-)
%doc CHANGELOG.md README.md
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}_v%{version}

%changelog
