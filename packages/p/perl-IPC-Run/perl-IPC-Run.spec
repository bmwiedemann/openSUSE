#
# spec file for package perl-IPC-Run
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


%define cpan_name IPC-Run
Name:           perl-IPC-Run
Version:        20231003.0.0
Release:        0
%define cpan_version 20231003.0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        System() and background procs w/ piping, redirs, ptys (Unix, Win32)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Pty) >= 1.08
BuildRequires:  perl(Readonly::Array)
Requires:       perl(IO::Pty) >= 1.08
Provides:       perl(IPC::Run) = 20231003.0.0
Provides:       perl(IPC::Run::Debug) = 20231003.0.0
Provides:       perl(IPC::Run::IO) = 20231003.0.0
Provides:       perl(IPC::Run::Timer) = 20231003.0.0
Provides:       perl(IPC::Run::Win32Helper) = 20231003.0.0
Provides:       perl(IPC::Run::Win32IO) = 20231003.0.0
Provides:       perl(IPC::Run::Win32Process) = 20231003.0.0
Provides:       perl(IPC::Run::Win32Pump) = 20231003.0.0
%undefine       __perllib_provides
Recommends:     perl(IO::Pty) >= 1.08
Recommends:     perl(Readonly)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  netcfg
# MANUAL END

%description
IPC::Run allows you to run and interact with child processes using files,
pipes, and pseudo-ttys. Both system()-style and scripted usages are
supported and may be mixed. Likewise, functional and OO API styles are both
supported and may be mixed.

Various redirection operators reminiscent of those seen on common Unix and
DOS command lines are provided.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644
# MANUAL BEGIN
# run.t sometimes fails with "Resource temporarily unavailable"
mv t/run.t t/run.tt
# MANUAL END

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
%doc Changelog README.md
%license LICENSE

%changelog
