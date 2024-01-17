#
# spec file for package perl-Graphics-Toolkit-Color
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


%define cpan_name Graphics-Toolkit-Color
Name:           perl-Graphics-Toolkit-Color
Version:        1.710.0
Release:        0
%define cpan_version 1.71
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Color palette constructor
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.35
BuildRequires:  perl(Test::More) >= 1.3
BuildRequires:  perl(Test::Warn) >= 0.30
Requires:       perl(Carp) >= 1.35
Provides:       perl(Graphics::Toolkit::Color) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Name) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Name::Constant) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Basis) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Hub) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CMY) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::CMYK) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HSB) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HSL) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HSV) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::HWB) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::LAB) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::RGB) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::XYZ) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Instance::YIQ) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Shape) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Space::Util) = 1.710.0
Provides:       perl(Graphics::Toolkit::Color::Values) = 1.710.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
ATTENTION: deprecated methods of the old API ( _string_, _rgb_, _red_,
_green_, _blue_, _rgb_hex_, _rgb_hash_, _hsl_, _hue_, _saturation_,
_lightness_, _hsl_hash_, _blend_with_, _gradient_to_, _rgb_gradient_to_,
_hsl_gradient_to_, _complementary_) will be removed on version 2.0.

Graphics::Toolkit::Color, for short GTC, is the top level API of this
module and the only one a regular user should be concerned with. Its main
purpose is the creation of sets of related colors, such as gradients,
complements and others.

GTC are read only color holding objects with no additional dependencies.
Create them in many different ways (see section CONSTRUCTOR). Access its
values via methods from section GETTER. Measure differences with the
_distance_ method. SINGLE-COLOR methods create one a object that is related
to the current one and COLOR-SETS methods will create a host of color that
are not only related to the current color but also have relations between
each other.

While this module can understand and output color values in many spaces,
such as YIQ, HSL and many more, RGB is the (internal) primal one, because
GTC is about colors that can be shown on the screen, and these are usually
encoded in RGB.

Humans access colors on hardware level (eye) in RGB, on cognition level in
HSL (brain) and on cultural level (language) with names. Having easy access
to all three and some color math should enable you to get the color palette
you desire quickly.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
