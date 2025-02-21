#
# spec file for package kappanhang
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           kappanhang
Version:        1.3
Release:        0
Summary:        Remotely open audio channels and a serial port to an Icom transceiver
License:        MIT
URL:            https://github.com/nonoo/kappanhang
Source:         https://github.com/nonoo/kappanhang/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  golang-packaging
BuildRequires:  pkgconfig
BuildRequires:  zstd
BuildRequires:  pkgconfig(libpulse-simple)

%description
kappanhang remotely opens audio channels and a serial port to an Icom RS-BA1
server. The app is mainly developed for connecting to the Icom IC-705
transceiver, which has built-in Wi-Fi and RS-BA1 server. All features of the
protocol are implemented including packet retransmission on packet loss.

%prep
%autosetup -p1 -a1

%build
go build \
	-mod=vendor \
	-buildmode=pie \
	%{nil}

%install
install -D -m0755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/kappanhang

%changelog
