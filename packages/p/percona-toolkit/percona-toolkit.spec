#
# spec file for package percona-toolkit
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


%define revision v%{version}

Name:           percona-toolkit
Version:        3.7.1
Release:        0
Summary:        Advanced MySQL and system command-line tools
License:        GPL-2.0-only
Group:          Productivity/Databases/Tools
URL:            https://www.percona.com/software/percona-toolkit/
Source:         https://github.com/percona/percona-toolkit/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        %{name}.conf
Source9:        series
Patch1:         go-build.patch
BuildRequires:  perl(DBD::mysql) >= 3
BuildRequires:  perl(DBI) >= 1.46
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Term::ReadKey) >= 2.10
BuildRequires:  perl(Time::HiRes)
Requires:       perl(DBD::mysql) >= 3
Requires:       perl(DBI) >= 1.46
Requires:       perl(IO::Socket::SSL)
Requires:       perl(Term::ReadKey) >= 2.10
Requires:       perl(Time::HiRes)
Provides:       maatkit = 7410.%{version}
Obsoletes:      maatkit < 7410
BuildRequires:  golang-packaging
BuildRequires:  zstd
BuildRequires:  golang(API)
%{perl_requires}

%description
Percona Toolkit is a collection of advanced command-line tools used by
Percona (http://www.percona.com/) support staff to perform a variety of
MySQL and system tasks that are too difficult or complex to perform manually.

These tools are ideal alternatives to private or "one-off" scripts because
they are professionally developed, formally tested, and fully documented.
They are also fully self-contained, so installation is quick and easy and
no libraries are installed.

Percona Toolkit is developed and supported by Percona Inc.  For more
information and other free, open-source software developed by Percona,
visit http://www.percona.com/software/.

This collection was formerly known as Maatkit.

%prep
%autosetup -p1 -a 1

%build
perl Makefile.PL INSTALLDIRS=vendor < /dev/null
sed -i 's|%{_bindir}/env perl|%{_bindir}/perl|' bin/*
sed -i 's|%{_bindir}/env bash|%{_bindir}/bash|' bin/*
%make_build \
  VERSION=%{version} \
  BUILD_DATE=$(date -u '+%FT%T%z' -d @${SOURCE_DATE_EPOCH}) \
  COMMIT=%{revision} \
  V=1

%install
%perl_make_install
%perl_process_packlist
rm -rf %{buildroot}%{_prefix}/lib
rm -rf %{buildroot}/lib
rm -rf %{buildroot}/%{perl_vendorarch}/auto/%{name}
rm -rf %{buildroot}%{_localstatedir}/adm/perl-modules/%{name}
# a blank configuration file
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/%{name}/
cp -a $(file bin/* | awk -F ':' '/ELF/ {print $1}') %{buildroot}%{_bindir}/

%files
%license COPYING
%doc README.md Changelog
%dir %{_sysconfdir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*.1p.gz
%config %{_sysconfdir}/%{name}/%{name}.conf

%changelog
