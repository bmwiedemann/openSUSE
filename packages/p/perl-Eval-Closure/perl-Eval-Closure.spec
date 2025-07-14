#
# spec file for package perl-Eval-Closure
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Eval-Closure
Name:           perl-Eval-Closure
Version:        0.140.0
Release:        0
# 0.14 -> normalize -> 0.140.0
%define cpan_version 0.14
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Safely and cleanly create closures via string eval
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
Provides:       perl(Eval::Closure) = %{version}
%undefine       __perllib_provides
Recommends:     perl(Devel::LexAlias) >= 0.50
Recommends:     perl(Perl::Tidy)
%{perl_requires}

%description
String eval is often used for dynamic code generation. For instance,
'Moose' uses it heavily, to generate inlined versions of accessors and
constructors, which speeds code up at runtime by a significant amount.
String eval is not without its issues however - it's difficult to control
the scope it's used in (which determines which variables are in scope
inside the eval), and it's easy to miss compilation errors, since eval
catches them and sticks them in $@ instead.

This module attempts to solve these problems. It provides an 'eval_closure'
function, which evals a string in a clean environment, other than a fixed
list of specified variables. Compilation errors are rethrown automatically.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
