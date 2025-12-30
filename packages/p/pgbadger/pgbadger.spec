#
# spec file for package pgbadger
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2013-2015 Lars Vogdt
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%if 0%{?is_opensuse}
%bcond_without jsonxs
%else
%bcond_with jsonxs
%endif

%if 0%{?suse_version} && 0%{?suse_version} < 1500
%bcond_without cron
%else
%bcond_with cron
%endif

Name:           pgbadger
Version:        13.2
Release:        0
License:        MIT
Summary:        A fast PostgreSQL log analyzer
URL:            https://pgbadger.darold.net/
Group:          System/Monitoring
Source0:        https://github.com/darold/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-cron
Source2:        %{name}.timer
Source3:        %{name}.service
Source4:        README.SUSE
BuildRequires:  cron
BuildRequires:  perl
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  perl(Text::CSV_XS)
BuildRequires:  perl(Time::Local)
%if %{with jsonxs}
BuildRequires:  perl(JSON::XS)
%endif
BuildRequires:  sed
Requires:       perl = %{perl_version}
Requires:       perl(Benchmark)
Requires:       perl(Encode)
Requires:       perl(File::Basename)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
Requires:       perl(FileHandle)
Requires:       perl(Getopt::Long)
Requires:       perl(IO::File)
Requires:       perl(IO::Handle)
Requires:       perl(IO::Pipe)
Requires:       perl(Socket)
Requires:       perl(Storable)
Requires:       perl(Text::Wrap)
Requires:       perl(Time::Local)
%{?systemd_ordering}

%if %{with cron}
Recommends:     cron
%endif

# handle package rename at 2023-11-27:
Obsoletes:      PgBadger < %{version}
Provides:       PgBadger = %{version}-%{release}
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
pgBadger is a PostgreSQL log analyzer build for speed with fully detailed
reports from your PostgreSQL log file. It's a single and small Perl script that
aims to replace and outperform the old php script pgFouine.

By the way, we would like to thank Guillaume Smet for all the work he has done
on this really nice tool. We've been using it a long time, it was a really
great tool!

pgBadger is written in pure Perl language. It uses a javascript library to draw
graphs so that you don't need additional Perl modules or any other package to
install. Furthermore, this library gives us more features such as zooming.

pgBadger is able to autodetect your log file format (syslog, stderr or csvlog).
It is designed to parse huge log files as well as gzip compressed file.

%prep
%autosetup -p1
sed -i "s|/usr/bin/env perl|%{_bindir}/perl|g" pgbadger tools/pgbadger_tools
chmod -x tools/pgbadger_tools

%build
perl Makefile.PL
make %{?_smp_mflags}

%if %{with jsonxs}
%check
make test
%endif

%install
%perl_make_install
%perl_process_packlist
rmdir %{buildroot}%{perl_vendorarch} || :
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}%{_unitdir}
mv tools %{buildroot}%{_defaultdocdir}/%{name}/
mv ChangeLog README* %{buildroot}%{_defaultdocdir}/%{name}/
%if %{with cron}
# keep the old behavior for now and install the cron job into the cron directory:
install -Dm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/cron.d/%{name}
%endif
# install the systemd timer and service in /usr/lib/systemd/system:
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}
install -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}
# install the README.SUSE in the documentation dir:
install -m 0644 %{SOURCE4} %{buildroot}%{_defaultdocdir}/%{name}/

%perl_gen_filelist

%pre
%service_add_pre pgbadger.timer pgbadger.service

%post
%service_add_post pgbadger.timer pgbadger.service

%preun
%service_del_preun pgbadger.timer pgbadger.service

%postun
%service_del_postun pgbadger.timer pgbadger.service

%files -f %{name}.files
%license LICENSE
%defattr(-, root, root, -)
%dir %{_defaultdocdir}/%{name}
%dir %{_defaultdocdir}/%{name}/tools
%{_defaultdocdir}/%{name}/*
%{_bindir}/pgbadger
%{_mandir}/man1/pgbadger.1*
%{_unitdir}/%{name}.timer
%{_unitdir}/%{name}.service
%if %{with cron}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%endif

%changelog
