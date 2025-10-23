#
# spec file for package perl-Log-Log4perl
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


%define cpan_name Log-Log4perl
Name:           perl-Log-Log4perl
Version:        1.570.0
Release:        0
# 1.57 -> normalize -> 1.570.0
%define cpan_version 1.57
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Log4j implementation for Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETJ/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(File::Path) >= 2.07
Provides:       perl(L4pResurrectable) = 0.10.0
Provides:       perl(Log::Log4perl) = %{version}
Provides:       perl(Log::Log4perl::Appender)
Provides:       perl(Log::Log4perl::Appender::Buffer) = 1.530.0
Provides:       perl(Log::Log4perl::Appender::DBI)
Provides:       perl(Log::Log4perl::Appender::File)
Provides:       perl(Log::Log4perl::Appender::Limit) = 1.530.0
Provides:       perl(Log::Log4perl::Appender::RRDs)
Provides:       perl(Log::Log4perl::Appender::Screen)
Provides:       perl(Log::Log4perl::Appender::ScreenColoredLevels)
Provides:       perl(Log::Log4perl::Appender::Socket)
Provides:       perl(Log::Log4perl::Appender::String)
Provides:       perl(Log::Log4perl::Appender::Synchronized) = 1.530.0
Provides:       perl(Log::Log4perl::Appender::TestArrayBuffer)
Provides:       perl(Log::Log4perl::Appender::TestBuffer)
Provides:       perl(Log::Log4perl::Appender::TestFileCreeper)
Provides:       perl(Log::Log4perl::Catalyst) = 1.530.0
Provides:       perl(Log::Log4perl::Config)
Provides:       perl(Log::Log4perl::Config::BaseConfigurator)
Provides:       perl(Log::Log4perl::Config::DOMConfigurator) = 0.30.0
Provides:       perl(Log::Log4perl::Config::PropertyConfigurator)
Provides:       perl(Log::Log4perl::Config::Watch)
Provides:       perl(Log::Log4perl::DateFormat)
Provides:       perl(Log::Log4perl::Filter)
Provides:       perl(Log::Log4perl::Filter::Boolean)
Provides:       perl(Log::Log4perl::Filter::LevelMatch)
Provides:       perl(Log::Log4perl::Filter::LevelRange)
Provides:       perl(Log::Log4perl::Filter::MDC)
Provides:       perl(Log::Log4perl::Filter::StringMatch)
Provides:       perl(Log::Log4perl::InternalDebug)
Provides:       perl(Log::Log4perl::JavaMap)
Provides:       perl(Log::Log4perl::JavaMap::ConsoleAppender)
Provides:       perl(Log::Log4perl::JavaMap::FileAppender)
Provides:       perl(Log::Log4perl::JavaMap::JDBCAppender)
Provides:       perl(Log::Log4perl::JavaMap::NTEventLogAppender)
Provides:       perl(Log::Log4perl::JavaMap::RollingFileAppender)
Provides:       perl(Log::Log4perl::JavaMap::SyslogAppender)
Provides:       perl(Log::Log4perl::JavaMap::TestBuffer)
Provides:       perl(Log::Log4perl::Layout)
Provides:       perl(Log::Log4perl::Layout::NoopLayout)
Provides:       perl(Log::Log4perl::Layout::PatternLayout)
Provides:       perl(Log::Log4perl::Layout::PatternLayout::Multiline)
Provides:       perl(Log::Log4perl::Layout::SimpleLayout)
Provides:       perl(Log::Log4perl::Level)
Provides:       perl(Log::Log4perl::Logger)
Provides:       perl(Log::Log4perl::MDC)
Provides:       perl(Log::Log4perl::NDC)
Provides:       perl(Log::Log4perl::Resurrector)
Provides:       perl(Log::Log4perl::Util)
Provides:       perl(Log::Log4perl::Util::Semaphore)
Provides:       perl(Log::Log4perl::Util::TimeTracker)
%undefine       __perllib_provides
Recommends:     perl(DBD::CSV) >= 0.330
Recommends:     perl(DBD::SQLite)
Recommends:     perl(DBI) >= 1.607
Recommends:     perl(Log::Dispatch)
Recommends:     perl(Log::Dispatch::FileRotate) >= 1.100
Recommends:     perl(SQL::Statement) >= 1.200
Recommends:     perl(XML::DOM) >= 1.290
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
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
