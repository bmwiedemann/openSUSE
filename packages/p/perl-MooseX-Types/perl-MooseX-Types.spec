#
# spec file for package perl-MooseX-Types
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


Name:           perl-MooseX-Types
Version:        0.50
Release:        0
%define cpan_name MooseX-Types
Summary:        Organise your Moose types in libraries
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Types/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp::Clan) >= 6.00
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 1.06
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Meta::TypeConstraint::Union)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(Scalar::Util) >= 1.19
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::ForMethods) >= 0.100052
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(namespace::autoclean) >= 0.16
Requires:       perl(Carp::Clan) >= 6.00
Requires:       perl(Module::Runtime)
Requires:       perl(Moose) >= 1.06
Requires:       perl(Moose::Exporter)
Requires:       perl(Moose::Meta::TypeConstraint::Union)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(Scalar::Util) >= 1.19
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::ForMethods) >= 0.100052
Requires:       perl(Sub::Install)
Requires:       perl(Sub::Name)
Requires:       perl(namespace::autoclean) >= 0.16
%{perl_requires}

%description
The type system provided by Moose effectively makes all of its builtin type
global, as are any types you declare with Moose. This means that every
module that declares a type named 'PositiveInt' is sharing the same type
object. This can be a problem when different parts of the code base want to
use the same name for different things.

This package lets you declare types using short names, but behind the
scenes it namespaces all your type declarations, effectively prevent name
clashes between packages.

This is done by creating a type library module like 'MyApp::Types' and then
importing types from that module into other modules.

As a side effect, the declaration mechanism allows you to write type names
as barewords (really function calls), which catches typos in names at
compile time rather than run time.

This module also provides some helper functions for using Moose types
outside of attribute declarations.

If you mix string-based names with types created by this module, it will
warn, with a few exceptions. If you are declaring a 'class_type()' or
'role_type()' within your type library, or if you use a fully qualified
name like '"MyApp::Foo"'.

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
