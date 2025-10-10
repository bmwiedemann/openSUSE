#
# spec file for package perl-Net-CIDR-Set
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


%define cpan_name Net-CIDR-Set
Name:           perl-Net-CIDR-Set
Version:        0.190.0
Release:        0
# 0.19 -> normalize -> 0.190.0
%define cpan_version 0.19
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Manipulate sets of IP addresses
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RR/RRWO/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.22
BuildRequires:  perl(Module::Metadata) >= 1.000015
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(namespace::autoclean)
Provides:       perl(Net::CIDR::Set) = %{version}
Provides:       perl(Net::CIDR::Set::IPv4) = %{version}
Provides:       perl(Net::CIDR::Set::IPv6) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'Net::CIDR::Set' represents sets of IP addresses and allows standard set
operations (union, intersection, membership test etc) to be performed on
them.

In spite of the name it can work with sets consisting of arbitrary ranges
of IP addresses - not just CIDR blocks.

Both IPv4 and IPv6 addresses are handled - but they may not be mixed in the
same set. You may explicitly set the personality of a set:

  my $ip4set = Net::CIDR::Set->new({ type => 'ipv4 }, '10.0.0.0/8');

Normally this isn't necessary - the set will guess its personality from the
first data that is added to it.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING.md README.md SECURITY.md
%license LICENSE

%changelog
