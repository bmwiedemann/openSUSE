#
# spec file for package tcping
#
# Copyright (c) 2022, Martin Hauke <mardnh@gmx.de>
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

Name:           tcping
Version:        1.12.1
Release:        0
Summary:        A ping program for TCP ports
License:        MIT
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/pouriyajamshidi/tcping
#Git-Clone:     https://github.com/pouriyajamshidi/tcping.git
Source:         https://github.com/pouriyajamshidi/tcping/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go >= 1.18
BuildRequires:  golang-packaging
%{go_provides}

%description
TCPing will send TCP probes to an IP address or a hostname specified
by you and prints the result.
It works with both IPv4 and IPv6.

TCPING uses different TCP sequence numbering for successful and
unsuccessful probes, so that when you look at the results and spot
a failed probe, understanding the total packet drops to that point
would be illustrative enough.

 * Monitor your network connection.
 * Determine packet loss.
 * Analyze the network's latency.
 * Show min/avg/max probes latency.
 * Use the -r flag to retry hostname resolution after a predetermined
   number of ping failures. If you want to test your DNS load
   balancing or Global Server Load Balancer (GSLB), you should
   utilize this option..
 * Print connection statistics on Enter key press.
 * Display the longest encountered downtime and uptime duration and
   time.
 * Monitor and audit your peers network.
 * Calculate the total uptime/downtime when conducting a maintenance.
 * An alternative to ping in environments that ICMP is blocked.

%prep
%autosetup -p 1 -a 1

%build
%{goprep} github.com/pouriyajamshidi/tcping
%{gobuild} -mod=vendor .

%install
%{goinstall}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/tcping

%changelog
