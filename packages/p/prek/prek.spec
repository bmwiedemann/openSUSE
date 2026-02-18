#
# spec file for package prek
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


Name:           prek
Version:        0.3.3
Release:        0
Summary:        Reimagined version of pre-commit, built in Rust
License:        MIT
URL:            https://github.com/j178/prek
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.90
BuildRequires:  cargo-packaging
# shell completions
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  zsh

# [  521s] rustc-LLVM ERROR: out of memory
ExcludeArch:   %{ix86} armv7hl armv7l armv7l:armv6l:armv5tel armv6hl

%description
prek is a reimagined version of pre-commit, built in Rust. It is designed to be
a faster, dependency-free and drop-in alternative for it, while also providing
some additional long-requested features.

Features

- A single binary with no dependencies, does not require Python or any other
runtime.
- Faster than pre-commit and uses only half the disk space.
- Fully compatible with the original pre-commit configurations and hooks.
- Built-in support for monorepos (i.e. workspace mode).
- Integration with uv for managing Python virtual environments and
dependencies.
- Improved toolchain installations for Python, Node.js, Go, Rust and Ruby,
shared between hooks.
- Built-in Rust-native implementation of some common hooks.

%package -n %{name}-bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description -n %{name}-bash-completion
Bash command line completion support for %{name}.

%package -n %{name}-fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description -n %{name}-fish-completion
Fish command line completion support for %{name}.

%package -n %{name}-zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description -n %{name}-zsh-completion
zsh command line completion support for %{name}.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

# create the bash completion file
mkdir -p %{buildroot}%{_datarootdir}/bash-completion/completions/
COMPLETE=bash %{buildroot}/%{_bindir}/%{name} | sed 's#%{buildroot}##g' > %{buildroot}%{_datarootdir}/bash-completion/completions/%{name}

# create the fish completion file
mkdir -p %{buildroot}%{_datarootdir}/fish/vendor_completions.d/
COMPLETE=fish %{buildroot}/%{_bindir}/%{name} | sed 's#%{buildroot}##g' > %{buildroot}%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

# create the zsh completion file
mkdir -p %{buildroot}%{_datarootdir}/zsh/site-functions/
COMPLETE=zsh %{buildroot}/%{_bindir}/%{name} | sed 's#%{buildroot}##g' > %{buildroot}%{_datarootdir}/zsh/site-functions/_%{name}

%check
%{buildroot}%{_bindir}/%{name} --version | grep %{version}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files -n %{name}-bash-completion
%{_datarootdir}/bash-completion/completions/%{name}

%files -n %{name}-fish-completion
%{_datarootdir}/fish/vendor_completions.d/%{name}.fish

%files -n %{name}-zsh-completion
%{_datarootdir}/zsh/site-functions/_%{name}

%changelog
