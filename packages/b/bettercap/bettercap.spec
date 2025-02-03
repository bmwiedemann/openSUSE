#
# spec file for package bettercap
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2019-2025, Martin Hauke <mardnh@gmx.de>
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
Version:        2.41.0
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
BuildRequires:  golang(API) >= 1.21
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
install -d %{buildroot}%{_sbindir}
install -d %{buildroot}%{_datadir}/bettercap
install -Dm 0644 bettercap.service  %{buildroot}%{_unitdir}/%{name}.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE.md
%doc README.md
%{_bindir}/bettercap
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%dir %{_datadir}/bettercap

%changelog
