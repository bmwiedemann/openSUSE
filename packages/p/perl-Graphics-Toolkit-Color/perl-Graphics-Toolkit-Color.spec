#
# spec file for package perl-Graphics-Toolkit-Color
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


%define cpan_name Graphics-Toolkit-Color
Name:           perl-Graphics-Toolkit-Color
Version:        1.972.0
Release:        0
# 1.972 -> normalize -> 1.972.0
%define cpan_version 1.972
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Calculate color (sets), IO many spaces and formats
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 1.3
Provides:       perl(Graphics::Toolkit::Color) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Name) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Name::Constant) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Name::Scheme) = %{version}
Provides:       perl(Graphics::Toolkit::Color::SetCalculator) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Basis) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Format) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Hub) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIELAB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIELCHab) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIELCHuv) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIELUV) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CIEXYZ) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CMY) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CMYK) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HSB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HSL) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HSV) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HWB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HunterLAB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::NCol) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::OKLAB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::OKLCH) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::RGB) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::YIQ) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::YUV) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Shape) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Space::Util) = %{version}
Provides:       perl(Graphics::Toolkit::Color::Values) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Graphics::Toolkit::Color, for short *GTC*, is the top level API of this
release and the only package a regular user should be concerned with. Its
main purpose is the creation of related colors or sets of them, such as
gradients, complements and others. But you can use it also to convert
and/or reformat color definitions.

GTC are read only, one color representing objects with no additional
dependencies. Create them in many different ways (see CONSTRUCTOR). Access
its values via methods from section GETTER. Measure differences with the
distance method. SINGLE-COLOR methods create one new object that is related
to the current one and COLOR-SETS methods will create a group of colors,
that are not only related to the current color but also have relations
between each other. Error messages will appear as return values instead of
the expected result.

While this module can understand and output color values to many color
spaces, RGB is the (internal) primal one, because GTC is about colors that
can be shown on the screen, and these are usually encoded in _RGB_. Humans
access colors on hardware level (eye) in _RGB_, on cognition level in _HSL_
(brain) and on cultural level (language) with names. Having easy access to
all of those plus some color math and many formats should enable you to get
the color palette you desire quickly.

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
