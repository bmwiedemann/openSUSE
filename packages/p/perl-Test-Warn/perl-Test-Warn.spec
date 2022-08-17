#
# spec file for package perl-Test-Warn
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


%define cpan_name Test-Warn
Name:           perl-Test-Warn
Version:        0.37
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension to test methods for warnings
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGJ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.22
BuildRequires:  perl(Sub::Uplevel) >= 0.12
Requires:       perl(Carp) >= 1.22
Requires:       perl(Sub::Uplevel) >= 0.12
%{perl_requires}

%description
A good style of Perl programming calls for a lot of diverse regression
tests.

This module provides a few convenience methods for testing warning
based-code.

If you are not already familiar with the Test::More manpage now would be
the time to go take a look.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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

%changelog
