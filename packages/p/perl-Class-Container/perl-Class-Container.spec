#
# spec file for package perl-Class-Container
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


Name:           perl-Class-Container
Version:        0.13
Release:        0
%define cpan_name Class-Container
Summary:        Glues object frameworks together transparently
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Class-Container/
Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.360100
BuildRequires:  perl(Params::Validate)
Requires:       perl(Params::Validate)
%{perl_requires}

%description
This class facilitates building frameworks of several classes that
inter-operate. It was first designed and built for 'HTML::Mason', in which
the Compiler, Lexer, Interpreter, Resolver, Component, Buffer, and several
other objects must create each other transparently, passing the appropriate
parameters to the right class, possibly substituting other subclasses for
any of these objects.

The main features of 'Class::Container' are:

  * Explicit declaration of containment relationships (aggregation, factory
creation, etc.)

  * Declaration of constructor parameters accepted by each member in a class
framework

  * Transparent passing of constructor parameters to the class that needs them

  * Ability to create one (automatic) or many (manual) contained objects
automatically and transparently

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
