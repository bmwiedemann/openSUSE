#
# spec file for package perl-MooseX-OneArgNew
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


Name:           perl-MooseX-OneArgNew
Version:        0.005
Release:        0
%define cpan_name MooseX-OneArgNew
Summary:        Teach ->New to Accept Single, Non-Hashref Arguments
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-OneArgNew/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized) >= 1.01
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Moose::Util::TypeConstraints)
Requires:       perl(MooseX::Role::Parameterized) >= 1.01
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
MooseX::OneArgNew lets your constructor take a single argument, which will
be translated into the value for a one-entry hashref. It is a the
parameterized role|MooseX::Role::Parameterized manpage with three
parameters:

* type

  The Moose type that the single argument must be for the one-arg form to
  work. This should be an existing type, and may be either a string type or
  a MooseX::Type.

* init_arg

  This is the string that will be used as the key for the hashref
  constructed from the one-arg call to new.

* coerce

  If true, a single argument to new will be coerced into the expected type
  if possible. Keep in mind that if there are no coercions for the type,
  this will be an error, and that if a coercion from HashRef exists, you
  might be getting yourself into a weird situation.

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
%doc Changes LICENSE README

%changelog
