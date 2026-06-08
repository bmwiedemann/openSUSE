#
# spec file for package perl-Test-Kwalitee
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Test-Kwalitee
Name:           perl-Test-Kwalitee
Version:        1.280.0
Release:        0
# 1.28 -> normalize -> 1.280.0
%define cpan_version 1.28
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Test the Kwalitee of a distribution before you release it
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Check) >= 0.11
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Module::CPANTS::Analyse) >= 0.920
BuildRequires:  perl(Test::Builder) >= 0.88
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Tester) >= 0.108
BuildRequires:  perl(Test::Warnings) >= 0.9
BuildRequires:  perl(parent)
BuildRequires:  perl(version)
Requires:       perl(Module::CPANTS::Analyse) >= 0.920
Requires:       perl(Test::Builder) >= 0.88
Requires:       perl(parent)
Provides:       perl(Test::Kwalitee) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Kwalitee is an automatically-measurable gauge of how good your software is.
That's very different from quality, which a computer really can't measure
in a general sense. (If you can, you've solved a hard problem in computer
science.)

In the world of the CPAN, the CPANTS project (CPAN Testing Service; also a
funny acronym on its own) measures Kwalitee with several metrics. If you
plan to release a distribution to the CPAN -- or even within your own
organization -- testing its Kwalitee before creating a release can help you
improve your quality as well.

'Test::Kwalitee' and a short test file will do this for you automatically.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
