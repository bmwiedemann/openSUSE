#
# spec file for package perl-Sys-SigAction
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


Name:           perl-Sys-SigAction
Version:        0.23
Release:        0
%define cpan_name Sys-SigAction
Summary:        Perl extension for Consistent Signal Handling
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sys-SigAction/
Source0:        http://www.cpan.org/authors/id/L/LB/LBAXTER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Prior to version 5.8.0 perl implemented 'unsafe' signal handling. The
reason it is consider unsafe, is that there is a risk that a signal will
arrive, and be handled while perl is changing internal data structures.
This can result in all kinds of subtle and not so subtle problems. For this
reason it has always been recommended that one do as little as possible in
a signal handler, and only variables that already exist be manipulated.

Perl 5.8.0 and later versions implements 'safe' signal handling on
platforms which support the POSIX sigaction() function. This is
accomplished by having perl note that a signal has arrived, but deferring
the execution of the signal handler until such time as it is safe to do so.
Unfortunately these changes can break some existing scripts, if they
depended on a system routine being interrupted by the signal's arrival. The
perl 5.8.0 implementation was modified further in version 5.8.2.

From the perl 5.8.2 *perlvar* man page:

   The default delivery policy of signals changed in Perl 5.8.0 
   from immediate (also known as "unsafe") to deferred, also 
   known as "safe signals".

The implementation of this changed the 'sa_flags' with which the signal
handler is installed by perl, and it causes some system routines (like
connect()) to return EINTR, instead of another error when the signal
arrives. The problem comes when the code that made the system call sees the
EINTR code and decides it's going to call it again before returning. Perl
doesn't do this but some libraries do, including for instance, the Oracle
OCI library.

Thus the 'deferred signal' approach (as implemented by default in perl 5.8
and later) results in some system calls being retried prior to the signal
handler being called by perl. This breaks timeout logic for DBD-Oracle
which works with earlier versions of perl. This can be particularly vexing,
when, for instance, the host on which a database resides is not available:
'DBI->connect()' hangs for minutes before returning an error (and cannot
even be interrupted with control-C, even when the intended timeout is only
seconds). This is because SIGINT appears to be deferred as well. The result
is that it is impossible to implement open timeouts with code that looks
like this in perl 5.8.0 and later:

   eval {
      eval {
         local $SIG{ALRM} = sub { die "timeout" };
         alarm 2;
         $sth = DBI->connect(...);
         alarm 0;
      };
      alarm 0;
      die if $@;
   };

Or as the author of bug #50628 pointed out, might probably better be
written as:

   eval {
      local $SIG{ALRM} = sub { die "timeout" };
      eval {
         alarm 2;
         $sth = DBI->connect(...);
         alarm 0;
      };
      alarm 0;
      die if $@;
   };

The solution, if your system has the POSIX sigaction() function, is to use
perl's 'POSIX::sigaction()' to install the signal handler. With
'sigaction()', one gets control over both the signal mask, and the
'sa_flags' that are used to install the handler. Further, with perl 5.8.2
and later, a 'safe' switch is provided which can be used to ask for safe(r)
signal handling.

Using sigaction() ensures that the system call won't be resumed after it's
interrupted, so long as die is called within the signal handler. This is no
longer the case when one uses '$SIG{name}' to set signal handlers in perls
>= 5.8.0.

The usage of sigaction() is not well documented however, and in perl
versions less than 5.8.0, it does not work at all. (But that's OK, because
just setting '$SIG' does work in that case.) Using sigaction() requires
approximately 4 or 5 lines of code where previously one only had to set a
code reference into the %SIG hash.

Unfortunately, at least with perl 5.8.0, the result is that doing this
effectively reverts to the 'unsafe' signals behavior. It is not clear
whether this would be the case in perl 5.8.2, since the safe flag can be
used to ask for safe signal handling. I suspect this separates the logic
which uses the 'sa_flags' to install the handler, and whether deferred
signal handling is used.

The reader should also note, that the behavior of the 'safe' attribute is
not consistent with what this author expected. Specifically, it appears to
disable signal masking. This can be examined further in the t/safe.t and
the t/mask.t regression tests. Never-the-less, Sys::SigAction provides an
easy mechanism for the user to recover the pre-5.8.0 behavior for signal
handling, and the mask attribute clearly works. (see t/mask.t) If one is
looking for specific safe signal handling behavior that is considered
broken, and the breakage can be demonstrated, then a patch to t/safe.t
would be most welcome.

This module wraps up the POSIX:: routines and objects necessary to call
sigaction() in a way that is as efficient from a coding perspective as just
setting a localized '$SIG{SIGNAL}' with a code reference. Further, the user
has control over the 'sa_flags' passed to sigaction(). By default, if no
additional args are passed to sigaction(), then the signal handler will be
called when a signal (such as SIGALRM) is delivered.

Since sigaction() is not fully functional in perl versions less than 5.8,
this module implements equivalent behavior using the standard '%SIG' array.
The version checking and implementation of the 'right' code is handled by
this module, so the user does not have to write perl version dependent
code. The attrs hashref argument to set_sig_handler() is silently ignored,
in perl versions less than 5.8. When this module was developed it was
tested on perl 5.005 on solaris. That was in 2004. Now only perl versions
>= 5.6 are supported. If you want this to work on perl 5.5 you will have
comment out "use warnings" everywhere.

It is hoped that with the use of this module, your signal handling behavior
can be coded in a way that does not change from one perl version to the
next, and that sigaction() will be easier for you to use.

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
