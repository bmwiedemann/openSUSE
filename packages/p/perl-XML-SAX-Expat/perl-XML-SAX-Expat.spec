#
# spec file for package perl-XML-SAX-Expat
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


Name:           perl-XML-SAX-Expat
Version:        0.51
Release:        0
%define cpan_name XML-SAX-Expat
Summary:        SAX2 Driver for Expat (XML::Parser)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-SAX-Expat/
Source0:        https://cpan.metacpan.org/authors/id/B/BJ/BJOERN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::NamespaceSupport) >= 0.03
BuildRequires:  perl(XML::Parser) >= 2.27
BuildRequires:  perl(XML::SAX) >= 0.03
BuildRequires:  perl(XML::SAX::Base) >= 1.00
Requires:       perl(XML::NamespaceSupport) >= 0.03
Requires:       perl(XML::Parser) >= 2.27
Requires:       perl(XML::SAX) >= 0.03
Requires:       perl(XML::SAX::Base) >= 1.00
%{perl_requires}

%description
This is an implementation of a SAX2 driver sitting on top of Expat
(XML::Parser) which Ken MacLeod posted to perl-xml and which I have
updated.

It is still incomplete, though most of the basic SAX2 events should be
available. The SAX2 spec is currently available from
http://perl-xml.sourceforge.net/perl-sax/.

A more friendly URL as well as a PODification of the spec are in the works.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%post
perl -MXML::SAX -e "XML::SAX->add_parser(q(XML::SAX::Expat))->save_parsers()"

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
