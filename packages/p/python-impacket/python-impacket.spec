#
# spec file for package python-impacket
#
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-impacket
Version:        0.9.21
Release:        0
Summary:        Python3 module to easily build and dissect network protocols
# License: modified Apache-1.1 (see file LICENSE)
License:        Apache-1.1
Group:          Development/Languages/Python
URL:            https://www.secureauth.com/labs/open-source-tools/impacket
Source:         https://files.pythonhosted.org/packages/source/i/impacket/impacket-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 1.0
Requires:       python-ldap3 >= 2.5
Requires:       python-ldapdomaindump >= 0.9.0
Requires:       python-pyOpenSSL >= 0.13.1
Requires:       python-pyasn1 >= 0.2.3
Requires:       python-pycryptodomex
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 1.0}
BuildRequires:  %{python_module ldap3 >= 2.5}
BuildRequires:  %{python_module ldapdomaindump >= 0.9.0}
BuildRequires:  %{python_module pyOpenSSL >= 0.13.1}
BuildRequires:  %{python_module pyasn1 >= 0.2.3}
BuildRequires:  %{python_module pycryptodomex}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Impacket is a collection of Python classes for working with network
protocols. Impacket is focused on providing low-level
programmatic access to the packets and for some protocols (e.g.
SMB1-3 and MSRPC) the protocol implementation itself.
Packets can be constructed from scratch, as well as parsed from
raw data, and the object oriented API makes it simple to work with
deep hierarchies of protocols. The library provides a set of tools
as examples of what can be done within the context of this library.

%prep
%setup -q -n impacket-%{version}
sed -e '/^#!\//, 1d' -i \
  impacket/examples/ntlmrelayx/servers/socksserver.py \
  impacket/mqtt.py

%build
%python_build

%install
%python_install
%python_expand cd %{buildroot}%{_bindir} && find . -name "*.py" -exec sh -c 'mv $0 impacket-`basename "$0" .py`' '{}' \;
%python_clone -a %{buildroot}%{_bindir}/impacket-GetADUsers
%python_clone -a %{buildroot}%{_bindir}/impacket-GetNPUsers
%python_clone -a %{buildroot}%{_bindir}/impacket-GetUserSPNs
%python_clone -a %{buildroot}%{_bindir}/impacket-addcomputer
%python_clone -a %{buildroot}%{_bindir}/impacket-atexec
%python_clone -a %{buildroot}%{_bindir}/impacket-dcomexec
%python_clone -a %{buildroot}%{_bindir}/impacket-dpapi
%python_clone -a %{buildroot}%{_bindir}/impacket-esentutl
%python_clone -a %{buildroot}%{_bindir}/impacket-findDelegation
%python_clone -a %{buildroot}%{_bindir}/impacket-getArch
%python_clone -a %{buildroot}%{_bindir}/impacket-getPac
%python_clone -a %{buildroot}%{_bindir}/impacket-getST
%python_clone -a %{buildroot}%{_bindir}/impacket-getTGT
%python_clone -a %{buildroot}%{_bindir}/impacket-goldenPac
%python_clone -a %{buildroot}%{_bindir}/impacket-ifmap
%python_clone -a %{buildroot}%{_bindir}/impacket-karmaSMB
%python_clone -a %{buildroot}%{_bindir}/impacket-kintercept
%python_clone -a %{buildroot}%{_bindir}/impacket-lookupsid
%python_clone -a %{buildroot}%{_bindir}/impacket-mimikatz
%python_clone -a %{buildroot}%{_bindir}/impacket-mqtt_check
%python_clone -a %{buildroot}%{_bindir}/impacket-mssqlclient
%python_clone -a %{buildroot}%{_bindir}/impacket-mssqlinstance
%python_clone -a %{buildroot}%{_bindir}/impacket-netview
%python_clone -a %{buildroot}%{_bindir}/impacket-nmapAnswerMachine
%python_clone -a %{buildroot}%{_bindir}/impacket-ntfs-read
%python_clone -a %{buildroot}%{_bindir}/impacket-ntlmrelayx
%python_clone -a %{buildroot}%{_bindir}/impacket-opdump
%python_clone -a %{buildroot}%{_bindir}/impacket-ping
%python_clone -a %{buildroot}%{_bindir}/impacket-ping6
%python_clone -a %{buildroot}%{_bindir}/impacket-psexec
%python_clone -a %{buildroot}%{_bindir}/impacket-raiseChild
%python_clone -a %{buildroot}%{_bindir}/impacket-rdp_check
%python_clone -a %{buildroot}%{_bindir}/impacket-reg
%python_clone -a %{buildroot}%{_bindir}/impacket-registry-read
%python_clone -a %{buildroot}%{_bindir}/impacket-rpcdump
%python_clone -a %{buildroot}%{_bindir}/impacket-sambaPipe
%python_clone -a %{buildroot}%{_bindir}/impacket-samrdump
%python_clone -a %{buildroot}%{_bindir}/impacket-secretsdump
%python_clone -a %{buildroot}%{_bindir}/impacket-services
%python_clone -a %{buildroot}%{_bindir}/impacket-smbclient
%python_clone -a %{buildroot}%{_bindir}/impacket-smbexec
%python_clone -a %{buildroot}%{_bindir}/impacket-smbrelayx
%python_clone -a %{buildroot}%{_bindir}/impacket-smbserver
%python_clone -a %{buildroot}%{_bindir}/impacket-sniff
%python_clone -a %{buildroot}%{_bindir}/impacket-sniffer
%python_clone -a %{buildroot}%{_bindir}/impacket-split
%python_clone -a %{buildroot}%{_bindir}/impacket-ticketConverter
%python_clone -a %{buildroot}%{_bindir}/impacket-ticketer
%python_clone -a %{buildroot}%{_bindir}/impacket-wmiexec
%python_clone -a %{buildroot}%{_bindir}/impacket-wmipersist
%python_clone -a %{buildroot}%{_bindir}/impacket-wmiquery
#
%python_expand rm %{buildroot}%{_datadir}/doc/impacket/LICENSE
%python_expand rm %{buildroot}%{_datadir}/doc/impacket/README.md
%python_expand %fdupes %{buildroot}%{$python_sitelib}
#
%python_expand rm %{buildroot}%{_bindir}/_current_flavor

%post
%python_install_alternative impacket-GetADUsers
%python_install_alternative impacket-GetNPUsers
%python_install_alternative impacket-GetUserSPNs
%python_install_alternative impacket-addcomputer
%python_install_alternative impacket-atexec
%python_install_alternative impacket-dcomexec
%python_install_alternative impacket-dpapi
%python_install_alternative impacket-esentutl
%python_install_alternative impacket-findDelegation
%python_install_alternative impacket-getArch
%python_install_alternative impacket-getPac
%python_install_alternative impacket-getST
%python_install_alternative impacket-getTGT
%python_install_alternative impacket-goldenPac
%python_install_alternative impacket-ifmap
%python_install_alternative impacket-karmaSMB
%python_install_alternative impacket-kintercept
%python_install_alternative impacket-lookupsid
%python_install_alternative impacket-mimikatz
%python_install_alternative impacket-mqtt_check
%python_install_alternative impacket-mssqlclient
%python_install_alternative impacket-mssqlinstance
%python_install_alternative impacket-netview
%python_install_alternative impacket-nmapAnswerMachine
%python_install_alternative impacket-ntfs-read
%python_install_alternative impacket-ntlmrelayx
%python_install_alternative impacket-opdump
%python_install_alternative impacket-ping
%python_install_alternative impacket-ping6
%python_install_alternative impacket-psexec
%python_install_alternative impacket-raiseChild
%python_install_alternative impacket-rdp_check
%python_install_alternative impacket-reg
%python_install_alternative impacket-registry-read
%python_install_alternative impacket-rpcdump
%python_install_alternative impacket-sambaPipe
%python_install_alternative impacket-samrdump
%python_install_alternative impacket-secretsdump
%python_install_alternative impacket-services
%python_install_alternative impacket-smbclient
%python_install_alternative impacket-smbexec
%python_install_alternative impacket-smbrelayx
%python_install_alternative impacket-smbserver
%python_install_alternative impacket-sniff
%python_install_alternative impacket-sniffer
%python_install_alternative impacket-split
%python_install_alternative impacket-ticketConverter
%python_install_alternative impacket-ticketer
%python_install_alternative impacket-wmiexec
%python_install_alternative impacket-wmipersist
%python_install_alternative impacket-wmiquery

%postun
%python_uninstall_alternative impacket-GetADUsers
%python_uninstall_alternative impacket-GetNPUsers
%python_uninstall_alternative impacket-GetUserSPNs
%python_uninstall_alternative impacket-addcomputer
%python_uninstall_alternative impacket-atexec
%python_uninstall_alternative impacket-dcomexec
%python_uninstall_alternative impacket-dpapi
%python_uninstall_alternative impacket-esentutl
%python_uninstall_alternative impacket-findDelegation
%python_uninstall_alternative impacket-getArch
%python_uninstall_alternative impacket-getPac
%python_uninstall_alternative impacket-getST
%python_uninstall_alternative impacket-getTGT
%python_uninstall_alternative impacket-goldenPac
%python_uninstall_alternative impacket-ifmap
%python_uninstall_alternative impacket-karmaSMB
%python_uninstall_alternative impacket-kintercept
%python_uninstall_alternative impacket-lookupsid
%python_uninstall_alternative impacket-mimikatz
%python_uninstall_alternative impacket-mqtt_check
%python_uninstall_alternative impacket-mssqlclient
%python_uninstall_alternative impacket-mssqlinstance
%python_uninstall_alternative impacket-netview
%python_uninstall_alternative impacket-nmapAnswerMachine
%python_uninstall_alternative impacket-ntfs-read
%python_uninstall_alternative impacket-ntlmrelayx
%python_uninstall_alternative impacket-opdump
%python_uninstall_alternative impacket-ping
%python_uninstall_alternative impacket-ping6
%python_uninstall_alternative impacket-psexec
%python_uninstall_alternative impacket-raiseChild
%python_uninstall_alternative impacket-rdp_check
%python_uninstall_alternative impacket-reg
%python_uninstall_alternative impacket-registry-read
%python_uninstall_alternative impacket-rpcdump
%python_uninstall_alternative impacket-sambaPipe
%python_uninstall_alternative impacket-samrdump
%python_uninstall_alternative impacket-secretsdump
%python_uninstall_alternative impacket-services
%python_uninstall_alternative impacket-smbclient
%python_uninstall_alternative impacket-smbexec
%python_uninstall_alternative impacket-smbrelayx
%python_uninstall_alternative impacket-smbserver
%python_uninstall_alternative impacket-sniff
%python_uninstall_alternative impacket-sniffer
%python_uninstall_alternative impacket-split
%python_uninstall_alternative impacket-ticketConverter
%python_uninstall_alternative impacket-ticketer
%python_uninstall_alternative impacket-wmiexec
%python_uninstall_alternative impacket-wmipersist
%python_uninstall_alternative impacket-wmiquery

%check
# Don't run tests thtat require online connections
rm tests/SMB_RPC/test_bkrp.py
rm tests/SMB_RPC/test_dcomrt.py
rm tests/SMB_RPC/test_dhcpm.py
rm tests/SMB_RPC/test_drsuapi.py
rm tests/SMB_RPC/test_epm.py
rm tests/SMB_RPC/test_even.py
rm tests/SMB_RPC/test_even6.py
rm tests/SMB_RPC/test_fasp.py
rm tests/SMB_RPC/test_ldap.py
rm tests/SMB_RPC/test_lsad.py
rm tests/SMB_RPC/test_lsat.py
rm tests/SMB_RPC/test_mgmt.py
rm tests/SMB_RPC/test_mimilib.py
rm tests/SMB_RPC/test_nmb.py
rm tests/SMB_RPC/test_nrpc.py
rm tests/SMB_RPC/test_rpcrt.py
rm tests/SMB_RPC/test_rprn.py
rm tests/SMB_RPC/test_rrp.py
rm tests/SMB_RPC/test_samr.py
rm tests/SMB_RPC/test_scmr.py
rm tests/SMB_RPC/test_secretsdump.py
rm tests/SMB_RPC/test_smb.py
rm tests/SMB_RPC/test_srvs.py
rm tests/SMB_RPC/test_tsch.py
rm tests/SMB_RPC/test_wkst.py
rm tests/SMB_RPC/test_wmi.py
rm tests/misc/test_dcerpc_v5_ndr.py
rm tests/misc/test_structure.py
%pytest

%files %{python_files}
%license LICENSE
%doc ChangeLog README.md
%python_alternative %{_bindir}/impacket-GetADUsers
%python_alternative %{_bindir}/impacket-GetNPUsers
%python_alternative %{_bindir}/impacket-GetUserSPNs
%python_alternative %{_bindir}/impacket-addcomputer
%python_alternative %{_bindir}/impacket-atexec
%python_alternative %{_bindir}/impacket-dcomexec
%python_alternative %{_bindir}/impacket-dpapi
%python_alternative %{_bindir}/impacket-esentutl
%python_alternative %{_bindir}/impacket-findDelegation
%python_alternative %{_bindir}/impacket-getArch
%python_alternative %{_bindir}/impacket-getPac
%python_alternative %{_bindir}/impacket-getST
%python_alternative %{_bindir}/impacket-getTGT
%python_alternative %{_bindir}/impacket-goldenPac
%python_alternative %{_bindir}/impacket-ifmap
%python_alternative %{_bindir}/impacket-karmaSMB
%python_alternative %{_bindir}/impacket-kintercept
%python_alternative %{_bindir}/impacket-lookupsid
%python_alternative %{_bindir}/impacket-mimikatz
%python_alternative %{_bindir}/impacket-mqtt_check
%python_alternative %{_bindir}/impacket-mssqlclient
%python_alternative %{_bindir}/impacket-mssqlinstance
%python_alternative %{_bindir}/impacket-netview
%python_alternative %{_bindir}/impacket-nmapAnswerMachine
%python_alternative %{_bindir}/impacket-ntfs-read
%python_alternative %{_bindir}/impacket-ntlmrelayx
%python_alternative %{_bindir}/impacket-opdump
%python_alternative %{_bindir}/impacket-ping
%python_alternative %{_bindir}/impacket-ping6
%python_alternative %{_bindir}/impacket-psexec
%python_alternative %{_bindir}/impacket-raiseChild
%python_alternative %{_bindir}/impacket-rdp_check
%python_alternative %{_bindir}/impacket-reg
%python_alternative %{_bindir}/impacket-registry-read
%python_alternative %{_bindir}/impacket-rpcdump
%python_alternative %{_bindir}/impacket-sambaPipe
%python_alternative %{_bindir}/impacket-samrdump
%python_alternative %{_bindir}/impacket-secretsdump
%python_alternative %{_bindir}/impacket-services
%python_alternative %{_bindir}/impacket-smbclient
%python_alternative %{_bindir}/impacket-smbexec
%python_alternative %{_bindir}/impacket-smbrelayx
%python_alternative %{_bindir}/impacket-smbserver
%python_alternative %{_bindir}/impacket-sniff
%python_alternative %{_bindir}/impacket-sniffer
%python_alternative %{_bindir}/impacket-split
%python_alternative %{_bindir}/impacket-ticketConverter
%python_alternative %{_bindir}/impacket-ticketer
%python_alternative %{_bindir}/impacket-wmiexec
%python_alternative %{_bindir}/impacket-wmipersist
%python_alternative %{_bindir}/impacket-wmiquery
%{python_sitelib}/impacket*

%changelog
