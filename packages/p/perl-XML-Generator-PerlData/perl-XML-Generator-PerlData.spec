#
# spec file for package perl-XML-Generator-PerlData
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


Name:           perl-XML-Generator-PerlData
Version:        0.95
Release:        0
%define cpan_name XML-Generator-PerlData
Summary:        Perl extension for generating SAX2 events from nested Perl data structures
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-Generator-PerlData/
Source0:        http://www.cpan.org/authors/id/K/KH/KHAMPTON/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::SAX::Base) >= 1.02
Requires:       perl(XML::SAX::Base) >= 1.02
%{perl_requires}

%description
XML::Generator::PerlData provides a simple way to generate SAX2 events from
nested Perl data structures, while providing finer-grained control over the
resulting document streams.

Processing comes in two flavors: *Simple Style* and *Stream Style*:

In a nutshell, 'simple style' is best used for those cases where you have a
a single Perl data structure that you want to convert to XML as quickly and
painlessly as possible. 'Stream style' is more useful for cases where you
are receiving chunks of data (like from a DBI handle) and you want to
process those chunks as they appear. See *PROCESSING METHODS* for more info
about how each style works.

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
%doc Changes TODO

%changelog
