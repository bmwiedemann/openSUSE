#
# spec file for package perl-CPAN-Perl-Releases
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


%define cpan_name CPAN-Perl-Releases
Name:           perl-CPAN-Perl-Releases
Version:        5.20221120
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Mapping Perl releases on CPAN to the location of the tarballs
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
CPAN::Perl::Releases is a module that contains the mappings of all 'perl'
releases that have been uploaded to CPAN to the 'authors/id/' path that the
tarballs reside in.

This is static data, but newer versions of this module will be made
available as new releases of 'perl' are uploaded to CPAN.

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
