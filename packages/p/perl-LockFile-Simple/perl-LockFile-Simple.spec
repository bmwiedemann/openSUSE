#
# spec file for package perl-LockFile-Simple
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


# MANUAL license
Name:           perl-LockFile-Simple
Version:        0.208
Release:        0
%define cpan_name LockFile-Simple
Summary:        Simple file locking scheme
License:        GPL-2.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/LockFile-Simple/
Source:         http://www.cpan.org/authors/id/S/SC/SCHWIGON/lockfile-simple/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(LockFile::Lock)
#BuildRequires: perl(LockFile::Lock::Simple)
#BuildRequires: perl(LockFile::Manager)
#BuildRequires: perl(LockFile::Simple)
%{perl_requires}

%description
This simple locking scheme is not based on any file locking system calls
such as 'flock()' or 'lockf()' but rather relies on basic file system
primitives and properties, such as the atomicity of the 'write()' system
call. It is not meant to be exempt from all race conditions, especially
over NFS. The algorithm used is described below in the *ALGORITHM* section.

It is possible to customize the locking operations to attempt locking once
every 5 seconds for 30 times, or delete stale locks (files that are deemed
too ancient) before attempting the locking.

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
%doc ChangeLog README

%changelog
