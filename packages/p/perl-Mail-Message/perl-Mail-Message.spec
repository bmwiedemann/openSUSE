#
# spec file for package perl-Mail-Message
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


%define cpan_name Mail-Message
Name:           perl-Mail-Message
Version:        3.15.0
Release:        0
%define cpan_version 3.015
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
Provides:       perl(Mail::Box::FastScalar) = %{version}
Provides:       perl(Mail::Box::Parser) = %{version}
Provides:       perl(Mail::Box::Parser::Perl) = %{version}
Provides:       perl(Mail::Message) = %{version}
Provides:       perl(Mail::Message::Body) = %{version}
Provides:       perl(Mail::Message::Body::File) = %{version}
Provides:       perl(Mail::Message::Body::Lines) = %{version}
Provides:       perl(Mail::Message::Body::Multipart) = %{version}
Provides:       perl(Mail::Message::Body::Nested) = %{version}
Provides:       perl(Mail::Message::Body::String) = %{version}
Provides:       perl(Mail::Message::Convert) = %{version}
Provides:       perl(Mail::Message::Convert::EmailSimple) = %{version}
Provides:       perl(Mail::Message::Convert::Html) = %{version}
Provides:       perl(Mail::Message::Convert::HtmlFormatPS) = %{version}
Provides:       perl(Mail::Message::Convert::HtmlFormatText) = %{version}
Provides:       perl(Mail::Message::Convert::MailInternet) = %{version}
Provides:       perl(Mail::Message::Convert::MimeEntity) = %{version}
Provides:       perl(Mail::Message::Convert::TextAutoformat) = %{version}
Provides:       perl(Mail::Message::Field) = %{version}
Provides:       perl(Mail::Message::Field::AddrGroup) = %{version}
Provides:       perl(Mail::Message::Field::Address) = %{version}
Provides:       perl(Mail::Message::Field::Addresses) = %{version}
Provides:       perl(Mail::Message::Field::Attribute) = %{version}
Provides:       perl(Mail::Message::Field::AuthResults) = %{version}
Provides:       perl(Mail::Message::Field::DKIM) = %{version}
Provides:       perl(Mail::Message::Field::Date) = %{version}
Provides:       perl(Mail::Message::Field::Fast) = %{version}
Provides:       perl(Mail::Message::Field::Flex) = %{version}
Provides:       perl(Mail::Message::Field::Full) = %{version}
Provides:       perl(Mail::Message::Field::Structured) = %{version}
Provides:       perl(Mail::Message::Field::URIs) = %{version}
Provides:       perl(Mail::Message::Field::Unstructured) = %{version}
Provides:       perl(Mail::Message::Head) = %{version}
Provides:       perl(Mail::Message::Head::Complete) = %{version}
Provides:       perl(Mail::Message::Head::FieldGroup) = %{version}
Provides:       perl(Mail::Message::Head::ListGroup) = %{version}
Provides:       perl(Mail::Message::Head::Partial) = %{version}
Provides:       perl(Mail::Message::Head::ResentGroup) = %{version}
Provides:       perl(Mail::Message::Head::SpamGroup) = %{version}
Provides:       perl(Mail::Message::Part) = %{version}
Provides:       perl(Mail::Message::Replace::MailHeader) = %{version}
Provides:       perl(Mail::Message::Replace::MailInternet) = %{version}
Provides:       perl(Mail::Message::Test) = %{version}
Provides:       perl(Mail::Message::TransferEnc) = %{version}
Provides:       perl(Mail::Message::TransferEnc::Base64) = %{version}
Provides:       perl(Mail::Message::TransferEnc::Binary) = %{version}
Provides:       perl(Mail::Message::TransferEnc::EightBit) = %{version}
Provides:       perl(Mail::Message::TransferEnc::QuotedPrint) = %{version}
Provides:       perl(Mail::Message::TransferEnc::SevenBit) = %{version}
Provides:       perl(Mail::Reporter) = %{version}
%undefine       __perllib_provides
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
