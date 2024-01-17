#
# spec file for package perl-IP-Country
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-IP-Country
Version:        2.28
Release:        0
#Upstream: GPL-1.0+ or Artistic-1.0
%define cpan_name IP-Country
Summary:        Fast Lookup of Country Codes From Ip Addresses
License:        (GPL-1.0+ or Artistic-1.0) and SUSE-Redistributable-Content
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IP-Country/
Source0:        http://www.cpan.org/authors/id/N/NW/NWETTERS/%{cpan_name}-%{version}.tar.gz
Source1:        perl-IP-Country-rpmlintrc
Source2:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
Requires:       perl(Geography::Countries)
%{perl_requires}

%description
Finding the home country of a client using only the IP address can be
difficult. Looking up the domain name associated with that address can
provide some help, but many IP address are not reverse mapped to any useful
domain, and the most common domain (.com) offers no help when looking for
country.

This module comes bundled with a database of countries where various IP
addresses have been assigned. Although the country of assignment will
probably be the country associated with a large ISP rather than the client
herself, this is probably good enough for most log analysis applications,
and under test has proved to be as accurate as reverse-DNS and WHOIS
lookup.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES README

%changelog
