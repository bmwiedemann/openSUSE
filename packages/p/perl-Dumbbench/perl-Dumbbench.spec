#
# spec file for package perl-Dumbbench
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


Name:           perl-Dumbbench
Version:        0.111
Release:        0
%define cpan_name Dumbbench
Summary:        More reliable benchmarking with the least amount of thinking
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Dumbbench/
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::XSAccessor) >= 1.05
BuildRequires:  perl(Devel::CheckOS)
BuildRequires:  perl(Number::WithError) >= 1.00
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Statistics::CaseResampling) >= 0.06
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(parent)
Requires:       perl(Capture::Tiny)
Requires:       perl(Class::XSAccessor) >= 1.05
Requires:       perl(Devel::CheckOS)
Requires:       perl(Number::WithError) >= 1.00
Requires:       perl(Params::Util)
Requires:       perl(Statistics::CaseResampling) >= 0.06
Requires:       perl(parent)
%{perl_requires}

%description
This module attempts to implement reasonably robust benchmarking with
little extra effort and expertise required from the user. That is to say,
benchmarking using this module is likely an improvement over

  time some-command --to --benchmark

or

  use Benchmark qw/timethis/;
  timethis(1000, 'system("some-command", ...)');

The module currently works similar to the former command line, except (in
layman terms) it will run the command many times, estimate the uncertainty
of the result and keep iterating until a certain user-defined precision has
been reached. Then, it calculates the resulting uncertainty and goes
through some pain to discard bad runs and subtract overhead from the
timings. The reported timing includes an uncertainty, so that multiple
benchmarks can more easily be compared.

Please note that 'Dumbbench' works entirely with wallclock time as reported
by 'Time::HiRes'' 'time()' function.

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
%doc Changes examples
%license LICENSE

%changelog
