#
# spec file for package perl-Net-DNS-Resolver-Mock
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Net-DNS-Resolver-Mock
Version:        1.20171219
Release:        0
%define cpan_name Net-DNS-Resolver-Mock
Summary:        Mock a DNS Resolver object for testing
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Net::DNS::Packet)
BuildRequires:  perl(Net::DNS::Question)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Net::DNS::ZoneFile)
Requires:       perl(Net::DNS::Packet)
Requires:       perl(Net::DNS::Question)
Requires:       perl(Net::DNS::Resolver)
Requires:       perl(Net::DNS::ZoneFile)
%{perl_requires}

%description
A subclass of Net::DNS::Resolver which parses a zonefile for it's data
source. Primarily for use in testing.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc README
%license LICENSE

%changelog
