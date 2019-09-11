#
# spec file for package perl-namespace-autoclean
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-namespace-autoclean
Version:        0.29
Release:        0
%define cpan_name namespace-autoclean
Summary:        Keep imports out of your namespace
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:  perl(Sub::Identify)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(namespace::clean) >= 0.20
Requires:       perl(B::Hooks::EndOfScope) >= 0.12
Requires:       perl(Sub::Identify)
Requires:       perl(namespace::clean) >= 0.20
%{perl_requires}

%description
When you import a function into a Perl package, it will naturally also be
available as a method.

The 'namespace::autoclean' pragma will remove all imported symbols at the
end of the current package's compile cycle. Functions called in the package
itself will still be bound by their name, but they won't show up as methods
on your class or instances.

This module is very similar to namespace::clean, except it will clean all
imported functions, no matter if you imported them before or after you
'use'd the pragma. It will also not touch anything that looks like a
method.

If you're writing an exporter and you want to clean up after yourself (and
your peers), you can use the '-cleanee' switch to specify what package to
clean:

  package My::MooseX::namespace::autoclean;
  use strict;

  use namespace::autoclean (); # no cleanup, just load

  sub import {
      namespace::autoclean->import(
        -cleanee => scalar(caller),
      );
  }

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
