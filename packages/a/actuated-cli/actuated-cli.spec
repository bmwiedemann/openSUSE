#
# spec file for package actuated-cli
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           actuated-cli
Version:        0.2.10
Release:        0
Summary:        CLI for actuated
License:        MIT
URL:            https://github.com/self-actuated/actuated-cli
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
CLI for actuated, which brings "blazingly fast, secure builds to self-hosted CI
runners".

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/self-actuated/actuated-cli/pkg.Version=v%{version} \
   -X github.com/self-actuated/actuated-cli/pkg.GitCommit=${COMMIT_HASH}" \
   -o bin/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%check
ACTUATED_URL="" %{buildroot}/%{_bindir}/%{name} version | grep v%{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
