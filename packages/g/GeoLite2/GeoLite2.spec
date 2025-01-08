#
# spec file for package GeoLite2
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


Name:           GeoLite2
Version:        2024.10.25
Release:        0
Summary:        Free Geolocation Data
License:        CC-BY-SA-4.0
URL:            https://github.com/P3TERX/GeoLite.mmdb
Source0:        %{name}-ASN.mmdb
Source1:        %{name}-City.mmdb
Source2:        %{name}-Country.mmdb
BuildRequires:  mmdblookup
BuildArch:      noarch

%description
This package includes %{name} data created by MaxMind, available from
https://www.maxmind.com

%package ASN
Summary:        Free Geolocation ASN Data

%description ASN
This package includes GeoLite2 data created by MaxMind, available from
https://www.maxmind.com

%package City
Summary:        Free Geolocation City Data

%description City
This package includes GeoLite2 data created by MaxMind, available from
https://www.maxmind.com

%package Country
Summary:        Free Geolocation Country Data

%description Country
This package includes GeoLite2 data created by MaxMind, available from
https://www.maxmind.com

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -Dpm0644 %{SOURCE0} %{buildroot}%{_datadir}/%{name}/%{name}-ASN.mmdb
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/%{name}-City.mmdb
install -Dpm0644 %{SOURCE2} %{buildroot}%{_datadir}/%{name}/%{name}-Country.mmdb

%check
# The GeoLite2-City.mmdb database should show correctly the cities of the Crimean IPs.
%define _ip 178.219.171.159
mmdblookup --file %{buildroot}%{_datadir}/%{name}/%{name}-ASN.mmdb --ip %{_ip} autonomous_system_organization
mmdblookup --file %{buildroot}%{_datadir}/%{name}/%{name}-City.mmdb --ip %{_ip} city names en
mmdblookup --file %{buildroot}%{_datadir}/%{name}/%{name}-Country.mmdb --ip %{_ip} country names en

%files ASN
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}-ASN.mmdb

%files City
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}-City.mmdb

%files Country
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}-Country.mmdb

%changelog
