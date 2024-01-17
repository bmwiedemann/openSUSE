#
# spec file for package perl-Config-MVP
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


%define cpan_name Config-MVP
Name:           perl-Config-MVP
Version:        2.200013
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Multivalue-property package-oriented configuration
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load) >= 0.17
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Module::Pluggable::Object)
BuildRequires:  perl(Moose) >= 0.91
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::OneArgNew)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Role::HasMessage)
BuildRequires:  perl(Role::Identifiable::HasIdent)
BuildRequires:  perl(StackTrace::Auto)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Throwable)
BuildRequires:  perl(Tie::IxHash)
BuildRequires:  perl(Try::Tiny)
Requires:       perl(Class::Load) >= 0.17
Requires:       perl(Module::Pluggable::Object)
Requires:       perl(Moose) >= 0.91
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::OneArgNew)
Requires:       perl(Params::Util)
Requires:       perl(Role::HasMessage)
Requires:       perl(Role::Identifiable::HasIdent)
Requires:       perl(StackTrace::Auto)
Requires:       perl(Test::More) >= 0.96
Requires:       perl(Throwable)
Requires:       perl(Tie::IxHash)
Requires:       perl(Try::Tiny)
%{perl_requires}

%description
MVP is a mechanism for loading configuration (or other information) for
libraries. It doesn't read a file or a database. It's a helper for things
that do.

The idea is that you end up with a Config::MVP::Sequence object, and that
you can use that object to fully configure your library or application. The
sequence will contain a bunch of Config::MVP::Section objects, each of
which is meant to provide configuration for a part of your program. Most of
these sections will be directly related to a Perl library that you'll use
as a plugin or helper. Each section will have a name, and every name in the
sequence will be unique.

This is a pretty abstract set of behaviors, so we'll provide some more
concrete examples that should help explain how things work.

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
