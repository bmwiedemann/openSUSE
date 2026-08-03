#
# spec file for package perl-Devel-NYTProf
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Devel-NYTProf
Name:           perl-Devel-NYTProf
Version:        6.150.0
Release:        0
# 6.15 -> normalize -> 6.150.0
%define cpan_version 6.15
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Powerful fast feature-rich Perl source code profiler
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/J/JK/JKEENAN/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::Which) >= 1.90
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Sub::Name) >= 0.110
BuildRequires:  perl(Test::Differences) >= 0.600
BuildRequires:  perl(Test::More) >= 0.84
Requires:       perl(File::Which) >= 1.90
Requires:       perl(JSON::MaybeXS)
Provides:       perl(Devel::NYTProf) = %{version}
Provides:       perl(Devel::NYTProf::Apache) = %{version}
Provides:       perl(Devel::NYTProf::Constants)
Provides:       perl(Devel::NYTProf::Core) = %{version}
Provides:       perl(Devel::NYTProf::Data) = %{version}
Provides:       perl(Devel::NYTProf::FileHandle)
Provides:       perl(Devel::NYTProf::FileInfo)
Provides:       perl(Devel::NYTProf::ReadStream) = %{version}
Provides:       perl(Devel::NYTProf::Reader) = %{version}
Provides:       perl(Devel::NYTProf::Run)
Provides:       perl(Devel::NYTProf::SubCallInfo)
Provides:       perl(Devel::NYTProf::SubInfo)
Provides:       perl(Devel::NYTProf::Util) = %{version}
%undefine       __perllib_provides
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
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes HACKING README.md

%changelog
