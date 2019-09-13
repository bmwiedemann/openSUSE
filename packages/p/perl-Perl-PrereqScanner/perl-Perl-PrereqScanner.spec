#
# spec file for package perl-Perl-PrereqScanner
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


Name:           perl-Perl-PrereqScanner
Version:        1.023
Release:        0
%define cpan_name Perl-PrereqScanner
Summary:        a tool to scan your Perl code for its prerequisites
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Perl-PrereqScanner/
Source:         http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.124
BuildRequires:  perl(Getopt::Long::Descriptive)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Path)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(PPI) >= 1.215
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(String::RewritePrefix) >= 0.005
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(CPAN::Meta::Requirements) >= 2.124
Requires:       perl(Getopt::Long::Descriptive)
Requires:       perl(List::MoreUtils)
Requires:       perl(Module::Path)
Requires:       perl(Moose)
Requires:       perl(Moose::Role)
Requires:       perl(PPI) >= 1.215
Requires:       perl(Params::Util)
Requires:       perl(String::RewritePrefix) >= 0.005
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
The scanner will extract loosely your distribution prerequisites from your
files.

The extraction may not be perfect but tries to do its best. It will
currently find the following prereqs:

* *

  plain lines beginning with 'use' or 'require' in your perl modules and
  scripts, including minimum perl version

* *

  regular inheritance declared with the 'base' and 'parent' pragmata

* *

  the Moose manpage inheritance declared with the 'extends' keyword

* *

  the Moose manpage roles included with the 'with' keyword

* *

  OO namespace aliasing using the 'aliased' module

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
%doc Changes LICENSE README

%changelog
