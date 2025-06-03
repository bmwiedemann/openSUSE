#
# spec file for package perl-App-CLI
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


%define cpan_name App-CLI
Name:           perl-App-CLI
Version:        0.520.0
Release:        0
# 0.52 -> normalize -> 0.520.0
%define cpan_version 0.52
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Dispatcher module for command line interface programs
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PT/PTC/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Pod::Simple::Text)
#BuildRequires:  perl(Test::Kwalitee)
BuildRequires:  perl(Test::Pod)
Requires:       perl(Capture::Tiny)
Requires:       perl(Class::Load)
Requires:       perl(Locale::Maketext::Simple)
Requires:       perl(Pod::Simple::Text)
Provides:       perl(App::CLI) = %{version}
Provides:       perl(App::CLI::Command)
Provides:       perl(App::CLI::Command::Commands)
Provides:       perl(App::CLI::Command::Help)
Provides:       perl(App::CLI::Command::Version)
Provides:       perl(App::CLI::Helper)
%undefine       __perllib_provides
%{perl_requires}

%description
'App::CLI' dispatches CLI (command line interface) based commands into
command classes. It also supports subcommand and per-command options.

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
%doc Changes README.md
%license LICENSE

%changelog
