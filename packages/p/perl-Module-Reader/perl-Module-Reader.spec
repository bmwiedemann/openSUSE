#
# spec file for package perl-Module-Reader
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


%define cpan_name Module-Reader
Name:           perl-Module-Reader
Version:        0.003003
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Find and read perl modules like perl does
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         0001-Adjust-require-exception-to-perl-5.37.8-wording.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
This module finds modules in '@INC' using the same algorithm perl does.
From that, it will give you the source content of a module, the file name
(where available), and how it was found. Searches (and content) are based
on the same internal rules that perl uses for _require|perlfunc/require_
and _do|perlfunc/do_.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

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

%changelog
