#
# spec file for package termshark
#
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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
# nodebuginfo

%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

Name:           termshark
Version:        2.4.0
Release:        0
Summary:        A terminal UI for tshark
License:        MIT
Group:          Productivity/Networking/Security
URL:            https://termshark.io/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  golang(API) >= 1.13
# Only tshark from wireshark package is required
# Separate package wireshark-cli or tshark would reduce TUI footprint for images and containers
Requires:       wireshark

%description
Termshark is a TUI for tshark inspired by Wireshark. It can read pcap files or
sniff live network interfaces, filter pcaps or live captures using Wireshark's
display filters, reassemble and inspect TCP and UDP flows, view network
conversations by protocol, and copy ranges of packets to the clipboard from the
terminal.

%prep
%autosetup -a 1

%build
# Build the binary.
go build \
   -mod=vendor \
   -tags extended \
   -buildmode=pie \
   ./cmd/termshark

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
