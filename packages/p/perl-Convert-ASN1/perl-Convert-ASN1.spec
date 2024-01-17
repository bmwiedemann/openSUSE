#
# spec file for package perl-Convert-ASN1
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


%define cpan_name Convert-ASN1
Name:           perl-Convert-ASN1
Version:        0.340.0
Release:        0
%define cpan_version 0.34
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Convert between perl data structures and ASN.1 encoded packets
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMLEGGE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl-Convert-ASN1-0.31-test.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Math::BigInt) >= 1.997
BuildRequires:  perl(Test::More) >= 0.90
Provides:       perl(Convert::ASN1) = 0.340.0
Provides:       perl(Convert::ASN1::parser) = 0.340.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
Convert::ASN1 encodes and decodes ASN.1 data structures using BER/DER
rules.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p0

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
%doc ChangeLog examples mkparse OldChanges parser.y README.md
%license LICENSE

%changelog
