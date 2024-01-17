#
# spec file for package perl-Path-Router
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Path-Router
Version:        0.15
Release:        0
%define cpan_name Path-Router
Summary:        Tool for Routing Paths
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Path-Router/
Source0:        http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.32
BuildRequires:  perl(Clone::PP) >= 1.04
BuildRequires:  perl(Data::Dumper) >= 2.154
BuildRequires:  perl(Eval::Closure) >= 0.13
BuildRequires:  perl(File::Spec::Unix) >= 3.40
BuildRequires:  perl(Moo) >= 2.000001
BuildRequires:  perl(Sub::Exporter) >= 0.981
BuildRequires:  perl(Term::ReadLine) >= 1.11
BuildRequires:  perl(Test::Builder) >= 1.001013
BuildRequires:  perl(Test::Deep) >= 0.113
BuildRequires:  perl(Test::Fatal) >= 0.012
BuildRequires:  perl(Test::More) >= 1.001013
BuildRequires:  perl(Try::Tiny) >= 0.19
BuildRequires:  perl(Type::Tiny) >= 1.000005
BuildRequires:  perl(Types::Standard) >= 1.000005
BuildRequires:  perl(constant) >= 1.24
BuildRequires:  perl(namespace::clean) >= 0.23
Requires:       perl(Carp) >= 1.32
Requires:       perl(Clone::PP) >= 1.04
Requires:       perl(Data::Dumper) >= 2.154
Requires:       perl(Eval::Closure) >= 0.13
Requires:       perl(File::Spec::Unix) >= 3.40
Requires:       perl(Moo) >= 2.000001
Requires:       perl(Sub::Exporter) >= 0.981
Requires:       perl(Term::ReadLine) >= 1.11
Requires:       perl(Test::Builder) >= 1.001013
Requires:       perl(Test::Deep) >= 0.113
Requires:       perl(Try::Tiny) >= 0.19
Requires:       perl(Type::Tiny) >= 1.000005
Requires:       perl(Types::Standard) >= 1.000005
Requires:       perl(constant) >= 1.24
Requires:       perl(namespace::clean) >= 0.23
%{perl_requires}

%description
This module provides a way of deconstructing paths into parameters suitable
for dispatching on. It also provides the inverse in that it will take a
list of parameters, and construct an appropriate uri for it.

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
%doc Changes LICENSE README TODO

%changelog
