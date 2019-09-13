#
# spec file for package perl-Log-Contextual
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


Name:           perl-Log-Contextual
Version:        0.008001
Release:        0
%define cpan_name Log-Contextual
Summary:        Simple logging interface with a contextual log
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Log-Contextual/
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(Exporter::Declare) >= 0.111
BuildRequires:  perl(Moo) >= 1.003
BuildRequires:  perl(Test::Fatal)
Requires:       perl(Data::Dumper::Concise)
Requires:       perl(Exporter::Declare) >= 0.111
Requires:       perl(Moo) >= 1.003
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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
