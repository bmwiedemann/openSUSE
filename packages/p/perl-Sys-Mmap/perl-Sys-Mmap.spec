#
# spec file for package perl-Sys-Mmap
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


%define cpan_name Sys-Mmap
Name:           perl-Sys-Mmap
Version:        0.200.0
Release:        0
# 0.20 -> normalize -> 0.200.0
%define cpan_version 0.20
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Uses mmap to map in a file as a Perl variable
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Sys::Mmap) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The Sys::Mmap module uses the POSIX at https://en.wikipedia.org/wiki/Mmap
call to map in a file as a Perl variable. Memory access by mmap may be
shared between threads or forked processes, and may be a disc file that has
been mapped into memory. Sys::Mmap depends on your operating system
supporting UNIX or POSIX.1b mmap, of course.

*Note* that PerlIO now defines a ':mmap' tag and presents mmap'd files as
regular files, if that is your cup of joe.

Several processes may share one copy of the file or string, saving memory,
and concurrently making changes to portions of the file or string. When not
used with a file, it is an alternative to SysV shared memory. Unlike SysV
shared memory, there are no arbitrary size limits on the shared memory
area, and sparse memory usage is handled optimally on most modern UNIX
implementations.

Using the 'new()' method provides a 'tie()''d interface to 'mmap()' that
allows you to use the variable as a normal variable. If a filename is
provided, the file is opened and mapped in. If the file is smaller than the
length provided, the file is grown to that length. If no filename is
provided, anonymous shared inheritable memory is used. Assigning to the
variable will replace a section in the file corresponding to the length of
the variable, leaving the remainder of the file intact and unmodified.
Using 'substr()' allows you to access the file at an offset, and does not
place any requirements on the length argument to 'substr()' or the length
of the variable being inserted, provided it does not exceed the length of
the memory region. This protects you from the pathological cases involved
in using 'mmap()' directly, documented below.

When calling 'mmap()' or 'hardwire()' directly, you need to be careful how
you use the variable. Some programming constructs may create copies of a
string which, while unimportant for smallish strings, are far less welcome
if you're mapping in a file which is a few gigabytes big. If you use
'PROT_WRITE' and attempt to write to the file via the variable you need to
be even more careful. One of the few ways in which you can safely write to
the string in-place is by using 'substr()' as an lvalue and ensuring that
the part of the string that you replace is exactly the same length. Other
functions will allocate other storage for the variable, and it will no
longer overlay the mapped in file.

* Sys::Mmap->new( 'VARIABLE', 'LENGTH', 'OPTIONALFILENAME' )

Maps 'LENGTH' bytes of (the contents of) 'OPTIONALFILENAME' if
'OPTIONALFILENAME' is provided, otherwise uses anonymous, shared
inheritable memory. This memory region is inherited by any 'fork()'ed
children. 'VARIABLE' will now refer to the contents of that file. Any
change to 'VARIABLE' will make an identical change to the file. If 'LENGTH'
is zero and a file is specified, the current length of the file will be
used. If 'LENGTH' is larger then the file, and 'OPTIONALFILENAME' is
provided, the file is grown to that length before being mapped. This is the
preferred interface, as it requires much less caution in handling the
variable. 'VARIABLE' will be tied into the "Sys::Mmap" package, and
'mmap()' will be called for you.

Assigning to 'VARIABLE' will overwrite the beginning of the file for a
length of the value being assigned in. The rest of the file or memory
region after that point will be left intact. You may use 'substr()' to
assign at a given position:

    substr(VARIABLE, POSITION, LENGTH) = NEWVALUE

* mmap(VARIABLE, LENGTH, PROTECTION, FLAGS, FILEHANDLE, OFFSET)

Maps 'LENGTH' bytes of (the underlying contents of) 'FILEHANDLE' into your
address space, starting at offset 'OFFSET' and makes 'VARIABLE' refer to
that memory. The 'OFFSET' argument can be omitted in which case it defaults
to zero. The 'LENGTH' argument can be zero in which case a stat is done on
'FILEHANDLE' and the size of the underlying file is used instead.

The 'PROTECTION' argument should be some ORed combination of the constants
'PROT_READ', 'PROT_WRITE' and 'PROT_EXEC', or else 'PROT_NONE'. The
constants 'PROT_EXEC' and 'PROT_NONE' are unlikely to be useful here but
are included for completeness.

The 'FLAGS' argument must include either 'MAP_SHARED' or 'MAP_PRIVATE' (the
latter is unlikely to be useful here). If your platform supports it, you
may also use 'MAP_ANON' or 'MAP_ANONYMOUS'. If your platform supplies
'MAP_FILE' as a non-zero constant (necessarily non-POSIX) then you should
also include that in 'FLAGS'. POSIX.1b does not specify 'MAP_FILE' as a
'FLAG' argument and most if not all versions of Unix have 'MAP_FILE' as
zero.

mmap returns 'undef' on failure, and the address in memory where the
variable was mapped to on success.

* munmap(VARIABLE)

Unmaps the part of your address space which was previously mapped in with a
call to 'mmap(VARIABLE, ...)' and makes VARIABLE become undefined.

munmap returns 1 on success and undef on failure.

* hardwire(VARIABLE, ADDRESS, LENGTH)

Specifies the address in memory of a variable, possibly within a region
you've 'mmap()'ed another variable to. You must use the same precautions to
keep the variable from being reallocated, and use 'substr()' with an exact
length. If you 'munmap()' a region that a 'hardwire()'ed variable lives in,
the 'hardwire()'ed variable will not automatically be 'undef'ed. You must
do this manually.

* Constants

The Sys::Mmap module exports the following constants into your namespace:

    MAP_SHARED MAP_PRIVATE MAP_ANON MAP_ANONYMOUS MAP_FILE
    MAP_NORESERVE MAP_POPULATE
    MAP_HUGETLB MAP_HUGE_2MB MAP_HUGE_1GB
    PROT_EXEC PROT_NONE PROT_READ PROT_WRITE

Of the constants beginning with 'MAP_', only 'MAP_SHARED' and 'MAP_PRIVATE'
are defined in POSIX.1b and only 'MAP_SHARED' is likely to be useful.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license Artistic Copying

%changelog
