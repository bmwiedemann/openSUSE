#
# spec file for package perl-Sub-Override
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Sub-Override
Name:           perl-Sub-Override
Version:        0.120.0
Release:        0
# 0.12 -> normalize -> 0.120.0
%define cpan_version 0.12
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for easily overriding subroutines
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MV/MVSJES/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Fatal) >= 0.010
Requires:       perl(Test::Fatal) >= 0.010
Provides:       perl(Sub::Override) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Perl extension for easily overriding subroutines

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
%doc Changes README README.md

%changelog
