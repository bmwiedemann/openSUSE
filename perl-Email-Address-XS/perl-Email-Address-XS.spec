#
# spec file for package perl-Email-Address-XS
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Email-Address-XS
Version:        1.04
Release:        0
%define cpan_name Email-Address-XS
Summary:        Parse and format RFC 5322 email addresses and groups
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Email-Address-XS/
Source0:        https://cpan.metacpan.org/authors/id/P/PA/PALI/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module implements at https://tools.ietf.org/html/rfc5322 parser and
formatter of email addresses and groups. It parses an input string from
email headers which contain a list of email addresses or a groups of email
addresses (like From, To, Cc, Bcc, Reply-To, Sender, ...). Also it can
generate a string value for those headers from a list of email addresses
objects. Module is backward compatible with at
https://tools.ietf.org/html/rfc2822 and at
https://tools.ietf.org/html/rfc822.

Parser and formatter functionality is implemented in XS and uses shared
code from Dovecot IMAP server.

It is a drop-in replacement for the Email::Address module which has several
security issues. E.g. issue at
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-7686, which allows
remote attackers to cause denial of service, is still present in
Email::Address version 1.908.

Email::Address::XS module was created to finally fix CVE-2015-7686.

Existing applications that use Email::Address module could be easily
switched to Email::Address::XS module. In most cases only changing 'use
Email::Address' to 'use Email::Address::XS' and replacing every
'Email::Address' occurrence with 'Email::Address::XS' is sufficient.

So unlike Email::Address, this module does not use regular expressions for
parsing but instead native XS implementation parses input string
sequentially according to RFC 5322 grammar.

Additionally it has support also for named groups and so can be use instead
of the Email::Address::List module.

If you are looking for the module which provides object representation for
the list of email addresses suitable for the MIME email headers, see
Email::MIME::Header::AddressList.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
