#
# spec file for package perl-App-Dochazka-CLI
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


Name:           perl-App-Dochazka-CLI
Version:        0.238
Release:        0
%define cpan_name App-Dochazka-CLI
Summary:        Dochazka command line client
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/App-Dochazka-CLI/
Source0:        App-Dochazka-CLI-0.238.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(App::CELL) >= 0.209
BuildRequires:  perl(App::Dochazka::Common) >= 0.199
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::ShareDir) >= 1.00
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Module::Build) >= 0.370000
BuildRequires:  perl(Params::Validate) >= 1.06
BuildRequires:  perl(Software::License)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Text::Table)
BuildRequires:  perl(Web::MREST::CLI) >= 0.28
Requires:       perl(App::CELL) >= 0.209
Requires:       perl(App::Dochazka::Common) >= 0.199
Requires:       perl(Date::Calc)
Requires:       perl(File::HomeDir)
Requires:       perl(File::ShareDir) >= 1.00
Requires:       perl(File::Slurp)
Requires:       perl(HTTP::Cookies)
Requires:       perl(HTTP::Request)
Requires:       perl(JSON)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Params::Validate) >= 1.06
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::ReadLine::Gnu)
Requires:       perl(Text::Table)
Requires:       perl(Web::MREST::CLI) >= 0.281
%{perl_requires}
# MANUAL BEGIN
Requires:       xdg-utils
# MANUAL END

%description
App::Dochazka::CLI is the Command Line Interface (CLI) component of the
Dochazka Attendance & Time Tracking system.

In order to work, the CLI must be pointed at a running App::Dochazka::REST
(i.e., Dochazka REST server) instance by setting the 'MREST_CLI_URI_BASE'
meta configuration parameter.

Detailed documentation covering configuration, deployment, and the commands
that can be used with the CLI can be found in App::Dochazka::CLI::Guide.

This module is used to store some "global" package variables that are used
throughout the CLI code base.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
# MANUAL BEGIN
install -dm0755 %{buildroot}%{_sysconfdir}/dochazka-cli
install -m0640 ext/CLI_SiteConfig.pm.example %{buildroot}%{_sysconfdir}/dochazka-cli/CLI_SiteConfig.pm
install -m0644 ext/CLI_SiteConfig.pm.example %{buildroot}%{_sysconfdir}/dochazka-cli/CLI_SiteConfig.pm.example

echo "%dir %{_sysconfdir}/dochazka-cli" >> %{name}.files
echo "%config(noreplace) %attr(0640,root,root) %{_sysconfdir}/dochazka-cli/CLI_SiteConfig.pm" >> %{name}.files
echo "%config %{_sysconfdir}/dochazka-cli/CLI_SiteConfig.pm.example" >> %{name}.files
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes config ext LICENSE README.rst

%changelog
