#
# spec file for package rye
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


Name:           rye
Version:        0.40.0
Release:        0
Summary:        Hassle-free Python project manager in Rust
License:        MIT
URL:            https://github.com/astral-sh/rye
Source0:        https://github.com/astral-sh/rye/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        https://github.com/spdx/license-list-data/archive/refs/tags/v3.24.0.tar.gz#/licenses.tar.gz
BuildRequires:  cargo >= 1.77
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  zstd
Requires:       python3
Recommends:     uv

%description
Rye is a comprehensive project and package management solution for Python. Born
from its creator's desire to establish a one-stop-shop for all Python users,
Rye provides a unified experience to install and manage Python installations,
pyproject.toml based projects, dependencies and virtualenvs seamlessly. It's
designed to accommodate complex projects, monorepos and to facilitate global
tool installations.

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       %{name}
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       %{name}
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       %{name}
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%prep
%autosetup -p1 -a1
# license crate feature 'offline' is bogus and not implemented
pushd vendor/license
mkdir -p license-list-data
tar xf %{SOURCE2} -C license-list-data --strip-components=1
popd

%build
pushd rye
%{cargo_build}
popd

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 -t %{buildroot}%{_bindir}/ %{_builddir}/%{name}-%{version}/target/release/rye

export PATH="%{buildroot}%{_bindir}:${PATH}"
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
rye self completion -s bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
rye self completion -s fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
rye self completion -s zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

# Tests require network
#%%check
#%%cargo_test

%files
%license LICENSE
%doc README.md
%{_bindir}/rye

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/%{name}.fish

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
