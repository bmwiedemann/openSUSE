#
# spec file for package perl-Test-SharedFork
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


%define cpan_name Test-SharedFork
Name:           perl-Test-SharedFork
Version:        0.350.0
Release:        0
# 0.35 -> normalize -> 0.350.0
%define cpan_version 0.35
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Fork test
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
Requires:       perl(Test::More) >= 0.88
Provides:       perl(Test::SharedFork) = %{version}
Provides:       perl(Test::SharedFork::Array)
Provides:       perl(Test::SharedFork::Scalar)
Provides:       perl(Test::SharedFork::Store)
%undefine       __perllib_provides
%{perl_requires}

%description
Test::SharedFork is utility module for Test::Builder.

This module makes fork(2) safety in your test case.

This module merges test count with parent process & child process.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes README.md README.mkdn
%license LICENSE

%changelog
