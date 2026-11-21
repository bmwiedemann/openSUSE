#
# spec file for package perl-Test-Timer
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Test-Timer
Name:           perl-Test-Timer
Version:        2.120.0
Release:        0
# 2.12 -> normalize -> 2.120.0
%define cpan_version 2.12
License:        Artistic-2.0
Summary:        Test module to test/assert response times
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JONASBN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Error)
BuildRequires:  perl(Module::Build) >= 0.30
BuildRequires:  perl(Pod::Coverage::TrustPod)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Kwalitee) >= 1.21
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
BuildRequires:  perl(Test::Tester) >= 1.302111
Requires:       perl(Error)
Provides:       perl(Test::Timer) = %{version}
Provides:       perl(Test::Timer::TimeoutException) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Test::Timer implements a set of test primitives to test and assert test
times from bodies of code.

The key features are subroutines to assert or test the following:

* * that a given piece of code does not exceed a specified time limit

* * that a given piece of code takes longer than a specified time limit and
  does not exceed another

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGELOG.md cpanfile.snapshot dictionary.dic docs perl-test-timer.code-workspace README
%license LICENSE

%changelog
