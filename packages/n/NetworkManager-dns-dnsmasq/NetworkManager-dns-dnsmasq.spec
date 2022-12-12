#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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

Name:           NetworkManager-dns-dnsmasq
Version:        1.0
Release:        0
Summary:        NetworkManager dispatcher script for DNS dnsmasq configuration
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            http://www.gnome.org/projects/NetworkManager/
Source0:        dns-dnsmasq.sh
Source1:        NetworkManager-dns-dnsmasq-COPYING
BuildRequires:  NetworkManager
Requires:       NetworkManager
Supplements:    (NetworkManager and dnsmasq)
BuildArch:      noarch

%description
NetworkManager attempts to keep an active network connection
available at all times. The point of NetworkManager is to make
networking configuration and setup as painless and automatic as
possible. If using DHCP, NetworkManager is intended to replace
default routes, obtain IP addresses from a DHCP server, and change
name servers whenever it sees fit.

This package provides a NetworkManager dispatcher script for DNS
dnsmasq configuration.

%prep
cp %{SOURCE1} COPYING

%build

%install
install -m0755 -D %{SOURCE0} %{buildroot}%{_prefix}/lib/NetworkManager/dispatcher.d/dns-dnsmasq.sh

%files
%license COPYING
%{_prefix}/lib/NetworkManager/dispatcher.d/dns-dnsmasq.sh

%changelog
