#
# spec file for package perl-Sys-CPU
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Sys-CPU
Version:        0.61
Release:        0
%define cpan_name Sys-CPU
Summary:        Perl extension for getting CPU information. Currently only number of CPU[cut]
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sys-CPU/
# Source:         http://www.cpan.org/authors/id/M/MZ/MZSANFORD/%{cpan_name}-%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
Patch0:         0001-Add-support-for-cpu_type-on-ARM-and-AArch64-Linux-pl.patch
Patch1:         0002-cpu_clock-can-be-undefined-on-an-ARM.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
In responce to a post on perlmonks.org, a module for counting the number of
CPU's on a system. Support has now also been added for type of CPU and
clock speed. While much of the code is from UNIX::Processors, win32 support
has been added (but not tested).

%prep
%setup -q -n %{cpan_name}-%{version}
%patch0 -p1
%patch1 -p1
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
