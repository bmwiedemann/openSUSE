#
# spec file for package perl-Mail-SPF
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


%define cpan_name Mail-SPF
Name:           perl-Mail-SPF
Version:        3.202.406.170
Release:        0
# 3.20240617 -> normalize -> 3.202.406.170
%define cpan_version 3.20240617
License:        BSD-3-Clause
Summary:        An object-oriented implementation of Sender Policy Framework
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         skip_test.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Error)
BuildRequires:  perl(Net::DNS::RR)
BuildRequires:  perl(Net::DNS::Resolver)
BuildRequires:  perl(Net::DNS::Resolver::Programmable)
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(URI::Escape) >= 1.13
Requires:       perl(Error)
Requires:       perl(Net::DNS::Resolver)
Requires:       perl(NetAddr::IP)
Requires:       perl(URI::Escape) >= 1.13
Provides:       perl(Mail::SPF) = %{version}
Provides:       perl(Mail::SPF::Base)
Provides:       perl(Mail::SPF::EAbstractClass)
Provides:       perl(Mail::SPF::EClassMethod)
Provides:       perl(Mail::SPF::EDNSError)
Provides:       perl(Mail::SPF::EDNSTimeout)
Provides:       perl(Mail::SPF::EDuplicateGlobalMod)
Provides:       perl(Mail::SPF::EInstanceMethod)
Provides:       perl(Mail::SPF::EInvalidMacro)
Provides:       perl(Mail::SPF::EInvalidMacroString)
Provides:       perl(Mail::SPF::EInvalidMech)
Provides:       perl(Mail::SPF::EInvalidMechQualifier)
Provides:       perl(Mail::SPF::EInvalidMod)
Provides:       perl(Mail::SPF::EInvalidOptionValue)
Provides:       perl(Mail::SPF::EInvalidRecordVersion)
Provides:       perl(Mail::SPF::EInvalidScope)
Provides:       perl(Mail::SPF::EInvalidTerm)
Provides:       perl(Mail::SPF::EJunkInRecord)
Provides:       perl(Mail::SPF::EJunkInTerm)
Provides:       perl(Mail::SPF::EMacroExpansionCtxRequired)
Provides:       perl(Mail::SPF::ENoAcceptableRecord)
Provides:       perl(Mail::SPF::ENoUnparsedText)
Provides:       perl(Mail::SPF::ENothingToParse)
Provides:       perl(Mail::SPF::EOptionRequired)
Provides:       perl(Mail::SPF::EProcessingLimitExceeded)
Provides:       perl(Mail::SPF::EReadOnlyValue)
Provides:       perl(Mail::SPF::ERecordSelectionError)
Provides:       perl(Mail::SPF::ERedundantAcceptableRecords)
Provides:       perl(Mail::SPF::ESyntaxError)
Provides:       perl(Mail::SPF::ETermDomainSpecExpected)
Provides:       perl(Mail::SPF::ETermIPv4AddressExpected)
Provides:       perl(Mail::SPF::ETermIPv4PrefixLengthExpected)
Provides:       perl(Mail::SPF::ETermIPv6AddressExpected)
Provides:       perl(Mail::SPF::ETermIPv6PrefixLengthExpected)
Provides:       perl(Mail::SPF::EUnexpectedTermObject)
Provides:       perl(Mail::SPF::Exception)
Provides:       perl(Mail::SPF::GlobalMod)
Provides:       perl(Mail::SPF::MacroString)
Provides:       perl(Mail::SPF::Mech)
Provides:       perl(Mail::SPF::Mech::A)
Provides:       perl(Mail::SPF::Mech::All)
Provides:       perl(Mail::SPF::Mech::Exists)
Provides:       perl(Mail::SPF::Mech::IP4)
Provides:       perl(Mail::SPF::Mech::IP6)
Provides:       perl(Mail::SPF::Mech::Include)
Provides:       perl(Mail::SPF::Mech::MX)
Provides:       perl(Mail::SPF::Mech::PTR)
Provides:       perl(Mail::SPF::Mod)
Provides:       perl(Mail::SPF::Mod::Exp)
Provides:       perl(Mail::SPF::Mod::Redirect)
Provides:       perl(Mail::SPF::PositionalMod)
Provides:       perl(Mail::SPF::Record)
Provides:       perl(Mail::SPF::Request)
Provides:       perl(Mail::SPF::Result)
Provides:       perl(Mail::SPF::Result::Error)
Provides:       perl(Mail::SPF::Result::Fail)
Provides:       perl(Mail::SPF::Result::Neutral)
Provides:       perl(Mail::SPF::Result::NeutralByDefault)
Provides:       perl(Mail::SPF::Result::None)
Provides:       perl(Mail::SPF::Result::Pass)
Provides:       perl(Mail::SPF::Result::PermError)
Provides:       perl(Mail::SPF::Result::SoftFail)
Provides:       perl(Mail::SPF::Result::TempError)
Provides:       perl(Mail::SPF::SenderIPAddrMech)
Provides:       perl(Mail::SPF::Server)
Provides:       perl(Mail::SPF::Term)
Provides:       perl(Mail::SPF::UnknownMod)
Provides:       perl(Mail::SPF::Util)
Provides:       perl(Mail::SPF::v1::Record)
Provides:       perl(Mail::SPF::v2::Record)
%undefine       __perllib_provides
%{perl_requires}

%description
*Mail::SPF* is an object-oriented implementation of Sender Policy Framework
(SPF). See http://www.openspf.org for more information about SPF.

This class collection aims to fully conform to the SPF specification (RFC
4408) so as to serve both as a production quality SPF implementation and as
a reference for other developers of SPF implementations.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README TODO
%license LICENSE

%changelog
