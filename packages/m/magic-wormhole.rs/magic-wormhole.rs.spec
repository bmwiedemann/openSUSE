#
# spec file for package magic-wormhole.rs
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


%bcond_without system_openssl
%if %{with system_openssl}
%define build_args --features=native-tls
%endif

%define bin wormhole-rs

Name:           magic-wormhole.rs
Version:        0.7.4
Release:        0
Summary:        Rust implementation of Magic Wormhole
License:        EUPL-1.2
URL:            https://github.com/magic-wormhole/magic-wormhole.rs
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
%if %{with system_openssl}
BuildRequires:  libopenssl-devel
%endif

%description
Rust implementation of Magic Wormhole, with new features and enhancements such as
* Can do direct connections across the internet (NATs) and firewalls
* Automatically copies your code to the clipboard
* Port forwarding in addition to file transfer
* Send a file to multiple people

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       %{name} = %{version}
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Requires:       %{name} = %{version}
Requires:       fish
BuildArch:      noarch

%description fish-completion
Fish command-line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       %{name} = %{version}
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -a 1
rm .cargo/config

%build
%{cargo_build} %{?build_args}

%install
install -Dm 755 -t "%{buildroot}%{_bindir}" target/release/%{bin}

# Completions
for sh in bash zsh fish; do
  ./target/release/%{bin} completion $sh > %{bin}.${sh}
done
install -Dm644 %{bin}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{bin}
install -Dm644 %{bin}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{bin}
install -Dm644 %{bin}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{bin}.fish

%check
%{cargo_test} %{?build_args}

%files
%doc README.md
%license LICENSE
%{_bindir}/%{bin}

%files bash-completion
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*

%changelog
