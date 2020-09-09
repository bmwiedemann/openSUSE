#
# spec file for package perl-Log-Log4perl
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Log-Log4perl
Version:        1.52
Release:        0
%define cpan_name Log-Log4perl
Summary:        Log4j implementation for Perl
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Path) >= 2.070000
Requires:       perl(File::Path) >= 2.070000
Recommends:     perl(DBD::CSV) >= 0.33
Recommends:     perl(DBD::SQLite)
Recommends:     perl(DBI) >= 1.607
Recommends:     perl(Log::Dispatch)
Recommends:     perl(Log::Dispatch::FileRotate) >= 1.10
Recommends:     perl(SQL::Statement) >= 1.20
Recommends:     perl(XML::DOM) >= 1.29
%{perl_requires}

%description
Log::Log4perl lets you remote-control and fine-tune the logging behaviour
of your system from the outside. It implements the widely popular
(Java-based) Log4j logging package in pure Perl.

*For a detailed tutorial on Log::Log4perl usage, please read*

http://www.perl.com/pub/a/2002/09/11/log4perl.html

Logging beats a debugger if you want to know what's going on in your code
during runtime. However, traditional logging packages are too static and
generate a flood of log messages in your log files that won't help you.

'Log::Log4perl' is different. It allows you to control the number of
logging messages generated at three different levels:

  * At a central location in your system (either in a configuration file or in
the startup code) you specify _which components_ (classes, functions) of
your system should generate logs.

  * You specify how detailed the logging of these components should be by
specifying logging _levels_.

  * You also specify which so-called _appenders_ you want to feed your log
messages to ("Print it to the screen and also append it to /tmp/my.log")
and which format ("Write the date first, then the file name and line
number, and then the log message") they should be in.

This is a very powerful and flexible mechanism. You can turn on and off
your logs at any time, specify the level of detail and make that dependent
on the subsystem that's currently executed.

Let me give you an example: You might find out that your system has a
problem in the 'MySystem::Helpers::ScanDir' component. Turning on detailed
debugging logs all over the system would generate a flood of useless log
messages and bog your system down beyond recognition. With 'Log::Log4perl',
however, you can tell the system: "Continue to log only severe errors to
the log file. Open a second log file, turn on full debug logs in the
'MySystem::Helpers::ScanDir' component and dump all messages originating
from there into the new log file". And all this is possible by just
changing the parameters in a configuration file, which your system can
re-read even while it's running!

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
