#
# spec file for package arpwatch-ethercodes
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           arpwatch-ethercodes
Version:        2016.03.28
Release:        0
Summary:        Ethercodes Data for arpwatch
License:        BSD-3-Clause
Group:          Productivity/Networking/Diagnostic
Url:            http://standards.ieee.org/regauth/oui/
Source0:        http://standards.ieee.org/regauth/oui/oui.txt
BuildRequires:  arpwatch-ethercodes-build
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
OUI and company ID data as fetched from IEEE.org prepared for arpwatch.

%prep

%build
pushd %{_datadir}/arpwatch
./massagevendor >${RPM_BUILD_DIR}/ethercodes.dat < %{SOURCE0}
popd
if [ ! -s ethercodes.dat ]; then
	echo "File ethercodes.dat is empty!"
	exit 1
fi

%install
mkdir -p \
	%{buildroot}/%{_datadir}/arpwatch
install -m 0444 ethercodes.dat %{buildroot}/%{_datadir}/arpwatch

%files
%defattr(-,root,root)
%{_datadir}/arpwatch

%changelog
