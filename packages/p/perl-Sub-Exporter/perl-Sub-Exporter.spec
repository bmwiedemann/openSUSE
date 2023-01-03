#
# spec file for package perl-Sub-Exporter
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


%define cpan_name Sub-Exporter
Name:           perl-Sub-Exporter
Version:        0.989
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Sophisticated exporter for custom-built routines
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::OptList) >= 0.100
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Params::Util) >= 0.14
BuildRequires:  perl(Sub::Install) >= 0.92
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Data::OptList) >= 0.100
Requires:       perl(Params::Util) >= 0.14
Requires:       perl(Sub::Install) >= 0.92
%{perl_requires}

%description
*ACHTUNG!* If you're not familiar with Exporter or exporting, read
Sub::Exporter::Tutorial first!

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
%doc Changes README
%license LICENSE

%changelog
