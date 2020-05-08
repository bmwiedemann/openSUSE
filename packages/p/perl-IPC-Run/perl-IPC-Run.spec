#
# spec file for package perl-IPC-Run
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


Name:           perl-IPC-Run
Version:        20200505.0
Release:        0
%define cpan_name IPC-Run
Summary:        System() and background procs w/ piping, redirs, ptys (Unix, Win32)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         IPC-Run-0.89-path.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Pty) >= 1.08
BuildRequires:  perl(Readonly::Array)
Requires:       perl(IO::Pty) >= 1.08
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
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644
%patch0 
# MANUAL BEGIN
# run.t sometimes fails with "Resource temporarily unavailable"
mv t/run.t t/run.tt
# MANUAL END

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
%doc Changelog README.md
%license LICENSE

%changelog
