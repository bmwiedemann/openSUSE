#
# spec file for package perl-XML-LibXML
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name XML-LibXML
Name:           perl-XML-LibXML
Version:        2.0207
Release:        0
Summary:        Perl Binding for libxml2
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Alien::Base::Wrapper)
BuildRequires:  perl(Alien::Libxml2) >= 0.14
BuildRequires:  perl(XML::NamespaceSupport) >= 1.07
BuildRequires:  perl(XML::SAX) >= 0.11
BuildRequires:  perl(XML::SAX::Base)
BuildRequires:  perl(XML::SAX::DocumentLocator)
BuildRequires:  perl(XML::SAX::Exception)
BuildRequires:  perl(parent)
Requires:       perl(XML::NamespaceSupport) >= 1.07
Requires:       perl(XML::SAX) >= 0.11
Requires:       perl(XML::SAX::Base)
Requires:       perl(XML::SAX::DocumentLocator)
Requires:       perl(XML::SAX::Exception)
Requires:       perl(parent)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.0
Provides:       perl-XML-LibXML-Common = %{version}
Obsoletes:      perl-XML-LibXML-Common < %{version}
# MANUAL END

%description
This module is an interface to libxml2, providing XML and HTML parsers with
DOM, SAX and XMLReader interfaces, a large subset of DOM Layer 3 interface
and a XML::XPath-like interface to XPath API of libxml2. The module is
split into several packages which are not described in this section; unless
stated otherwise, you only need to 'use XML::LibXML;' in your programs.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes docs example HACKING.txt README TODO
%license LICENSE

%changelog
