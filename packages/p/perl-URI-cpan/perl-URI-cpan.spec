#
# spec file for package perl-URI-cpan
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


%define cpan_name URI-cpan
Name:           perl-URI-cpan
Version:        1.9.0
Release:        0
%define cpan_version 1.009
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        URLs that refer to things on the CPAN
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(URI)
BuildRequires:  perl(parent)
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(URI)
Requires:       perl(parent)
Provides:       perl(URI::cpan) = 1.9.0
Provides:       perl(URI::cpan::author) = 1.9.0
Provides:       perl(URI::cpan::dist) = 1.9.0
Provides:       perl(URI::cpan::distfile) = 1.9.0
Provides:       perl(URI::cpan::module) = 1.9.0
Provides:       perl(URI::cpan::package) = 1.9.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
URLs that refer to things on the CPAN

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
%license LICENSE

%changelog
