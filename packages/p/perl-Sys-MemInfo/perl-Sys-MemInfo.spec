#
# spec file for package perl-Sys-MemInfo
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Sys-MemInfo
Version:        0.99
Release:        0
%define cpan_name Sys-MemInfo
Summary:        Query the total free and used physical memory
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/S/SC/SCRESTO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Sys::MemInfo return the total amount of free and used physical memory in
bytes in totalmem and freemem variables.

Total amount of free and user swap memory are alse returned in totalswap
and freeswap variables.

This module has been tested on Linux 3.13.0, UnixWare 7.1.2, AIX5, OpenBSD
3.8, NetBSD 2.0.2, FreBSD 5.4, HPUX11, Solaris 9, Tru64 5.1, Irix 6.5, Mac
OS X 10.2 darwin and Windows XP.

It should work on FreeBSD 4 and Windows 9X/ME/NT/200X/Vista.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
