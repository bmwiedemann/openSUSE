#
# spec file for package perl-Filesys-Statvfs
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Filesys-Statvfs
Version:        0.82
Release:        0
%define cpan_name Filesys-Statvfs
Summary:        Perl extension for statvfs() and fstatvfs()
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Filesys-Statvfs/
Source0:        https://cpan.metacpan.org/authors/id/I/IG/IGUTHRIE/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Interface for statvfs() and fstatvfs()

Unless you need access to the bsize, flag, and namemax values, you should
probably look at using Filesys::DfPortable or Filesys::Df instead. They
will generally provide you with more functionality and portability.

The module should work with all flavors of Unix that implement the
'statvfs()' and 'fstatvfs()' calls. This would include Linux, *BSD, HP-UX,
AIX, Solaris, Mac OS X, Irix, Cygwin, etc ...

The 'statvfs()' and 'fstatvfs()' functions will return a list of values, or
will return 'undef' and set '$!' if there was an error.

The values returned are described in the statvfs/fstatvfs header or the
'statvfs()/fstatvfs()' man page.

The module assumes that if you have 'statvfs()', 'fstatvfs()' will also be
available.

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
