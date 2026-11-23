#
# spec file for package bettercap
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2019-2026, Martin Hauke <mardnh@gmx.de>
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


Name:           bettercap
Version:        2.42.0
Release:        0
Summary:        Swiss army knife for network attacks and monitoring
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://www.bettercap.org/
#Git-Clone:     https://github.com/bettercap/bettercap.git
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
BuildRequires:  golang-packaging
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
# go.mod requires toolchains support (>= 1.21)
BuildRequires:  golang(API) >= 1.25
BuildRequires:  pkgconfig(libnetfilter_queue)
BuildRequires:  pkgconfig(libusb-1.0)
Requires:       libnetfilter_queue1
Recommends:     iw
Recommends:     wireless-tools
%{go_provides}
%{?systemd_requires}

%description
The Swiss Army knife for WiFi, Bluetooth Low Energy, wireless HID hijacking and
Ethernet networks reconnaissance and MITM attacks.

%prep
%autosetup -a 1
find . -type f -exec sed -i 's|%{_prefix}/local/|%{_prefix}/|g' {} \;

%build
go build \
  -mod=vendor \
  -buildmode=pie \
  -o bettercap .

%install
install -Dm 0755 bettercap %{buildroot}%{_bindir}/bettercap
install -d %{buildroot}%{_datadir}/bettercap

%files
%license LICENSE.md
%doc README.md
%{_bindir}/bettercap
%dir %{_datadir}/bettercap

%changelog
