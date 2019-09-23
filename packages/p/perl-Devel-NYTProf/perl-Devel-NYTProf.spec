#
# spec file for package perl-Devel-NYTProf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Devel-NYTProf
Version:        6.06
Release:        0
%define cpan_name Devel-NYTProf
Summary:        Powerful fast feature-rich Perl source code profiler
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-NYTProf/
Source0:        https://cpan.metacpan.org/authors/id/T/TI/TIMB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which) >= 1.09
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Test::Differences) >= 0.60
BuildRequires:  perl(Test::More) >= 0.84
Requires:       perl(File::Which) >= 1.09
Requires:       perl(JSON::MaybeXS)
Requires:       perl(Test::Differences) >= 0.60
Requires:       perl(Test::More) >= 0.84
%{perl_requires}

%description
Devel::NYTProf is a powerful, fast, feature-rich perl source code profiler.

  * Performs per-line statement profiling for fine detail

  * Performs per-subroutine statement profiling for overview

  * Performs per-opcode profiling for slow perl builtins

  * Performs per-block statement profiling (the first profiler to do so)

  * Accounts correctly for time spent after calls return

  * Performs inclusive and exclusive timing of subroutines

  * Subroutine times are per calling location (a powerful feature)

  * Can profile compile-time activity, just run-time, or just END time

  * Uses novel techniques for efficient profiling

  * Sub-microsecond (100ns) resolution on supported systems

  * Very fast - the fastest statement and subroutine profilers for perl

  * Handles applications that fork, with no performance cost

  * Immune from noise caused by profiling overheads and I/O

  * Program being profiled can stop/start the profiler

  * Generates richly annotated and cross-linked html reports

  * Captures source code, including string evals, for stable results

  * Trivial to use with mod_perl - add one line to httpd.conf

  * Includes an extensive test suite

  * Tested on very large codebases

NYTProf is effectively two profilers in one: a statement profiler, and a
subroutine profiler.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes HACKING README.md

%changelog
