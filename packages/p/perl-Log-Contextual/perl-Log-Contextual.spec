#
# spec file for package perl-Log-Contextual
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Log-Contextual
Name:           perl-Log-Contextual
Version:        0.009001
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple logging interface with a contextual log
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(Moo) >= 1.003000
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
Requires:       perl(Data::Dumper::Concise)
Requires:       perl(Moo) >= 1.003000
%{perl_requires}

%description
Major benefits:

* * Efficient

The default logging functions take blocks, so if a log level is disabled,
the block will not run:

  # the following won't run if debug is off
  log_debug { "the new count in the database is " . $rs->count };

Similarly, the 'D' prefixed methods only 'Dumper' the input if the level is
enabled.

* * Handy

The logging functions return their arguments, so you can stick them in the
middle of expressions:

  for (log_debug { "downloading:\n" . join qq(\n), @_ } @urls) { ... }

* * Generic

'Log::Contextual' is an interface for all major loggers. If you log through
'Log::Contextual' you will be able to swap underlying loggers later.

* * Powerful

'Log::Contextual' chooses which logger to use based on user defined
'CodeRef's. Normally you don't need to know this, but you can take
advantage of it when you need to later.

* * Scalable

If you just want to add logging to your basic application, start with
Log::Contextual::SimpleLogger and then as your needs grow you can switch to
Log::Dispatchouli or Log::Dispatch or Log::Log4perl or whatever else.

This module is a simple interface to extensible logging. It exists to
abstract your logging interface so that logging is as painless as possible,
while still allowing you to switch from one logger to another.

It is bundled with a really basic logger, Log::Contextual::SimpleLogger,
but in general you should use a real logger instead. For something more
serious but not overly complicated, try Log::Dispatchouli (see SYNOPSIS for
example.)

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
