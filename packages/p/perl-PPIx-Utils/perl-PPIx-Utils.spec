#
# spec file for package perl-PPIx-Utils
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


%define cpan_name PPIx-Utils
Name:           perl-PPIx-Utils
Version:        0.4.0
Release:        0
# 0.004 -> normalize -> 0.4.0
%define cpan_version 0.004
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Utility functions for PPI
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Keywords) >= 1.90.0
BuildRequires:  perl(PPI) >= 1.250
BuildRequires:  perl(PPI::Dumper)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(B::Keywords) >= 1.90.0
Requires:       perl(PPI) >= 1.250
Provides:       perl(PPIx::Utils) = %{version}
Provides:       perl(PPIx::Utils::Classification) = %{version}
Provides:       perl(PPIx::Utils::Language) = %{version}
Provides:       perl(PPIx::Utils::Traversal) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
'PPIx::Utils' is a collection of utility functions for working with PPI
documents. The functions are organized into submodules, and may be imported
from the appropriate submodule or via this module.

These functions were originally from Perl::Critic::Utils and related
modules, and have been split off to this distribution for use outside of
Perl::Critic.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING.md README
%license LICENSE

%changelog
