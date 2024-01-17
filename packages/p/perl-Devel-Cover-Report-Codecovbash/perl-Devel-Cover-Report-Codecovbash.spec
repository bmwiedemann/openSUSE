#
# spec file for package perl-Devel-Cover-Report-Codecovbash
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Devel-Cover-Report-Codecovbash
Name:           perl-Devel-Cover-Report-Codecovbash
Version:        0.04
Release:        0
Summary:        Generate a JSON file to be uploaded with the codecov bash script
License:        MIT
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TINITA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(JSON::MaybeXS)
Requires:       perl(namespace::autoclean)
%{perl_requires}

%description
This is a coverage reporter for Codecov. It generates a JSON file that can
be uploaded with the bash script provided by codecov. See
https://docs.codecov.io/docs/about-the-codecov-bash-uploader for details.

The generated file will be named _codecov.json_ and will be in the
_cover_db_ directory by default.

Nearly all of the code in this distribution was simply copied from Pine
Mizune's at https://metacpan.org/release/Devel-Cover-Report-Codecov
distribution.

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
