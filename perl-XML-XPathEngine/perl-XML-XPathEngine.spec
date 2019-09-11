#
# spec file for package perl-XML-XPathEngine
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-XML-XPathEngine
Version:        0.14
Release:        0
%define cpan_name XML-XPathEngine
Summary:        Re-usable XPath engine for DOM-like trees
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-XPathEngine/
Source:         http://www.cpan.org/authors/id/M/MI/MIROD/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(attribute)
#BuildRequires: perl(minidom::node)
#BuildRequires: perl(minitree)
#BuildRequires: perl(XML::XPathEngine)
#BuildRequires: perl(XML::XPathEngine::Boolean)
#BuildRequires: perl(XML::XPathEngine::Expr)
#BuildRequires: perl(XML::XPathEngine::Function)
#BuildRequires: perl(XML::XPathEngine::Literal)
#BuildRequires: perl(XML::XPathEngine::LocationPath)
#BuildRequires: perl(XML::XPathEngine::NodeSet)
#BuildRequires: perl(XML::XPathEngine::Number)
#BuildRequires: perl(XML::XPathEngine::Root)
#BuildRequires: perl(XML::XPathEngine::Step)
#BuildRequires: perl(XML::XPathEngine::Variable)
%{perl_requires}

%description
This module provides an XPath engine, that can be re-used by other
module/classes that implement trees.

In order to use the XPath engine, nodes in the user module need to mimick
DOM nodes. The degree of similitude between the user tree and a DOM
dictates how much of the XPath features can be used. A module implementing
all of the DOM should be able to use this module very easily (you might
need to add the cmp method on nodes in order to get ordered result sets).

This code is a more or less direct copy of the the XML::XPath manpage
module by Matt Sergeant. I only removed the XML processing part to remove
the dependency on XML::Parser, applied a couple of patches, renamed a whole
lot of methods to make Pod::Coverage happy, and changed the docs.

The article eXtending XML XPath,
http://www.xmltwig.com/article/extending_xml_xpath/ should give authors who
want to use this module enough background to do so.

Otherwise, my email is below ;--)

*WARNING*: while the underlying code is rather solid, this module mostly
lacks docs. As they say, "patches welcome"...

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
%doc Changes README

%changelog
