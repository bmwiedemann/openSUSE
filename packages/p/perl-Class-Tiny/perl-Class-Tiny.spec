#
# spec file for package perl-Class-Tiny
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Class-Tiny
Version:        1.008
Release:        0
%define cpan_name Class-Tiny
Summary:        Minimalist class construction
License:        Apache-2.0
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
%{perl_requires}

%description
This module offers a minimalist class construction kit in around 120 lines
of code. Here is a list of features:

  * defines attributes via import arguments

  * generates read-write accessors

  * supports lazy attribute defaults

  * supports custom accessors

  * superclass provides a standard 'new' constructor

  * 'new' takes a hash reference or list of key/value pairs

  * 'new' supports providing 'BUILDARGS' to customize constructor options

  * 'new' calls 'BUILD' for each class from parent to child

  * superclass provides a 'DESTROY' method

  * 'DESTROY' calls 'DEMOLISH' for each class from child to parent

Multiple-inheritance is possible, with superclass order determined via
mro::get_linear_isa.

It uses no non-core modules for any recent Perl. On Perls older than v5.10
it requires MRO::Compat. On Perls older than v5.14, it requires
Devel::GlobalDestruction.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING.mkdn README
%license LICENSE

%changelog
