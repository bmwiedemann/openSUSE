#
# spec file for package renovate-pretty-log
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


Name:           renovate-pretty-log
Version:        0.1.2
Release:        0
Summary:        Two utilities for exploring Renovate debug log files
License:        Apache-2.0
URL:            https://gitlab.com/tanna.dev/renovate-pretty-log/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  golang(API) >= 1.23
BuildRequires:  zsh

%description
Two utilities for exploring Renovate debug log files:

The renovate-pretty-log-tui command provides a Terminal User Interface (TUI)
for interacting with a Renovate debug log export.

The renovate-pretty-log provides a Terminal User Interface (TUI) for
interacting with a Renovate debug log export.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/renovate-pretty-log ./cmd/renovate-pretty-log

go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/renovate-pretty-log-tui ./cmd/renovate-pretty-log-tui

%install
# Install the binary.
install -D -m 0755 bin/renovate-pretty-log %{buildroot}/%{_bindir}/renovate-pretty-log
install -D -m 0755 bin/renovate-pretty-log-tui %{buildroot}/%{_bindir}/renovate-pretty-log-tui

%check
%{buildroot}/%{_bindir}/renovate-pretty-log --help
%{buildroot}/%{_bindir}/renovate-pretty-log-tui --help
%files
%doc README.md
%license LICENSE
%{_bindir}/renovate-pretty-log
%{_bindir}/renovate-pretty-log-tui

%changelog
