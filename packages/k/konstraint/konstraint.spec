#
# spec file for package konstraint
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


Name:           konstraint
Version:        0.43.0
Release:        0
Summary:        A policy management tool for interacting with Gatekeeper
License:        Apache-2.0
URL:            https://github.com/plexsystems/konstraint
Source:         konstraint-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.22

%description
Konstraint is a CLI tool to assist with the creation and management of
templates and constraints when using Gatekeeper.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -ldflags="-X github.com/plexsystems/konstraint/internal/commands.version=%{version}"

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%check
%{buildroot}/%{_bindir}/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
