#
# spec file for package packetdrill
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


Name:           packetdrill
Version:        2.0+git.20241204
Release:        0
Summary:        Testing tool for kernel networking stack
License:        GPL-2.0-only
URL:            https://github.com/google/packetdrill
Source:         %{name}-%{version}.tar.gz
Patch99:        make-build-more-consistent-with-openSUSE-packaging.patch
BuildRequires:  bison
BuildRequires:  flex

%description
The packetdrill scripting tool enables quick, precise tests for entire
TCP/UDP/IPv4/IPv6 network stacks, from the system call layer down to the
NIC hardware. packetdrill currently works on Linux, FreeBSD, OpenBSD, and
NetBSD. It can test network stack behavior over physical NICs on a LAN, or
on a single machine using a tun virtual network device.

%package tests
Summary:        Sample test scripts for packetdrill
BuildArch:      noarch

%description tests
Collection of sample test scripts from Google for packetdrill utility.

%prep
%autosetup -p1

%build
cd gtests/net/packetdrill
CFLAGS="%{optflags} -Wall -Wno-unused-result -Wno-address-of-packed-member -Werror"
%configure
%make_build

%check
cd gtests/net/packetdrill
%make_build tests

%install
cd gtests/net/packetdrill
mkdir -p %{buildroot}%{_bindir}
install packetdrill %{buildroot}%{_bindir}/
find tests/linux -name '*.pkt' -exec chmod 644 {} \;
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r tests/linux/* %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/packetdrill

%files tests
%{_datadir}/%{name}

%changelog
