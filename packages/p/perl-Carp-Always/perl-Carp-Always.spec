#
# spec file for package perl-Carp-Always
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


%define cpan_name Carp-Always
Name:           perl-Carp-Always
Version:        0.160.0
Release:        0
# 0.16 -> normalize -> 0.160.0
%define cpan_version 0.16
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Warns and dies noisily with stack backtraces
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Base)
Provides:       perl(Carp::Always) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module is meant as a debugging aid. It can be used to make a script
complain loudly with stack backtraces when warn()ing or die()ing.

Here are how stack backtraces produced by this module looks:

  # it works for explicit die's and warn's
  $ perl -MCarp::Always -e 'sub f { die "arghh" }; sub g { f }; g'
  arghh at -e line 1
          main::f() called at -e line 1
          main::g() called at -e line 1

  # it works for interpreter-thrown failures
  $ perl -MCarp::Always -w -e 'sub f { $a = shift; @a = @$a };' \
                           -e 'sub g { f(undef) }; g'
  Use of uninitialized value in array dereference at -e line 1
          main::f('undef') called at -e line 2
          main::g() called at -e line 2

In the implementation, the Carp module does the heavy work, through
'longmess()'. The actual implementation sets the signal hooks
$SIG{__WARN__} and $SIG{__DIE__} to emit the stack backtraces.

Also, all uses of 'carp' and 'croak' are made verbose, behaving like
'cluck' and 'confess'.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
