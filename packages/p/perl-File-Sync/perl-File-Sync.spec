#
# spec file for package perl-File-Sync
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           perl-File-Sync
Version:        0.11
Release:        1
License:        GPL-1.0+ or Artistic-1.0
%define cpan_name File-Sync
Summary:        Perl access to fsync() and sync() function calls
Url:            http://search.cpan.org/dist/File-Sync/
Group:          Development/Libraries/Perl
Source:         http://search.cpan.org/CPAN/authors/id/B/BR/BRIANSKI/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(File::Sync)
%{perl_requires}

%description
The fsync() function takes a Perl file handle as its only argument, and
passes its fileno() to the C function fsync(). It returns _undef_ on
failure, or _true_ on success.

The fsync_fd() function is used internally by fsync(); it takes a file
descriptor as its only argument.

The sync() function is identical to the C function sync().

This module does *not* export any methods by default, but fsync() is made
available as a method of the _FileHandle_ and _IO::Handle_ classes.

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
