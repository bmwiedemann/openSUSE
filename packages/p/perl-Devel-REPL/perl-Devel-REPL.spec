#
# spec file for package perl-Devel-REPL
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


%define cpan_name Devel-REPL
Name:           perl-Devel-REPL
Version:        1.3.29
Release:        0
# 1.003029 -> normalize -> 1.3.29
%define cpan_version 1.003029
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Modern perl interactive shell
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Keywords)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.121
BuildRequires:  perl(Data::Dump::Streamer) >= 2.390
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(File::Next)
BuildRequires:  perl(Lexical::Persistence)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.930
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Getopt) >= 0.180
BuildRequires:  perl(MooseX::Object::Pluggable) >= 0.0.900
BuildRequires:  perl(PPI)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(B::Keywords)
Requires:       perl(Data::Dump::Streamer) >= 2.390
Requires:       perl(Data::Dumper::Concise)
Requires:       perl(File::Next)
Requires:       perl(Lexical::Persistence)
Requires:       perl(Module::Runtime)
Requires:       perl(Moose) >= 0.930
Requires:       perl(Moose::Meta::Role)
Requires:       perl(Moose::Role)
Requires:       perl(MooseX::Getopt) >= 0.180
Requires:       perl(MooseX::Object::Pluggable) >= 0.0.900
Requires:       perl(PPI)
Requires:       perl(Task::Weaken)
Requires:       perl(namespace::autoclean)
Provides:       perl(Devel::REPL) = %{version}
Provides:       perl(Devel::REPL::Error) = %{version}
Provides:       perl(Devel::REPL::Meta::Plugin) = %{version}
Provides:       perl(Devel::REPL::Plugin) = %{version}
Provides:       perl(Devel::REPL::Plugin::B::Concise) = %{version}
Provides:       perl(Devel::REPL::Plugin::Colors) = %{version}
Provides:       perl(Devel::REPL::Plugin::Commands) = %{version}
Provides:       perl(Devel::REPL::Plugin::Completion) = %{version}
Provides:       perl(Devel::REPL::Plugin::CompletionDriver::Globals) = %{version}
Provides:       perl(Devel::REPL::Plugin::CompletionDriver::INC) = %{version}
Provides:       perl(Devel::REPL::Plugin::CompletionDriver::Keywords) = %{version}
Provides:       perl(Devel::REPL::Plugin::CompletionDriver::LexEnv) = %{version}
Provides:       perl(Devel::REPL::Plugin::CompletionDriver::Methods) = %{version}
Provides:       perl(Devel::REPL::Plugin::CompletionDriver::Turtles) = %{version}
Provides:       perl(Devel::REPL::Plugin::DDC) = %{version}
Provides:       perl(Devel::REPL::Plugin::DDS) = %{version}
Provides:       perl(Devel::REPL::Plugin::DumpHistory) = %{version}
Provides:       perl(Devel::REPL::Plugin::FancyPrompt) = %{version}
Provides:       perl(Devel::REPL::Plugin::FindVariable) = %{version}
Provides:       perl(Devel::REPL::Plugin::History) = %{version}
Provides:       perl(Devel::REPL::Plugin::Interrupt) = %{version}
Provides:       perl(Devel::REPL::Plugin::LexEnv) = %{version}
Provides:       perl(Devel::REPL::Plugin::MultiLine::PPI) = %{version}
Provides:       perl(Devel::REPL::Plugin::Nopaste) = %{version}
Provides:       perl(Devel::REPL::Plugin::OutputCache) = %{version}
Provides:       perl(Devel::REPL::Plugin::PPI) = %{version}
Provides:       perl(Devel::REPL::Plugin::Packages) = %{version}
Provides:       perl(Devel::REPL::Plugin::Peek) = %{version}
Provides:       perl(Devel::REPL::Plugin::ReadLineHistory) = %{version}
Provides:       perl(Devel::REPL::Plugin::Refresh) = %{version}
Provides:       perl(Devel::REPL::Plugin::ShowClass) = %{version}
Provides:       perl(Devel::REPL::Plugin::Timing) = %{version}
Provides:       perl(Devel::REPL::Plugin::Turtles) = %{version}
Provides:       perl(Devel::REPL::Profile) = %{version}
Provides:       perl(Devel::REPL::Profile::Default) = %{version}
Provides:       perl(Devel::REPL::Profile::Minimal) = %{version}
Provides:       perl(Devel::REPL::Profile::Standard) = %{version}
Provides:       perl(Devel::REPL::Script) = %{version}
%undefine       __perllib_provides
Recommends:     perl(App::Nopaste)
Recommends:     perl(B::Keywords)
Recommends:     perl(Data::Dump::Streamer) >= 2.390
Recommends:     perl(Data::Dumper::Concise)
Recommends:     perl(File::Next)
Recommends:     perl(Lexical::Persistence)
Recommends:     perl(Module::Refresh)
Recommends:     perl(PPI)
Recommends:     perl(PPI::XS) >= 0.902
Recommends:     perl(Sys::SigAction)
%{perl_requires}

%description
This is an interactive shell for Perl, commonly known as a REPL - Read,
Evaluate, Print, Loop. The shell provides for rapid development or testing
of code without the need to create a temporary source code file.

Through a plugin system, many features are available on demand. You can
also tailor the environment through the use of profiles and run control
files, for example to pre-load certain Perl modules when working on a
particular project.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes CONTRIBUTING examples README
%license LICENCE

%changelog
