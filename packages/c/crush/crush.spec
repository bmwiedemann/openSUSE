#
# spec file for package crush
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
Name:           crush
Version:        0.63.0
Release:        0
Summary:        The glamourous AI coding agent for your favourite terminal
License:        MIT
URL:            https://github.com/charmbracelet/crush
Source0:        crush-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.26.1
BuildRequires:  golang-packaging
BuildRequires:  zstd

%description
Your new coding bestie, now available in your favourite terminal.
Your tools, your code, and your workflows, wired into your LLM of choice.
Crush is a multi-model, flexible, session-based, and LSP-enhanced AI coding agent.
It is extensible and works everywhere, with first-class support in every terminal on Linux.

%prep

%autosetup -p1 -a1

%build
go build \
  -mod=vendor \
  -buildmode=pie -trimpath -ldflags="-s -w \
  -X github.com/charmbracelet/crush/internal/version.Version=%{version}"

%install
mkdir -p %{buildroot}%{_bindir}
install -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%check
CRUSH_DISABLE_PROVIDER_AUTO_UPDATE=1 go test -skip 'github.com/charmbracelet/crush/internal/agent|TestCoderAgent' ./...

%files
%{_bindir}/%{name}
%license LICENSE.md
%doc README.md

%changelog
