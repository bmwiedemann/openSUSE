#
# spec file for package perl-MailTools
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


%define cpan_name MailTools
Name:           perl-MailTools
Version:        2.220.0
Release:        0
# 2.22 -> normalize -> 2.220.0
%define cpan_version 2.22
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Various ancient e-mail related modules
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(Date::Parse)
Requires:       perl(Date::Format)
Requires:       perl(Date::Parse)
Provides:       perl(Mail::Address) = %{version}
Provides:       perl(Mail::Cap) = %{version}
Provides:       perl(Mail::Field) = %{version}
Provides:       perl(Mail::Field::AddrList) = %{version}
Provides:       perl(Mail::Field::Date) = %{version}
Provides:       perl(Mail::Field::Generic) = %{version}
Provides:       perl(Mail::Filter) = %{version}
Provides:       perl(Mail::Header) = %{version}
Provides:       perl(Mail::Internet) = %{version}
Provides:       perl(Mail::Mailer) = %{version}
Provides:       perl(Mail::Mailer::qmail) = %{version}
Provides:       perl(Mail::Mailer::rfc822) = %{version}
Provides:       perl(Mail::Mailer::sendmail) = %{version}
Provides:       perl(Mail::Mailer::smtp) = %{version}
Provides:       perl(Mail::Mailer::smtp::pipe) = %{version}
Provides:       perl(Mail::Mailer::smtps) = %{version}
Provides:       perl(Mail::Mailer::smtps::pipe) = %{version}
Provides:       perl(Mail::Mailer::testfile) = %{version}
Provides:       perl(Mail::Mailer::testfile::pipe) = %{version}
Provides:       perl(Mail::Send) = %{version}
Provides:       perl(Mail::Util) = %{version}
Provides:       perl(MailTools) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
MailTools is a bundle: an ancient form of combining packages into one
distribution. Gladly, it can be distributed as if it is a normal
distribution as well.

*Be warned:* The code you find here is very old. It works for simple
emails, but when you start with new code then please use more sofisticated
libraries. The main reason that you still find this code on CPAN, is
because many books use it as example.

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
%doc ChangeLog examples MailTools.ppd README README.demos README.md

%changelog
