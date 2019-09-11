#
# spec file for package perl-Test-Identity
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


Name:           perl-Test-Identity
Version:        0.01
Release:        0
%define cpan_name Test-Identity
Summary:        Assert the Referential Identity of a Reference
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Identity/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.360000
%{perl_requires}

%description
This module provides a single testing function, 'identical'. It asserts
that a given reference is as expected; that is, it either refers to the
same object or is 'undef'. It is similar to 'Test::More::is' except that it
uses 'refaddr', ensuring that it behaves correctly even if the references
under test are objects that overload stringification or numification.

It also provides better diagnostics if the test fails:

 $ perl -MTest::More=tests,1 -MTest::Identity -e'identical [], {}'
 1..1
 not ok 1
 #   Failed test at -e line 1.
 # Expected an anonymous HASH ref, got an anonymous ARRAY ref
 # Looks like you failed 1 test of 1.

 $ perl -MTest::More=tests,1 -MTest::Identity -e'identical [], []'
 1..1
 not ok 1
 #   Failed test at -e line 1.
 # Expected an anonymous ARRAY ref to the correct object
 # Looks like you failed 1 test of 1.

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
%doc Changes LICENSE README

%changelog
