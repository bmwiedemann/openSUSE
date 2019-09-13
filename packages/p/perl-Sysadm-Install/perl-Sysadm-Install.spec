#
# spec file for package perl-Sysadm-Install
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


Name:           perl-Sysadm-Install
Version:        0.48
Release:        0
%define cpan_name Sysadm-Install
Summary:        Typical installation tasks for system administrators
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sysadm-Install/
Source0:        http://www.cpan.org/authors/id/M/MS/MSCHILLI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Which) >= 1.09
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Log::Log4perl) >= 1.28
BuildRequires:  perl(Term::ReadKey)
Requires:       perl(File::Which) >= 1.09
Requires:       perl(LWP::Simple)
Requires:       perl(Log::Log4perl) >= 1.28
Requires:       perl(Term::ReadKey)
%{perl_requires}

%description
Have you ever wished for your installation shell scripts to run
reproducibly, without much programming fuzz, and even with optional logging
enabled? Then give up shell programming, use Perl.

'Sysadm::Install' executes shell-like commands performing typical
installation tasks: Copying files, extracting tarballs, calling 'make'. It
has a 'fail once and die' policy, meticulously checking the result of every
operation and calling 'die()' immediately if anything fails.

'Sysadm::Install' also supports a _dry_run_ mode, in which it logs
everything, but suppresses any write actions. Dry run mode is enabled by
calling 'Sysadm::Install::dry_run(1)'. To switch back to normal, call
'Sysadm::Install::dry_run(0)'.

As of version 0.17, 'Sysadm::Install' supports a _confirm_ mode, in which
it interactively asks the user before running any of its functions (just
like 'rm -i'). _confirm_ mode is enabled by calling
'Sysadm::Install::confirm(1)'. To switch back to normal, call
'Sysadm::Install::confirm(0)'.

'Sysadm::Install' is fully Log4perl-enabled. To start logging, just
initialize 'Log::Log4perl'. 'Sysadm::Install' acts as a wrapper class,
meaning that file names and line numbers are reported from the calling
program's point of view.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

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
%doc Changes README

%changelog
