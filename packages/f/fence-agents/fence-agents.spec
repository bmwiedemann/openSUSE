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


%define agent_list aliyun alom apc apc_snmp aws azure_arm bladecenter brocade cisco_mds cisco_ucs compute docker drac5 dummy eaton_snmp eaton_ssh emerson eps evacuate gce hds_cb hpblade ibmblade ibmz ibm_powervs ibm_vpc ifmib ilo ilo_moonshot ilo_mp ilo_ssh intelmodular ipdu ipmilan ironic kdump ldom lpar mpath netio openstack powerman pve raritan rcd_serial redfish rhevm rsa rsb sanbox2 sbd scsi vbox virsh vmware vmware_rest wti xenapi zvm
Name:           fence-agents
Summary:        Set of unified programs capable of host isolation ("fencing")
Version:        4.15.0+git.1731052905.05fd299e
Release:        0
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          Productivity/Clustering/HA
URL:            https://github.com/ClusterLabs/fence-agents
Source0:        %{name}-%{version}.tar.xz

%define boto3_br 1

# skipped: pve, raritan, rcd-serial, virsh
# Removed sle15->sle16 evacuate, ironic, openstack,  pve, raritan, rcd_serial
# fence-agents-azure-arm has special requirements
%global allfenceagents %(cat <<EOF
fence-agents-alom \\
fence-agents-apc \\
fence-agents-apc-snmp \\
fence-agents-aws \\
fence-agents-bladecenter \\
fence-agents-brocade \\
fence-agents-cisco-mds \\
fence-agents-cisco-ucs \\
fence-agents-docker \\
fence-agents-drac5 \\
fence-agents-eaton-snmp \\
fence-agents-eaton-ssh \\
fence-agents-emerson \\
fence-agents-eps \\
fence-agents-gce \\
fence-agents-hds-cb \\
fence-agents-hpblade \\
fence-agents-ibmblade \\
fence-agents-ibmz \\
fence-agents-ibm-powervs \\
fence-agents-ibm-vpc \\
fence-agents-ifmib \\
fence-agents-ilo-moonshot \\
fence-agents-ilo-mp \\
fence-agents-ilo-ssh \\
fence-agents-ilo2 \\
fence-agents-intelmodular \\
fence-agents-ipdu \\
fence-agents-ipmilan \\
fence-agents-kdump \\
fence-agents-ldom \\
fence-agents-lpar \\
fence-agents-mpath \\
fence-agents-netio \\
fence-agents-redfish \\
fence-agents-rhevm \\
fence-agents-rsa \\
fence-agents-rsb \\
fence-agents-sanbox2 \\
fence-agents-sbd \\
fence-agents-scsi \\
fence-agents-vbox \\
fence-agents-vmware \\
fence-agents-vmware-rest \\
fence-agents-wti \\
fence-agents-xenapi \\
fence-agents-zvm \\

EOF)

#Agents not in sles
#fence-agents-amt-ws \\
#fence-agents-amt \\
#fence-agents-cdu \\
#fence-agents-cyberpower-ssh \\
#fence-agents-ecloud \\
#fence-agents-heuristics-ping \\
#fence-agents-ovh \\
#fence-agents-ovm \\
#fence-agents-vmware-soap \\
#fence-agents-vmware-vcloud \\
#fence-virt \\
#kubevirt

%ifarch x86_64 ppc64le
%global allfenceagents %(cat <<EOF
%{allfenceagents} \\
fence-agents-aws \\
fence-agents-compute \\
fence-agents-gce \\
fence-agents-ironic \\
fence-agents-openstack

EOF)
%endif

# Build dependencies
## general
BuildRequires:  autoconf automake libtool make
## compiled code (-kdump)
BuildRequires:  gcc
## man pages generating
BuildRequires:  libxslt
## Python dependencies
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module httplib2}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module pycurl}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module suds}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
BuildRequires:  openwsman-python3
%if %{boto3_br}
BuildRequires:  python3-boto3
%endif
%else
%if %{boto3_br}
BuildRequires:  %{python_module boto3}
%endif
%endif

# fence-virt
%if 0%{?suse_version}
%define nss_devel mozilla-nss-devel
%define nspr_devel mozilla-nspr-devel
%define systemd_units systemd
%else
%define nss_devel nss-devel
%define nspr_devel nspr-devel
%define systemd_units systemd-units
%endif

BuildRequires:  %{systemd_units}
BuildRequires:  bison
%if 0%{?suse_version}
BuildRequires:  corosync-devel
%else
BuildRequires:  corosynclib-devel
%endif
BuildRequires:  flex
BuildRequires:  libuuid-devel
BuildRequires:  libvirt-devel
BuildRequires:  libxml2-devel %{nss_devel} %{nspr_devel}
# for test
BuildRequires:  time

# turn off the brp-python-bytecompile script
# (for F28+ or equivalent, the latter is the preferred form)
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompilespace:.*$!!g')
#undefine __brp_python_bytecompile

%prep
%autosetup -p1 -n %{name}-%{version}
# prevent compilation of something that won't get used anyway
sed -i.orig 's|FENCE_ZVM=1|FENCE_ZVM=0|' configure.ac

%build
CFLAGS="${CFLAGS} ${RPM_OPT_FLAGS}"
export CFLAGS
export PYTHON="%{__python3}"
echo "%{version}" >.tarball-version
./autogen.sh
%{configure} --with-agents='%{agent_list}' \
%if %{defined _tmpfilesdir}
	SYSTEMD_TMPFILES_DIR=%{_tmpfilesdir} \
	--with-fencetmpdir=/run/fence-agents
%endif
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/%{_unitdir}/
# bytecompile Python source code in a non-standard location
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/fence
%endif
# XXX unsure if /usr/sbin/fence_* should be compiled as well

## tree fix up
# fix libfence permissions
chmod 0755 %{buildroot}%{_datadir}/fence/*.py
# remove docs
rm -rf %{buildroot}/usr/share/doc/fence-agents
# remove .a files
rm -f %{buildroot}/%{_libdir}/%{name}/*.*a
rm -f %{buildroot}/%{_libdir}/fence-virt/*.*a
#%fdupes %buildroot%{_sbindir}
#%fdupes %buildroot%{_datadir}/cluster
%if %{defined python3_fix_shebang_path}
%python3_fix_shebang_path %{buildroot}/%{_sbindir}/*
%endif

%check
make check

%post
ccs_update_schema > /dev/null 2>&1 ||:
# https://fedoraproject.org/wiki/Packaging:ScriptletSnippets#Systemd
if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun

%postun

%description
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar. They operate through a unified interface
(calling conventions) devised for the original Red Hat clustering solution.

%package common
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Common base for Fence Agents
Requires:       python3-pexpect
Requires:       python3-pycurl
BuildArch:      noarch

%description common
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar.

This package contains support files including the Python fencing library.

%files common
%doc doc/COPYING.* doc/COPYRIGHT doc/README.licence
%{_datadir}/fence
%exclude %{_datadir}/fence/azure_fence.*
%exclude %{_datadir}/fence/__pycache__/azure_fence.*
%exclude %{_datadir}/fence/XenAPI.*
%exclude %{_datadir}/fence/__pycache__/XenAPI.*
%{_datadir}/cluster
%exclude %{_datadir}/cluster/fence_mpath_check*
%exclude %{_datadir}/cluster/fence_scsi_check*
%exclude %{_sbindir}/*
%exclude %{_mandir}/man8/*
%if %{defined _tmpfilesdir}
%{_tmpfilesdir}/%{name}.conf
%endif
%if %{defined _tmpfilesdir}
%ghost %attr (1755, root, root)	/run/%{name}
%else
%dir %attr (1755, root, root)	%{_var}/run/%{name}
%endif

%package all
License:        Apache-2.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Set of unified programs capable of host isolation ("fencing")
Requires:       %{allfenceagents}
Provides:       fence-agents = %{version}-%{release}
Obsoletes:      fence-agents < %{version}-%{release}
Conflicts:      fence-agents < %{version}-%{release}

%description all
A collection of executables to handle isolation ("fencing") of possibly
misbehaving hosts by the means of remote power management, blocking
network, storage, or similar.

This package serves as a catch-all for all supported fence agents.

%files all

%package devel
Summary:        Fence Agents for High Availability
License:        GPL-2.0-only AND LGPL-2.1-only
Group:          Development/Tools/Other
Requires:       fence-agents-common = %{version}-%{release}

%description devel
Fence agents are device drivers able to prevent computers from
destroying data on shared storage. Their aim is to isolate a
corrupted computer by controlling power, network or storage
configuration. This package provides agents suitable only for
development.

%files devel
%{_datadir}/pkgconfig/%{name}.pc
%{_sbindir}/fence_dummy
%{_mandir}/man8/fence_dummy*

%ifarch x86_64
%package aliyun
License:        Apache-2.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND BSD-3-Clause AND MIT
Group:          System Environment/Base
Summary:        Fence agent for Alibaba Cloud (Aliyun)
Requires:       fence-agents-common >= %{version}-%{release}
Requires:       python3-jmespath >= 0.9.0
Conflicts:      %{name} < %{version}-%{release}

%description aliyun
The fence-agents-aliyun package contains a fence agent for Alibaba Cloud (Aliyun) instances.

%files aliyun
%defattr(-,root,root,-)
%{_sbindir}/fence_aliyun
%{_mandir}/man8/fence_aliyun.8*
%endif

%package alom
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for SUN ALOM
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description alom
Fence agent for SUN ALOM.

%files alom
%{_sbindir}/fence_alom
%{_mandir}/man8/fence_alom.8*

%package apc
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for APC devices
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description apc
Fence agent for APC devices that are accessed via telnet or SSH.

%files apc
%{_sbindir}/fence_apc
%{_mandir}/man8/fence_apc.8*

%package apc-snmp
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agents for APC devices (SNMP)
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       net-snmp-utils
%else
Requires:       net-snmp
%endif
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description apc-snmp
Fence agents for APC devices that are accessed via the SNMP protocol.

%files apc-snmp
%{_sbindir}/fence_apc_snmp
%{_mandir}/man8/fence_apc_snmp.8*
%{_sbindir}/fence_tripplite_snmp
%{_mandir}/man8/fence_tripplite_snmp.8*

%package aws
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Amazon AWS
Requires:       fence-agents-common = %{version}-%{release}
Requires:       python3-boto3
BuildArch:      noarch
Conflicts:      %{name} < %{version}-%{release}

%description aws
Fence agent for Amazon AWS instances.

%files aws
%{_sbindir}/fence_aws
%{_mandir}/man8/fence_aws.8*

%package azure-arm
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Azure Resource Manager
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?rhel} && 0%{?rhel} < 9
Requires:       python3-azure-sdk
%else
Requires:       python311-azure-common
Requires:       python311-azure-identity
Requires:       python311-azure-mgmt-compute
Requires:       python311-azure-mgmt-network
Requires:       python311-msrestazure
Requires:       python311-pexpect
Requires:       python311-pycurl
%endif
BuildArch:      noarch
Conflicts:      %{name} < %{version}-%{release}

%description azure-arm
Fence agent for Azure Resource Manager instances.

%files azure-arm
%{_sbindir}/fence_azure_arm
%{_datadir}/fence/azure_fence.py*
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
%{_datadir}/fence/__pycache__/azure_fence.*
%endif
%{_mandir}/man8/fence_azure_arm.8*

%package bladecenter
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for IBM BladeCenter
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description bladecenter
Fence agent for IBM BladeCenter devices that are accessed
via telnet or SSH.

%files bladecenter
%{_sbindir}/fence_bladecenter
%{_mandir}/man8/fence_bladecenter.8*

%package brocade
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Brocade switches
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description brocade
Fence agent for Brocade devices that are accessed via telnet or SSH.

%files brocade
%{_sbindir}/fence_brocade
%{_mandir}/man8/fence_brocade.8*

%package cisco-mds
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Cisco MDS 9000 series
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       net-snmp-utils
%else
Requires:       net-snmp
%endif
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description cisco-mds
Fence agent for Cisco MDS 9000 series devices that are accessed
via the SNMP protocol.

%files cisco-mds
%{_sbindir}/fence_cisco_mds
%{_mandir}/man8/fence_cisco_mds.8*

%package cisco-ucs
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Cisco UCS series
Requires:       fence-agents-common = %{version}-%{release}
Requires:       python3-pycurl
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description cisco-ucs
Fence agent for Cisco UCS series devices that are accessed
via the SNMP protocol.

%files cisco-ucs
%{_sbindir}/fence_cisco_ucs
%{_mandir}/man8/fence_cisco_ucs.8*

%ifarch x86_64 ppc64le
%package compute
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Nova compute nodes
Requires:       fence-agents-common = %{version}-%{release}
Requires:       python3-novaclient
Requires:       python3-requests
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description compute
Fence agent for Nova compute nodes.

%files compute
%{_sbindir}/fence_compute
%{_sbindir}/fence_evacuate
%{_mandir}/man8/fence_compute.8*
%{_mandir}/man8/fence_evacuate.8*
%endif

%package docker
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Docker
Requires:       fence-agents-common = %{version}-%{release}
Requires:       python3-pycurl
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description docker
Fence agent for Docker images that are accessed over HTTP.

%files docker
%{_sbindir}/fence_docker
%{_mandir}/man8/fence_docker.8*

%package drac5
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Dell DRAC 5
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description drac5
Fence agent for Dell DRAC 5 series devices that are accessed
via telnet or SSH.

%files drac5
%{_sbindir}/fence_drac5
%{_mandir}/man8/fence_drac5.8*

%package eaton-snmp
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Eaton network power switches
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       net-snmp-utils
%else
Requires:       net-snmp
%endif
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description eaton-snmp
Fence agent for Eaton network power switches that are accessed
via the SNMP protocol.

%files eaton-snmp
%{_sbindir}/fence_eaton_snmp
%{_mandir}/man8/fence_eaton_snmp.8*

%package eaton-ssh
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Eaton network power switches
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description eaton-ssh
Fence agent for Eaton network power switches that are accessed
via the serial protocol tunnel over SSH.

%files eaton-ssh
%{_sbindir}/fence_eaton_ssh
%{_mandir}/man8/fence_eaton_ssh.8*

%package emerson
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Emerson devices (SNMP)
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description emerson
Fence agent for Emerson devices that are accessed via
the SNMP protocol.

%files emerson
%{_sbindir}/fence_emerson
%{_mandir}/man8/fence_emerson.8*

%package eps
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for ePowerSwitch 8M+ power switches
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description eps
Fence agent for ePowerSwitch 8M+ power switches that are accessed
via the HTTP(s) protocol.

%files eps
%{_sbindir}/fence_eps*
%{_mandir}/man8/fence_eps*.8*

%package gce
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for GCE (Google Cloud Engine)
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       python3-google-api-client
%else
Requires:       python3-google-api-python-client
%endif
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description gce
Fence agent for GCE (Google Cloud Engine) instances.

%files gce
%{_sbindir}/fence_gce
%{_mandir}/man8/fence_gce.8*

%package hds-cb
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Hitachi Compute Blade systems
Requires:       fence-agents-common = %{version}-%{release}
Requires:       telnet
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description hds-cb
Fence agent for Hitachi Compute Blades that are accessed via telnet.

%files hds-cb
%{_sbindir}/fence_hds_cb
%{_mandir}/man8/fence_hds_cb.8*

%package hpblade
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for HP BladeSystem devices
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description hpblade
Fence agent for HP BladeSystem devices that are accessed via telnet
or SSH.

%files hpblade
%{_sbindir}/fence_hpblade
%{_mandir}/man8/fence_hpblade.8*

%package ibmblade
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for IBM BladeCenter
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       net-snmp-utils
%else
Requires:       net-snmp
%endif
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ibmblade
Fence agent for IBM BladeCenter devices that are accessed
via the SNMP protocol.

%files ibmblade
%{_sbindir}/fence_ibmblade
%{_mandir}/man8/fence_ibmblade.8*

%package ibmz
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for IBM z LPARs
Requires:       fence-agents-common = %{version}-%{release}
Requires:       python3-requests
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ibmz
Fence agent for IBM z LPARs that are accessed via the HMC
Web Services REST API.

%files ibmz
%{_sbindir}/fence_ibmz
%{_mandir}/man8/fence_ibmz.8*

%package ibm-powervs
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for IBM PowerVS
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ibm-powervs
Fence agent for IBM PowerVS that are accessed via REST API.

%files ibm-powervs
%{_sbindir}/fence_ibm_powervs
%{_mandir}/man8/fence_ibm_powervs.8*

%package ibm-vpc
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for IBM Cloud VPC
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ibm-vpc
Fence agent for IBM Cloud VPC that are accessed via REST API.

%files ibm-vpc
%{_sbindir}/fence_ibm_vpc
%{_mandir}/man8/fence_ibm_vpc.8*

%package ifmib
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for devices with IF-MIB interfaces
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       net-snmp-utils
%else
Requires:       net-snmp
%endif
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ifmib
Fence agent for IF-MIB interfaces that are accessed via
the SNMP protocol.

%files ifmib
%{_sbindir}/fence_ifmib
%{_mandir}/man8/fence_ifmib.8*

%package ilo2
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agents for HP iLO2 devices
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       gnutls-utils
%else
Requires:       gnutls
%endif
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ilo2
Fence agents for HP iLO2 devices that are accessed via
the HTTP(s) protocol.

%files ilo2
%{_sbindir}/fence_ilo
%{_sbindir}/fence_ilo2
%{_mandir}/man8/fence_ilo.8*
%{_mandir}/man8/fence_ilo2.8*

%package ilo-moonshot
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for HP iLO Moonshot devices
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ilo-moonshot
Fence agent for HP iLO Moonshot devices that are accessed
via telnet or SSH.

%files ilo-moonshot
%{_sbindir}/fence_ilo_moonshot
%{_mandir}/man8/fence_ilo_moonshot.8*

%package ilo-mp
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for HP iLO MP devices
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ilo-mp
Fence agent for HP iLO MP devices that are accessed via telnet or SSH.

%files ilo-mp
%{_sbindir}/fence_ilo_mp
%{_mandir}/man8/fence_ilo_mp.8*

%package ilo-ssh
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agents for HP iLO devices over SSH
Requires:       fence-agents-common = %{version}-%{release}
Requires:       openssh-clients
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ilo-ssh
Fence agents for HP iLO devices that are accessed via telnet or SSH.

%files ilo-ssh
%{_sbindir}/fence_ilo_ssh
%{_mandir}/man8/fence_ilo_ssh.8*
%{_sbindir}/fence_ilo3_ssh
%{_mandir}/man8/fence_ilo3_ssh.8*
%{_sbindir}/fence_ilo4_ssh
%{_mandir}/man8/fence_ilo4_ssh.8*
%{_sbindir}/fence_ilo5_ssh
%{_mandir}/man8/fence_ilo5_ssh.8*

%package intelmodular
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for devices with Intel Modular interfaces
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       net-snmp-utils
%else
Requires:       net-snmp
%endif
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description intelmodular
Fence agent for Intel Modular interfaces that are accessed
via the SNMP protocol.

%files intelmodular
%{_sbindir}/fence_intelmodular
%{_mandir}/man8/fence_intelmodular.8*

%package ipdu
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for IBM iPDU network power switches
Requires:       fence-agents-common = %{version}-%{release}
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       net-snmp-utils
%else
Requires:       net-snmp
%endif
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ipdu
Fence agent for IBM iPDU network power switches that are accessed
via the SNMP protocol.

%files ipdu
%{_sbindir}/fence_ipdu
%{_mandir}/man8/fence_ipdu.8*

%package ipmilan
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agents for devices with IPMI interface
Requires:       /usr/bin/ipmitool
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ipmilan
Fence agents for devices with IPMI interface.

%files ipmilan
%{_sbindir}/fence_ipmilan
%{_mandir}/man8/fence_ipmilan.8*
%{_sbindir}/fence_idrac
%{_mandir}/man8/fence_idrac.8*
%{_sbindir}/fence_ilo3
%{_mandir}/man8/fence_ilo3.8*
%{_sbindir}/fence_ilo4
%{_mandir}/man8/fence_ilo4.8*
%{_sbindir}/fence_ilo5
%{_mandir}/man8/fence_ilo5.8*
%{_sbindir}/fence_ipmilanplus
%{_mandir}/man8/fence_ipmilanplus.8*
%{_sbindir}/fence_imm
%{_mandir}/man8/fence_imm.8*

%ifarch x86_64 ppc64le
%package ironic
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for OpenStack's Ironic (Bare Metal as a service)
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ironic
Fence agent for OpenStack's Ironic (Bare Metal as a service) service.

%files ironic
%{_sbindir}/fence_ironic
%{_mandir}/man8/fence_ironic.8*
%endif

%package kdump
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for use with kdump crash recovery service
Conflicts:      %{name} < %{version}-%{release}
Requires:       fence-agents-common = %{version}-%{release}

# this cannot be noarch since it's compiled
%description kdump
Fence agent for use with kdump crash recovery service.

%files kdump
%{_sbindir}/fence_kdump
%{_libexecdir}/fence_kdump_send
%{_mandir}/man8/fence_kdump.8*
%{_mandir}/man8/fence_kdump_send.8*

%package ldom
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Sun LDom virtual machines
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description ldom
Fence agent for APC devices that are accessed via telnet or SSH.

%files ldom
%{_sbindir}/fence_ldom
%{_mandir}/man8/fence_ldom.8*

%package lpar
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for IBM LPAR
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description lpar
Fence agent for IBM LPAR devices that are accessed via telnet or SSH.

%files lpar
%{_sbindir}/fence_lpar
%{_mandir}/man8/fence_lpar.8*

%package mpath
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for reservations over Device Mapper Multipath
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
Requires:       device-mapper-multipath
%else
Requires:       multipath-tools
%endif
Requires:       fence-agents-common = %{version}-%{release}
Conflicts:      %{name} < %{version}-%{release}
BuildArch:      noarch

%description mpath
Fence agent for SCSI persistent reservation over
Device Mapper Multipath.

%files mpath
%{_sbindir}/fence_mpath
%{_datadir}/cluster/fence_mpath_check*
%{_mandir}/man8/fence_mpath.8*

%package netio
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Koukaam NETIO devices
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
BuildArch:      noarch

%description netio
Fence agent for Koukaam NETIO devices that are accessed
via telnet or SSH.

%files netio
%{_sbindir}/fence_netio
%{_mandir}/man8/fence_netio.8*

%ifarch x86_64 ppc64le
%package openstack
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for OpenStack's Nova service
Requires:       fence-agents-common = %{version}-%{release}
Requires:       python3-requests
BuildArch:      noarch

%description openstack
Fence agent for OpenStack's Nova service.

%files openstack
%{_sbindir}/fence_openstack
%{_mandir}/man8/fence_openstack.8*
%endif

# skipped from allfenceagents
%package pve
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for PVE
Requires:       fence-agents-common = %{version}-%{release}
Requires:       python3-pycurl
BuildArch:      noarch

%description pve
Fence agent for PVE.

%files pve
%{_sbindir}/fence_pve
%{_mandir}/man8/fence_pve.8*

# skipped from allfenceagents
%package raritan
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Raritan Dominion PX
Requires:       fence-agents-common = %{version}-%{release}
BuildArch:      noarch

%description raritan
Fence agent for Raritan Dominion PX.

%files raritan
%{_sbindir}/fence_raritan
%{_mandir}/man8/fence_raritan.8*

# skipped from allfenceagents
%package rcd-serial
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for RCD serial
Requires:       fence-agents-common = %{version}-%{release}
BuildArch:      noarch

%description rcd-serial
Fence agent for RCD serial.

%files rcd-serial
%{_sbindir}/fence_rcd_serial
%{_mandir}/man8/fence_rcd_serial.8*

%package redfish
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          System Environment/Base
Summary:        Fence agent for Redfish
Requires:       fence-agents-common >= %{version}-%{release}
Requires:       python3-requests
Obsoletes:      fence-agents < %{version}

%description redfish
The fence-agents-redfish package contains a fence agent for Redfish

%files redfish
%defattr(-,root,root,-)
%{_sbindir}/fence_redfish
%{_mandir}/man8/fence_redfish.8*

%package rhevm
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for RHEV-M
Requires:       fence-agents-common = %{version}-%{release}
BuildArch:      noarch

%description rhevm
Fence agent for RHEV-M via REST API.

%files rhevm
%{_sbindir}/fence_rhevm
%{_mandir}/man8/fence_rhevm.8*

%package rsa
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for IBM RSA II
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
BuildArch:      noarch

%description rsa
Fence agent for IBM RSA II devices that are accessed
via telnet or SSH.

%files rsa
%{_sbindir}/fence_rsa
%{_mandir}/man8/fence_rsa.8*

%package rsb
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Fujitsu RSB
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
BuildArch:      noarch

%description rsb
Fence agent for Fujitsu RSB devices that are accessed
via telnet or SSH.

%files rsb
%{_sbindir}/fence_rsb
%{_mandir}/man8/fence_rsb.8*

%package sanbox2
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for QLogic SANBox2 FC switches
Requires:       fence-agents-common = %{version}-%{release}
Requires:       telnet
BuildArch:      noarch

%description sanbox2
Fence agent for QLogic SANBox2 switches that are accessed via telnet.

%files sanbox2
%{_sbindir}/fence_sanbox2
%{_mandir}/man8/fence_sanbox2.8*

%package sbd
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for SBD (storage-based death)
Requires:       fence-agents-common = %{version}-%{release}
Requires:       sbd
BuildArch:      noarch

%description sbd
Fence agent for SBD (storage-based death).

%files sbd
%{_sbindir}/fence_sbd
%{_mandir}/man8/fence_sbd.8*

%package scsi
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for SCSI persistent reservations
Requires:       fence-agents-common = %{version}-%{release}
Requires:       sg3_utils
BuildArch:      noarch

%description scsi
Fence agent for SCSI persistent reservations.

%files scsi
%{_sbindir}/fence_scsi
%{_datadir}/cluster/fence_scsi_check
%{_datadir}/cluster/fence_scsi_check_hardreboot
%{_mandir}/man8/fence_scsi.8*

%package vbox
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for VirtualBox
Requires:       fence-agents-common = %{version}-%{release}
Requires:       openssh-clients
BuildArch:      noarch

%description vbox
Fence agent for VirtualBox dom0 accessed via SSH.

%files vbox
%{_sbindir}/fence_vbox
%{_mandir}/man8/fence_vbox.8*

# skipped from allfenceagents
%package virsh
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for virtual machines based on libvirt
Requires:       /usr/bin/virsh
Requires:       fence-agents-common = %{version}-%{release}
Requires:       openssh-clients
BuildArch:      noarch

%description virsh
Fence agent for virtual machines that are accessed via SSH.

%files virsh
%{_sbindir}/fence_virsh
%{_mandir}/man8/fence_virsh.8*

%package vmware
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for VMWare with VI Perl Toolkit or vmrun
Requires:       fence-agents-common = %{version}-%{release}
Requires:       python3-pexpect
BuildArch:      noarch

%description vmware
Fence agent for VMWare accessed with VI Perl Toolkit or vmrun.

%files vmware
%{_sbindir}/fence_vmware
%{_mandir}/man8/fence_vmware.8*

%package vmware-rest
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for VMWare with REST API
Requires:       fence-agents-common = %{version}-%{release}
BuildArch:      noarch
Obsoletes:      fence-agents < %{version}

%description vmware-rest
Fence agent for VMWare with REST API.

%files vmware-rest
%{_sbindir}/fence_vmware_rest
%{_mandir}/man8/fence_vmware_rest.8*

%package wti
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for WTI Network power switches
Requires:       openssh-clients
%if 0%{?fedora} < 33 || (0%{?rhel} && 0%{?rhel} < 9) || (0%{?centos} && 0%{?centos} < 9) || 0%{?suse_version}
Recommends:     telnet
%endif
Requires:       fence-agents-common = %{version}-%{release}
BuildArch:      noarch

%description wti
Fence agent for WTI network power switches that are accessed
via telnet or SSH.

%files wti
%{_sbindir}/fence_wti
%{_mandir}/man8/fence_wti.8*

%package xenapi
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for Citrix XenServer over XenAPI
Requires:       fence-agents-common = %{version}-%{release}
Requires:       python3-pexpect
BuildArch:      noarch

%description xenapi
Fence agent for Citrix XenServer accessed over XenAPI.

%files xenapi
%{_sbindir}/fence_xenapi
%{_datadir}/fence/XenAPI.py*
%if 0%{?fedora} || 0%{?centos} || 0%{?rhel}
%{_datadir}/fence/__pycache__/XenAPI.*
%endif
%{_mandir}/man8/fence_xenapi.8*

%package zvm
Conflicts:      %{name} < %{version}-%{release}
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Summary:        Fence agent for IBM z/VM over IP
Requires:       fence-agents-common = %{version}-%{release}
BuildArch:      noarch

%description zvm
Fence agent for IBM z/VM over IP.

%files zvm
%{_sbindir}/fence_zvmip
%{_mandir}/man8/fence_zvmip.8*

%changelog
