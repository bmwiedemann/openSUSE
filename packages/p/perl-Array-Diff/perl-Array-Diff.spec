#
# spec file for package perl-Array-Diff
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


%define cpan_name Array-Diff
Name:           perl-Array-Diff
Version:        0.90.0
Release:        0
# 0.09 -> normalize -> 0.90.0
%define cpan_version 0.09
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Find the differences between two arrays
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Algorithm::Diff) >= 1.190
BuildRequires:  perl(Class::Accessor::Fast)
Requires:       perl(Algorithm::Diff) >= 1.190
Requires:       perl(Class::Accessor::Fast)
Provides:       perl(Array::Diff) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module compares two *pre-sorted* arrays and returns the added or
deleted elements in two separate arrays. It's a simple wrapper around
Algorithm::Diff.

*Note*: the arrays must be sorted before you call 'diff'.

And if you need more complex array tools, check Array::Compare.

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
