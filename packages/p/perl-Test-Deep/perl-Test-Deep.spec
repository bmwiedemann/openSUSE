#
# spec file for package perl-Test-Deep
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


%define cpan_name Test-Deep
Name:           perl-Test-Deep
Version:        1.205.0
Release:        0
# 1.205 -> normalize -> 1.205.0
%define cpan_version 1.205
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Extremely flexible deep comparison
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tester) >= 0.107
Requires:       perl(Test::More) >= 0.96
Provides:       perl(Over)
Provides:       perl(Test::Deep) = %{version}
Provides:       perl(Test::Deep::All) = %{version}
Provides:       perl(Test::Deep::Any) = %{version}
Provides:       perl(Test::Deep::Array) = %{version}
Provides:       perl(Test::Deep::ArrayEach) = %{version}
Provides:       perl(Test::Deep::ArrayElementsOnly) = %{version}
Provides:       perl(Test::Deep::ArrayLength) = %{version}
Provides:       perl(Test::Deep::ArrayLengthOnly) = %{version}
Provides:       perl(Test::Deep::Blessed) = %{version}
Provides:       perl(Test::Deep::Boolean) = %{version}
Provides:       perl(Test::Deep::Cache) = %{version}
Provides:       perl(Test::Deep::Cache::Simple) = %{version}
Provides:       perl(Test::Deep::Class) = %{version}
Provides:       perl(Test::Deep::Cmp) = %{version}
Provides:       perl(Test::Deep::Code) = %{version}
Provides:       perl(Test::Deep::Hash) = %{version}
Provides:       perl(Test::Deep::HashEach) = %{version}
Provides:       perl(Test::Deep::HashElements) = %{version}
Provides:       perl(Test::Deep::HashKeys) = %{version}
Provides:       perl(Test::Deep::HashKeysOnly) = %{version}
Provides:       perl(Test::Deep::Ignore) = %{version}
Provides:       perl(Test::Deep::Isa) = %{version}
Provides:       perl(Test::Deep::ListMethods) = %{version}
Provides:       perl(Test::Deep::MM) = %{version}
Provides:       perl(Test::Deep::Methods) = %{version}
Provides:       perl(Test::Deep::NoTest) = %{version}
Provides:       perl(Test::Deep::None) = %{version}
Provides:       perl(Test::Deep::Number) = %{version}
Provides:       perl(Test::Deep::Obj) = %{version}
Provides:       perl(Test::Deep::Ref) = %{version}
Provides:       perl(Test::Deep::RefType) = %{version}
Provides:       perl(Test::Deep::Regexp) = %{version}
Provides:       perl(Test::Deep::RegexpMatches) = %{version}
Provides:       perl(Test::Deep::RegexpOnly) = %{version}
Provides:       perl(Test::Deep::RegexpRef) = %{version}
Provides:       perl(Test::Deep::RegexpRefOnly) = %{version}
Provides:       perl(Test::Deep::RegexpVersion) = %{version}
Provides:       perl(Test::Deep::ScalarRef) = %{version}
Provides:       perl(Test::Deep::ScalarRefOnly) = %{version}
Provides:       perl(Test::Deep::Set) = %{version}
Provides:       perl(Test::Deep::Shallow) = %{version}
Provides:       perl(Test::Deep::Stack) = %{version}
Provides:       perl(Test::Deep::String) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
# necessary because Test::Deep::NoTest does "require Test::Builder"
Requires:       perl(Test::Simple)
# MANUAL END

%description
If you don't know anything about automated testing in Perl then you should
probably read about Test::Simple and Test::More before preceding.
Test::Deep uses the Test::Builder framework.

Test::Deep gives you very flexible ways to check that the result you got is
the result you were expecting. At its simplest it compares two structures
by going through each level, ensuring that the values match, that arrays
and hashes have the same elements and that references are blessed into the
correct class. It also handles circular data structures without getting
caught in an infinite loop.

Where it becomes more interesting is in allowing you to do something
besides simple exact comparisons. With strings, the 'eq' operator checks
that 2 strings are exactly equal but sometimes that's not what you want.
When you don't know exactly what the string should be but you do know some
things about how it should look, 'eq' is no good and you must use pattern
matching instead. Test::Deep provides pattern matching for complex data
structures

Test::Deep has *_a lot_* of exports. See EXPORTS below.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README TODO
%license LICENSE

%changelog
