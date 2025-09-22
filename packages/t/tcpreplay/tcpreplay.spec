#
# spec file for package tcpreplay
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           tcpreplay
Version:        4.5.1
Release:        0
Summary:        Network analysis and testing tools
License:        GPL-3.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://tcpreplay.appneta.com/
Source0:        https://github.com/appneta/tcpreplay/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/appneta/tcpreplay/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# CVE-2025-8746 [bsc#1247917], improper input validation and memory bounds checking when processing certain malformed configuration files
Patch0:         tcpreplay-CVE-2025-8746.patch
BuildRequires:  dbus-1-devel
BuildRequires:  libdnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  tcpdump
Requires:       tcpdump
%if 0%{?suse_version} >= 1130
BuildRequires:  libnl3-devel
%else
# only needed for suse_version < 1130 (i.e. SLE11)
BuildRequires:  xz
%endif

%description
Tcpreplay is a suite of utilities for editing and replaying
previously captured network traffic. It was originally designed to
replay malicious traffic patterns to Intrusion Detection/Prevention
Systems, and is meanwhile capable of replaying to web servers. It
supports switches, routers and IP Flow/NetFlow appliances.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -std=gnu11"
%configure \
  --enable-dynamic-link
%make_build

%install
%make_install

%files
%license docs/LICENSE
%doc docs/CHANGELOG
%{_bindir}/*
%{_mandir}/man1/*

%changelog
