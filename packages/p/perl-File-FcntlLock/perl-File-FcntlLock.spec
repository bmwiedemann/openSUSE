#
# spec file for package perl-File-FcntlLock
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


Name:           perl-File-FcntlLock
Version:        0.22
Release:        0
%define cpan_name File-FcntlLock
Summary:        File locking with L<fcntl(2)>
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-FcntlLock/
Source:         http://www.cpan.org/authors/id/J/JT/JTT/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
File locking in Perl is usually done using the 'flock' function.
Unfortunately, this only allows locks on whole files and is often
implemented in terms of the the flock(2) manpage system function which has
some shortcomings (especially concerning locks on remotely mounted file
systems) and slightly different behaviour than the fcntl(2) manpage.

Using this module file locking via the fcntl(2) manpage can be done
(obviously, this restricts the use of the module to systems that have a the
fcntl(2) manpage system call). Before a file (or parts of a file) can be
locked, an object simulating a flock structure, containing information in a
binary format to be passed to the fcntl(2) manpage for locking requests,
must be created and its properties set. Afterwards, by calling the the
lock() manpage method a lock can be set and removed or it can be determined
if and which process currently holds the lock.

File::FcntlLock (or its alias File::FcntlLock::XS) uses a shared library,
build during installation, to call the the fcntl(2) manpage system function
directly. If this is unsuitable there are two alternatives,
File::FcntlLock::Pure and File::FcntlLock::Inline. Both call the Perl
'fcntl' function instead and use Perl code to assemble and disassemble the
structure. For this at some time the (system-dependent) binary layout of
the flock structure must have been determined via a program written in C.
The difference between File::FcntlLock::Pure and File::FcntlLock::Inline is
that for the former this happened when the package is installed while for
the latter it is done each time the package is loaded (e.g., with 'use').
Thus, for File::FcntlLock::Inline to work a C compiler must be available.
There are some minor differences in the functionality and the behaviour on
passing the method for locking invalid arguments to be described below.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
