#
# spec file for package mininet
#
# Copyright (c) 2023 SUSE LLC
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


Name:           mininet
Version:        2.3.0
Release:        0
Summary:        Network emulator for rapid prototyping of Software Defined Networks (SDN)
# mininet is MIT and util/sch_htb-ofbuf/sch_htb.c is GPL-2.0+
License:        MIT AND GPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            http://mininet.org
Source0:        https://github.com/mininet/mininet/archive/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       ethtool
Requires:       iperf
Requires:       iproute2
Requires:       openvswitch
Requires:       socat
Requires:       telnet
# In case we do not have a controller already.
Suggests:       openvswitch-test

%description
Mininet emulates a complete network of hosts, links, and switches on a single
machine. Mininet is useful for interactive development, testing, and demos, especially
those using OpenFlow and SDN. OpenFlow-based network controllers prototyped in
Mininet can usually be transferred to hardware with minimal changes for full
line-rate execution.

%prep
%setup -q -n mininet-%{version}

# remove shebang to make rpmlint happy
sed -i "/#\!\/usr\/bin\/env python$/d" mininet/topo.py

# fix the shebangs
sed -i "s/#\!\/usr\/bin\/env python$/\#\!\/usr\/bin\/python3/g" examples/*py

# add missing shebangs
sed -i "1s/^/\#\!\/usr\/bin\/python3\n/" mininet/examples/__init__.py

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" man mnexec PYTHON=%{_bindir}/python3
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}
install -Dm 644 mn.1 %{buildroot}%{_mandir}/man1/mn.1
install -Dm 644 mnexec.1 %{buildroot}%{_mandir}/man1/mnexec.1
install -Dm 755 mnexec %{buildroot}%{_bindir}/mnexec

%files
%license LICENSE
%doc README.md
%{_bindir}/mn
%{_mandir}/man1/mn.1%{?ext_man}
%{_bindir}/mnexec
%{_mandir}/man1/mnexec.1%{?ext_man}
%{python3_sitelib}/*

%changelog
