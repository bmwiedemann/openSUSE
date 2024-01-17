#
# spec file for package perl-MooseX-Types-Stringlike
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-Types-Stringlike
Version:        0.003
Release:        0
%define cpan_name MooseX-Types-Stringlike
Summary:        Moose type constraints for strings or string-like objects
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Types-Stringlike/
Source:         http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(version)
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Moose)
%{perl_requires}

%description
This module provides a more general version of the 'Str' type. If coercions
are enabled, it will accepts objects that overload stringification and
coerces them into strings.

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
%doc Changes CONTRIBUTING cpanfile LICENSE perlcritic.rc README tidyall.ini

%changelog
