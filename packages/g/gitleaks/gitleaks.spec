#
# spec file for package gitleaks
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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

Name:           gitleaks
Version:        8.18.4
Release:        0
Summary:        Protect and discover secrets using Gitleaks
License:        MIT
URL:            https://github.com/gitleaks/gitleaks
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.19

%description
Gitleaks is a SAST tool for detecting and preventing hardcoded secrets like
passwords, api keys, and tokens in git repos. Gitleaks is an easy-to-use,
all-in-one solution for detecting secrets, past or present, in your code.

%prep
%setup -q
%setup -q -T -D -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags="-X=github.com/zricethezav/gitleaks/v8/cmd.Version=%{version}"

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
