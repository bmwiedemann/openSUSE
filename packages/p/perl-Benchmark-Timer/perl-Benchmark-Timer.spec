#
# spec file for package perl-Benchmark-Timer
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


%define cpan_name Benchmark-Timer
Name:           perl-Benchmark-Timer
Version:        0.711.200
Release:        0
# 0.7112 -> normalize -> 0.711.200
%define cpan_version 0.7112
#Upstream: GPL-2.0-or-later
License:        GPL-2.0-or-later
Summary:        Benchmarking with statistical confidence
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCOPPIT/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(UNIVERSAL::require)
BuildRequires:  perl(URI::Escape)
%{perl_requires}

%description
The Benchmark::Timer class allows you to time portions of code
conveniently, as well as benchmark code by allowing timings of repeated
trials. It is perfect for when you need more precise information about the
running time of portions of your code than the Benchmark module will give
you, but don't want to go all out and profile your code.

The methodology is simple; create a Benchmark::Timer object, and wrap
portions of code that you want to benchmark with 'start()' and 'stop()'
method calls. You can supply a tag to those methods if you plan to time
multiple portions of code. If you provide error and confidence values, you
can also use 'need_more_samples()' to determine, statistically, whether you
need to collect more data.

After you have run your code, you can obtain information about the running
time by calling the 'results()' method, or get a descriptive benchmark
report by calling 'report()'. If you run your code over multiple trials,
the average time is reported. This is wonderful for benchmarking
time-critical portions of code in a rigorous way. You can also optionally
choose to skip any number of initial trials to cut down on initial case
irregularities.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
sed -i -e 's,/usr/local/bin/perl,/usr/bin/perl,' delta.pl
# MANUAL END

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc CHANGES README TODO
%license LICENSE

%changelog
