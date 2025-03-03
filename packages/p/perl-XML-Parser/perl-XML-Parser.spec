#
# spec file for package perl-XML-Parser
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name XML-Parser
Name:           perl-XML-Parser
Version:        2.470.0
Release:        0
# 2.47 -> normalize -> 2.470.0
%define cpan_version 2.47
#Upstream: Artistic-1.0 or GPL-1.0-or-later
License:        Artistic-2.0
Summary:        Perl module for parsing XML documents
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         XML-Parser-2.40.diff
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(LWP::UserAgent)
Requires:       perl(LWP::UserAgent)
Provides:       perl(XML::Parser) = %{version}
Provides:       perl(XML::Parser::Expat) = %{version}
Provides:       perl(XML::Parser::Style::Debug)
Provides:       perl(XML::Parser::Style::Objects)
Provides:       perl(XML::Parser::Style::Stream)
Provides:       perl(XML::Parser::Style::Subs)
Provides:       perl(XML::Parser::Style::Tree)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  libexpat-devel
# MANUAL END

%description
This module provides ways to parse XML documents. It is built on top of
XML::Parser::Expat, which is a lower level interface to James Clark's expat
library. Each call to one of the parsing methods creates a new instance of
XML::Parser::Expat which is then used to parse the document. Expat options
may be provided when the XML::Parser object is created. These options are
then passed on to the Expat object on each parse call. They can also be
given as extra arguments to the parse methods, in which case they override
options given at XML::Parser creation time.

The behavior of the parser is controlled either by 'STYLES' and/or
'HANDLERS' options, or by setHandlers method. These all provide mechanisms
for XML::Parser to set the handlers needed by XML::Parser::Expat. If
neither 'Style' nor 'Handlers' are specified, then parsing just checks the
document for being well-formed.

When underlying handlers get called, they receive as their first parameter
the _Expat_ object, not the Parser object.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p0

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
chmod 644 samples/{canonical,xml*}
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README README.md samples
%license LICENSE

%changelog
