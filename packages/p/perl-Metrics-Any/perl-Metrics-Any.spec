#
# spec file for package perl-Metrics-Any
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


%define cpan_name Metrics-Any
Name:           perl-Metrics-Any
Version:        0.09
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Abstract collection of monitoring metrics
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::Util) >= 1.29
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(List::Util) >= 1.29
%{perl_requires}

%description
Provides a central location for modules to report monitoring metrics, such
as counters of the number of times interesting events have happened, and
programs to collect up and send those metrics to monitoring services.

Inspired by Log::Any, this module splits the overall problem into two
sides. Modules wishing to provide metrics for monitoring purposes can use
the 'use Metrics::Any' statement to obtain a _collector_ into which they
can report metric events. By default this collector doesn't actually do
anything, so modules can easily use it without adding extra specific
dependencies for specific reporting.

A program using one or more such modules can apply a different policy and
request a particular _adapter_ implementation in order to actually report
these metrics to some external system, by using the 'use
Metrics::Any::Adapter' statement.

This separation of concerns allows module authors to write code which will
report metrics without needing to care about the exact mechanism of that
reporting (as well as to write code which does not itself depend on the
code required to perform that reporting).

%prep
%autosetup  -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
