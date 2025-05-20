#
# spec file for package ktoblzcheck-data
#
# Copyright (c) 2025 SUSE LLC
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
%define pysuffix         3
%define pydep            python3 python3-openpyxl
%define pyversion %(echo `python%{pysuffix} -c "import sys; sys.stdout.write(sys.version[:3])"`)

%define _kname  ktoblzcheck
%define _name   ktoblzcheck-data
Name:           %{_name}
Summary:        A library to check account numbers and bank codes of German banks
Version:        20250515
Release:        0
Source:         http://downloads.sourceforge.net/project/%{_kname}/%{_name}-%{version}.tar.gz
Source1:        download---bankleitzahlen-602592
Source2:        BIC-lijst-NL-2.xlsx
Source3:        bcbankenstamm
Source4:        verzeichnis-der-erreichbaren-zahlungsdienstleister-data.csv
Group:          Productivity/Office/Finance
License:        LGPL-2.1-only
URL:            http://ktoblzcheck.sourceforge.net
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  %{pydep}
BuildArch:      noarch

%description
KtoBLZCheck is a library to check account numbers and bank codes
of German banks. Both a library for other programs as well as a
short command-line tool is available. It is possible to check
pairs of account numbers and bank codes (BLZ) of German banks,
and to map bank codes (BLZ) to the clear-text name and location
of the bank.

%prep
%autosetup -p1 -n %{_name}-%{version}
cp %{SOURCE1} data/blz_$(date '+%Y%m%d').txt
cp %{SOURCE2} data/nl_data.xlsx
cp %{SOURCE3} data/ch_data.txt
cp %{SOURCE4} data/sepa_$(date '+%Y%m%d').txt

%build
%cmake \
    -DINSTALL_RAW_BANKDATA_FILE=1\
    -DENABLE_BANKDATA_DOWNLOAD=0
%cmake_build

%install
%cmake_install DESTDIR=%{buildroot}

%files
%defattr(-,root,root)
%doc README.md
%{_datadir}/%{_kname}

%changelog
