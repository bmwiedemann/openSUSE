#
# spec file for package perl-Hash-Merge-Simple
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


%define cpan_name Hash-Merge-Simple
Name:           perl-Hash-Merge-Simple
Version:        0.52.0
Release:        0
# 0.052 -> normalize -> 0.52.0
%define cpan_version 0.052
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Recursively merge two or more hashes, simply
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Clone)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Clone)
Provides:       perl(Hash::Merge::Simple) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Hash::Merge::Simple will recursively merge two or more hashes and return
the result as a new hash reference. The merge function will descend and
merge hashes that exist under the same node in both the left and right
hash, but doesn't attempt to combine arrays, objects, scalars, or anything
else. The rightmost hash also takes precedence, replacing whatever was in
the left hash if a conflict occurs.

This code was pretty much taken straight from Catalyst::Utils, and modified
to handle more than 2 hashes at the same time.

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
