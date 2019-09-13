#
# spec file for package perl-Mail-IMAPClient
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Mail-IMAPClient
Version:        3.42
Release:        0
%define cpan_name Mail-IMAPClient
Summary:        An IMAP Client API
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLOBBES/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Parse::RecDescent) >= 1.94
Requires:       perl(Parse::RecDescent) >= 1.94
%{perl_requires}

%description
This module provides methods implementing the IMAP protocol to support
interacting with IMAP message stores.

The module is used by constructing or instantiating a new IMAPClient object
via the new constructor method. Once the object has been instantiated, the
connect method is either implicitly or explicitly called. At that point
methods are available that implement the IMAP client commands as specified
in *RFC3501*. When processing is complete, the logout object method should
be called.

This documentation is not meant to be a replacement for RFC3501 nor any
other IMAP related RFCs.

Note that this documentation uses the term _folder_ in place of RFC3501's
use of _mailbox_. This documentation reserves the use of the term _mailbox_
to refer to the set of folders owned by a specific IMAP id.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
for f in examples/*.pl
do
   sed -i 's|^#!/usr/local/bin/perl|%{__perl}|' ${f}
done
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples prepare_dist README test_template.txt

%changelog
