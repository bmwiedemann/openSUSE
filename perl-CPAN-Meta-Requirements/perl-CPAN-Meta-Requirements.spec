#
# spec file for package perl-CPAN-Meta-Requirements
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


Name:           perl-CPAN-Meta-Requirements
Version:        2.140000
Release:        0
%define cpan_version 2.140
Provides:       perl(CPAN::Meta::Requirements) = 2.140000
%define cpan_name CPAN-Meta-Requirements
Summary:        Set of Version Requirements for a Cpan Dist
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/CPAN-Meta-Requirements/
Source0:        http://www.cpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.88
Requires:       perl(version) >= 0.88
%{perl_requires}

%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the _META.yml_ or _META.json_ files in CPAN
distributions, and as defined by CPAN::Meta::Spec; It can be built up by
adding more and more constraints, and it will reduce them to the simplest
representation.

Logically impossible constraints will be identified immediately by thrown
exceptions.

%prep
%setup -q -n %{cpan_name}-%{cpan_version}

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
%doc Changes CONTRIBUTING.mkdn LICENSE README

%changelog
