#
# spec file for package perl-Module-Metadata
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


%define cpan_name Module-Metadata
Name:           perl-Module-Metadata
Version:        1.000038
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Gather package and POD information from perl module files
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version) >= 0.87
Requires:       perl(version) >= 0.87
%{perl_requires}

%description
This module provides a standard way to gather metadata about a .pm file
through (mostly) static analysis and (some) code execution. When
determining the version of a module, the '$VERSION' assignment is 'eval'ed,
as is traditional in the CPAN toolchain.

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
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
