#
# spec file for package python-impacket
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020-2024, Martin Hauke <mardnh@gmx.de>
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


%define binaries impacket-GetADUsers impacket-GetADComputers impacket-Get-GPPPassword impacket-GetLAPSPassword impacket-GetNPUsers impacket-GetUserSPNs impacket-DumpNTLMInfo impacket-addcomputer impacket-atexec impacket-changepasswd impacket-dacledit impacket-dcomexec impacket-describeTicket impacket-dpapi impacket-esentutl impacket-exchanger impacket-findDelegation impacket-getArch impacket-getPac impacket-getST impacket-getTGT impacket-goldenPac impacket-karmaSMB impacket-keylistattack impacket-kintercept impacket-lookupsid impacket-machine_role impacket-mimikatz impacket-mqtt_check impacket-mssqlclient impacket-mssqlinstance impacket-net impacket-netview impacket-ntfs-read impacket-ntlmrelayx impacket-owneredit impacket-ping impacket-ping6 impacket-psexec impacket-raiseChild impacket-rbcd impacket-rdp_check impacket-reg impacket-registry-read impacket-rpcmap impacket-rpcdump impacket-sambaPipe impacket-samrdump impacket-secretsdump impacket-services impacket-smbclient impacket-smbexec impacket-smbserver impacket-sniff impacket-sniffer impacket-split impacket-ticketConverter impacket-ticketer impacket-tstool impacket-wmiexec impacket-wmipersist impacket-wmiquery

Name:           python-impacket
Version:        0.12.0
Release:        0
Summary:        Python3 module to easily build and dissect network protocols
# License: modified Apache-1.1 (see file LICENSE)
License:        Apache-1.1
Group:          Development/Languages/Python
URL:            https://www.secureauth.com/labs/open-source-tools/impacket
#Git-Clone:     https://github.com/fortra/impacket.git
Source:         https://files.pythonhosted.org/packages/source/i/impacket/impacket-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 1.0
Requires:       python-charset-normalizer
Requires:       python-ldap3 >= 2.5
Requires:       python-ldapdomaindump >= 0.9.0
Requires:       python-pyOpenSSL >= 0.13.1
Requires:       python-pyasn1 >= 0.2.3
Requires:       python-pycryptodomex
Requires:       python-setuptools
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Flask >= 1.0}
BuildRequires:  %{python_module chardet}
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
%autosetup -p1 -n impacket-%{version}
sed -e '/^#!\//, 1d' -i \
  impacket/examples/ntlmrelayx/servers/socksserver.py \
  impacket/examples/mssqlshell.py \
  impacket/mqtt.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand cd %{buildroot}%{_bindir} && find . -name "*.py" -exec sh -c 'mv $0 impacket-`basename "$0" .py`' '{}' \;
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
#
%python_expand rm -f %{buildroot}%{_datadir}/doc/impacket/LICENSE
%python_expand rm -f %{buildroot}%{_datadir}/doc/impacket/README.md
%python_expand %fdupes %{buildroot}%{$python_sitelib}
#
%python_expand rm %{buildroot}%{_bindir}/_current_flavor

%post
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_install_alternative " .. b .. "\n"))
end}

%postun
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_uninstall_alternative " .. b .. "\n"))
end}

%check
# Don't run tests that require online connections
rm tests/dcerpc/test_bkrp.py
rm tests/dcerpc/test_dcomrt.py
rm tests/dcerpc/test_dhcpm.py
rm tests/dcerpc/test_drsuapi.py
rm tests/dcerpc/test_epm.py
rm tests/dcerpc/test_even.py
rm tests/dcerpc/test_even6.py
rm tests/dcerpc/test_fasp.py
rm tests/SMB_RPC/test_ldap.py
rm tests/dcerpc/test_lsad.py
rm tests/dcerpc/test_lsat.py
rm tests/dcerpc/test_mgmt.py
rm tests/dcerpc/test_mimilib.py
rm tests/SMB_RPC/test_nmb.py
rm tests/dcerpc/test_nrpc.py
rm tests/dcerpc/test_par.py
rm tests/SMB_RPC/test_rpch.py
rm tests/SMB_RPC/test_rpcrt.py
rm tests/dcerpc/test_rprn.py
rm tests/dcerpc/test_rrp.py
rm tests/dcerpc/test_samr.py
rm tests/dcerpc/test_scmr.py
rm tests/SMB_RPC/test_secretsdump.py
rm tests/SMB_RPC/test_smb.py
rm tests/dcerpc/test_srvs.py
rm tests/dcerpc/test_tsch.py
rm tests/dcerpc/test_wkst.py
rm tests/SMB_RPC/test_wmi.py
rm tests/misc/test_dcerpc_v5_ndr.py
rm tests/misc/test_structure.py
rm tests/SMB_RPC/test_smbserver.py
#%%pytest -k 'not (test_well_formed)'
%pytest

%files %{python_files}
%license LICENSE
%doc ChangeLog.md README.md
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. b .. "\n"))
end}
%{python_sitelib}/impacket
%{python_sitelib}/impacket-%{version}.dist-info

%changelog
