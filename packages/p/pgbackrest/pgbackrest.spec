#
# spec file for package pgbackrest
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019-2022 Ioda-Net Sàrl, Charmoille, Switzerland.
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


%define services pgbackrest.target pgbackrest-diff@.service pgbackrest-full@.service pgbackrest-incr@.service pgbackrest.service pgbackrest-diff@.timer pgbackrest-full@.timer pgbackrest-incr@.timer

Name:           pgbackrest
Version:        2.43
Release:        0
Summary:        Reliable PostgreSQL Backup & Restore
License:        MIT
Group:          Productivity/Databases/Tools
URL:            http://www.pgbackrest.org
Source:         https://github.com/%{name}/%{name}/archive/release/%{version}/%{name}-%{version}.tar.gz
Source1:        pgbackrest.conf

Source10:       pgbackrest-diff@.service
Source11:       pgbackrest-diff@.timer
Source12:       pgbackrest-full@.service
Source13:       pgbackrest-full@.timer
Source14:       pgbackrest-incr@.service
Source15:       pgbackrest-incr@.timer
Source16:       pgbackrest.service
Source17:       pgbackrest.target
Source18:       pgbackrest.tmpfiles.d

Source98:       README.SUSE
Source99:       series

Patch0:         libpq-fe.h_localisation.patch
Patch1:         use-run-pgbackrest.patch
BuildRequires:  libyaml-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(liblz4)
%endif
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libxml-2.0)
%if 0%{?is_opensuse} || 0%{?sle_version} >= 150100
BuildRequires:  pkgconfig(libzstd)
%endif
BuildRequires:  pkgconfig(systemd)

# This is a bit awkward as we only need this for directory ownership
Requires(pre):  postgresql-server

%description
pgBackRest aims to be a simple, reliable backup and restore system for
PostgreSQL that can seamlessly scale up to the largest databases and
workloads.

The following features are available:
- Parallel backup & restore
- Local or remote operation
- Full, incremental, differential backups
- Backup rotation & archive expiration
- Backup integrity
- Page checksums
- Backup resume
- Streaming compression & checksums
- Delta restore
- Parallel, asynchronous WAL push & get
- Tablespace & link support
- Amazon S3 support
- Encryption
- Compatibility with PostgreSQL >= 8.3

%prep
%autosetup -p1 -n %{name}-release-%{version}

%build
cp %{SOURCE98} .
pushd src
%configure
# make_build doesn't work on sle12, as long we want to support that we can not use the macro here
make %{?_smp_mflags}
popd

%install
%make_install -C src

install -D -d -m 0700                         \
  %{buildroot}%{_localstatedir}/lib/%{name}   \
  %{buildroot}%{_localstatedir}/log/%{name}   \
  %{buildroot}%{_localstatedir}/spool/%{name}

install -D -d -m 0755        \
  %{buildroot}%{_sysconfdir} \
  %{buildroot}%{_unitdir}

install -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name}.conf
install -m 0644 \
    %{SOURCE10} \
    %{SOURCE11} \
    %{SOURCE12} \
    %{SOURCE13} \
    %{SOURCE14} \
    %{SOURCE15} \
    %{SOURCE16} \
    %{SOURCE17} \
  %{buildroot}%{_unitdir}

install -D -m 0644 \
    %{SOURCE18} \
    %{buildroot}%{_tmpfilesdir}/%{name}.conf

%check
# Tests are only available with Vagrant
# We just test that the binary works.
%{buildroot}/%{_bindir}/%{name} version || exit 1

%pre
%service_add_pre %{services}

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{services}

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%files
%doc README.md README.SUSE
%license LICENSE
%config(noreplace) %attr (640,root,postgres) %{_sysconfdir}/%{name}.conf
# We still can do that as postgres user is system fixed
%attr(-,postgres,postgres) %{_localstatedir}/log/%{name}
%attr(-,postgres,postgres) %{_localstatedir}/lib/%{name}
%attr(-,postgres,postgres) %{_localstatedir}/spool/%{name}
%ghost %dir %attr(750,postgres,postgres) /run/pgbackrest
%{_bindir}/%{name}
%{_unitdir}/pgbackrest-diff@.service
%{_unitdir}/pgbackrest-diff@.timer
%{_unitdir}/pgbackrest-full@.service
%{_unitdir}/pgbackrest-full@.timer
%{_unitdir}/pgbackrest-incr@.service
%{_unitdir}/pgbackrest-incr@.timer
%{_unitdir}/pgbackrest.service
%{_unitdir}/pgbackrest.target
%{_tmpfilesdir}/%{name}.conf

%changelog
