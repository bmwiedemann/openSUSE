#
# spec file for package kubo
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


%define commit acc53c0

Name:           kubo
Version:        0.43.1
Release:        0
Summary:        IPFS implementation in Go
License:        Apache-2.0 AND MIT
URL:            https://github.com/ipfs/kubo
Source0:        %{name}-%{version}.tar
Source1:        vendor.tar.zst
BuildRequires:  fdupes
BuildRequires:  go1.26 >= 1.26.5
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  zstd
Recommends:     fuse
Recommends:     kubo-bash-completion = %{version}
Recommends:     kubo-fish-completion = %{version}
Recommends:     kubo-zsh-completion = %{version}

Provides:       go-ipfs = %{version}
Provides:       ipfs
Obsoletes:      go-ipfs <= 0.25.0

%systemd_requires

%description
IPFS is a global, versioned, peer-to-peer filesystem.
It combines good ideas from Git, BitTorrent, Kademlia, SFS, and the Web.
It is like a single bittorrent swarm, exchanging git objects.
IPFS provides an interface as simple as the HTTP web, but with permanence built in.
You can also mount the world at /ipfs.

%package bash-completion
Summary:        Bash completions for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command-line completion definitions for kubo.

%package zsh-completion
Summary:        Zsh completions for kubo
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion definitions for kubo.

%package fish-completion
Summary:        Fish completions for kubo
Requires:       %{name} = %{version}
Requires:       fish
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish command-line completion definitions for kubo.

%prep
%autosetup -p1 -a1

%build
go build -mod=vendor -buildmode=pie -trimpath \
  -ldflags="-X github.com/ipfs/kubo.CurrentCommit=%{commit} \
            -X github.com/ipfs/kubo.taggedRelease=%{version}" \
  -v -o ./cmd/ipfs/ipfs ./cmd/ipfs

%sysusers_generate_pre misc/systemd/ipfs-sysusers.conf ipfs ipfs.pre

%install
mkdir -p %{buildroot}%{_bindir}
cp cmd/ipfs/ipfs %{buildroot}%{_bindir}

install -D -m 0644 misc/systemd/ipfs.service %{buildroot}%{_unitdir}/ipfs.service
install -D -m 0644 misc/systemd/ipfs-hardened.service %{buildroot}%{_unitdir}/ipfs-hardened.service
install -D -m 0644 misc/systemd/ipfs-api.socket %{buildroot}%{_unitdir}/ipfs-api.socket
install -D -m 0644 misc/systemd/ipfs-gateway.socket %{buildroot}%{_unitdir}/ipfs-gateway.socket
install -D -m 0644 misc/systemd/ipfs-sysusers.conf %{buildroot}%{_sysusersdir}/ipfs.conf

# Fix ExecStart path: upstream uses /usr/local/bin, we package to /usr/bin
sed -i 's|%{_prefix}/local/bin/ipfs|%{_bindir}/ipfs|g' \
  %{buildroot}%{_unitdir}/ipfs.service \
  %{buildroot}%{_unitdir}/ipfs-hardened.service

# Shell completions (built-in, no daemon needed)
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
./cmd/ipfs/ipfs commands completion bash > %{buildroot}%{_datadir}/bash-completion/completions/ipfs
./cmd/ipfs/ipfs commands completion zsh  > %{buildroot}%{_datadir}/zsh/site-functions/_ipfs
./cmd/ipfs/ipfs commands completion fish > %{buildroot}%{_datadir}/fish/vendor_completions.d/ipfs.fish
sed -i '1{/^#!/d;}' \
  %{buildroot}%{_datadir}/bash-completion/completions/ipfs \
  %{buildroot}%{_datadir}/zsh/site-functions/_ipfs \
  %{buildroot}%{_datadir}/fish/vendor_completions.d/ipfs.fish

# Install documentation into the buildroot so duplicate files can be linked.
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a docs/. %{buildroot}%{_docdir}/%{name}/
%fdupes %{buildroot}%{_docdir}/%{name}

%check
./cmd/ipfs/ipfs version

%pre -f ipfs.pre
%service_add_pre ipfs.service ipfs-hardened.service ipfs-api.socket ipfs-gateway.socket

%post
%service_add_post ipfs.service ipfs-hardened.service ipfs-api.socket ipfs-gateway.socket

%preun
%service_del_preun ipfs.service ipfs-hardened.service ipfs-api.socket ipfs-gateway.socket

%postun
%service_del_postun ipfs.service ipfs-hardened.service ipfs-api.socket ipfs-gateway.socket

%files
%{_bindir}/ipfs
%{_unitdir}/ipfs.service
%{_unitdir}/ipfs-hardened.service
%{_unitdir}/ipfs-api.socket
%{_unitdir}/ipfs-gateway.socket
%{_sysusersdir}/ipfs.conf
%license LICENSE LICENSE-MIT LICENSE-APACHE
%{_docdir}/%{name}/

%files bash-completion
%{_datadir}/bash-completion/completions/ipfs

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_ipfs

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/ipfs.fish

%changelog
