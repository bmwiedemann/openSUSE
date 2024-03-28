#
# spec file for package perl-HTML-Tagset
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


%define cpan_name HTML-Tagset
Name:           perl-HTML-Tagset
Version:        3.240.0
Release:        0
# 3.24 -> normalize -> 3.240.0
%define cpan_version 3.24
License:        Artistic-2.0
Summary:        Data tables useful in parsing HTML
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.46
BuildRequires:  perl(Test::More) >= 0.95
Provides:       perl(HTML::Tagset) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module contains several data tables useful in various kinds of HTML
parsing operations.

Note that all tag names used are lowercase.

In the following documentation, a "hashset" is a hash being used as a set
-- the hash conveys that its keys are there, and the actual values
associated with the keys are not significant. (But what values are there,
are always true.)

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
%doc Changes README.md

%changelog
