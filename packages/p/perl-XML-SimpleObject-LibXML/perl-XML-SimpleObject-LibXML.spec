#
# spec file for package perl-XML-SimpleObject-LibXML
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-XML-SimpleObject-LibXML
Version:        0.60
Release:        1
License:        Artistic-1.0
%define cpan_name XML-SimpleObject-LibXML
Summary:        Perl extension allowing a simple(r) object representation of an XML::Lib[cut]
Url:            http://search.cpan.org/dist/XML-SimpleObject-LibXML/
Group:          Development/Libraries/Perl
Source:         http://www.cpan.org/authors/id/D/DB/DBRIAN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::LibXML)
Requires:       perl(XML::LibXML)
%{perl_requires}

%description
This is a short and simple class allowing simple object access to a parsed
XML::LibXML tree, with methods for fetching children and attributes in as
clean a manner as possible. My apologies for further polluting the XML::
space; this is a small and quick module, with easy and compact usage. Some
will rightfully question placing another interface over the DOM methods
provided by XML::LibXML, but my experience is that people appreciate the
total simplicity provided by this module, despite its limitations. These
limitations include a minor loss of speed compared to the DOM, loss of
control over node types, and protection (aka lack of knowledge) about the
DOM. I encourage those who want more control and understanding over the DOM
to study XML::LibXML; this module's source can be instructive, too.

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
