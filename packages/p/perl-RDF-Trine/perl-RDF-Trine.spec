#
# spec file for package perl-RDF-Trine
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


Name:           perl-RDF-Trine
Version:        1.019
Release:        0
%define cpan_name RDF-Trine
Summary:        An RDF Framework for Perl
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/RDF-Trine/
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Algorithm::Combinatorics)
BuildRequires:  perl(Cache::LRU)
BuildRequires:  perl(DBD::SQLite) >= 1.14
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::Connector)
BuildRequires:  perl(Data::UUID)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Error)
BuildRequires:  perl(HTTP::Negotiate)
BuildRequires:  perl(IRI)
BuildRequires:  perl(JSON) >= 2
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(List::Util) >= 1.33
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Load::Conditional) >= 0.38
BuildRequires:  perl(Moose) >= 2
BuildRequires:  perl(MooseX::ArrayRef)
BuildRequires:  perl(Scalar::Util) >= 1.24
BuildRequires:  perl(Set::Scalar)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::JSON)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(URI) >= 1.52
BuildRequires:  perl(XML::CommonNS) >= 0.04
BuildRequires:  perl(XML::Namespace)
BuildRequires:  perl(XML::SAX) >= 0.96
Requires:       perl(Algorithm::Combinatorics)
Requires:       perl(Cache::LRU)
Requires:       perl(DBD::SQLite) >= 1.14
Requires:       perl(DBI)
Requires:       perl(DBIx::Connector)
Requires:       perl(Data::UUID)
Requires:       perl(Digest::SHA)
Requires:       perl(Error)
Requires:       perl(HTTP::Negotiate)
Requires:       perl(IRI)
Requires:       perl(JSON) >= 2
Requires:       perl(LWP::UserAgent)
Requires:       perl(List::Util) >= 1.33
Requires:       perl(Log::Log4perl)
Requires:       perl(Module::Load::Conditional) >= 0.38
Requires:       perl(Moose) >= 2
Requires:       perl(MooseX::ArrayRef)
Requires:       perl(Scalar::Util) >= 1.24
Requires:       perl(Set::Scalar)
Requires:       perl(Text::CSV_XS)
Requires:       perl(Text::Table)
Requires:       perl(URI) >= 1.52
Requires:       perl(XML::CommonNS) >= 0.04
Requires:       perl(XML::Namespace)
Requires:       perl(XML::SAX) >= 0.96
Recommends:     perl(XML::LibXML) >= 1.7
%{perl_requires}

%description
RDF::Trine provides an Resource Descriptive Framework (RDF) with an
emphasis on extensibility, API stability, and the presence of a test suite.
The package consists of several components:

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

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes.ttl examples README

%changelog
