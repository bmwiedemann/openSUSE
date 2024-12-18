#
# spec file for package tailscale
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


Name:           tailscale
Version:        1.78.3
Release:        0
Summary:        The easiest, most secure way to use WireGuard and 2FA
License:        BSD-3-Clause
URL:            https://github.com/tailscale/tailscale
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}d.service
Source3:        %{name}d.defaults
# FIX-CVE-2024-45337
Patch0:         https://github.com/tailscale/tailscale/commit/73128e25230fda8c82696ed0ffef991bce68cecc.patch#/fix-CVE-2024-45337.patch
Patch1:         build-verbose.patch
Patch2:         disable-auto-update.patch
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  git-core
BuildRequires:  golang-packaging
BuildRequires:  zsh
BuildRequires:  golang(API) = 1.23
Requires:       %{default_firewall_backend}
ExcludeArch:    i586
%{?systemd_requires}

%description
Tailscale is a modern VPN built on top of Wireguard. It works like an overlay
network between the computers of your networks using NAT traversal.

%package bash-completion
Summary:        Tailscale bash completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
bash completions for %{name}

%package zsh-completion
Summary:        Tailsacle zsh completion
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
zsh completion for %{name}

%package fish-completion
Summary:        Tailscale fish completion
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
fish completion for %{name}

%prep
%autosetup -a1 -p1

%build
%ifnarch ppc64
export GOFLAGS="-buildmode=pie"
%endif
export VERSION_SHORT=%{version}
export VERSION_LONG=%{version}
export VERSION_GIT_HASH='$(git rev-parse v%{version})'
./build_dist.sh ./cmd/%{name}
./build_dist.sh ./cmd/%{name}d

#generate completions
./%{name} completion bash > ./%{name}.bash
./%{name} completion zsh > ./%{name}.zsh
./%{name} completion fish > ./%{name}.fish

%check
./%{name} version
./%{name}d -version

%install
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0755 %{name}d %{buildroot}%{_sbindir}/%{name}d

# service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}d.service
%if 0%{?suse_version} < 1600
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}d
%endif

# defaults
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/default/%{name}d

install -D -p -m 0644 ./%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -D -p -m 0644 ./%{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}
install -D -p -m 0644 ./%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}

%pre
%service_add_pre %{name}d.service

%post
%service_add_post %{name}d.service

%preun
%service_del_preun %{name}d.service

%postun
%service_del_postun %{name}d.service

%files
%license LICENSE PATENTS
%doc README.md SECURITY.md
%config(noreplace) %{_sysconfdir}/default/%{name}d
%dir %{_sharedstatedir}/%{name}
%{_bindir}/%{name}
%{_sbindir}/%{name}d
%{_unitdir}/%{name}d.service
%if 0%{?suse_version} < 1600
%{_sbindir}/rc%{name}d
%endif

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%{_datadir}/zsh/site-functions/_%{name}

%files fish-completion
%{_datadir}/fish/vendor_completions.d/%{name}

%changelog
