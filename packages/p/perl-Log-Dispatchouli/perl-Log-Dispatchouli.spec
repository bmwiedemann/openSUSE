#
# spec file for package perl-Log-Dispatchouli
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


%define cpan_name Log-Dispatchouli
Name:           perl-Log-Dispatchouli
Version:        3.002
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple wrapper around Log::Dispatch
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Log::Dispatch)
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(Log::Dispatch::File)
BuildRequires:  perl(Log::Dispatch::Screen)
BuildRequires:  perl(Log::Dispatch::Syslog)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(String::Flogger)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Exporter::GlobExporter) >= 0.002
BuildRequires:  perl(Sys::Syslog) >= 0.16
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Try::Tiny) >= 0.04
BuildRequires:  perl(experimental)
Requires:       perl(Log::Dispatch)
Requires:       perl(Log::Dispatch::Array)
Requires:       perl(Log::Dispatch::File)
Requires:       perl(Log::Dispatch::Screen)
Requires:       perl(Log::Dispatch::Syslog)
Requires:       perl(Params::Util)
Requires:       perl(String::Flogger)
Requires:       perl(Sub::Exporter)
Requires:       perl(Sub::Exporter::GlobExporter) >= 0.002
Requires:       perl(Sys::Syslog) >= 0.16
Requires:       perl(Try::Tiny) >= 0.04
Requires:       perl(experimental)
%{perl_requires}

%description
Log::Dispatchouli is a thin layer above Log::Dispatch and meant to make it
dead simple to add logging to a program without having to think much about
categories, facilities, levels, or things like that. It is meant to make
logging just configurable enough that you can find the logs you want and
just easy enough that you will actually log things.

Log::Dispatchouli can log to syslog (if you specify a facility), standard
error or standard output, to a file, or to an array in memory. That last
one is mostly useful for testing.

In addition to providing as simple a way to get a handle for logging
operations, Log::Dispatchouli uses String::Flogger to process the things to
be logged, meaning you can easily log data structures. Basically: strings
are logged as is, arrayrefs are taken as (sprintf format, args), and
subroutines are called only if needed. For more information read the
String::Flogger docs.

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
%doc Changes README
%license LICENSE

%changelog
