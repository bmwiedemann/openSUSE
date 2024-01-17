#
# spec file for package perl-Devel-Leak
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


Name:           perl-Devel-Leak
%define cpan_name Devel-Leak
Summary:        Utility for looking for perl objects that are not reclaimed
License:        GPL-1.0 or Artistic-1.0
Group:          Development/Libraries/Perl
Version:        0.03
Release:        0
Url:            http://search.cpan.org/~ni-s/Devel-Leak-0.03
Source:         %{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description

 %{cpan_name} module for perl
  Devel::Leak has two functions NoteSV and CheckSV.
  NoteSV walks the perl internal table of allocated SVs (scalar values)
   - (which actually contains arrays and hashes too),
   and records their addresses in a table. It returns a count of these "things",
   and stores a pointer to the table (which is obtained from the heap
   using malloc()) in its argument.
  CheckSV is passed argument which holds a pointer to a table created by NoteSV.
   It re-walks the perl-internals and calls sv_dump() for any "things"
   which did not exist when NoteSV was called.
   It returns a count of the number of "things" now allocated.
  Author:	Nick Ing-Simmons <nick@ni-s.u-net.com>

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%clean 
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
# normally you only need to check for doc files
%defattr(-,root,root)
%doc README

%changelog
