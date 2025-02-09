#
# spec file for package lazygit
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


Name:           lazygit
Version:        0.45.2
Release:        0
Summary:        Simple terminal UI for git commands
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/jesseduffield/lazygit
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.22
Requires:       git-core

%description
lazygit is a terminal UI for git commmands that helps make common and complex
git operations easy and accessible without requiring expertise with the git
command line.

%prep
%autosetup -a 1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%check
# execute the binary as a basic check
./%{name} --help

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
