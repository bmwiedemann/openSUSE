#
# spec file for package perl-Log-Any
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


%define cpan_name Log-Any
Name:           perl-Log-Any
Version:        1.713
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Bringing loggers and listeners together
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PR/PREACTION/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'Log::Any' provides a standard log production API for modules.
Log::Any::Adapter allows applications to choose the mechanism for log
consumption, whether screen, file or another logging mechanism like
Log::Dispatch or Log::Log4perl.

Many modules have something interesting to say. Unfortunately there is no
standard way for them to say it - some output to STDERR, others to 'warn',
others to custom file logs. And there is no standard way to get a module to
start talking - sometimes you must call a uniquely named method, other
times set a package variable.

This being Perl, there are many logging mechanisms available on CPAN. Each
has their pros and cons. Unfortunately, the existence of so many mechanisms
makes it difficult for a CPAN author to commit his/her users to one of
them. This may be why many CPAN modules invent their own logging or choose
not to log at all.

To untangle this situation, we must separate the two parts of a logging
API. The first, _log production_, includes methods to output logs (like
'$log->debug') and methods to inspect whether a log level is activated
(like '$log->is_debug'). This is generally all that CPAN modules care
about. The second, _log consumption_, includes a way to configure where
logging goes (a file, the screen, etc.) and the code to send it there. This
choice generally belongs to the application.

A CPAN module uses 'Log::Any' to get a log producer object. An application,
in turn, may choose one or more logging mechanisms via Log::Any::Adapter,
or none at all.

'Log::Any' has a very tiny footprint and no dependencies beyond Perl 5.8.1,
which makes it appropriate for even small CPAN modules to use. It defaults
to 'null' logging activity, so a module can safely log without worrying
about whether the application has chosen (or will ever choose) a logging
mechanism.

See http://www.openswartz.com/2007/09/06/standard-logging-api/ for the
original post proposing this module.

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes CONTRIBUTING.md README
%license LICENSE

%changelog
