#
# spec file for package perl-MooseX-Method-Signatures
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


Name:           perl-MooseX-Method-Signatures
Version:        0.49
Release:        0
%define cpan_name MooseX-Method-Signatures
Summary:        (DEPRECATED) Method declarations with type constraints and no source filter
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Method-Signatures/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.10
BuildRequires:  perl(Context::Preserve)
BuildRequires:  perl(Devel::Declare) >= 0.005011
BuildRequires:  perl(Devel::Declare::Context::Simple)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Runtime) >= 0.012
BuildRequires:  perl(Moose) >= 0.89
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Meta::Method)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::LazyRequire) >= 0.06
BuildRequires:  perl(MooseX::Meta::TypeConstraint::ForceCoercion)
BuildRequires:  perl(MooseX::Types) >= 0.35
BuildRequires:  perl(MooseX::Types::Moose) >= 0.19
BuildRequires:  perl(MooseX::Types::Structured) >= 0.24
BuildRequires:  perl(MooseX::Types::Util)
BuildRequires:  perl(Parse::Method::Signatures) >= 1.003014
BuildRequires:  perl(Parse::Method::Signatures::Param::Named)
BuildRequires:  perl(Parse::Method::Signatures::Param::Placeholder)
BuildRequires:  perl(Parse::Method::Signatures::TypeConstraint)
BuildRequires:  perl(Parse::Method::Signatures::Types)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(aliased)
BuildRequires:  perl(metaclass)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean) >= 0.19
Requires:       perl(B::Hooks::EndOfScope) >= 0.10
Requires:       perl(Context::Preserve)
Requires:       perl(Devel::Declare) >= 0.005011
Requires:       perl(Devel::Declare::Context::Simple)
Requires:       perl(Eval::Closure)
Requires:       perl(Module::Runtime) >= 0.012
Requires:       perl(Moose) >= 0.89
Requires:       perl(Moose::Meta::Class)
Requires:       perl(Moose::Meta::Method)
Requires:       perl(Moose::Util)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::LazyRequire) >= 0.06
Requires:       perl(MooseX::Meta::TypeConstraint::ForceCoercion)
Requires:       perl(MooseX::Types) >= 0.35
Requires:       perl(MooseX::Types::Moose) >= 0.19
Requires:       perl(MooseX::Types::Structured) >= 0.24
Requires:       perl(MooseX::Types::Util)
Requires:       perl(Parse::Method::Signatures) >= 1.003014
Requires:       perl(Parse::Method::Signatures::Param::Named)
Requires:       perl(Parse::Method::Signatures::Param::Placeholder)
Requires:       perl(Parse::Method::Signatures::TypeConstraint)
Requires:       perl(Parse::Method::Signatures::Types)
Requires:       perl(Sub::Name)
Requires:       perl(Task::Weaken)
Requires:       perl(aliased)
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
Provides a proper method keyword, like "sub" but specifically for making
methods and validating their arguments against Moose type constraints.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENCE README

%changelog
