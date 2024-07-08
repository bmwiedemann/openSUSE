#
# spec file for package feroxbuster
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2022-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           feroxbuster
Version:        2.10.4
Release:        0
Summary:        A recursive content discovery tool
License:        MIT
Group:          Productivity/Networking/Diagnostic
URL:            https://epi052.github.io/feroxbuster-docs/
#Git-Clone:     https://github.com/epi052/feroxbuster.git
Source:         https://github.com/epi052/feroxbuster/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  rust
Suggests:       seclists

%description
Forced browsing is an attack where the aim is to enumerate and access
resources that are not referenced by the web application, but are
still accessible by an attacker.

feroxbuster uses brute force combined with a wordlist to search for
unlinked content in target directories. These resources may store
sensitive information about web applications and operational systems,
such as source code, credentials, internal network addressing, etc...

This attack is also known as Predictable Resource Location, File
Enumeration, Directory Enumeration, and Resource Enumeration.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Productivity/Networking/Diagnostic
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
cargo install --no-track --root=%{buildroot}%{_prefix} --path .
install -D -m0644 shell_completions/feroxbuster.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license LICENSE
%doc ferox-config.toml.example README.md
%{_bindir}/feroxbuster

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
