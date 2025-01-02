#
# spec file for package helm-schema
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


Name:           helm-schema
Version:        0.18.1
Release:        0
Summary:        Generate jsonschemas from helm charts
License:        MIT
URL:            https://github.com/dadav/helm-schema
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.23.1

%description
This tool tries to help you to easily create some nice JSON schema for your helm chart.

By default it will traverse the current directory and look for Chart.yaml
files. For every file, helm-schema will try to find one of the given value
filenames. The first files found will be read and a jsonschema will be created.
For every dependency defined in the Chart.yaml file, a reference to the
dependencies JSON schema will be created.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/%{name} ./cmd/helm-schema

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
%{buildroot}/%{_bindir}/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
