#
# spec file for package perl-Number-Bytes-Human
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Number-Bytes-Human
Name:           perl-Number-Bytes-Human
Version:        0.11
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Convert byte count to human readable format
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
THIS IS ALPHA SOFTWARE: THE DOCUMENTATION AND THE CODE WILL SUFFER CHANGES
SOME DAY (THANKS, GOD!).

This module provides a formatter which turns byte counts to usual readable
format, like '2.0K', '3.1G', '100B'. It was inspired in the '-h' option of
Unix utilities like 'du', 'df' and 'ls' for "human-readable" output.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
