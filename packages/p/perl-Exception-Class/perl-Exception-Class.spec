#
# spec file for package perl-Exception-Class
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


Name:           perl-Exception-Class
Version:        1.44
Release:        0
%define cpan_name Exception-Class
Summary:        Module That Allows You to Declare Real Exception Classes in Perl
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Exception-Class/
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Data::Inheritable) >= 0.02
BuildRequires:  perl(Devel::StackTrace) >= 2.00
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Class::Data::Inheritable) >= 0.02
Requires:       perl(Devel::StackTrace) >= 2.00
%{perl_requires}

%description
*RECOMMENDATION 1*: If you are writing modern Perl code with Moose or Moo I
highly recommend using Throwable instead of this module.

*RECOMMENDATION 2*: Whether or not you use Throwable, you should use
Try::Tiny.

Exception::Class allows you to declare exception hierarchies in your
modules in a "Java-esque" manner.

It features a simple interface allowing programmers to 'declare' exception
classes at compile time. It also has a base exception class,
Exception::Class::Base, that can be easily extended.

It is designed to make structured exception handling simpler and better by
encouraging people to use hierarchies of exceptions in their applications,
as opposed to a single catch-all exception class.

This module does not implement any try/catch syntax. Please see the "OTHER
EXCEPTION MODULES (try/catch syntax)" section for more information on how
to get this syntax.

You will also want to look at the documentation for Exception::Class::Base,
which is the default base class for all exception objects created by this
module.

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
%doc appveyor.yml Changes CONTRIBUTING.md README.md
%license LICENSE

%changelog
