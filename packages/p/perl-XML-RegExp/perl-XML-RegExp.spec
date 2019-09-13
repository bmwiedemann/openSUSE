#
# spec file for package perl-XML-RegExp
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-XML-RegExp
Version:        0.04
Release:        0
%define cpan_name XML-RegExp
Summary:        Regular expressions for XML tokens
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-RegExp/
Source:         http://www.cpan.org/authors/id/T/TJ/TJMATHER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(XML::RegExp)
%{perl_requires}

%description
This package contains regular expressions for the following XML tokens:
BaseChar, Ideographic, Letter, Digit, Extender, CombiningChar, NameChar,
EntityRef, CharRef, Reference, Name, NmToken, and AttValue.

The definitions of these tokens were taken from the XML spec (Extensible
Markup Language 1.0) at the http://www.w3.org/TR/REC-xml manpage.

Also contains the regular expressions for the following tokens from the XML
Namespaces spec at the http://www.w3.org/TR/REC-xml-names manpage:
NCNameChar, NCName, QName, Prefix and LocalPart.

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
