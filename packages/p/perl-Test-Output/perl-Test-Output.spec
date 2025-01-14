#
# spec file for package perl-Test-Output
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


%define cpan_name Test-Output
Name:           perl-Test-Output
Version:        1.35.0
Release:        0
# 1.035 -> normalize -> 1.35.0
%define cpan_version 1.035
License:        Artistic-2.0
Summary:        Utilities to test STDOUT and STDERR messages
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRIANDFOY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.17
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(File::Temp) >= 0.17
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Tester) >= 0.107
Requires:       perl(Capture::Tiny) >= 0.17
Requires:       perl(File::Temp) >= 0.17
Provides:       perl(Test::Output) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Test::Output provides a simple interface for testing output sent to
'STDOUT' or 'STDERR'. A number of different utilities are included to try
and be as flexible as possible to the tester.

Likewise, Capture::Tiny provides a much more robust capture mechanism
without than the original Test::Output::Tie.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes SECURITY.md
%license LICENSE

%changelog
