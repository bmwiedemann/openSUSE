#
# spec file for package perl-Math-Round
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


%define cpan_name Math-Round
Name:           perl-Math-Round
Version:        0.80.0
Release:        0
%define cpan_version 0.08
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for rounding numbers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(parent)
Requires:       perl(parent)
Provides:       perl(Math::Round) = 0.80.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
*Math::Round* supplies functions that will round numbers in different ways.
The functions *round* and *nearest* are exported by default; others are
available as described below. "use ... qw(:all)" exports all functions.

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
