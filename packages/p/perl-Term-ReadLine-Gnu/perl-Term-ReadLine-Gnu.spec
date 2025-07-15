#
# spec file for package perl-Term-ReadLine-Gnu
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


%define cpan_name Term-ReadLine-Gnu
Name:           perl-Term-ReadLine-Gnu
Version:        1.470.0
Release:        0
# 1.47 -> normalize -> 1.470.0
%define cpan_version 1.47
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl extension for the GNU Readline/History Library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAYASHI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Term::ReadLine::Gnu) = %{version}
Provides:       perl(Term::ReadLine::Gnu::AU)
Provides:       perl(Term::ReadLine::Gnu::Var)
Provides:       perl(Term::ReadLine::Gnu::XS) = %{version}
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
Obsoletes:      perl-TermReadLine-Gnu < 1.36
Provides:       perl-TermReadLine-Gnu = %{version}
# MANUAL END

%description
This is an implementation of Term::ReadLine using the GNU Readline/History
Library.

For basic functions object oriented interface is provided. These are
described in the section "Standard Methods" and "Term::ReadLine::Gnu
Functions".

This package also has the interface with the almost all functions and
variables which are documented in the GNU Readline/History Library Manual.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
