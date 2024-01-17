#
# spec file for package perl-Proc-Simple
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Proc-Simple
Version:        1.32
Release:        0
%define cpan_name Proc-Simple
Summary:        Launch and Control Background Processes
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Proc-Simple/
Source0:        http://www.cpan.org/authors/id/M/MS/MSCHILLI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The Proc::Simple package provides objects mimicing real-life processes from
a user's point of view. A new process object is created by

   $myproc = Proc::Simple->new();

Either external programs or perl subroutines can be launched and controlled
as processes in the background.

A 10-second sleep process, for example, can be launched as an external
program as in

   $myproc->start("/bin/sleep 10");    # or
   $myproc->start("/bin/sleep", "10");

or as a perl subroutine, as in

   sub mysleep { sleep(shift); }    # Define mysleep()
   $myproc->start(\&mysleep, 10);   # Launch it.

or even as

   $myproc->start(sub { sleep(10); });

The _start_ Method returns immediately after starting the specified process
in background, i.e. there's no blocking. It returns _1_ if the process has
been launched successfully and _0_ if not.

The _poll_ method checks if the process is still running

   $running = $myproc->poll();

and returns _1_ if it is, _0_ if it's not. Finally,

   $myproc->kill();

terminates the process by sending it the SIGTERM signal. As an option,
another signal can be specified.

   $myproc->kill("SIGUSR1");

sends the SIGUSR1 signal to the running process. _kill_ returns _1_ if it
succeeds in sending the signal, _0_ if it doesn't.

The methods are discussed in more detail in the next section.

A destructor is provided so that a signal can be sent to the forked
processes automatically should the process object be destroyed or if the
process exits. By default this behaviour is turned off (see the
kill_on_destroy and signal_on_destroy methods).

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
