#
# spec file for package dhtest
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           dhtest
Version:        1.5
Release:        0
Summary:        A DHCP client simulation tool
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/saravana815
#Git-Clone:     https://github.com/saravana815/dhtest.git
Source:         https://github.com/saravana815/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
dhtest - linux DHCP client simulation tool. It can simulate hundreds of DHCP
client from a linux machine. Linux root login is needed because the tool
requires layer2 raw socket for sending and receiving DHCP packets.

%prep
%setup -q

%build
make CFLAGS='%{optflags} -fcommon' %{?_smp_mflags}

%install
install -Dpm 0755 dhtest %{buildroot}/%{_sbindir}/dhtest

%files
%license LICENSE
%doc README.txt
%{_sbindir}/dhtest

%changelog
