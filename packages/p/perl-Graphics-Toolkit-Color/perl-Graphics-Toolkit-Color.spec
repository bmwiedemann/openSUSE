#
# spec file for package perl-Graphics-Toolkit-Color
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Graphics-Toolkit-Color
Name:           perl-Graphics-Toolkit-Color
Version:        2.220.0
Release:        0
# 2.22 -> normalize -> 2.220.0
%define cpan_version 2.22
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Calculate color (sets), IO many spaces and formats
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Builder) >= 1
BuildRequires:  perl(Test::More) >= 1.3
BuildRequires:  perl(Test::Warn) >= 0.300
Provides:       perl(Graphics::Toolkit::Color) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Calculator) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Error) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Name) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Name::Constant) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Name::Scheme) = %{version}
Provides:       perl(Graphics::Toolkit::Color::SetCalculator) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Basis) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Format) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Hub) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::AdobeRGB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::AppleRGB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIELAB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIELCHab) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIELCHuv) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIELUV) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIERGB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIEXYZ) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CMY) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CMYK) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::DCIP3) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::DCIP3Linear) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::DisplayP3) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::DisplayP3Linear) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HSB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HSL) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HSV) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HWB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::Helper::OK) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HunterLAB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::NCol) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::OKHSL) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::OKHSV) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::OKHWB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::OKLAB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::OKLCH) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::ProPhotoRGB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::RGB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::RGBLinear) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::Rec2020) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::Rec709) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::WideGamutRGB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::YIQ) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::YPbPr) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Shape) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Util) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Values) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Graphics::Toolkit::Color, for short *GTC*, is the top level API of this
library and the only package a regular user should be concerned with. Its
main purpose is the creation of related colors or sets of them, such as
gradients, complements and more. But if you want to convert, quantize,
round or reformat color definitions or translate from and to color names,
it can be helpful too.

This page will give you a quick overview of all GTC methods. The Manual
contains deeper explanations and describes every argument and topic of
interest in detail. Therefore each chapter here starts with a link to the
appropriate paragraph of a manual page.

While this module can understand and output color values of many (33) color
spaces, RGB is the internal and primary one for input and output, because
GTC is about colors that can be shown on the screen, and these are usually
encoded in _RGB_ (nonlinear standard RGB). However, many color calculations
are operating by default in _OKLAB_ or _OKHSL_ to give perceptually uniform
results.

Each GTC object represents one color and is read-only. It has no runtime
dependencies. Only Test::Simple and Test::Warn are needed for testing. The
behavior of error messages can be chosen, but defaults to using Carp.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
