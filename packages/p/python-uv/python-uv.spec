#
# spec file for package python-uv
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


%if 0%{?suse_version} && 0%{?suse_version} < 1550
%global force_gcc_version 13
%endif

%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-uv
Version:        0.4.9
Release:        0
Summary:        A Python package installer and resolver, written in Rust
License:        Apache-2.0 OR MIT
URL:            https://github.com/astral-sh/uv
Source0:        https://files.pythonhosted.org/packages/source/u/uv/uv-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module tomli}
BuildRequires:  alts
BuildRequires:  cargo-packaging
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc%{?force_gcc_version}-c++
BuildRequires:  python-rpm-macros
BuildRequires:  rust >= 1.80
BuildRequires:  zstd
Obsoletes:      uv < %{version}
Provides:       uv = %{version}
Requires:       alts
Requires:       python3

%package        fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%python_subpackages

%description
uv is a Python package installer and resolver, written in Rust. Designed as a
drop-in replacement for common pip and pip-tools workflows.

%prep
%autosetup -p1 -a1 -n uv-%{version}

%build
export CARGO_NET_OFFLINE=true
%ifarch %rust_tier1_arches
export CARGO_PROFILE_RELEASE_DEBUG=full
%else
export CARGO_PROFILE_RELEASE_DEBUG=limited
%endif
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%if 0%{?force_gcc_version}
export CC="gcc-%{?force_gcc_version}"
export CXX="g++-%{?force_gcc_version}"
%endif
%pyproject_wheel

%install
export CARGO_NET_OFFLINE=true
%ifarch %rust_tier1_arches
export CARGO_PROFILE_RELEASE_DEBUG=full
%else
export CARGO_PROFILE_RELEASE_DEBUG=limited
%endif
export CARGO_PROFILE_RELEASE_SPLIT_DEBUGINFO=off
export CARGO_PROFILE_RELEASE_STRIP=false
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_clone -a %{buildroot}%{_bindir}/uv
%python_group_libalternatives uv
%python_clone -a %{buildroot}%{_bindir}/uvx
%python_group_libalternatives uvx

export PATH="%{buildroot}%{_bindir}:${PATH}"
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
%{python_expand  # avoid whitespace when using this macro so putting random comment for that
  uv-%{$python_bin_suffix} --generate-shell-completion bash > %{buildroot}%{_datadir}/bash-completion/completions/uv-%{$python_bin_suffix}
  uv-%{$python_bin_suffix} --generate-shell-completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/uv-%{$python_bin_suffix}.fish
  uv-%{$python_bin_suffix} --generate-shell-completion zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_uv-%{$python_bin_suffix}
}

%pre
%python_libalternatives_reset_alternative uv
%python_libalternatives_reset_alternative uvx

%files %{python_files}
%license LICENSE-*
%doc README.md
%python_alternative %{_bindir}/uv
%python_alternative %{_bindir}/uvx
%{python_sitearch}/uv
%{python_sitearch}/uv-%{version}.dist-info

%files %{python_files bash-completion}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/uv-%{python_bin_suffix}

%files %{python_files fish-completion}
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/uv-%{python_bin_suffix}.fish

%files %{python_files zsh-completion}
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_uv-%{python_bin_suffix}

%changelog
