#
# spec file for package trivy
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
# nodebuginfo


%define goipath github.com/aquasecurity/trivy

Name:           trivy
Version:        0.9.2
Release:        0
Summary:        Vulnerability Scanner for Containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/aquasecurity/trivy
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.13

%description
A Simple and Comprehensive Vulnerability Scanner for Containers and other Artifacts,
Suitable for CI.

%prep
%setup -q -n %{name}-%{version}
%setup -q -T -D -a 1

%build
%goprep %{goipath}

export CGO_ENABLED=0

%gobuild -mod vendor cmd/trivy

%install
%goinstall

%files
%license LICENSE
%doc README.md
%{_bindir}/trivy

%changelog
