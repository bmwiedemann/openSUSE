#
# spec file for package perl-Linux-Pid
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Linux-Pid
Version:        0.04
Release:        0
%define cpan_name Linux-Pid
Summary:        Get the native PID and the PPID on Linux
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Linux-Pid/
Source:         http://www.cpan.org/authors/id/R/RG/RGARCIA/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Linux::Pid)
%{perl_requires}

%description
Why should one use a module to get the PID and the PPID of a process where
there are the '$$' variable and the 'getppid()' builtin ? (Not mentioning
the equivalent 'POSIX::getpid()' and 'POSIX::getppid()' functions.)

In fact, this is useful on Linux, with multithreaded programs. Linux' C
library, using the linux thread model, returns different values of the PID
and the PPID from different threads. (Other thread models such as NPTL
don't have the same behaviour). This module forces perl to call the
underlying C functions 'getpid()' and 'getppid()'.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
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
