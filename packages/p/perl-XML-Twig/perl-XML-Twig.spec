#
# spec file for package perl-XML-Twig
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


%define cpan_name XML-Twig
Name:           perl-XML-Twig
Version:        3.530.0
Release:        0
# 3.53 -> normalize -> 3.530.0
%define cpan_version 3.53
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        XML, The Perl Way
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIROD/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl-XML-Twig-CVE-2016-9180.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::Parser) >= 2.23
Requires:       perl(XML::Parser) >= 2.23
Provides:       perl(XML::Twig) = %{version}
Provides:       perl(XML::Twig::Elt)
Provides:       perl(XML::Twig::Entity)
Provides:       perl(XML::Twig::Entity_list)
Provides:       perl(XML::Twig::Notation)
Provides:       perl(XML::Twig::Notation_list)
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  expat
BuildRequires:  perl-HTML-Tidy
BuildRequires:  perl-IO-CaptureOutput
BuildRequires:  perl-Test-Exception
BuildRequires:  perl-Test-Pod
BuildRequires:  perl-Text-Iconv
BuildRequires:  perl-Text-Wrapper
BuildRequires:  perl-Tie-IxHash
BuildRequires:  perl-Unicode-Map8
BuildRequires:  perl-XML-Filter-BufferText
BuildRequires:  perl-XML-Handler-YAWriter
BuildRequires:  perl-XML-Parser
BuildRequires:  perl-XML-SAX-Writer
BuildRequires:  perl-XML-Simple
BuildRequires:  perl-XML-XPath
BuildRequires:  perl-XML-XPathEngine
Requires:       expat
Requires:       perl-XML-Parser
Requires:       perl(Encode)
# MANUAL END

%description
This module provides a way to process XML documents. It is build on top of
'XML::Parser'.

The module offers a tree interface to the document, while allowing you to
output the parts of it that have been completely processed.

It allows minimal resource (CPU and memory) usage by building the tree only
for the parts of the documents that need actual processing, through the use
of the 'twig_roots ' and 'twig_print_outside_roots ' options. The 'finish '
and 'finish_print ' methods also help to increase performances.

XML::Twig tries to make simple things easy so it tries its best to takes
care of a lot of the (usually) annoying (but sometimes necessary) features
that come with XML and XML::Parser.

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
%doc Changes check_optional_modules filter_for_5.005 README speedup Twig_pm.slow

%changelog
