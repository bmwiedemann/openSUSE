#
# spec file for package perl-Geo-IP2Location
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Geo-IP2Location
Name:           perl-Geo-IP2Location
Version:        8.800.0
Release:        0
# 8.80 -> normalize -> 8.800.0
%define cpan_version 8.80
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        MIT
Summary:        Lookup of country, region, city, latitude, longitude, ZIP code, time zon[cut]
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LO/LOCATION/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Geo::IP2Location) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This Perl module provides a fast and simple way to look up geolocation and
network information for an IP address using an IP2Location BIN database.

It allows you to retrieve a wide range of data using IPv4 and IPv6
addresses, including:

 a) Geolocation: Country, Region, City, Latitude, Longitude, ZIP Code, Time Zone, District, Elevation
 b) Network: ISP, Domain Name, Connection Type, IP Address Type, Usage Type
 c) Carrier Information: Mobile Country Code (MCC), Mobile Network Code (MNC), Mobile Carrier Brand
 d) Autonomous System (AS): AS Number, AS Name, AS Domain Name, AS Usage Type, AS CIDR
 e) Additional Data: IDD Code, Area Code, Weather Station Code, Weather Station Name, IAB Advertising Category

This module can be used in many types of project such as:

 1) Selecting the geographically closest mirror for content delivery.
 2) Analyzing web server logs to determine the countries of your visitors.
 3) Detecting and preventing credit card fraud.
 4) Implementing software export controls.
 5) Displaying native languages and currencies to users.
 6) Preventing password sharing and service abuse.
 7) Geotargeting content and advertisements.

To ensure high accuracy, the commercial databases are updated on a daily,
weekly or semi-monthly basis.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

# MANUAL BEGIN
sed -i 's/\r$//' samples/WHERE_TO_DOWNLOAD_MORE_SAMPLES.TXT
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README samples
%license LICENSE

%changelog
