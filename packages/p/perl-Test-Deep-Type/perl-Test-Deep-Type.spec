#
# spec file for package perl-Test-Deep-Type
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


Name:           perl-Test-Deep-Type
Version:        0.008
Release:        0
%define cpan_name Test-Deep-Type
Summary:        Test::Deep plugin for validating type constraints
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Deep-Type/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Deep::Cmp)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Tester) >= 0.108
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(parent)
Requires:       perl(Test::Deep::Cmp)
Requires:       perl(Try::Tiny)
Requires:       perl(parent)
%{perl_requires}

%description
This is a Test::Deep plugin that provides the sub 'is_type' to indicate
that the data being tested must validate against the passed type. This is
an actual type _object_, not a string name -- for example something
provided via MooseX::Types, or a plain old coderef that returns a bool
(such as what might be used in a Moo type constraint).

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
%doc Changes CONTRIBUTING examples LICENCE README

%changelog
