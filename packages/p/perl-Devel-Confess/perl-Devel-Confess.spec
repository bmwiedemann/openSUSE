#
# spec file for package perl-Devel-Confess
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Devel-Confess
Version:        0.009004
Release:        0
%define cpan_name Devel-Confess
Summary:        Include stack traces on all warnings and errors
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-Confess/
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
This module is meant as a debugging aid. It can be used to make a script
complain loudly with stack backtraces when 'warn()'ing or 'die()'ing.
Unlike other similar modules (e.g. Carp::Always), stack traces will also be
included when exception objects are thrown.

The stack traces are generated using Carp, and will work for all types of
errors. Carp's 'carp' and 'croak' functions will also be made to include
stack traces.

  # it works for explicit die's and warn's
  $ perl -d:Confess -e 'sub f { die "arghh" }; sub g { f }; g'
  arghh at -e line 1.
          main::f() called at -e line 1
          main::g() called at -e line 1

  # it works for interpreter-thrown failures
  $ perl -d:Confess -w -e 'sub f { $a = shift; @a = @$a };' \
                                        -e 'sub g { f(undef) }; g'
  Use of uninitialized value $a in array dereference at -e line 1.
          main::f(undef) called at -e line 2
          main::g() called at -e line 2

Internally, this is implemented with $SIG{__WARN__} and $SIG{__DIE__}
hooks.

Stack traces are also included if raw non-object references are thrown.

This module is compatible with all perl versions back to 5.6.2, without
additional prerequisites. It contains workarounds for a number of bugs in
the perl interpreter, some of which effect comparatively simpler modules,
like Carp::Always.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
