#
# spec file for package perl-Net-DNS
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.490.0
Release:        0
# 1.49 -> normalize -> 1.490.0
%define cpan_version 1.49
License:        MIT
Summary:        Perl Interface to the Domain Name System
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.1
BuildRequires:  perl(Digest::HMAC) >= 1.03
BuildRequires:  perl(Digest::MD5) >= 2.37
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
BuildRequires:  perl(Socket) >= 1.81
BuildRequires:  perl(Test::Builder) >= 0.8
BuildRequires:  perl(Test::More) >= 0.8
BuildRequires:  perl(Time::Local) >= 1.19
BuildRequires:  perl(base) >= 2.13
BuildRequires:  perl(constant) >= 1.17
BuildRequires:  perl(overload) >= 1.06
#BuildRequires:  perl(warnings) >= 1.05
Requires:       perl(base) >= 2.13
Requires:       perl(Carp) >= 1.1
Requires:       perl(Digest::HMAC) >= 1.03
Requires:       perl(Digest::MD5) >= 2.37
Requires:       perl(Digest::SHA) >= 5.23
Requires:       perl(Encode) >= 2.26
Requires:       perl(Exporter) >= 5.63
Requires:       perl(File::Spec) >= 3.29
Requires:       perl(IO::File) >= 1.14
Requires:       perl(IO::Socket) >= 1.3
Requires:       perl(IO::Socket::IP) >= 0.38
Requires:       perl(PerlIO) >= 1.05
Requires:       perl(Scalar::Util) >= 1.19
Requires:       perl(Socket) >= 1.81
Requires:       perl(Time::Local) >= 1.19
Requires:       perl(constant) >= 1.17
Requires:       perl(overload) >= 1.06
#Requires:       perl(warnings) >= 1.0501
Provides:       perl(Net::DNS) = %{version}
Provides:       perl(Net::DNS::Domain)
Provides:       perl(Net::DNS::DomainName)
Provides:       perl(Net::DNS::DomainName1035)
Provides:       perl(Net::DNS::DomainName2535)
Provides:       perl(Net::DNS::Header)
Provides:       perl(Net::DNS::Mailbox)
Provides:       perl(Net::DNS::Mailbox1035)
Provides:       perl(Net::DNS::Mailbox2535)
Provides:       perl(Net::DNS::Nameserver)
Provides:       perl(Net::DNS::Packet)
Provides:       perl(Net::DNS::Parameters)
Provides:       perl(Net::DNS::Question)
Provides:       perl(Net::DNS::RR)
Provides:       perl(Net::DNS::RR::A)
Provides:       perl(Net::DNS::RR::AAAA)
Provides:       perl(Net::DNS::RR::AFSDB)
Provides:       perl(Net::DNS::RR::AMTRELAY)
Provides:       perl(Net::DNS::RR::APL)
Provides:       perl(Net::DNS::RR::APL::Item)
Provides:       perl(Net::DNS::RR::CAA)
Provides:       perl(Net::DNS::RR::CDNSKEY)
Provides:       perl(Net::DNS::RR::CDS)
Provides:       perl(Net::DNS::RR::CERT)
Provides:       perl(Net::DNS::RR::CNAME)
Provides:       perl(Net::DNS::RR::CSYNC)
Provides:       perl(Net::DNS::RR::DELEG)
Provides:       perl(Net::DNS::RR::DHCID)
Provides:       perl(Net::DNS::RR::DNAME)
Provides:       perl(Net::DNS::RR::DNSKEY)
Provides:       perl(Net::DNS::RR::DS)
Provides:       perl(Net::DNS::RR::DSYNC)
Provides:       perl(Net::DNS::RR::EUI48)
Provides:       perl(Net::DNS::RR::EUI64)
Provides:       perl(Net::DNS::RR::GPOS)
Provides:       perl(Net::DNS::RR::HINFO)
Provides:       perl(Net::DNS::RR::HIP)
Provides:       perl(Net::DNS::RR::HTTPS)
Provides:       perl(Net::DNS::RR::IPSECKEY)
Provides:       perl(Net::DNS::RR::ISDN)
Provides:       perl(Net::DNS::RR::KEY)
Provides:       perl(Net::DNS::RR::KX)
Provides:       perl(Net::DNS::RR::L32)
Provides:       perl(Net::DNS::RR::L64)
Provides:       perl(Net::DNS::RR::LOC)
Provides:       perl(Net::DNS::RR::LP)
Provides:       perl(Net::DNS::RR::MB)
Provides:       perl(Net::DNS::RR::MG)
Provides:       perl(Net::DNS::RR::MINFO)
Provides:       perl(Net::DNS::RR::MR)
Provides:       perl(Net::DNS::RR::MX)
Provides:       perl(Net::DNS::RR::NAPTR)
Provides:       perl(Net::DNS::RR::NID)
Provides:       perl(Net::DNS::RR::NS)
Provides:       perl(Net::DNS::RR::NSEC)
Provides:       perl(Net::DNS::RR::NSEC3)
Provides:       perl(Net::DNS::RR::NSEC3PARAM)
Provides:       perl(Net::DNS::RR::NULL)
Provides:       perl(Net::DNS::RR::OPENPGPKEY)
Provides:       perl(Net::DNS::RR::OPT)
Provides:       perl(Net::DNS::RR::OPT::CHAIN)
Provides:       perl(Net::DNS::RR::OPT::CLIENT_SUBNET)
Provides:       perl(Net::DNS::RR::OPT::COOKIE)
Provides:       perl(Net::DNS::RR::OPT::DAU)
Provides:       perl(Net::DNS::RR::OPT::DHU)
Provides:       perl(Net::DNS::RR::OPT::EXPIRE)
Provides:       perl(Net::DNS::RR::OPT::EXTENDED_ERROR)
Provides:       perl(Net::DNS::RR::OPT::KEY_TAG)
Provides:       perl(Net::DNS::RR::OPT::N3U)
Provides:       perl(Net::DNS::RR::OPT::NSID)
Provides:       perl(Net::DNS::RR::OPT::PADDING)
Provides:       perl(Net::DNS::RR::OPT::REPORT_CHANNEL)
Provides:       perl(Net::DNS::RR::OPT::TCP_KEEPALIVE)
Provides:       perl(Net::DNS::RR::OPT::ZONEVERSION)
Provides:       perl(Net::DNS::RR::PTR)
Provides:       perl(Net::DNS::RR::PX)
Provides:       perl(Net::DNS::RR::RP)
Provides:       perl(Net::DNS::RR::RRSIG)
Provides:       perl(Net::DNS::RR::RT)
Provides:       perl(Net::DNS::RR::SIG)
Provides:       perl(Net::DNS::RR::SMIMEA)
Provides:       perl(Net::DNS::RR::SOA)
Provides:       perl(Net::DNS::RR::SPF)
Provides:       perl(Net::DNS::RR::SRV)
Provides:       perl(Net::DNS::RR::SSHFP)
Provides:       perl(Net::DNS::RR::SVCB)
Provides:       perl(Net::DNS::RR::TKEY)
Provides:       perl(Net::DNS::RR::TLSA)
Provides:       perl(Net::DNS::RR::TSIG)
Provides:       perl(Net::DNS::RR::TXT)
Provides:       perl(Net::DNS::RR::URI)
Provides:       perl(Net::DNS::RR::X25)
Provides:       perl(Net::DNS::RR::ZONEMD)
Provides:       perl(Net::DNS::Resolver)
Provides:       perl(Net::DNS::Resolver::Base)
Provides:       perl(Net::DNS::Resolver::MSWin32)
Provides:       perl(Net::DNS::Resolver::Recurse)
Provides:       perl(Net::DNS::Resolver::UNIX)
Provides:       perl(Net::DNS::Resolver::android)
Provides:       perl(Net::DNS::Resolver::cygwin)
Provides:       perl(Net::DNS::Resolver::os2)
Provides:       perl(Net::DNS::Resolver::os390)
Provides:       perl(Net::DNS::Text)
Provides:       perl(Net::DNS::Update)
Provides:       perl(Net::DNS::ZoneFile)
Provides:       perl(Net::DNS::ZoneFile::Generator)
Provides:       perl(Net::DNS::ZoneFile::Text)
%undefine       __perllib_provides
Recommends:     perl(Digest::BubbleBabble) >= 0.20.0
Recommends:     perl(Net::LibIDN2) >= 1
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(warnings) >= 1.05
Requires:       perl(warnings) >= 1.05
# MANUAL END

%description
Net::DNS is a collection of Perl modules that act as a Domain Name System
(DNS) resolver. It allows the programmer to perform DNS queries that are
beyond the capabilities of "gethostbyname" and "gethostbyaddr".

The programmer should be familiar with the structure of a DNS packet and
the zone file presentation format described in RFC1035.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
