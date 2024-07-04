#
# spec file for package fence-agents
#
# Copyright (c) 2024 SUSE LLC
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


%define python_version python3

%global plugin_dir %{_libdir}/stonith/plugins/rhcs
%define agent_list aliyun alom amt amt_ws apc apc_snmp aws azure_arm bladecenter brocade cisco_mds cisco_ucs compute docker drac5 dummy eaton_snmp emerson eps evacuate gce hds_cb hpblade ibmblade ibm_powervs ibm_vpc ibmz ifmib ilo ilo_moonshot ilo_mp ilo_ssh intelmodular ipdu ipmilan ironic kdump ldom lpar mpath netio openstack powerman pve raritan rcd_serial redfish rhevm rsa rsb sanbox2 sbd scsi vbox virsh vmware vmware_rest wti xenapi zvm

Name:           fence-agents
Summary:        Fence Agents for High Availability
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Productivity/Clustering/HA
Version:        4.15.0+git.1719822011.7a2c0a7f
Release:        0
URL:            https://github.com/ClusterLabs/fence-agents
Source0:        %{name}-%{version}.tar.xz
Patch1:         0001-Use-Python-3-for-all-scripts-bsc-1065966.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{python_version}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxml2-tools
BuildRequires:  libxslt
BuildRequires:  mozilla-nspr-devel
BuildRequires:  mozilla-nss-devel
BuildRequires:  perl
BuildRequires:  perl-Net-Telnet
BuildRequires:  pkg-config
BuildRequires:  python3-google-api-python-client
BuildRequires:  python3-keystoneclient
BuildRequires:  python3-novaclient
BuildRequires:  python3-openwsman
BuildRequires:  python3-pexpect
BuildRequires:  python3-pycurl
BuildRequires:  python3-requests
BuildRequires:  python3-xml
BuildRequires:  xz
Requires:       net-snmp
Requires:       openssh
Requires:       perl-Net-Telnet
Requires:       python3-pexpect
Requires:       python3-pycurl
Requires:       python3-requests
Requires:       sg3_utils
Requires:       telnet

# This is required by fence_virsh. Per discussion on fedora-devel
# switching from package to file based require.
Recommends:     /usr/bin/virsh

# This is required by fence_ipmilan. it appears that the packages
# have changed Requires around. Make sure to get the right one.
Recommends:     /usr/bin/ipmitool

Recommends:     python3-openwsman

%if 0%{?with_regression_tests}
BuildRequires:  time
%endif

%description
Fence agents are device drivers able to prevent computers from
destroying data on shared storage. Their aim is to isolate a
corrupted computer by controlling power, network or storage
configuration. This package provides both a Python API for
creating agents as well as a collection of existing agents.

%package amt_ws
Summary:        Fence Agent for  Intel AMT (WS)
License:        Apache-2.0
Group:          Productivity/Clustering/HA
Requires:       %{name} = %{version}

%description amt_ws
Fence agents are device drivers able to prevent computers from
destroying data on shared storage. Their aim is to isolate a
corrupted computer by controlling power, network or storage
configuration. This packages provides an agent for Intel AMT (WS).

%package devel
Summary:        Fence Agents for High Availability
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description devel
Fence agents are device drivers able to prevent computers from
destroying data on shared storage. Their aim is to isolate a
corrupted computer by controlling power, network or storage
configuration. This package provides agents suitable only for
development.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
CFLAGS="${CFLAGS} ${RPM_OPT_FLAGS}"
export CFLAGS
PYTHON="%{_bindir}/python3"
export PYTHON
echo "%{version}" >.tarball-version
./autogen.sh
%{configure} --with-agents='%{agent_list}'
make

%install
make install DESTDIR=%{buildroot}

## tree fix up
# fix libfence permissions
chmod 0755 %{buildroot}%{_datadir}/fence/fenc*.py
# remove docs
rm -rf %{buildroot}/usr/share/doc/fence-agents
# create links to agents in the plugins dir
mkdir -p %{buildroot}%{plugin_dir}
ln -s %{_sbindir}/fence_cisco_ucs %{buildroot}%{plugin_dir}
%fdupes %buildroot%{_sbindir}
%fdupes %buildroot%{_datadir}/cluster

%if 0%{?with_regression_tests}
%check
make check
PYTHONPATH=fence/agents/lib "%{python_version}" fence/agents/lib/tests/test_fencing.py
%endif

%files
%defattr(-,root,root,-)
%license doc/COPYING.* doc/COPYRIGHT doc/README.licence
%dir %{plugin_dir}
%dir %{_libdir}/stonith/plugins
%dir %{_libdir}/stonith
%{_datadir}/fence
%{_datadir}/cluster
%{plugin_dir}/fence_cisco_ucs
%{_sbindir}/fence_*
%exclude %{_sbindir}/fence_amt_ws
%exclude %{_mandir}/man8/fence_amt_ws*
%exclude %{_sbindir}/fence_dummy
%exclude %{_mandir}/man8/fence_dummy*
%{_mandir}/man8/fence_*
%{_libexecdir}/fence_*

%files amt_ws
%{_sbindir}/fence_amt_ws
%{_mandir}/man8/fence_amt_ws*

%files devel
/usr/share/pkgconfig/fence-agents.pc
%{_sbindir}/fence_dummy
%{_mandir}/man8/fence_dummy*

%changelog
