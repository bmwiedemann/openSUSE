#
# spec file for package perl-Config-MVP
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Config-MVP
Version:        2.200011
Release:        0
%define cpan_name Config-MVP
Summary:        Multivalue-Property Package-Oriented Configuration
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Config-MVP/
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Load) >= 0.17
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
%doc Changes README
%license LICENSE

%changelog
