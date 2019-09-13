#
# spec file for package snmpsim
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           snmpsim
Version:        0.4.7
Release:        0
Summary:        SNMP Agents simulator
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/etingof/snmpsim
Source:         https://files.pythonhosted.org/packages/source/s/snmpsim/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-dbm
BuildRequires:  python3-pycryptodomex
BuildRequires:  python3-pysnmp
BuildRequires:  python3-setuptools
Requires:       python3-dbm
Requires:       python3-pysnmp >= 4.4.3
BuildArch:      noarch

%description
SNMP Simulator is a software that would act like a multitude of real
physical devices from SNMP Manager's point of view. Simulator builds
and uses a database of physical devices' SNMP footprints to respond
like their real counterparts do.

Typical use case for this software starts with recording a snapshot
of SNMP objects of donor agents into text files. Once you have your
snapshots at hand, a simulator script could be run over the snapshots
responding to SNMP queries in the same way as donor SNMP agents did
at the time of recording.

Technically, SNMP Simulator is a multi-context SNMP agent. That means
that it handles multiple sets of managed object all at once.
Each device is simulated within a dedicated SNMP context.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install \
  --root=%{buildroot} \
  --prefix=%{_prefix} \
  --exec-prefix=%{_prefix} \
  --install-data=%{_datadir}

mv %{buildroot}%{_bindir}/datafile.py %{buildroot}%{_bindir}/snmpsim-datafile
mv %{buildroot}%{_bindir}/mib2dev.py %{buildroot}%{_bindir}/snmpsim-mib2dev
mv %{buildroot}%{_bindir}/pcap2dev.py %{buildroot}%{_bindir}/pcap2dev
mv %{buildroot}%{_bindir}/snmprec.py %{buildroot}%{_bindir}/snmprec
mv %{buildroot}%{_bindir}/snmpsimd.py %{buildroot}%{_bindir}/snmpsimd

%fdupes %{buildroot}%{python3_sitelib}

%check
python3 setup.py test

%files
%license LICENSE.txt
%doc CHANGES.txt README.md
%{_bindir}/snmpsim-datafile
%{_bindir}/snmpsim-mib2dev
%{_bindir}/pcap2dev
%{_bindir}/snmprec
%{_bindir}/snmpsimd
%{python3_sitelib}/*
%{_datadir}/snmpsim

%changelog
