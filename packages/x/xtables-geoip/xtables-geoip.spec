#
# spec file for package xtables-geoip
#
# Copyright (c) 2020 SUSE LLC
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


%define year    2020
%define month   10

Name:           xtables-geoip
Version:        %year%{month}01
Release:        0
Summary:        Geolocation database files for xt_geoip
License:        CC-BY-4.0
Group:          Productivity/Networking/Security
URL:            https://db-ip.com/db/lite.php
Source:         https://download.db-ip.com/free/dbip-country-lite-%year-%month.csv.gz
Source4:        %name-rpmlintrc
BuildRequires:  xtables-addons >= 3.8
BuildArch:      noarch
#db format changed
Conflicts:      xtables-addons < 3.2

%description
The package contains the GeoIP definition files (which IP addresses
belong to which country) that are needed for Xtables-addons's
xt_geoip module.

This product includes Country Lite data created by DBIP, available from
https://db-ip.com/db/lite.php .
Please do not contact them for errors with this package.

%prep
gunzip --stdout %{SOURCE0} > dbip-country-lite.csv

%build

%install
install -d "%buildroot/%_datadir/xt_geoip"
"%_libexecdir/xtables-addons/xt_geoip_build" -D "%buildroot/%_datadir/xt_geoip/"

%files
%_datadir/xt_geoip/

%changelog
