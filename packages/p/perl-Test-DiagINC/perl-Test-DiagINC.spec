#
# spec file for package perl-Test-DiagINC
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Test-DiagINC
Name:           perl-Test-DiagINC
Version:        0.010
Release:        0
License:        Apache-2.0
Summary:        List modules and versions loaded if tests fail
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny) >= 0.21
%{perl_requires}

%description
Assuming you shipped your module to CPAN with working tests, test failures
from at http://www.cpantesters.org/ might be due to platform issues, Perl
version issues or problems with dependencies. This module helps you
diagnose deep dependency problems by showing you exactly what modules and
versions were loaded during a test run.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes CONTRIBUTING.mkdn examples README
%license LICENSE

%changelog
