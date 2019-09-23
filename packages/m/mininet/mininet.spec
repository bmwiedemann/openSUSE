#
# spec file for package mininet
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           mininet
Version:        2.2.1
Release:        0
Summary:        Network emulator for rapid prototyping of Software Defined Networks (SDN)
# mininet is MIT and util/sch_htb-ofbuf/sch_htb.c is GPL-2.0+
License:        MIT and GPL-2.0+
Group:          Productivity/Networking/Other
Url:            http://mininet.org
Source0:        https://github.com/mininet/mininet/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM mininet-2.2.1-private-mount.patch gh#mininet/mininet/565
Patch0:         mininet-2.2.1-private-mount.patch
# PATCH-FIX-UPSTREAM mininet-2.2.1-ovs-testcontroller
Patch1:         mininet-2.2.1-add-ovs-testcontroller.patch
# PATCH-FIX-UPSTREAM mininet-2.2.1-ovs-testcontroller gh#mininet/mininet/pull/608
Patch2:         mininet-2.2.1-fallback-to-ovs-testcontroller.patch
# PATCH-FIX-UPSTREAM mininet-2.2.1-default-ofport.patch gh#mininet/mininet/545
Patch3:         mininet-2.2.1-default-ofport.patch
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python-devel
BuildRequires:  python-setuptools
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
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# remove shebang to make rpmlint happy
sed -i "/#\!\/usr\/bin\/env python$/d" %{name}/topo.py

%build
make %{?_smp_mflags} man mnexec
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
# Makefile needs some love
install -d %{buildroot}%{_mandir}/man1
install -m 644 mn.1 mnexec.1 %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_bindir}
install -m 755 mnexec %{buildroot}%{_bindir}
# Set the exec bit on examples files because they are standalone
# scripts.
chmod a+x %{buildroot}%{python_sitelib}/%{name}/examples/[a-z0-9]*.py

%fdupes %{buildroot}/%{python_sitelib}

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{_bindir}/mn
%{_bindir}/mnexec
%{_mandir}/man1/mn.1*
%{_mandir}/man1/mnexec.1*
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-*.egg-info

%changelog
