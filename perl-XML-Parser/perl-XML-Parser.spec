#
# spec file for package perl-XML-Parser
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


%define cpan_name XML-Parser
Name:           perl-XML-Parser
Version:        2.44
Release:        0
Summary:        A perl module for parsing XML documents
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source:         https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         XML-Parser-2.40.diff
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
BuildRequires:  perl(LWP::UserAgent)
Requires:       perl(LWP::UserAgent)
# MANUAL BEGIN
BuildRequires:  libexpat-devel
# MANUAL END

%description
This module provides ways to parse XML documents. It is built on top of the
XML::Parser::Expat manpage, which is a lower level interface to James
Clark's expat library. Each call to one of the parsing methods creates a
new instance of XML::Parser::Expat which is then used to parse the
document. Expat options may be provided when the XML::Parser object is
created. These options are then passed on to the Expat object on each parse
call. They can also be given as extra arguments to the parse methods, in
which case they override options given at XML::Parser creation time.

The behavior of the parser is controlled either by 'the /STYLES manpage'
and/or 'the /HANDLERS manpage' options, or by the /setHandlers manpage
method. These all provide mechanisms for XML::Parser to set the handlers
needed by XML::Parser::Expat. If neither 'Style' nor 'Handlers' are
specified, then parsing just checks the document for being well-formed.

When underlying handlers get called, they receive as their first parameter
the _Expat_ object, not the Parser object.

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
chmod 644 samples/{canonical,xml*}
# MANUAL END

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README samples/

%changelog
