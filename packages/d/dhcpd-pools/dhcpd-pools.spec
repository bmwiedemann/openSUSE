#
# spec file for package dhcpd-pools
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


Name:           dhcpd-pools
Version:        3.2
Release:        0
Summary:        ISC DHCP pool analysis
License:        BSD-2-Clause
Group:          Productivity/Networking/Other
URL:            http://dhcpd-pools.sourceforge.net/
Source:         http://downloads.sourceforge.net/project/dhcpd-pools/%{name}-%{version}.tar.xz
BuildRequires:  uthash-devel
Requires:       dhcp-server

%description
This is dhcpd-pools ISC dhcp shared network and pool range usage
analysis. Purpose of command is to count usage ratio of each IP range
and shared network pool which ISC dhcpd is in control of users of the
command are most likely ISPs and other organizations that have large
IP space.
This tools can also be used as a Icinga/Nagios plugin.

%prep
%setup -q

%build
%configure \
    --with-dhcpd-conf=%{_sysconfdir}/dhcpd.conf \
    --with-dhcpd-leases=%{_localstatedir}/lib/dhcp/db/dhcpd.leases \
    --docdir=%{_docdir}/%{name}/samples
%make_build

%install
%make_install
mv %{buildroot}/%{_datadir}/dhcpd-pools/{nagios.conf,snmptest.pl} %{buildroot}/%{_docdir}/%{name}/samples/

%check
%make_build check

%files
%license COPYING
%doc README AUTHORS ChangeLog NEWS
%{_docdir}/%{name}/samples/
%{_bindir}/dhcpd-pools
%{_mandir}/man1/dhcpd-pools.1%{?ext_man}

%changelog
