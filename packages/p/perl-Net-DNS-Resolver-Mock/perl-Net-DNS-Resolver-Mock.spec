#
# spec file for package perl-Net-DNS-Resolver-Mock
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


%define cpan_name Net-DNS-Resolver-Mock
Name:           perl-Net-DNS-Resolver-Mock
Version:        1.20230216
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Mock a DNS Resolver object for testing
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Net::DNS::Packet)
BuildRequires:  perl(Net::DNS::Question)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Net::DNS::ZoneFile)
BuildRequires:  perl(Test::Exception)
Requires:       perl(Net::DNS::Packet)
Requires:       perl(Net::DNS::Question)
Requires:       perl(Net::DNS::Resolver)
Requires:       perl(Net::DNS::ZoneFile)
%{perl_requires}

%description
A subclass of Net::DNS::Resolver which parses a zonefile for it's data
source. Primarily for use in testing.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
