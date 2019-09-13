#
# spec file for package perl-Devel-REPL
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Devel-REPL
Version:        1.003028
Release:        0
%define cpan_name Devel-REPL
Summary:        Modern Perl Interactive Shell
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-REPL/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(B::Keywords)
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(Data::Dump::Streamer) >= 2.39
BuildRequires:  perl(Data::Dumper::Concise)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Next)
BuildRequires:  perl(JSON::PP) >= 2.27300
BuildRequires:  perl(Lexical::Persistence)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moose) >= 0.93
BuildRequires:  perl(Moose::Meta::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Getopt) >= 0.18
BuildRequires:  perl(MooseX::Object::Pluggable) >= 0.0009
BuildRequires:  perl(PPI)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(namespace::autoclean)
Requires:       perl(B::Keywords)
Requires:       perl(Data::Dump::Streamer) >= 2.39
Requires:       perl(Data::Dumper::Concise)
Requires:       perl(File::HomeDir)
Requires:       perl(File::Next)
Requires:       perl(JSON::PP) >= 2.27300
Requires:       perl(Lexical::Persistence)
Requires:       perl(Module::Runtime)
Requires:       perl(Moose) >= 0.93
Requires:       perl(Moose::Meta::Role)
Requires:       perl(Moose::Role)
Requires:       perl(MooseX::Getopt) >= 0.18
Requires:       perl(MooseX::Object::Pluggable) >= 0.0009
Requires:       perl(PPI)
Requires:       perl(Task::Weaken)
Requires:       perl(namespace::autoclean)
Recommends:     perl(App::Nopaste)
Recommends:     perl(B::Keywords)
Recommends:     perl(Data::Dumper::Concise)
Recommends:     perl(Data::Dump::Streamer) >= 2.39
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
%doc Changes CONTRIBUTING examples LICENCE README

%changelog
