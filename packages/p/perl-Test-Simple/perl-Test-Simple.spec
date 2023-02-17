#
# spec file for package perl-Test-Simple
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


%define cpan_name Test-Simple
Name:           perl-Test-Simple
Version:        1.302192
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Basic utilities for writing tests
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
Obsoletes:      perl-Test-Tester <= 0.109
Obsoletes:      perl-Test-use-ok <= 0.11
# MANUAL END

%description
** If you are unfamiliar with testing *read Test::Tutorial first!* **

This is an extremely simple, extremely basic module for writing tests
suitable for CPAN modules and other pursuits. If you wish to do more
complicated testing, use the Test::More module (a drop-in replacement for
this one).

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
%doc appveyor.yml Changes examples README README.md
%license LICENSE

%changelog
