#
# spec file for package tailscale
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.104.7
Release:        0
Summary:        The easiest, most secure way to use WireGuard and 2FA
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND BSD-2-Clause AND ISC AND (FTL OR GPL-2.0-or-later)
URL:            https://github.com/tailscale/tailscale
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}d.service
Source3:        %{name}d.defaults
# license texts of the vendored github.com/golang/freetype, dropped by go mod vendor
Source4:        https://raw.githubusercontent.com/golang/freetype/e2365dfdc4a05e4b8299a783240d4a7d5a65d4e4/licenses/ftl.txt#/freetype-ftl.txt
Source5:        https://raw.githubusercontent.com/golang/freetype/e2365dfdc4a05e4b8299a783240d4a7d5a65d4e4/licenses/gpl.txt#/freetype-gpl.txt
Patch0:         build-verbose.patch
Patch1:         disable-auto-update.patch
BuildRequires:  bash-completion
BuildRequires:  fish
BuildRequires:  git-core
BuildRequires:  go1.27 >= 1.27.4
BuildRequires:  golang-packaging
BuildRequires:  zsh
Requires:       %{default_firewall_backend}
ExcludeArch:    %{ix86}
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

# license texts and NOTICE files of third-party code linked into the binaries
mkdir third-party-licenses
cp -p licenses/tailscale.md third-party-licenses/
cp -p vendor/github.com/aws/aws-sdk-go-v2/LICENSE.txt third-party-licenses/Apache-2.0.txt
cp -p vendor/github.com/aws/aws-sdk-go-v2/NOTICE.txt third-party-licenses/NOTICE.aws-sdk-go-v2
cp -p vendor/github.com/aws/smithy-go/NOTICE third-party-licenses/NOTICE.smithy-go
cp -p vendor/github.com/coreos/go-iptables/NOTICE third-party-licenses/NOTICE.go-iptables
cp -p vendor/go.yaml.in/yaml/v2/NOTICE third-party-licenses/NOTICE.go-yaml-v2
cp -p vendor/github.com/golang/freetype/LICENSE third-party-licenses/LICENSE.freetype
cp -p %{SOURCE4} %{SOURCE5} third-party-licenses/
echo "tailscale is based in part on the work of the FreeType Team (https://freetype.org)." \
  > third-party-licenses/NOTICE.freetype

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
%license LICENSE PATENTS third-party-licenses/*
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
