#
# spec file for package perl-ExtUtils-F77
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


Name:           perl-ExtUtils-F77
Version:        1.24
Release:        0
%define cpan_name ExtUtils-F77
Summary:        Simple interface to F77 libs
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/K/KG/KGB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which)
Requires:       perl(File::Which)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gcc-fortran
BuildRequires:  gmp-devel
# MANUAL END

%description
This module tries to figure out how to link C programs with Fortran
subroutines on your system. Basically one must add a list of Fortran
runtime libraries. The problem is their location and name varies with each
OS/compiler combination! It was originally developed to make building and
installation of the PGPLOT module easier, which links to the pgplot Fortran
graphics library. It is now used by a numnber of perl modules.

This module tries to implement a simple 'rule-of-thumb' database for
various flavours of UNIX systems. A simple self-documenting Perl database
of knowledge/code for figuring out how to link for various combinations of
OS and compiler is embedded in the modules Perl code. Please help save the
world by submitted patches for new database entries for your system at
https://github.com/PDLPorters/extutils-f77

Note the default on most systems is now to search for a generic 'GNU'
compiler which can be gfortran, g77, g95 or fort77 (in that order based on
usage) and then find the appropriate link libraries automatically. (This is
the 'Generic' 'GNU' database entry in the code.)

The library list which the module returns can be explicitly overridden by
setting the environment variable F77LIBS, e.g.

  % setenv F77LIBS "-lfoo -lbar"
  % perl -MExtUtils::F77 -e 'print ExtUtils::F77->compiler, "\n"'
  ...

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc CHANGES README
%license COPYING

%changelog
