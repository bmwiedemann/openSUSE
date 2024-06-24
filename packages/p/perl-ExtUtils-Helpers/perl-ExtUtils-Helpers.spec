#
# spec file for package perl-ExtUtils-Helpers
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


%define cpan_name ExtUtils-Helpers
Name:           perl-ExtUtils-Helpers
Version:        0.27.0
Release:        0
# 0.027 -> normalize -> 0.27.0
%define cpan_version 0.027
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Various portability utilities for module builders
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(ExtUtils::Helpers) = %{version}
Provides:       perl(ExtUtils::Helpers::Unix) = %{version}
Provides:       perl(ExtUtils::Helpers::VMS) = %{version}
Provides:       perl(ExtUtils::Helpers::Windows) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides various portable helper functions for module building
modules.

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
