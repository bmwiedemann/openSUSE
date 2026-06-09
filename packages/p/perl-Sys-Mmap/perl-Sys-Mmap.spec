#
# spec file for package perl-Sys-Mmap
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        0.210.0
Release:        0
# 0.21 -> normalize -> 0.210.0
%define cpan_version 0.21
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Uses mmap to map in a file as a Perl variable
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
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

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
