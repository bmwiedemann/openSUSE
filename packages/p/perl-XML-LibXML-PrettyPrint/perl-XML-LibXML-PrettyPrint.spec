#
# spec file for package perl-XML-LibXML-PrettyPrint
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


Name:           perl-XML-LibXML-PrettyPrint
Version:        0.006
Release:        0
%define cpan_name XML-LibXML-PrettyPrint
Summary:        Add pleasant whitespace to a DOM tree
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-LibXML-PrettyPrint/
Source:         http://www.cpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(XML::LibXML) >= 1.62
Requires:       perl(Exporter::Tiny)
Requires:       perl(XML::LibXML) >= 1.62
Requires:       perl(XML::Simple)
%{perl_requires}

%description
Long XML files can be daunting for humans to read. Of course, XML is really
designed for computers to read - not people - but there are times when mere
mortals do need to read and edit XML by hand. For example, if your
application stores its configuration in XML, or you need to dump some XML
to STDOUT for debugging purposes.

Syntax highlighting helps, but to really make sense of some XML, proper
indentation can be vital. Hence 'XML::LibXML::PrettyPrint' - it can be
applied to an the XML::LibXML manpage DOM tree to reformat it into a more
readable result.

Pretty-printing XML is not as CPU-efficient as dumping it out sloppily, so
unless you're pretty sure that a human is going to need to make sense of
your XML, you should probably not use this module.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
# Fix env-script-interpreter badness
sed -i 's|/usr/bin/env perl|/usr/bin/perl|g' bin/xml-pretty
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
%doc Changes CONTRIBUTING COPYRIGHT CREDITS doap.ttl README
%license LICENSE

%changelog
