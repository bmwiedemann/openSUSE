#
# spec file for package perl-Log-Dispatch
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Log-Dispatch
Name:           perl-Log-Dispatch
Version:        2.710.0
Release:        0
# 2.71 -> normalize -> 2.710.0
%define cpan_version 2.71
License:        Artistic-2.0
Summary:        Dispatches messages to one or more outputs
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::GlobalDestruction)
BuildRequires:  perl(Dist::CheckConflicts) >= 0.20
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::ValidationCompiler)
BuildRequires:  perl(Specio) >= 0.320
BuildRequires:  perl(Specio::Declare)
BuildRequires:  perl(Specio::Exporter)
BuildRequires:  perl(Specio::Library::Builtins)
BuildRequires:  perl(Specio::Library::Numeric)
BuildRequires:  perl(Specio::Library::String)
BuildRequires:  perl(Sys::Syslog) >= 0.28
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(parent)
Requires:       perl(Devel::GlobalDestruction)
Requires:       perl(Dist::CheckConflicts) >= 0.20
Requires:       perl(Module::Runtime)
Requires:       perl(Params::ValidationCompiler)
Requires:       perl(Specio) >= 0.320
Requires:       perl(Specio::Declare)
Requires:       perl(Specio::Exporter)
Requires:       perl(Specio::Library::Builtins)
Requires:       perl(Specio::Library::Numeric)
Requires:       perl(Specio::Library::String)
Requires:       perl(Sys::Syslog) >= 0.28
Requires:       perl(Try::Tiny)
Requires:       perl(namespace::autoclean)
Requires:       perl(parent)
Provides:       perl(Log::Dispatch) = %{version}
Provides:       perl(Log::Dispatch::ApacheLog) = %{version}
Provides:       perl(Log::Dispatch::Base) = %{version}
Provides:       perl(Log::Dispatch::Code) = %{version}
Provides:       perl(Log::Dispatch::Email) = %{version}
Provides:       perl(Log::Dispatch::Email::MIMELite) = %{version}
Provides:       perl(Log::Dispatch::Email::MailSend) = %{version}
Provides:       perl(Log::Dispatch::Email::MailSender) = %{version}
Provides:       perl(Log::Dispatch::Email::MailSendmail) = %{version}
Provides:       perl(Log::Dispatch::File) = %{version}
Provides:       perl(Log::Dispatch::File::Locked) = %{version}
Provides:       perl(Log::Dispatch::Handle) = %{version}
Provides:       perl(Log::Dispatch::Null) = %{version}
Provides:       perl(Log::Dispatch::Output) = %{version}
Provides:       perl(Log::Dispatch::Screen) = %{version}
Provides:       perl(Log::Dispatch::Syslog) = %{version}
Provides:       perl(Log::Dispatch::Types) = %{version}
Provides:       perl(Log::Dispatch::Vars) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module manages a set of Log::Dispatch::* output objects that can be
logged to via a unified interface.

The idea is that you create a Log::Dispatch object and then add various
logging objects to it (such as a file logger or screen logger). Then you
call the 'log' method of the dispatch object, which passes the message to
each of the objects, which in turn decide whether or not to accept the
message and what to do with it.

This makes it possible to call single method and send a message to a log
file, via email, to the screen, and anywhere else, all with very little
code needed on your part, once the dispatching object has been created.

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
%doc Changes CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%license LICENSE

%changelog
