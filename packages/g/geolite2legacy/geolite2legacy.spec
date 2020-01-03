#
# spec file for package geolite2legacy
#
# Copyright (c) 2019 SUSE LLC
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


Name:           geolite2legacy
Version:        0+git20200101.56d8a4f
Release:        0
Summary:        GeoLite2 (CSV) to Legacy format converter
License:        MIT
Url:            https://github.com/sherpya/geolite2legacy 
Source:         %{name}-%{version}.tar.xz
Patch0:         0001-Automatically-determine-output-file-name.patch
Patch1:         0001-Use-realpath-to-determine-fips-file-location.patch
BuildArch:      noarch

%description
Script to convert the GeoLite2 CSV database to Legacy GeoIP
format. Note that GeoIP is deprecated by upstream and should be
replaced by GeoLite2.

%prep
%autosetup
sed -i -e 's/env python3\?/python3/' *.py

%build

%install
mkdir -p %{buildroot}%{_datadir}/geolite2legacy %{buildroot}%{_bindir}
install -m 755 geolite2legacy.py geoname2fips.py %{buildroot}%{_datadir}/geolite2legacy
install -m 644 geoname2fips.csv pygeoip_const.py %{buildroot}%{_datadir}/geolite2legacy
ln -s %{_datadir}/geolite2legacy/geolite2legacy.py %{buildroot}%{_bindir}/geolite2legacy

%files
%doc README.md LICENSE
%{_bindir}/geolite2legacy
%{_datadir}/geolite2legacy

%changelog

