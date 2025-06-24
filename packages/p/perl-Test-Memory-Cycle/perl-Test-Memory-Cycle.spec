#
# spec file for package perl-Test-Memory-Cycle
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


%define cpan_name Test-Memory-Cycle
Name:           perl-Test-Memory-Cycle
Version:        1.60.0
Release:        0
# 1.06 -> normalize -> 1.60.0
%define cpan_version 1.06
#Upstream:  This program is free software; you can redistribute it and/or modify it under the terms of the Artistic License v2.0. See http://www.perlfoundation.org/artistic_license_2_0 or the LICENSE file that comes with the Test::Memory::Cycle distribution.
License:        Artistic-2.0
Summary:        Verifies code hasn't left circular references
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::Cycle) >= 1.70
BuildRequires:  perl(PadWalker)
Requires:       perl(Devel::Cycle) >= 1.70
Requires:       perl(PadWalker)
Provides:       perl(Test::Memory::Cycle) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Verifies code hasn't left circular references

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
%doc Changes README.md
%license LICENSE

%changelog
