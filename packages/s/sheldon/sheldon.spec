#
# spec file for package sheldon
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


Name:           sheldon
Version:        0.8.1
Release:        0
Summary:        Fast, configurable, shell plugin manager
License:        MIT OR Apache-2.0 AND MIT AND Zlib AND LGPL-2.1-or-later AND CC-BY-SA-4.0 AND Apache-2.0 WITH LLVM-exception AND BSD-4-clause AND OpenSSL AND Unicode AND SUSE-GPL-2.0-with-linking-exception
URL:            https://sheldon.cli.rs/
Source:         https://github.com/rossmacarthur/sheldon/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
ExclusiveArch:  %{rust_tier1_arches}

%description
Sheldon is a fast, configurable, command-line tool to manage your shell plugins.

How does it work?

Plugins are specified in a TOML configuration file and Sheldon renders an install script using user configurable templates.

A ~/.zshrc or ~/.bashrc that uses Sheldon simply contains the following.

eval "$(sheldon source)"
Sheldon can manage GitHub or Git repositories, Gists, arbitrary remote scripts or binaries, local plugins, and inline plugins.
Plugins are installed and updated in parallel and as a result Sheldon is blazingly fast.

%package        bash-completion
Summary:        Bash completion for %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description    bash-completion
Bash command line completion support for %{name}.

%package        zsh-completion
Summary:        ZSH completion for %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description    zsh-completion
ZSH command line completion support for %{name}.

%prep
%autosetup -a1

%build
export OPENSSL_NO_VENDOR=1
export LIBSSH_NO_VENDOR=1
export LIBCURL_NO_VENDOR=1

%{cargo_build}

%install
%{cargo_install}
install -Dm0644 completions/sheldon.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/sheldon
install -Dm0644 completions/sheldon.zsh \
    %{buildroot}%{_datadir}/zsh/site-functions/_sheldon

%files
%license LICENSE*
%doc README.md RELEASES.md
%{_bindir}/sheldon

%files bash-completion
%{_datadir}/bash-completion/

%files zsh-completion
%{_datadir}/zsh/

%changelog
