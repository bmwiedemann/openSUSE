#
# spec file for package perl-Data-Validate-Domain
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


%define cpan_name Data-Validate-Domain
Name:           perl-Data-Validate-Domain
Version:        0.150.0
Release:        0
# 0.15 -> normalize -> 0.150.0
%define cpan_version 0.15
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Domain and host name validation
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Net::Domain::TLD) >= 1.740
BuildRequires:  perl(Test2::Plugin::UTF8)
BuildRequires:  perl(Test::More) >= 1.302015
Requires:       perl(Net::Domain::TLD) >= 1.740
Provides:       perl(Data::Validate::Domain) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module offers a few subroutines for validating domain and host names.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
