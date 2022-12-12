#
# spec file for package arpwatch-ethercodes
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2018 LISA GmbH, Bingen, Germany.
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


Name:           arpwatch-ethercodes
Version:        20221212
Release:        0
Summary:        Ethercodes Data for arpwatch
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
URL:            https://standards.ieee.org/products-services/regauth/index.html
# can't use url as it's not stable and bots will decline submission. Update it 
# from here: http://standards-oui.ieee.org/oui/oui.csv
Source0:        oui.csv
Source1:        fetch_ethercodes.py
BuildRequires:  python3
BuildArch:      noarch

%description
Fetch OUI and company ID data from IEEE.org prepared for arpwatch.

%prep
%setup -q -cT
cp -p %{SOURCE0} .
cp -p %{SOURCE1} .

%build
# update oui.csv by executing
#  python3 fetch_ethercodes.py -vvtp arpwatch-ethercodes.spec
# in a local build

# (re)generate ethercodes.dat from oui.csv
python3 fetch_ethercodes.py -vvkt

%install
install -Dm0444 ethercodes.dat %{buildroot}/%{_datadir}/arpwatch/ethercodes.dat

%files
%dir %{_datadir}/arpwatch
%{_datadir}/arpwatch/ethercodes.dat

%changelog
