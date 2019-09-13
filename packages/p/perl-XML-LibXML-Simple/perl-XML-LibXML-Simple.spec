#
# spec file for package perl-XML-LibXML-Simple
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-XML-LibXML-Simple
Version:        0.99
Release:        0
%define cpan_name XML-LibXML-Simple
Summary:        XML::LibXML clone of XML::Simple::XMLin()
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-LibXML-Simple/
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::LibXML) >= 1.64
Requires:       perl(XML::LibXML) >= 1.64
%{perl_requires}

%description
This module is a blunt rewrite of XML::Simple (by Grant McLean) to use the
XML::LibXML parser for XML structures, where the original uses plain Perl
or SAX parsers.

*Be warned:* this module thinks to be smart. You may very well shoot
yourself in the foot with this DWIMmery. Read the whole manual page at
least once before you start using it. If your XML is described in a schema
or WSDL, then use XML::Compile for maintainable code.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc ChangeLog README

%changelog
