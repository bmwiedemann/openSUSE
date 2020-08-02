#
# spec file for package perl-MooseX-Traits
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


Name:           perl-MooseX-Traits
Version:        0.13
Release:        0
%define cpan_name MooseX-Traits
Summary:        Automatically apply roles at object creation time
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Traits/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Module::Build::Tiny) >= 0.007
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(ok)
Requires:       perl(Class::Load)
Requires:       perl(Moose::Role)
Requires:       perl(Sub::Exporter)
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
Often you want to create components that can be added to a class
arbitrarily. This module makes it easy for the end user to use these
components. Instead of requiring the user to create a named class with the
desired roles applied, or apply roles to the instance one-by-one, he can
just create a new class from yours with 'with_traits', and then instantiate
that.

There is also 'new_with_traits', which exists for compatibility reasons. It
accepts a 'traits' parameter, creates a new class with those traits, and
then instantiates it.

   Class->new_with_traits( traits => [qw/Foo Bar/], foo => 42, bar => 1 )

returns exactly the same object as

   Class->with_traits(qw/Foo Bar/)->new( foo => 42, bar => 1 )

would. But you can also store the result of 'with_traits', and call other
methods:

   my $c = Class->with_traits(qw/Foo Bar/);
   $c->new( foo => 42 );
   $c->whatever( foo => 1234 );

And so on.

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
