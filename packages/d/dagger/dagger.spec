#
# spec file for package dagger
#
# Copyright (c) 2022 SUSE LLC
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

Name:           dagger
Version:        0.3.5
Release:        0
Summary:        A portable devkit for CI/CD pipelines
License:        GPL-3.0-only
URL:            https://github.com/dagger/dagger
Source:         dagger-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.16

%description
Dagger is a portable devkit for CICD.

Using Dagger, software teams can develop powerful CICD pipelines with minimal effort, then run them anywhere. Benefits include:
* Unify dev and CI environments. Write your pipeline once, Dagger will run it the same everywhere.
* Reduce CI lock-in. No more re-writing everything from scratch every 6 months.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/dagger ./cmd/dagger

%install
# Install the binary.
install -D -m 0755 bin/%{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
