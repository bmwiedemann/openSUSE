#
# spec file for package perl-GD-Barcode
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


%define cpan_name GD-Barcode
Name:           perl-GD-Barcode
Version:        2.0.0
Release:        0
%define cpan_version 2.00
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Create barcode image with GD
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test2::V0) >= 0.000060
BuildRequires:  perl(parent)
Requires:       perl(parent)
Provides:       perl(GD::Barcode) = 2.0.0
Provides:       perl(GD::Barcode::COOP2of5) = 2.0.0
Provides:       perl(GD::Barcode::Code39) = 2.0.0
Provides:       perl(GD::Barcode::EAN13) = 2.0.0
Provides:       perl(GD::Barcode::EAN8) = 2.0.0
Provides:       perl(GD::Barcode::IATA2of5) = 2.0.0
Provides:       perl(GD::Barcode::ITF) = 2.0.0
Provides:       perl(GD::Barcode::Industrial2of5) = 2.0.0
Provides:       perl(GD::Barcode::Matrix2of5) = 2.0.0
Provides:       perl(GD::Barcode::NW7) = 2.0.0
Provides:       perl(GD::Barcode::QRcode) = 2.0.0
Provides:       perl(GD::Barcode::UPCA) = 2.0.0
Provides:       perl(GD::Barcode::UPCE) = 2.0.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
GD::Barcode is a subclass of GD and allows you to create barcode image with
GD. This module based on "Generate Barcode Ver 1.02 By Shisei Hanai
97/08/22".

From 1.14, you can use this module even if no GD (except plot method).

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
%doc Changes README

%changelog
