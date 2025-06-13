#
# spec file for package perl-Cache-LRU
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


%define cpan_name Cache-LRU
Name:           perl-Cache-LRU
Version:        0.40.0
Release:        0
# 0.04 -> normalize -> 0.40.0
%define cpan_version 0.04
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple, fast implementation of LRU cache in pure perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Patch0:         perl526.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Requires)
Provides:       perl(Cache::LRU) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Cache::LRU is a simple, fast implementation of an in-memory LRU cache in
pure perl.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
