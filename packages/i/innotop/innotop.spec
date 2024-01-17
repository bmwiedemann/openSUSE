#
# spec file for package innotop
#
# Copyright (c) 2021 SUSE LLC
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


Name:           innotop
Version:        1.13.0
Release:        0
Summary:        A MySQL and InnoDB monitor program
License:        GPL-2.0-only
Group:          Productivity/Databases/Tools
URL:            https://github.com/innotop/innotop/
Source0:        https://github.com/innotop/innotop/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(Time::HiRes)
Requires:       perl(DBD::mysql)
Requires:       perl(DBI)
Requires:       perl(File::Basename)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(List::Util)
Requires:       perl(Term::ReadKey)
Requires:       perl(Time::HiRes)
BuildArch:      noarch
%if 0%{?suse_version} < 1140
Requires:       perl = %{perl_version}
%else
%{perl_requires}
%endif

%description
Innotop is a powerful "top" clone for MySQL. It connects to a MySQL database server
and retrieves information from it, then displays it in a manner similar to the UNIX
top program. Innotop uses the data from SHOW VARIABLES, SHOW GLOBAL STATUS, SHOW FULL
PROCESSLIST, and SHOW ENGINE INNODB STATUS, among other things.

%prep
%setup -q

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*

%check
%make_build test

%files
%license COPYING LICENSE
%doc Changelog
%{_bindir}/innotop
%{_mandir}/man1/innotop.1%{?ext_man}

%changelog
