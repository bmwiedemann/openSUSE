#
# spec file for package perl-MooseX-Declare
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


Name:           perl-MooseX-Declare
Version:        0.43
Release:        0
%define cpan_name MooseX-Declare
Summary:        (DEPRECATED) Declarative syntax for Moose
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Declare/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::Declare) >= 0.005011
BuildRequires:  perl(Devel::Declare::Context::Simple)
BuildRequires:  perl(Module::Build::Tiny) >= 0.007
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.90
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Method::Signatures) >= 0.36
BuildRequires:  perl(MooseX::Method::Signatures::Meta::Method)
BuildRequires:  perl(MooseX::Method::Signatures::Types)
BuildRequires:  perl(MooseX::Role::Parameterized) >= 0.12
BuildRequires:  perl(MooseX::Types::Moose) >= 0.20
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(Parse::Method::Signatures)
BuildRequires:  perl(Parse::Method::Signatures::Param::Placeholder)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Test::More) >= 0.89
BuildRequires:  perl(aliased)
BuildRequires:  perl(namespace::autoclean) >= 0.16
BuildRequires:  perl(namespace::clean) >= 0.19
Requires:       perl(Devel::Declare) >= 0.005011
Requires:       perl(Devel::Declare::Context::Simple)
Requires:       perl(Module::Runtime)
Requires:       perl(Moose) >= 0.90
Requires:       perl(Moose::Meta::Class)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::Method::Signatures) >= 0.36
Requires:       perl(MooseX::Method::Signatures::Meta::Method)
Requires:       perl(MooseX::Method::Signatures::Types)
Requires:       perl(MooseX::Role::Parameterized) >= 0.12
Requires:       perl(MooseX::Types::Moose) >= 0.20
Requires:       perl(Parse::Method::Signatures)
Requires:       perl(Parse::Method::Signatures::Param::Placeholder)
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Install)
Requires:       perl(aliased)
Requires:       perl(namespace::autoclean) >= 0.16
Requires:       perl(namespace::clean) >= 0.19
%{perl_requires}

%description
This module provides syntactic sugar for Moose, the postmodern object
system for Perl 5. When used, it sets up the 'class' and 'role' keywords.

*Note:* Please see the the /WARNING manpage section below!

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
%doc Changes CONTRIBUTING LICENSE README

%changelog
