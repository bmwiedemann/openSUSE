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
Version:        1.08
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Color palette creation helper
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.35
BuildRequires:  perl(Test::More) >= 1.3
BuildRequires:  perl(Test::Warn) >= 0.30
Requires:       perl(Carp) >= 1.35
%{perl_requires}

%description
Read only color holding objects with no additional dependencies. Create
them in many different ways (see section _CONSTRUCTOR_). Access its values
via methods from section _GETTER_ or create related color objects via
methods listed under _METHODS_.

Humans access colors on hardware level (eye) in RGB, on cognition level in
HSL (brain) and on cultural level (language) with names. Having easy access
to all three and some color math should enable you to get the color palette
you desire quickly.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
