#
# spec file for package perl-Chart
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Chart
Name:           perl-Chart
Version:        2.403.8
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Series of charting modules
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LI/LICHTKIND/%{cpan_name}-v%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Carp) >= 1.35
BuildRequires:  perl(File::Temp) >= 0.19
BuildRequires:  perl(GD) >= 2
BuildRequires:  perl(Graphics::Toolkit::Color) >= 1
BuildRequires:  perl(Test::More) >= 1.3
BuildRequires:  perl(Test::Warn) >= 0.30
Requires:       perl(Carp) >= 1.35
Requires:       perl(GD) >= 2
Requires:       perl(Graphics::Toolkit::Color) >= 1
%{perl_requires}

%description
Chart helps you to create PNG and JPG images with visualizations of numeric
data. This page gives you a summary how to use it. For a more thorough
documentation and lots of example code please visit the Chart::Manual.

%prep
%autosetup  -n %{cpan_name}-v%{version}

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
%doc Changes CONTRIBUTING README TODO
%license LICENSE

%changelog
