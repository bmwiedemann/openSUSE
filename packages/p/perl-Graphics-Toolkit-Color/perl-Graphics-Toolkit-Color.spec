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
Version:        1.530.0
Release:        0
%define cpan_version 1.53
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Color palette creation helper
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
Provides:       perl(Graphics::Toolkit::Color) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::Constant) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::Space) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::SpaceBasis) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::Util) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::Value) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::Value::CMY) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::Value::CMYK) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::Value::HSL) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::Value::HSV) = 1.530.0
Provides:       perl(Graphics::Toolkit::Color::Value::RGB) = 1.530.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
ATTENTION: deprecated methods of the old API will be removed on version
2.0.

Graphics::Toolkit::Color, for short GTC, is the top level API of this
module. It is designed to get a fast access to a set of related colors,
that serve your need. While it can understand and output many color
formats, its primary (internal) format is RGB, because this it is about
colors that can be shown on the screen.

Humans access colors on hardware level (eye) in RGB, on cognition level in
HSL (brain) and on cultural level (language) with names. Having easy access
to all three and some color math should enable you to get the color palette
you desire quickly.

GTC are read only color holding objects with no additional dependencies.
Create them in many different ways (see section _CONSTRUCTOR_). Access its
values via methods from section _GETTER_ or measure differences and create
related color objects via methods listed under _METHODS_.

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
