#
# spec file for package perl-Test-Strict
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name Test-Strict
Name:           perl-Test-Strict
Version:        0.52
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Check syntax, presence of use strict; and test coverage
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-UPSTREAM test-perl-5.38.patch gh#manwar/Test-Strict#33 -- Don't simultaneously test -c and -v switches
Patch0:         test-perl-5.38.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::More) >= 1.00
%{perl_requires}

%description
The most basic test one can write is "does it compile ?". This module tests
if the code compiles and play nice with Test::Simple modules.

Another good practice this module can test is to "use strict;" in all perl
files.

By setting a minimum test coverage through 'all_cover_ok()', a code author
can ensure his code is tested above a preset level of _kwality_ throughout
the development cycle.

Along with Test::Pod, this module can provide the first tests to setup for
a module author.

This module should be able to run under the -T flag for perl >= 5.6. All
paths are untainted with the following pattern: 'qr|^([-+@\w./:\\]+)$|'
controlled by '$Test::Strict::UNTAINT_PATTERN'.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

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
%doc Changes README
%license LICENSE

%changelog
