#
# spec file for package perl-Text-Levenshtein
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Text-Levenshtein
Name:           perl-Text-Levenshtein
Version:        0.15
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Calculate the Levenshtein edit distance between two strings
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Unicode::Collate) >= 1.04
BuildRequires:  perl(parent)
Requires:       perl(Unicode::Collate) >= 1.04
%{perl_requires}

%description
This module implements the Levenshtein edit distance, which measures the
difference between two strings, in terms of the _edit distance_. This
distance is the number of substitutions, deletions or insertions ("edits")
needed to transform one string into the other one (and vice versa). When
two strings have distance 0, they are the same.

To learn more about the Levenshtein metric, have a look at the at
http://en.wikipedia.org/wiki/Levenshtein_distance.

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
%doc Changes README
%license LICENSE

%changelog
