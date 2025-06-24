#
# spec file for package perl-CPAN-Meta-Check
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


%define cpan_name CPAN-Meta-Check
Name:           perl-CPAN-Meta-Check
Version:        0.18.0
Release:        0
# 0.018 -> normalize -> 0.18.0
%define cpan_version 0.018
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Verify requirements in a CPAN::Meta object
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta) >= 2.120920
BuildRequires:  perl(CPAN::Meta::Prereqs) >= 2.132830
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(Module::Metadata) >= 1.000023
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(CPAN::Meta::Prereqs) >= 2.132830
Requires:       perl(CPAN::Meta::Requirements) >= 2.121
Requires:       perl(Module::Metadata) >= 1.000023
Provides:       perl(CPAN::Meta::Check) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module verifies if requirements described in a CPAN::Meta object are
present.

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
