#
# spec file for package perl-Mail-Transport
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


%define cpan_name Mail-Transport
Name:           perl-Mail-Transport
Version:        4.10.0
Release:        0
# 4.01 -> normalize -> 4.10.0
%define cpan_version 4.01
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Email message exchange
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Log::Report) >= 1.420
BuildRequires:  perl(Mail::Reporter) >= 4.0
BuildRequires:  perl(String::Print) >= 1.10
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Pod) >= 1
Requires:       perl(Log::Report) >= 1.420
Requires:       perl(Mail::Reporter) >= 4.0
Requires:       perl(String::Print) >= 1.10
Provides:       perl(Mail::Transport) = %{version}
Provides:       perl(Mail::Transport::Exim) = %{version}
Provides:       perl(Mail::Transport::Mailx) = %{version}
Provides:       perl(Mail::Transport::Qmail) = %{version}
Provides:       perl(Mail::Transport::Receive) = %{version}
Provides:       perl(Mail::Transport::SMTP) = %{version}
Provides:       perl(Mail::Transport::Send) = %{version}
Provides:       perl(Mail::Transport::Sendmail) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Objects which extend 'Mail::Transport' implement sending and/or receiving
of messages, using various protocols.

*Be aware:* This module versions 4.00 and up is not fully compatible with
older releases: mainly the exception handling has changed. When you need to
upgrade, please read _https://github.com/markov2/perl5-Mail-Box/wiki/_
*Version 3 is still maintained* and may see new releases as well.

Mail::Transport::Send extends this class, and offers general functionality
for send protocols, like SMTP. Mail::Transport::Receive also extends this
class, and offers receive method. Some transport protocols will implement
both sending and receiving.

Extends "DESCRIPTION" in Mail::Reporter.

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
%doc ChangeLog README.md

%changelog
