#
# spec file for package perl-Test-Unit-Lite
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Test-Unit-Lite
Version:        0.1202
Release:        0
%define cpan_name Test-Unit-Lite
Summary:        Unit testing without external dependencies
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Test-Unit-Lite/
Source:         http://www.cpan.org/authors/id/D/DE/DEXTER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
#BuildRequires: perl(Error)
#BuildRequires: perl(ExceptionChecker)
#BuildRequires: perl(File::Slurp)
#BuildRequires: perl(InheritedSuite::BaseTest)
#BuildRequires: perl(InheritedSuite::DerivedTest)
#BuildRequires: perl(InheritedSuite::OverrideNew)
#BuildRequires: perl(InheritedSuite::OverrideNewName)
#BuildRequires: perl(InheritedSuite::Simple)
#BuildRequires: perl(OneTestCaseTest)
#BuildRequires: perl(Readonly)
#BuildRequires: perl(Taint::Runtime)
#BuildRequires: perl(Test::CheckChanges)
#BuildRequires: perl(Test::CPAN::Changes)
#BuildRequires: perl(Test::CPAN::Meta)
#BuildRequires: perl(Test::DistManifest)
#BuildRequires: perl(Test::Distribution)
#BuildRequires: perl(Test::EOL)
#BuildRequires: perl(Test::Kwalitee)
#BuildRequires: perl(Test::NoTabs)
#BuildRequires: perl(TestObject)
#BuildRequires: perl(Test::Perl::Critic)
#BuildRequires: perl(Test::Pod) >= 1.14
#BuildRequires: perl(Test::Pod::Coverage) >= 1.04
#BuildRequires: perl(Test::Signature)
#BuildRequires: perl(Test::Spelling)
#BuildRequires: perl(Test::Unit::Lite)
#BuildRequires: perl(Test::Unit::TestCase)
#BuildRequires: perl(Test::Unit::TestRunner)
#BuildRequires: perl(Test::Unit::TestSuite)
%{perl_requires}

%description
This framework provides lighter version of the Test::Unit manpage
framework. It implements some of the the Test::Unit manpage classes and
methods needed to run test units. The the Test::Unit::Lite manpage tries to
be compatible with public API of the Test::Unit manpage. It doesn't
implement all classes and methods at 100% and only those necessary to run
tests are available.

The the Test::Unit::Lite manpage can be distributed as a part of package
distribution, so the package can be distributed without dependency on
modules outside standard Perl distribution. The the Test::Unit::Lite
manpage is provided as a single file.

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
%doc Changes examples LICENSE README README.md

%changelog
