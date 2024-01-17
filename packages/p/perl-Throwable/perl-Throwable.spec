#
# spec file for package perl-Throwable
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Throwable
Name:           perl-Throwable
Version:        1.001
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Role for classes that can be thrown
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::StackTrace) >= 1.32
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Module::Runtime) >= 0.002
BuildRequires:  perl(Moo) >= 1.000001
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Devel::StackTrace) >= 1.32
Requires:       perl(Module::Runtime) >= 0.002
Requires:       perl(Moo) >= 1.000001
Requires:       perl(Moo::Role)
Requires:       perl(Sub::Quote)
%{perl_requires}

%description
Throwable is a role for classes that are meant to be thrown as exceptions
to standard program flow. It is very simple and does only two things: saves
any previous value for '$@' and calls 'die $self'.

Throwable is implemented with Moo, so you can stick to Moo or use Moose, as
you prefer.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes README
%license LICENSE

%changelog
