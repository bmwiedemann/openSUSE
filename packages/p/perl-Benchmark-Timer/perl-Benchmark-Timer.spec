#
# spec file for package perl-Benchmark-Timer
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


Name:           perl-Benchmark-Timer
Version:        0.7112
Release:        0
#Upstream: GPL-2.0+
%define cpan_name Benchmark-Timer
Summary:        Benchmarking with statistical confidence
License:        GPL-2.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Benchmark-Timer/
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCOPPIT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Compile)
BuildRequires:  perl(UNIVERSAL::require)
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
sed -i -e 's,/usr/local/bin/perl,/usr/bin/perl,' delta.pl
# MANUAL END

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
%doc CHANGES README TODO
%license LICENSE

%changelog
