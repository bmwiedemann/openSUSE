#
# spec file for package tfupdate
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           tfupdate
Version:        0.9.3
Release:        0
Summary:        Update version constraints in your Terraform configurations
License:        MPL-2.0
URL:            https://github.com/minamijoyo/tfupdate
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.24

%description
Features

* Update version constraints of Terraform core, OpenTofu core, providers, and
  modules
* Update dependency lock files (.terraform.lock.hcl) without Terraform CLI
* Update all your Terraform configurations and lock files recursively under a
  given directory
* Get the latest release version from the GitHub, GitLab, Terraform Registry,
  or OpenTofu Registry
* Terraform v0.12+ support

If you integrate tfupdate with your favorite CI or job scheduler, you can check
the latest release daily and create a Pull Request automatically.

%prep
%autosetup -p1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o ./bin/%{name}

%install
# Install the binary.
install -D -m 0755 ./bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
%{buildroot}/%{_bindir}/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
