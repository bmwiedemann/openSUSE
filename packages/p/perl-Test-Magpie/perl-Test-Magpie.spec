#
# spec file for package perl-Test-Magpie
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Test-Magpie
Version:        0.11
Release:        0
%define cpan_name Test-Magpie
Summary:        Mocking framework with method stubs and behaviour verification
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/ST/STEVENL/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::PartialDump)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(Set::Object)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Moose)
BuildRequires:  perl(Throwable)
BuildRequires:  perl(UNIVERSAL::ref)
BuildRequires:  perl(aliased)
BuildRequires:  perl(experimental)
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(Devel::PartialDump)
Requires:       perl(Moose)
Requires:       perl(Moose::Meta::Class)
Requires:       perl(Moose::Role)
Requires:       perl(Moose::Util)
Requires:       perl(MooseX::Types)
Requires:       perl(MooseX::Types::Moose)
Requires:       perl(MooseX::Types::Structured)
Requires:       perl(Set::Object)
Requires:       perl(UNIVERSAL::ref)
Requires:       perl(aliased)
Requires:       perl(experimental)
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
Test::Magpie is a test double framework heavily inspired by the Mockito
framework for Java, and also the Python-Mockito project. In Mockito, you
"spy" on objects for their behaviour, rather than being upfront about what
should happen. I find this approach to be significantly more flexible and
easier to work with than mocking systems like EasyMock, so I created a Perl
implementation.

* Mock objects

Mock objects, represented by Test::Magpie::Mock objects, are objects that
pretend to be everything you could ever want them to be. A mock object can
have any method called on it, does every roles, and isa subclass of any
superclass. This allows you to easily throw a mock object around it will be
treated as though it was a real object.

* Method stubbing

Any method can be called on a mock object, and it will be logged as an
invocation. By default, method calls return 'undef' in scalar context or an
empty list in list context. Often, though, clients will be interested in
the result of calling a method with some arguments. So you may specify how
a method stub should respond when it is called.

* Verify interactions

After calling your concrete code (the code under test) you may want to
check that the code did operate correctly on the mock. To do this, you can
use verifications to make sure code was called, with correct parameters and
the correct amount of times.

* Argument matching

Magpie gives you some helpful methods to validate arguments passed in to
calls. You can check equality between arguments, or consume a general type
of argument, or consume multiple arguments. See
Test::Magpie::ArgumentMatcher for the juicy details.

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
%doc Changes README
%license LICENSE

%changelog
