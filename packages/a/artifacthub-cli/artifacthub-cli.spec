#
# spec file for package artifacthub-cli
#
# Copyright (c) 2025 SUSE LLC
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

%define executable_name ah

Name:           artifacthub-cli
Version:        1.20.0
Release:        0
Summary:        CLI for Artifact Hub
License:        Apache-2.0
URL:            https://github.com/artifacthub/hub
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.23
BuildRequires:  zsh
Provides:       ah = %{version}

%description
Artifact Hub includes a command line interface tool named ah. You can check
that your packages are ready to be listed on AH by using the lint subcommand.

Integrating the linter into your CI workflow may help catching errors early.

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.version=v%{version} \
   -X main.gitCommit=${COMMIT_HASH}" \
   -o bin/%{executable_name} ./cmd/%{executable_name}

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%check
%{buildroot}/%{_bindir}/%{executable_name} version | grep v%{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
