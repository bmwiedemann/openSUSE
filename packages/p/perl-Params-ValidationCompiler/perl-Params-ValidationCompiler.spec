#
# spec file for package perl-Params-ValidationCompiler
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


Name:           perl-Params-ValidationCompiler
Version:        0.30
Release:        0
%define cpan_name Params-ValidationCompiler
Summary:        Build an optimized subroutine parameter validator once, use it forever
License:        Artistic-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Params-ValidationCompiler/
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
Recommends:     perl(Class::XSAccessor)
Recommends:     perl(Sub::Util) >= 1.40
%{perl_requires}

%description
This module creates a customized, highly efficient parameter checking
subroutine. It can handle named or positional parameters, and can return
the parameters as key/value pairs or a list of values.

In addition to type checks, it also supports parameter defaults, optional
parameters, and extra "slurpy" parameters.

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
%doc appveyor.yml Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md test-matrix.als
%license LICENSE

%changelog
