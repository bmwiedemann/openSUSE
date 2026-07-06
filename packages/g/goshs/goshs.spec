#
# spec file for package goshs
#
# Copyright (c) 2021-2026, Martin Hauke <mardnh@gmx.de>
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

Name:           goshs
Version:        2.1.4
Release:        0
Summary:        A simple HTTP server
License:        MIT
Group:          Productivity/Networking/Web/Servers
URL:            https://goshs.de/
#Git-Clone:     https://github.com/patrickhener/goshs.git
Source:         https://github.com/patrickhener/goshs/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  zsh
BuildRequires:  fish
BuildRequires:  go >= 1.24.1
BuildRequires:  golang-packaging
# shared-mime-info needed for tests
BuildRequires:  shared-mime-info
%{go_provides}

%description
goshs is a replacement for Python's SimpleHTTPServer.
It allows uploading and downloading via HTTP/S with either
self-signed certificate or user provided certificate and
you can use HTTP basic auth.

%prep
%autosetup -p 1 -a 1

%build
go build \
  -mod=vendor \
  -buildmode=pie \
  -o goshs.bin .

%install
install -Dm 0755 goshs.bin %{buildroot}%{_bindir}/goshs

for shell in bash fish zsh; do
  %{buildroot}%{_bindir}/goshs --completion "$shell"
done
install -Dm 0644 /home/abuild/.local/share/bash-completion/completions/goshs %{buildroot}/%{_datadir}/bash-completion/completions/%{name}.bash
install -Dm 0644 /home/abuild/.config/fish/completions/goshs.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm 0644 /home/abuild/.local/share/zsh/site-functions/_goshs %{buildroot}/%{_datadir}/zsh/site-functions/_%{name}

%check
%make_build run-unit-no-network

%files
%license LICENSE
%doc README.md
%doc example/goshs.json.example
%{_bindir}/goshs
%{_datadir}/bash-completion/completions/goshs.bash
%dir %{_datadir}/fish
%{_datadir}/fish/*
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
