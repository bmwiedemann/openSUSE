#
# spec file for package trufflehog
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


Name:           trufflehog
Version:        3.78.2
Release:        0
Summary:        CLI tool to find exposed secrets in source and archives
License:        AGPL-3.0-or-later
URL:            https://github.com/trufflesecurity/trufflehog
Source:         trufflehog-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.22

%description
TruffleHog is a scanning engine that helps find exposed secrets
within e.g. GitHub/GitLab repos, AWS S3 buckets, GCS buckets,
Docker images, Circle CI/Travis CI setups, or in individual files.

%prep
%autosetup -D -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%check
# execute the binary as a basic check
./%{name} --help

%install
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
