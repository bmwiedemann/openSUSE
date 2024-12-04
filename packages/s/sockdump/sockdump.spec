#
# spec file for package sockdump
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


Name:           sockdump
Version:        20231211
Release:        0
Summary:        Dump UNIX domain socket traffic with eBPF
License:        Unlicense
URL:            https://github.com/mechpen/sockdump
Source:         sockdump-%{version}.tar.xz
BuildRequires:  python-rpm-macros
Requires:       python3-bcc >= 0.32
BuildArch:      noarch

%description
sockdump passively monitors UNIX domain sockets using BPF and dumps any traffic
as plain-text or in pcap format.

%prep
%setup -q

%build

%install
install -Dm 0755 sockdump.py %{buildroot}%{_sbindir}/sockdump

%check

%files
%{_sbindir}/sockdump
%license LICENSE
%doc README.md

%changelog
