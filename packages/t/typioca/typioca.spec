#
# spec file for package typioca
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


Name:           typioca
Version:        2.11.2
Release:        1
Summary:        Minimal terminal based typing speed tester
License:        MIT
Group:          Productivity/Text/Utilities
URL:            https://github.com/bloznelis/typioca
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.22

%description
A typing speed tester in the terminal

Features:
- Time or word/sentence count based typing speed tests
- Proper WPM results based on https://www.speedtypingonline.com/typing-equations
- Multiple word/sentence lists made out of classical books to spice your test up
- Cursor aware word lines
- Interactive menu
- ctrl+w support
- SSH server typioca serve
- Dynamic word lists
- Custom word lists
- Linux/Mac/Win support

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       bash-completion
BuildArch:      noarch
Requires:       %{name}
Supplements:    (%{name} and bash-completion)

%description bash-completion
The official bash completion script for %{name}, generated during the build.

%package zsh-completion
Summary:        ZSH Completion for %{name}
Group:          System/Shells
BuildArch:      noarch
Requires:       %{name}
Supplements:    (%{name} and zsh)

%description zsh-completion
The official zsh completion script for %{name}, generated during the build.

%prep
%autosetup -a 1

%build
# Build the binary.
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
go build

%check
# execute the binary as a basic check
./%{name} --help

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

# Build the shell autocomplete files
%{buildroot}/%{_bindir}/%{name} completion bash > %{name}-autocomplete.bash
%{buildroot}/%{_bindir}/%{name} completion zsh > %{name}-autocomplete.zsh

# Install the shell autocomplete files
install -Dm 644 %{name}-autocomplete.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm 644 %{name}-autocomplete.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%files bash-completion
%{_datadir}/bash-completion

%files zsh-completion
%{_datadir}/zsh

%changelog
