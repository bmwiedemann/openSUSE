#
# spec file for package editorconfig-checker
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


%define executable_name ec

Name:           editorconfig-checker
Version:        3.1.1
Release:        0
Summary:        Tool to verify that your files are in harmony with your .editorconfig
License:        MIT
URL:            https://github.com/editorconfig-checker/editorconfig-checker
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  go >= 1.22
BuildRequires:  zsh
Provides:       ec = %{version}

%description
This is a tool to check if your files consider your .editorconfig rules. Most
tools—like linters, for example—only test one filetype and need an extra
configuration. This tool only needs your .editorconfig to check all files.

If you don't know about editorconfig already you can read about it here:
editorconfig.org.

%prep
%autosetup -p 1 -a 1

%build
go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X main.version=v%{version}" \
   -o bin/%{executable_name} ./cmd/%{name}

%install
# Install the binary.
install -D -m 0755 bin/%{executable_name} %{buildroot}/%{_bindir}/%{executable_name}

%check
%{buildroot}/%{_bindir}/%{executable_name} -version | grep v%{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{executable_name}

%changelog
