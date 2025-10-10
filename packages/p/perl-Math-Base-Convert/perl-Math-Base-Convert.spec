#
# spec file for package perl-Math-Base-Convert
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name Math-Base-Convert
Name:           perl-Math-Base-Convert
Version:        0.130.0
Release:        0
# 0.13 -> normalize -> 0.130.0
%define cpan_version 0.13
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Very fast base to base conversion
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIKER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
Patch0:         reproducible.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Math::Base::Convert) = %{version}
Provides:       perl(Math::Base::Convert::Bases) = 0.30.0
Provides:       perl(Math::Base::Convert::Bitmaps) = 0.20.0
Provides:       perl(Math::Base::Convert::CalcPP) = 0.30.0
Provides:       perl(Math::Base::Convert::Shortcuts) = 0.50.0
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides fast functions and methods to convert between
arbitrary number bases from 2 (binary) thru 65535.

This module is pure Perl, has no external dependencies, and is backward
compatible with old versions of Perl 5.

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
%doc bitmaps Changes README recurse2txt

%changelog
