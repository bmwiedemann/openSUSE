#
# spec file for package perl-MooseX-Types-Structured
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-MooseX-Types-Structured
Version:        0.36
Release:        0
#Upstream: Artistic-1.0 or GPL-1.0+
%define cpan_name MooseX-Types-Structured
Summary:        Structured Type Constraints for Moose
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Types-Structured/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Devel::PartialDump) >= 0.13
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::TypeCoercion)
BuildRequires:  perl(Moose::Meta::TypeConstraint)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Parameterizable)
BuildRequires:  perl(Moose::Util::TypeConstraints) >= 1.06
BuildRequires:  perl(MooseX::Types) >= 0.22
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Sub::Exporter) >= 0.982
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(namespace::clean) >= 0.19
Requires:       perl(Devel::PartialDump) >= 0.13
Requires:       perl(Moose)
Requires:       perl(Moose::Meta::TypeCoercion)
Requires:       perl(Moose::Meta::TypeConstraint)
Requires:       perl(Moose::Meta::TypeConstraint::Parameterizable)
Requires:       perl(Moose::Util::TypeConstraints) >= 1.06
Requires:       perl(MooseX::Types) >= 0.22
Requires:       perl(Sub::Exporter) >= 0.982
Requires:       perl(namespace::clean) >= 0.19
%{perl_requires}

%description
A structured type constraint is a standard container Moose type constraint,
such as an 'ArrayRef' or 'HashRef', which has been enhanced to allow you to
explicitly name all the allowed type constraints inside the structure. The
generalized form is:

    TypeConstraint[@TypeParameters or %TypeParameters]

Where 'TypeParameters' is an array reference or hash references of
Moose::Meta::TypeConstraint objects.

This type library enables structured type constraints. It is built on top
of the MooseX::Types library system, so you should review the documentation
for that if you are not familiar with it.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
