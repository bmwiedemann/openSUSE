#
# spec file for package perl-Dumbbench
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Dumbbench
Name:           perl-Dumbbench
Version:        0.503
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        More reliable benchmarking with the least amount of thinking
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/B/BD/BDFOY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::XSAccessor) >= 1.05
BuildRequires:  perl(Devel::CheckOS)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.64
BuildRequires:  perl(Number::WithError) >= 1.00
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Statistics::CaseResampling) >= 0.06
BuildRequires:  perl(Test::More) >= 1
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
%autosetup  -n %{cpan_name}-%{version}

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
%doc Changes examples
%license LICENSE

%changelog
