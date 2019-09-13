#
# spec file for package check_postgres
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           check_postgres
Version:        2.24.0
Release:        0
Summary:        Postgres monitoring script
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://bucardo.org/wiki/Check_postgres
Source:         https://github.com/bucardo/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        nagios-commands-postgres.cfg
Source2:        create_manpage.pl
BuildRequires:  nagios-rpm-macros
BuildRequires:  perl-macros
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Time::HiRes)
Requires:       perl = %{perl_version}
Requires:       postgresql
Requires:       perl(Cwd)
Requires:       perl(Data::Dumper)
Requires:       perl(File::Basename)
Requires:       perl(File::Temp)
Requires:       perl(Getopt::Long)
Requires:       perl(Time::HiRes)
Recommends:     coreutils
Recommends:     util-linux
Recommends:     perl(Date::Parse)
Recommends:     perl(Digest::MD5)
BuildArch:      noarch

%description
check_postgres.pl is a Perl script that runs many different tests against one
or more Postgres databases. It uses the psql program to gather the information,
and outputs the results in one of three formats: Nagios, MRTG, or simple.

%package -n monitoring-plugins-postgres
Summary:        Postgres monitoring script using check_postgres.pl
# FIXME: use proper Requires(pre/post/preun/...)
Group:          System/Monitoring
PreReq:         %{name} = %{version}
Provides:       nagios-plugins-postgres = %{version}-%{release}
Obsoletes:      nagios-plugins-postgres < %{version}-%{release}

%description -n monitoring-plugins-postgres
This package contains the symlinks to execute special checks via the standard
monitoring plugins way.

%prep
%setup -q
install -m 0644 %{SOURCE1} nagios-commands-postgres.cfg

%build
perl Makefile.PL
make %{?_smp_mflags}

%install
# install the module
%perl_make_install
# do not perl_process_packlist (noarch)
# remove .packlist file
rm -rf %{buildroot}%{perl_vendorarch}
# remove perllocal.pod file
rm -rf %{buildroot}%{perl_archlib}
%perl_gen_filelist
# create symlinks for monitoring-plugins-postgres package
mkdir -p %{buildroot}%{nagios_plugindir}
pushd %{buildroot}%{nagios_plugindir}
%{buildroot}%{_bindir}/check_postgres.pl --symlinks
# fix symlinks, as they point to the buildroot
for link in *; do
	rm "$link"
	ln -s "%{_bindir}/check_postgres.pl" "$link"
done
popd
# create man page
mkdir -p %{buildroot}/%{_mandir}/man1
perl %{SOURCE2} "%{version}" "1" check_postgres.pl > %{buildroot}/%{_mandir}/man1/check_postgres.pl.1

%files -f %{name}.files
%doc MANIFEST README* TODO nagios-commands-postgres.cfg check_postgres.pl.html
%if 0%{?suse_version} > 1315
%license LICENSE
%else
%doc LICENSE
%endif
%{_mandir}/man1/check_postgres.pl.1%{?ext_man}

%files -n monitoring-plugins-postgres
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%{nagios_plugindir}/*

%changelog
