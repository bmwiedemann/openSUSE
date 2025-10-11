#
# spec file for package perl-Probe-Perl
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Probe-Perl
Name:           perl-Probe-Perl
Version:        0.30.0
Release:        0
# 0.03 -> normalize -> 0.30.0
%define cpan_version 0.03
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Information about the currently running perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Probe::Perl) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides methods for obtaining information about the currently
running perl interpreter. It originally began life as code in the
'Module::Build' project, but has been externalized here for general use.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
