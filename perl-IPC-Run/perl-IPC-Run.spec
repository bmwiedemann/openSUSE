#
# spec file for package perl-IPC-Run
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


Name:           perl-IPC-Run
Version:        20180523.0
Release:        0
%define cpan_name IPC-Run
Summary:        System() and Background Procs W/ Piping, Redirs, Ptys (Unix, Win32)
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IPC-Run/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         IPC-Run-0.89-path.diff
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Pty) >= 1.08
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Readonly::Array)
Requires:       perl(IO::Pty) >= 1.08
Recommends:     perl(IO::Pty) >= 1.08
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
%patch0 
# MANUAL BEGIN
# run.t sometimes fails with "Resource temporarily unavailable"
mv t/run.t t/run.tt
# MANUAL END

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
%doc Changes README README.md TODO
%license LICENSE

%changelog
