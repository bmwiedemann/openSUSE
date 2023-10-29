#
# spec file for package perl-Mail-Message
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


%define cpan_name Mail-Message
Name:           perl-Mail-Message
Version:        3.14.0
Release:        0
%define cpan_version 3.014
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Processing MIME messages
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Encode) >= 2.26
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(MIME::Types) >= 1.004
BuildRequires:  perl(Mail::Address) >= 2.17
BuildRequires:  perl(Time::Zone)
BuildRequires:  perl(URI) >= 1.23
BuildRequires:  perl(User::Identity) >= 1.02
Requires:       perl(Date::Format)
Requires:       perl(Date::Parse)
Requires:       perl(Encode) >= 2.26
Requires:       perl(IO::Scalar)
Requires:       perl(MIME::Types) >= 1.004
Requires:       perl(Mail::Address) >= 2.17
Requires:       perl(Time::Zone)
Requires:       perl(URI) >= 1.23
Requires:       perl(User::Identity) >= 1.02
Provides:       perl(Mail::Box::FastScalar) = 3.14.0
Provides:       perl(Mail::Box::Parser) = 3.14.0
Provides:       perl(Mail::Box::Parser::Perl) = 3.14.0
Provides:       perl(Mail::Message) = 3.14.0
Provides:       perl(Mail::Message::Body) = 3.14.0
Provides:       perl(Mail::Message::Body::File) = 3.14.0
Provides:       perl(Mail::Message::Body::Lines) = 3.14.0
Provides:       perl(Mail::Message::Body::Multipart) = 3.14.0
Provides:       perl(Mail::Message::Body::Nested) = 3.14.0
Provides:       perl(Mail::Message::Body::String) = 3.14.0
Provides:       perl(Mail::Message::Convert) = 3.14.0
Provides:       perl(Mail::Message::Convert::EmailSimple) = 3.14.0
Provides:       perl(Mail::Message::Convert::Html) = 3.14.0
Provides:       perl(Mail::Message::Convert::HtmlFormatPS) = 3.14.0
Provides:       perl(Mail::Message::Convert::HtmlFormatText) = 3.14.0
Provides:       perl(Mail::Message::Convert::MailInternet) = 3.14.0
Provides:       perl(Mail::Message::Convert::MimeEntity) = 3.14.0
Provides:       perl(Mail::Message::Convert::TextAutoformat) = 3.14.0
Provides:       perl(Mail::Message::Field) = 3.14.0
Provides:       perl(Mail::Message::Field::AddrGroup) = 3.14.0
Provides:       perl(Mail::Message::Field::Address) = 3.14.0
Provides:       perl(Mail::Message::Field::Addresses) = 3.14.0
Provides:       perl(Mail::Message::Field::Attribute) = 3.14.0
Provides:       perl(Mail::Message::Field::AuthResults) = 3.14.0
Provides:       perl(Mail::Message::Field::DKIM) = 3.14.0
Provides:       perl(Mail::Message::Field::Date) = 3.14.0
Provides:       perl(Mail::Message::Field::Fast) = 3.14.0
Provides:       perl(Mail::Message::Field::Flex) = 3.14.0
Provides:       perl(Mail::Message::Field::Full) = 3.14.0
Provides:       perl(Mail::Message::Field::Structured) = 3.14.0
Provides:       perl(Mail::Message::Field::URIs) = 3.14.0
Provides:       perl(Mail::Message::Field::Unstructured) = 3.14.0
Provides:       perl(Mail::Message::Head) = 3.14.0
Provides:       perl(Mail::Message::Head::Complete) = 3.14.0
Provides:       perl(Mail::Message::Head::FieldGroup) = 3.14.0
Provides:       perl(Mail::Message::Head::ListGroup) = 3.14.0
Provides:       perl(Mail::Message::Head::Partial) = 3.14.0
Provides:       perl(Mail::Message::Head::ResentGroup) = 3.14.0
Provides:       perl(Mail::Message::Head::SpamGroup) = 3.14.0
Provides:       perl(Mail::Message::Part) = 3.14.0
Provides:       perl(Mail::Message::Replace::MailHeader) = 3.14.0
Provides:       perl(Mail::Message::Replace::MailInternet) = 3.14.0
Provides:       perl(Mail::Message::Test) = 3.14.0
Provides:       perl(Mail::Message::TransferEnc) = 3.14.0
Provides:       perl(Mail::Message::TransferEnc::Base64) = 3.14.0
Provides:       perl(Mail::Message::TransferEnc::Binary) = 3.14.0
Provides:       perl(Mail::Message::TransferEnc::EightBit) = 3.14.0
Provides:       perl(Mail::Message::TransferEnc::QuotedPrint) = 3.14.0
Provides:       perl(Mail::Message::TransferEnc::SevenBit) = 3.14.0
Provides:       perl(Mail::Reporter) = 3.14.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
A 'Mail::Message' object is a container for MIME-encoded message
information, as defined by RFC2822. Everything what is not specificaly
related to storing the messages in mailboxes (folders) is implemented in
this class. Methods which are related to folders is implemented in the
Mail::Box::Message extension.

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
%doc ChangeLog README README.md

%changelog
