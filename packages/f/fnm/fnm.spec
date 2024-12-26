#
# spec file for package fnm
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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           fnm
Version:        1.38.1
Release:        0
Summary:        Fast and simple Node.js version manager in Rust
License:        GPL-3.0-only
URL:            https://github.com/Schniz/fnm
Source0:        https://github.com/Schniz/fnm/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
%if 0%{?suse_version}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}
%else
BuildRequires:  cargo >= 1.64
BuildRequires:  rust >= 1.64
%endif

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

%description
fnm is a Node.js version manager in Rust that aims to be
- 🌎 Cross-platform support (macOS, Windows, Linux)
- ✨ Single file, easy installation, instant startup
- 🚀 Built with speed in mind
- 📂 Works with .node-version and .nvmrc files

%prep
%autosetup -a1

%build
%if 0%{?fedora}
unset LIBSSH2_SYS_USE_PKG_CONFIG
export CARGO_AUDITABLE=auditable
export CARGO_FEATURE_VENDORED=1
cargo build --offline --release --all-features
%else
%{cargo_build} --all-features
%endif

%install
%if 0%{?fedora}
unset LIBSSH2_SYS_USE_PKG_CONFIG
export CARGO_AUDITABLE=auditable
export CARGO_FEATURE_VENDORED=1
cargo install --offline --no-track --root="%{buildroot}%{_prefix}" --path .
%else
%{cargo_install}
%endif
export PATH="%{buildroot}%{_bindir}:${PATH}"
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
fnm completions --shell bash > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
fnm completions --shell fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
fnm completions --shell zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%{_bindir}/fnm
%license LICENSE
%doc README.md

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
