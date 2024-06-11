#
# spec file for package kubo
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


%define repo github.com/ipfs/kubo
Name:           kubo
Version:        0.29.0
Release:        0
Summary:        IPFS implementation in Go
License:        MIT
Group:          Productivity/Networking/Other
URL:            https://%{repo}
#Source0:        https://%{repo}/archive/v%{version}.tar.gz
# bundle with all deps from ./fetch.sh and ./findfiles.sh :
Source0:        kubo-%version.tar
Source1:        vendor.tar.zst

BuildRequires:  git
# >= 1.14.4 is ambiguous
BuildRequires:  go1.22
BuildRequires:  systemd-rpm-macros
BuildRequires:  zstd
Requires:       fuse
Requires:       nss-myhostname
%systemd_requires

Provides:       go-ipfs = %version
Provides:       ipfs
Obsoletes:      go-ipfs <= 0.21.0

%description
IPFS is a global, versioned, peer-to-peer filesystem. It combines good ideas from Git, BitTorrent, Kademlia, SFS, and the Web. It is like a single bittorrent swarm, exchanging git objects. IPFS provides an interface as simple as the HTTP web, but with permanence built in. You can also mount the world at /ipfs.

%prep
%autosetup -p1 -a1

%build
go build -mod=vendor -buildmode=pie -o ./cmd/ipfs/ipfs ./cmd/ipfs
#make build

%install
#make install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_userunitdir}
mkdir -p %{buildroot}%{_unitdir}

cp cmd/ipfs/ipfs %{buildroot}%{_bindir}
cat << EOF >>  %{buildroot}%{_userunitdir}/ipfs.service
[Unit]
Description=InterPlanetary File System (IPFS) daemon
After=network-online.target
Wants=network-online.target

[Service]
ExecStart=/usr/bin/ipfs daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF
cat << EOF >> %{buildroot}%{_unitdir}/ipfs@.service
[Unit]
Description=InterPlanetary File System (IPFS) daemon
After=network-online.target
Wants=network-online.target

[Service]
User=%i
ExecStart=/usr/bin/ipfs daemon
Restart=on-failure

[Install]
WantedBy=default.target
EOF

rm -rf docs/examples/example-folder/test-dir/

%pre
#service_add_pre ipfs@.service

%post
#service_add_post ipfs@.service

%preun
#service_del_preun ipfs@.service

%postun
#service_del_postun ipfs@.service

%files
%{_bindir}/ipfs
%{_userunitdir}/ipfs.service
%{_unitdir}/ipfs@.service
%license LICENSE*
%doc docs/*

%changelog
