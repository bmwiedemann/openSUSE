#
# spec file for package perl-namespace-clean
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


%define cpan_name namespace-clean
Name:           perl-namespace-clean
Version:        0.270.0
Release:        0
# 0.27 -> normalize -> 0.270.0
%define cpan_version 0.27
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Keep imports and functions out of your namespace
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RI/RIBASUSHI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.120
BuildRequires:  perl(Package::Stash) >= 0.230
Requires:       perl(B::Hooks::EndOfScope) >= 0.120
Requires:       perl(Package::Stash) >= 0.230
Provides:       perl(namespace::clean) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Keep imports and functions out of your namespace

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
%doc Changes

%changelog
