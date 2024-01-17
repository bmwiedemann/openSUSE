#
# spec file for package perl-Statistics-Descriptive
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


%define cpan_name Statistics-Descriptive
Name:           perl-Statistics-Descriptive
Version:        3.0801
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Module of basic descriptive statistical functions
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build) >= 0.280000
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(parent)
Requires:       perl(List::MoreUtils)
Requires:       perl(parent)
%{perl_requires}

%description
This module provides basic functions used in descriptive statistics. It has
an object oriented design and supports two different types of data storage
and calculation objects: sparse and full. With the sparse method, none of
the data is stored and only a few statistical measures are available. Using
the full method, the entire data set is retained and additional functions
are available.

Whenever a division by zero may occur, the denominator is checked to be
greater than the value '$Statistics::Descriptive::Tolerance', which
defaults to 0.0. You may want to change this value to some small positive
value such as 1e-24 in order to obtain error messages in case of very small
denominators.

Many of the methods (both Sparse and Full) cache values so that subsequent
calls with the same arguments are faster.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes examples README UserSurvey.txt
%license LICENSE

%changelog
