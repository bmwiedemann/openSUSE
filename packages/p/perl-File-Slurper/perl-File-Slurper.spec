#
# spec file for package perl-File-Slurper
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


%define cpan_name File-Slurper
Name:           perl-File-Slurper
Version:        0.14.0
Release:        0
# 0.014 -> normalize -> 0.14.0
%define cpan_version 0.014
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple, sane and efficient module to slurp a file
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Warnings)
Provides:       perl(File::Slurper) = %{version}
%undefine       __perllib_provides
Recommends:     perl(PerlIO::utf8_strict)
%{perl_requires}

%description
This module provides functions for fast and correct slurping and spewing.
All functions are optionally exported. All functions throw exceptions on
errors, write functions don't return any meaningful value.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
