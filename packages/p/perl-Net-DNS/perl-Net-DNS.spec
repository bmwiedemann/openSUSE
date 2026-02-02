#
# spec file for package perl-Net-DNS
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.540.0
Release:        0
# 1.54 -> normalize -> 1.540.0
%define cpan_version 1.54
License:        MIT
Summary:        Perl Interface to the Domain Name System
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NL/NLNETLABS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.1
BuildRequires:  perl(Digest::HMAC) >= 1.30
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
Requires:       perl(Digest::HMAC) >= 1.30
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
Provides:       perl(Net::DNS::Domain) = 2002.0.0
Provides:       perl(Net::DNS::DomainName) = 2005.0.0
Provides:       perl(Net::DNS::DomainName1035)
Provides:       perl(Net::DNS::DomainName2535)
Provides:       perl(Net::DNS::Header) = 2042.0.0
Provides:       perl(Net::DNS::Mailbox) = 2002.0.0
Provides:       perl(Net::DNS::Mailbox1035)
Provides:       perl(Net::DNS::Mailbox2535)
Provides:       perl(Net::DNS::Nameserver) = 2002.0.0
Provides:       perl(Net::DNS::Packet) = 2003.0.0
Provides:       perl(Net::DNS::Parameters) = 2043.0.0
Provides:       perl(Net::DNS::Question) = 2002.0.0
Provides:       perl(Net::DNS::RR) = 2037.0.0
Provides:       perl(Net::DNS::RR::A) = 2003.0.0
Provides:       perl(Net::DNS::RR::AAAA) = 2003.0.0
Provides:       perl(Net::DNS::RR::AFSDB) = 2002.0.0
Provides:       perl(Net::DNS::RR::AMTRELAY) = 2003.0.0
Provides:       perl(Net::DNS::RR::APL) = 2003.0.0
Provides:       perl(Net::DNS::RR::APL::Item)
Provides:       perl(Net::DNS::RR::CAA) = 2003.0.0
Provides:       perl(Net::DNS::RR::CDNSKEY) = 2003.0.0
Provides:       perl(Net::DNS::RR::CDS) = 2003.0.0
Provides:       perl(Net::DNS::RR::CERT) = 2042.0.0
Provides:       perl(Net::DNS::RR::CNAME) = 2003.0.0
Provides:       perl(Net::DNS::RR::CSYNC) = 2003.0.0
Provides:       perl(Net::DNS::RR::DELEG) = 2043.0.0
Provides:       perl(Net::DNS::RR::DELEGI) = 2043.0.0
Provides:       perl(Net::DNS::RR::DHCID) = 2003.0.0
Provides:       perl(Net::DNS::RR::DNAME) = 2003.0.0
Provides:       perl(Net::DNS::RR::DNSKEY) = 2042.0.0
Provides:       perl(Net::DNS::RR::DS) = 2042.0.0
Provides:       perl(Net::DNS::RR::DSYNC) = 2003.0.0
Provides:       perl(Net::DNS::RR::EUI48) = 2003.0.0
Provides:       perl(Net::DNS::RR::EUI64) = 2003.0.0
Provides:       perl(Net::DNS::RR::GPOS) = 2003.0.0
Provides:       perl(Net::DNS::RR::HINFO) = 2003.0.0
Provides:       perl(Net::DNS::RR::HIP) = 2003.0.0
Provides:       perl(Net::DNS::RR::HTTPS) = 2002.0.0
Provides:       perl(Net::DNS::RR::IPSECKEY) = 2003.0.0
Provides:       perl(Net::DNS::RR::ISDN) = 2002.0.0
Provides:       perl(Net::DNS::RR::KEY) = 2002.0.0
Provides:       perl(Net::DNS::RR::KX) = 2003.0.0
Provides:       perl(Net::DNS::RR::L32) = 2003.0.0
Provides:       perl(Net::DNS::RR::L64) = 2003.0.0
Provides:       perl(Net::DNS::RR::LOC) = 2003.0.0
Provides:       perl(Net::DNS::RR::LP) = 2003.0.0
Provides:       perl(Net::DNS::RR::MB) = 2002.0.0
Provides:       perl(Net::DNS::RR::MG) = 2002.0.0
Provides:       perl(Net::DNS::RR::MINFO) = 2002.0.0
Provides:       perl(Net::DNS::RR::MR) = 2002.0.0
Provides:       perl(Net::DNS::RR::MX) = 2002.0.0
Provides:       perl(Net::DNS::RR::NAPTR) = 2003.0.0
Provides:       perl(Net::DNS::RR::NID) = 2003.0.0
Provides:       perl(Net::DNS::RR::NS) = 2003.0.0
Provides:       perl(Net::DNS::RR::NSEC) = 2002.0.0
Provides:       perl(Net::DNS::RR::NSEC3) = 2003.0.0
Provides:       perl(Net::DNS::RR::NSEC3PARAM) = 2003.0.0
Provides:       perl(Net::DNS::RR::NULL) = 2002.0.0
Provides:       perl(Net::DNS::RR::OPENPGPKEY) = 2003.0.0
Provides:       perl(Net::DNS::RR::OPT) = 2005.0.0
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
Provides:       perl(Net::DNS::RR::PTR) = 2002.0.0
Provides:       perl(Net::DNS::RR::PX) = 2003.0.0
Provides:       perl(Net::DNS::RR::RESINFO) = 2003.0.0
Provides:       perl(Net::DNS::RR::RP) = 2002.0.0
Provides:       perl(Net::DNS::RR::RRSIG) = 2042.0.0
Provides:       perl(Net::DNS::RR::RT) = 2003.0.0
Provides:       perl(Net::DNS::RR::SIG) = 2042.0.0
Provides:       perl(Net::DNS::RR::SMIMEA) = 2003.0.0
Provides:       perl(Net::DNS::RR::SOA) = 2002.0.0
Provides:       perl(Net::DNS::RR::SPF) = 2003.0.0
Provides:       perl(Net::DNS::RR::SRV) = 2003.0.0
Provides:       perl(Net::DNS::RR::SSHFP) = 2003.0.0
Provides:       perl(Net::DNS::RR::SVCB) = 2043.0.0
Provides:       perl(Net::DNS::RR::TKEY) = 2035.0.0
Provides:       perl(Net::DNS::RR::TLSA) = 2003.0.0
Provides:       perl(Net::DNS::RR::TSIG) = 2003.0.0
Provides:       perl(Net::DNS::RR::TXT) = 2003.0.0
Provides:       perl(Net::DNS::RR::URI) = 2003.0.0
Provides:       perl(Net::DNS::RR::X25) = 2002.0.0
Provides:       perl(Net::DNS::RR::ZONEMD) = 2003.0.0
Provides:       perl(Net::DNS::Resolver) = 2017.0.0
Provides:       perl(Net::DNS::Resolver::Base) = 2031.0.0
Provides:       perl(Net::DNS::Resolver::MSWin32) = 2002.0.0
Provides:       perl(Net::DNS::Resolver::Recurse) = 2002.0.0
Provides:       perl(Net::DNS::Resolver::UNIX) = 2007.0.0
Provides:       perl(Net::DNS::Resolver::android) = 2007.0.0
Provides:       perl(Net::DNS::Resolver::cygwin) = 2002.0.0
Provides:       perl(Net::DNS::Resolver::os2) = 2007.0.0
Provides:       perl(Net::DNS::Resolver::os390) = 2007.0.0
Provides:       perl(Net::DNS::Text) = 2043.0.0
Provides:       perl(Net::DNS::Update) = 2017.0.0
Provides:       perl(Net::DNS::ZoneFile) = 2002.0.0
Provides:       perl(Net::DNS::ZoneFile::Generator)
Provides:       perl(Net::DNS::ZoneFile::Text)
%undefine       __perllib_provides
Recommends:     perl(Digest::BubbleBabble) >= 0.20
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
%doc Changes README
%license LICENSE

%changelog
