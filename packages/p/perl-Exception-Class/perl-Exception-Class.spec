#
# spec file for package perl-Exception-Class
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


%define cpan_name Exception-Class
Name:           perl-Exception-Class
Version:        1.450.0
Release:        0
# 1.45 -> normalize -> 1.450.0
%define cpan_version 1.45
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Module that allows you to declare real exception classes in Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Data::Inheritable) >= 0.20
BuildRequires:  perl(Devel::StackTrace) >= 2.0
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Class::Data::Inheritable) >= 0.20
Requires:       perl(Devel::StackTrace) >= 2.0
Provides:       perl(Exception::Class) = %{version}
Provides:       perl(Exception::Class::Base) = %{version}
%undefine       __perllib_provides
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
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
