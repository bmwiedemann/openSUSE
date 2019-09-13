#
# spec file for package perl-XML-DOM
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-XML-DOM
Version:        1.45
Release:        0
%define cpan_name XML-DOM
Summary:        Perl Module for Building Dom Level 1 Compliant Document Structures
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-DOM/
Source0:        http://www.cpan.org/authors/id/T/TJ/TJMATHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(XML::Parser) >= 2.30
BuildRequires:  perl(XML::Parser::PerlSAX) >= 0.07
BuildRequires:  perl(XML::RegExp)
Requires:       perl(LWP::UserAgent)
Requires:       perl(XML::Parser) >= 2.30
Requires:       perl(XML::Parser::PerlSAX) >= 0.07
Requires:       perl(XML::RegExp)
%{perl_requires}

%description
This module extends the XML::Parser module by Clark Cooper. The XML::Parser
module is built on top of XML::Parser::Expat, which is a lower level
interface to James Clark's expat library.

XML::DOM::Parser is derived from XML::Parser. It parses XML strings or
files and builds a data structure that conforms to the API of the Document
Object Model as described at http://www.w3.org/TR/REC-DOM-Level-1. See the
XML::Parser manpage for other available features of the XML::DOM::Parser
class. Note that the 'Style' property should not be used (it is set
internally.)

The XML::Parser _NoExpand_ option is more or less supported, in that it
will generate EntityReference objects whenever an entity reference is
encountered in character data. I'm not sure how useful this is. Any
comments are welcome.

As described in the synopsis, when you create an XML::DOM::Parser object,
the parse and parsefile methods create an _XML::DOM::Document_ object from
the specified input. This Document object can then be examined, modified
and written back out to a file or converted to a string.

When using XML::DOM with XML::Parser version 2.19 and up, setting the
XML::DOM::Parser option _KeepCDATA_ to 1 will store CDATASections in
CDATASection nodes, instead of converting them to Text nodes. Subsequent
CDATASection nodes will be merged into one. Let me know if this is a
problem.

When using XML::Parser 2.27 and above, you can suppress expansion of
parameter entity references (e.g. %pent;) in the DTD, by setting
_ParseParamEnt_ to 1 and _ExpandParamEnt_ to 0. See /_Hidden_Nodes_ for
details.

A Document has a tree structure consisting of _Node_ objects. A Node may
contain other nodes, depending on its type. A Document may have Element,
Text, Comment, and CDATASection nodes. Element nodes may have Attr,
Element, Text, Comment, and CDATASection nodes. The other nodes may not
have any child nodes.

This module adds several node types that are not part of the DOM spec
(yet.) These are: ElementDecl (for <!ELEMENT ...> declarations),
AttlistDecl (for <!ATTLIST ...> declarations), XMLDecl (for <?xml ...?>
declarations) and AttDef (for attribute definitions in an AttlistDecl.)

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
%doc BUGS Changes FAQ.xml README samples XML-Parser-2.31.patch

%changelog
