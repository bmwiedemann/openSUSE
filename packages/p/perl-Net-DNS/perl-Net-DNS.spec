#
# spec file for package perl-Net-DNS
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Net-DNS
Name:           perl-Net-DNS
Version:        1.36
Release:        0
License:        MIT
Summary:        Perl Interface to the Domain Name System
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.1
BuildRequires:  perl(Digest::HMAC) >= 1.03
BuildRequires:  perl(Digest::SHA) >= 5.23
BuildRequires:  perl(Encode) >= 2.26
BuildRequires:  perl(Exporter) >= 5.63
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.48
BuildRequires:  perl(File::Find) >= 1.13
BuildRequires:  perl(File::Spec) >= 3.29
BuildRequires:  perl(Getopt::Long) >= 2.43
BuildRequires:  perl(IO::File) >= 1.14
BuildRequires:  perl(IO::Socket) >= 1.3
BuildRequires:  perl(IO::Socket::IP) >= 0.38
BuildRequires:  perl(PerlIO) >= 1.05
BuildRequires:  perl(Scalar::Util) >= 1.19
BuildRequires:  perl(Test::Builder) >= 0.8
BuildRequires:  perl(Test::More) >= 0.8
BuildRequires:  perl(Time::Local) >= 1.19
Requires:       perl(Carp) >= 1.1
Requires:       perl(Digest::HMAC) >= 1.03
Requires:       perl(Digest::SHA) >= 5.23
Requires:       perl(Encode) >= 2.26
Requires:       perl(Exporter) >= 5.63
Requires:       perl(File::Spec) >= 3.29
Requires:       perl(IO::File) >= 1.14
Requires:       perl(IO::Socket) >= 1.3
Requires:       perl(IO::Socket::IP) >= 0.38
Requires:       perl(PerlIO) >= 1.05
Requires:       perl(Scalar::Util) >= 1.19
Requires:       perl(Time::Local) >= 1.19
Recommends:     perl(Digest::BubbleBabble) >= 0.02
Recommends:     perl(Net::LibIDN2) >= 1
%{perl_requires}

%description
Net::DNS is a collection of Perl modules that act as a Domain Name System
(DNS) resolver. It allows the programmer to perform DNS queries that are
beyond the capabilities of "gethostbyname" and "gethostbyaddr".

The programmer should be familiar with the structure of a DNS packet. See
RFC 1035 or DNS and BIND (Albitz & Liu) for details.

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
