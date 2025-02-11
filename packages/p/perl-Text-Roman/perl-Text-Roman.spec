#
# spec file for package perl-Text-Roman
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


%define cpan_name Text-Roman
Name:           perl-Text-Roman
Version:        3.500.0
Release:        0
# 3.5 -> normalize -> 3.500.0
%define cpan_version 3.5
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Allows conversion between Roman and Arabic algarisms
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SY/SYP/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Text::Roman) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This package supports both conventional Roman algarisms (which range from
_1_ to _3999_) and Milhar Romans, a variation which uses a bar across the
algarism to indicate multiplication by _1_000_. For the purposes of this
module, acceptable syntax consists of an underscore suffixed to the
algarism e.g. IV_V = _4_005_. The term Milhar apparently derives from the
Portuguese word for "thousands" and the range of this notation extends the
range of Roman numbers to _3999 * 1000 + 3999 = 4_002_999_.

Note: the functions in this package treat Roman algarisms in a
case-insensitive manner such that "VI" == "vI" == "Vi" == "vi".

The following functions may be imported into the caller package by name:

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
