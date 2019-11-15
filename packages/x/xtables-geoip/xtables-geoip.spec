#
# spec file for package xtables-geoip
#
# Copyright (c) 2019 SUSE LLC.
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


Name:           xtables-geoip
Version:        20191112
Release:        0
Summary:        Geolocation database files for xt_geoip
License:        CC-BY-SA-4.0
Group:          Productivity/Networking/Security
URL:            https://dev.maxmind.com/geoip/geoip2/geolite2/
# Source:       https://geolite.maxmind.com/download/geoip/database/GeoLite2-Country-CSV_%version.zip
Source:         GeoLite2-Country-CSV_%version.zip
Source4:        %name-rpmlintrc
BuildArch:      noarch
BuildRequires:  unzip
BuildRequires:  xtables-addons >= 3.2
#db format changed at that time
Conflicts:      xtables-addons < 1.33

%description
The package contains the GeoIP definition files (which IP addresses
belong to which country) that are needed for Xtables-addons's
xt_geoip module.

This product includes GeoLite data created by MaxMind, available from
http://maxmind.com/.

Author(s):
----------
	The GeoIP data is from MaxMind.com.
Please do not contact them for errors with this package.

%prep
%setup -qn GeoLite2-Country-CSV_%version

%build

%install
b="%buildroot"
mkdir -p "$b/%_datadir/xt_geoip"
%_libexecdir/xtables-addons/xt_geoip_build -D "$b/%_datadir/xt_geoip/"

%files
%defattr(-,root,root)
%_datadir/xt_geoip/

%changelog
