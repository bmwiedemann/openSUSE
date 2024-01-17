#
# spec file for package perl-Geo-IP2Location
#
# Copyright (c) 2023 SUSE LLC
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
Version:        8.70
Release:        0
#Upstream: CHECK(Artistic-1.0 or GPL-1.0-or-later)
License:        MIT
Summary:        Lookup of country, region, city, latitude, longitude, ZIP code, time zon[cut]
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LO/LOCATION/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This Perl module provides fast lookup of country, region, city, latitude,
longitude, ZIP code, time zone, ISP, domain name, connection type, IDD
code, area code, weather station code and station, MCC, MNC, mobile carrier
brand, elevation, usage type, IP address type, IAB advertising category,
district, AS number and AS name from IP address using IP2Location database.
This module uses a file based BIN database available at at
https://www.ip2location.com/database/ip2location upon subscription. You can
visit at https://www.ip2location.com/development-libraries to download BIN
sample files. This database consists of IP address as keys and other
information as values. It supports all IP addresses in IPv4 and IPv6.

This module can be used in many types of project such as:

 1) auto-select the geographically closest mirror server
 2) analyze web server logs to determine the countries of visitors
 3) credit card fraud detection
 4) software export controls
 5) display native language and currency
 6) prevent password sharing and abuse of service
 7) geotargeting in advertisement

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
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
