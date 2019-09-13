#
# spec file for package perl-IPC-ShareLite
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


Name:           perl-IPC-ShareLite
Version:        0.17
Release:        0
%define cpan_name IPC-ShareLite
Summary:        Lightweight interface to shared memory
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IPC-ShareLite/
Source:         http://www.cpan.org/authors/id/A/AN/ANDYA/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
IPC::ShareLite provides a simple interface to shared memory, allowing data
to be efficiently communicated between processes. Your operating system
must support SysV IPC (shared memory and semaphores) in order to use this
module.

IPC::ShareLite provides an abstraction of the shared memory and semaphore
facilities of SysV IPC, allowing the storage of arbitrarily large data; the
module automatically acquires and removes shared memory segments as needed.
Storage and retrieval of data is atomic, and locking functions are provided
for higher-level synchronization.

In many respects, this module is similar to IPC::Shareable. However,
IPC::ShareLite does not provide a tied interface, does not (automatically)
allow the storage of variables, and is written in C for additional speed.

Construct an IPC::ShareLite object by calling its constructor:

    my $share = IPC::ShareLite->new(
        -key     => 1971,
        -create  => 'yes',
        -destroy => 'no'
    ) or die $!;

Once an instance has been created, data can be written to shared memory by
calling the store() method:

	$share->store("This is going in shared memory");

Retrieve the data by calling the fetch() method:

	my $str = $share->fetch();

The store() and fetch() methods are atomic; any processes attempting to
read or write to the memory are blocked until these calls finish. However,
in certain situations, you'll want to perform multiple operations
atomically. Advisory locking methods are available for this purpose.

An exclusive lock is obtained by calling the lock() method:

	$share->lock();

Happily, the lock() method also accepts all of the flags recognized by the
flock() system call. So, for example, you can obtain a shared lock like
this:

	$share->lock( LOCK_SH );

Or, you can make either type of lock non-blocking:

	$share->lock( LOCK_EX|LOCK_NB );

Release the lock by calling the unlock() method:

	$share->unlock;

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
