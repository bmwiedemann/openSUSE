#
# spec file for package perl-Term-ReadLine-Gnu
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Term-ReadLine-Gnu
Version:        1.36
Release:        0
%define cpan_name Term-ReadLine-Gnu
Summary:        Perl extension for the GNU Readline/History Library
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAYASHI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
