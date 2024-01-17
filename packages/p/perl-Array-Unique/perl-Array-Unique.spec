#
# spec file for package perl-Array-Unique
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


%define cpan_name Array-Unique
Name:           perl-Array-Unique
Version:        0.09
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Tie-able array that allows only unique values
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SZ/SZABGAB/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build) >= 0.420000
%{perl_requires}

%description
This package lets you create an array which will allow only one occurrence
of any value.

In other words no matter how many times you put in 42 it will keep only the
first occurrence and the rest will be dropped.

You use the module via tie and once you tied your array to this module it
will behave correctly.

Uniqueness is checked with the 'eq' operator so among other things it is
case sensitive.

As a side effect the module does not allow undef as a value in the array.

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README README.md

%changelog
