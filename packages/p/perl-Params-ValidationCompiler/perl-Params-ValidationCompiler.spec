#
# spec file for package perl-Params-ValidationCompiler
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Params-ValidationCompiler
Name:           perl-Params-ValidationCompiler
Version:        0.31
Release:        0
License:        Artistic-2.0
Summary:        Build an optimized subroutine parameter validator once, use it forever
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Exception::Class)
BuildRequires:  perl(List::Util) >= 1.29
BuildRequires:  perl(Specio) >= 0.14
BuildRequires:  perl(Test2::Plugin::NoWarnings)
BuildRequires:  perl(Test2::Require::Module)
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(Test::Without::Module)
Requires:       perl(Eval::Closure)
Requires:       perl(Exception::Class)
Requires:       perl(List::Util) >= 1.29
Recommends:     perl(Class::XSAccessor) >= 1.17
Recommends:     perl(Sub::Util) >= 1.40
%{perl_requires}

%description
This module creates a customized, highly efficient parameter checking
subroutine. It can handle named or positional parameters, and can return
the parameters as key/value pairs or a list of values.

In addition to type checks, it also supports parameter defaults, optional
parameters, and extra "slurpy" parameters.

%prep
%autosetup  -n %{cpan_name}-%{version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md test-matrix.als
%license LICENSE

%changelog
