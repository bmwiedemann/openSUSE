#
# spec file for package perl-XML-Simple
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name XML-Simple
Name:           perl-XML-Simple
Version:        2.250.0
Release:        0
# 2.25 -> normalize -> 2.250.0
%define cpan_version 2.25
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        An API for simple XML files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GR/GRANTM/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(XML::NamespaceSupport) >= 1.40
BuildRequires:  perl(XML::SAX) >= 0.150
BuildRequires:  perl(XML::SAX::Expat)
Requires:       perl(XML::NamespaceSupport) >= 1.40
Requires:       perl(XML::SAX) >= 0.150
Requires:       perl(XML::SAX::Expat)
Provides:       perl(XML::Simple) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The XML::Simple module provides a simple API layer on top of an underlying
XML parsing module (either XML::Parser or one of the SAX2 parser modules).
Two functions are exported: 'XMLin()' and 'XMLout()'. Note: you can
explicitly request the lower case versions of the function names:
'xml_in()' and 'xml_out()'.

The simplest approach is to call these two functions directly, but an
optional object oriented interface (see "OPTIONAL OO INTERFACE" below)
allows them to be called as methods of an *XML::Simple* object. The object
interface can also be used at either end of a SAX pipeline.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README
%license LICENSE

%changelog
