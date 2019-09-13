#
# spec file for package mongodb
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


%define _home_dir       %{_var}/lib/%{name}
%define _mongodb_user     %{name}
%define _mongodb_group    %{name}
%if 0%{?suse_version} > 1220
    %bcond_without systemd
%else
    %bcond_with systemd
%endif
%if %{?suse_version} >= 1500
%define scons_bin %{_bindir}/scons
%else
%define scons_bin buildscripts/scons.py
%endif
Name:           mongodb
Version:        3.6.13
Release:        0
Summary:        The MongoDB document-oriented database system (metapackage)
License:        AGPL-3.0-only
Group:          Productivity/Databases/Servers
URL:            http://www.mongodb.org
Source0:        https://fastdl.mongodb.org/src/mongodb-src-r%{version}.tar.gz
Source1:        mongodb.init
Source2:        mongodb.logrotate
Source3:        mongodb.conf
Source4:        mongodb.service
Source5:        mongodb-tmpfile
Patch0:         mongo-src-3.6.8-python3.patch
Patch1:         mongodb-3.6.8-fix-syntax.patch
BuildRequires:  glibc-devel
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  scons >= 2.3
BuildRequires:  snappy-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(yaml-cpp)
Requires:       logrotate
Requires:       mongodb-mongoperf = %{version}
Requires:       mongodb-mongos = %{version}
Requires:       mongodb-server = %{version}
Requires:       mongodb-shell = %{version}
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Conflicts:      mongo-10gen-enterprise
Conflicts:      mongodb-enterprise
Conflicts:      mongodb-enterprise-unstable
Conflicts:      mongodb-org
Conflicts:      mongodb-org-unstable
ExcludeArch:    i586 ppc
# MongoDB (upstream) does NOT support PPC, PPC64 or PPC64LE
# on the 3.0.X series.
#
# MongoDB specifically recommends NOT
# building and using mongodb on PPC, including
# PPC64 and PPC64LE because it may, among
# other things, corrupt data. Compiling pure upstream
# mongodb also fails on PPC, PPC64 and PPC64LE.
#
# MongoDB is working and plans to support PPC64 and PPC64LE
# in the future.
#
# Leave PPC lines in spec file to make it (much) easier to enable
# PPC building when updating mongodb to newer version
# since they have been known to work and have been suggested by upstream
ExcludeArch:    ppc64 ppc64le
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
%endif
%if 0%{?sle_version} == 120200 || 0%{?sle_version} == 120300
BuildRequires:  gcc6
BuildRequires:  gcc6-c++
%else
BuildRequires:  gcc-c++ >= 5.3
%endif
%if 0%{?suse_version} >= 1500
BuildRequires:  python3-Cheetah3
BuildRequires:  python3-PyYAML
BuildRequires:  python3-regex
BuildRequires:  python3-setuptools
%else
BuildRequires:  python-Cheetah
BuildRequires:  python-PyYAML
BuildRequires:  python-regex
BuildRequires:  python-setuptools
BuildRequires:  python-typing
%endif
%ifarch ppc64 ppc64le
BuildRequires:  gperftools-devel
%endif
%if %{with systemd}
BuildRequires:  systemd
%{?systemd_requires}
%else
Requires(post): %insserv_prereq
Requires(pre):  %fillup_prereq
Requires(pre):  %insserv_prereq
%endif

%description
MongoDB is a document-oriented database program. Classified as a
NoSQL database program, MongoDB uses JSON-like documents with
schemas. It has auto-sharding, built-in replication, TTL indexes,
text search as well as an aggregation framework and native MapReduce.

This metapackage will install the mongo shell, import/export tools,
other client utilities, server software, default configuration, and
init.d scripts.

%package server
Summary:        Document-oriented database server
Group:          Productivity/Databases/Servers
Requires:       openssl
Requires:       shadow
Conflicts:      mongo-10gen-enterprise-server
Conflicts:      mongodb-enterprise-server
Conflicts:      mongodb-enterprise-unstable-server
Conflicts:      mongodb-org-server
Conflicts:      mongodb-org-unstable-server

%description server
MongoDB is a document-oriented database program. Classified as a
NoSQL database program, MongoDB uses JSON-like documents with
schemas. It has auto-sharding, built-in replication, TTL indexes,
text search as well as an aggregation framework and native MapReduce.

This package contains the MongoDB server software, default
configuration files, and service scripts.

%package shell
Summary:        MongoDB shell client
Group:          Productivity/Databases/Clients
Requires:       mongodb-server = %{version}
Requires:       openssl
Conflicts:      mongo-10gen-enterprise-shell
Conflicts:      mongodb-enterprise-shell
Conflicts:      mongodb-enterprise-unstable-shell
Conflicts:      mongodb-org-shell
Conflicts:      mongodb-org-unstable-shell

%description shell
MongoDB is a document-oriented database program. Classified as a
NoSQL database program, MongoDB uses JSON-like documents with
schemas. It has auto-sharding, built-in replication, TTL indexes,
text search as well as an aggregation framework and native MapReduce.

This package contains the mongo shell.

%package mongos
Summary:        MongoDB sharded cluster query router
Group:          Productivity/Databases/Tools
Conflicts:      mongo-10gen-enterprise-mongos
Conflicts:      mongodb-enterprise-mongos
Conflicts:      mongodb-enterprise-unstable-mongos
Conflicts:      mongodb-org-mongos
Conflicts:      mongodb-org-unstable-mongos

%description mongos
MongoDB is a document-oriented database program. Classified as a
NoSQL database program, MongoDB uses JSON-like documents with
schemas. It has auto-sharding, built-in replication, TTL indexes,
text search as well as an aggregation framework and native MapReduce.

This package contains mongos, the MongoDB sharded cluster query router.

%package mongoperf
Summary:        MongoDB utility to check disk I/O performance
Group:          Productivity/Databases/Tools
Conflicts:      mongo-10gen-enterprise-mongoperf
Conflicts:      mongodb-enterprise-mongoperf
Conflicts:      mongodb-enterprise-unstable-mongoperf
Conflicts:      mongodb-org-mongoperf
Conflicts:      mongodb-org-unstable-mongoperf

%description mongoperf
MongoDB is a document-oriented database program. Classified as a
NoSQL database program, MongoDB uses JSON-like documents with
schemas. It has auto-sharding, built-in replication, TTL indexes,
text search as well as an aggregation framework and native MapReduce.

This package contains mongoperf.

%prep
%setup -q -n mongodb-src-r%{version}
%if %{?suse_version} >= 1500
%patch0 -p1
%endif
%patch1 -p1

# change default database path to reflect the default database user directory
sed -i 's|/data/db/|%{_home_dir}/|' src/mongo/db/storage/storage_options.cpp

%build
%{scons_bin} \
%ifarch aarch64
    CCFLAGS="-march=armv8-a+crc" \
%endif
%if 0%{?sle_version} == 120200 || 0%{?sle_version} == 120300
    CC=%{_bindir}/gcc-6 CXX=%{_bindir}/g++-6 \
%endif
    core \
    %{?_smp_mflags} \
    --disable-warnings-as-errors \
    --nostrip \
    --ssl \
%ifarch x86_64  aarch64
    --wiredtiger=on \
%else
    --wiredtiger=off \
    --mmapv1=on \
%endif
%ifarch ppc64 ppc64le
    --js-engine=none \
    --allocator=system \
%endif
%if 0%{?suse_version} >= 1500
    --use-system-boost \
%endif
    --use-system-pcre \
    --use-system-snappy \
    --use-system-yaml \
    --use-system-zlib \

%install
%{scons_bin} \
%ifarch aarch64
    CCFLAGS="-march=armv8-a+crc" \
%endif
%if 0%{?sle_version} == 120200 || 0%{?sle_version} == 120300
    CC=%{_bindir}/gcc-6 CXX=%{_bindir}/g++-6 \
%endif
    install --prefix=%{buildroot}%{_prefix} \
    --disable-warnings-as-errors \
    --nostrip \
    --ssl \
%ifarch x86_64  aarch64
    --wiredtiger=on \
%else
    --wiredtiger=off \
    --mmapv1=on \
%endif
%ifarch ppc64 ppc64le
    --js-engine=none \
    --allocator=system \
%endif
%if 0%{?suse_version} >= 1500
    --use-system-boost \
%endif
    --use-system-pcre \
    --use-system-snappy \
    --use-system-yaml \
    --use-system-zlib \

mkdir -p %{buildroot}%{_sbindir}
mv %{buildroot}%{_bindir}/mongod %{buildroot}%{_sbindir}/mongod
mv %{buildroot}%{_bindir}/mongos %{buildroot}%{_sbindir}/mongos

mkdir -p %{buildroot}%{_var}/log/mongodb
mkdir -p %{buildroot}%{_var}/lib/mongodb

%if %{with systemd}
    install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}.service
    install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_sbindir}/rc%{name}
    install -d -m 0755 %{buildroot}%{_tmpfilesdir}/
    install -D -p -m 0644 %{SOURCE5} %{buildroot}%{_tmpfilesdir}/%{name}.conf
%else
    install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/%{name}
    ln -sf %{_initddir}/%{name} %{buildroot}%{_sbindir}/rc%{name}
    mkdir -p %{buildroot}/run/%{pkg_name}
%endif

install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/%{name}.conf

mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 0644 debian/mongod.1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 debian/mongoperf.1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 debian/mongos.1 %{buildroot}%{_mandir}/man1/
install -p -m 0644 debian/mongo.1 %{buildroot}%{_mandir}/man1/

%pre server
if ! %{_bindir}/id -g %{_mongodb_group} &>/dev/null; then
    %{_sbindir}/groupadd -r %{_mongodb_group}
fi
if ! %{_bindir}/id %{_mongodb_user} &>/dev/null; then
    %{_sbindir}/useradd -M -r -g %{_mongodb_group} \
        -d %{_home_dir} -s /bin/false \
        -c "MongoDB database admin" %{_mongodb_user} > /dev/null 2>&1
fi

%if %{with systemd}
    %{service_add_pre %{name}.service}
%endif

%post server
/sbin/ldconfig
%if %{with systemd}
    %tmpfiles_create %{_tmpfilesdir}/%{name}.conf
    %{service_add_post %{name}.service}
%else
    %{fillup_and_insserv -f %{name}}
%endif

%preun server
%if %{with systemd}
    %{service_del_preun %{name}.service}
%else
    %{stop_on_removal %{name}}
%endif

%postun server
/sbin/ldconfig
%if %{with systemd}
    %{service_del_postun %{name}.service}
%else
    %{restart_on_update %{name}}
    %insserv_cleanup
%endif

%files

%files server
%{_sbindir}/mongod
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_sbindir}/rc%{name}
%{_mandir}/man1/mongod.1%{?ext_man}

%if %{with systemd}
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/%{name}.conf
%ghost %dir /run/%{name}
%else
%{_sysconfdir}/init.d/%{name}
%endif
%attr(0750,mongodb,mongodb) %{_var}/log/%{name}
%attr(0750,mongodb,mongodb) %{_var}/lib/%{name}

%files shell
%{_bindir}/mongo
%{_bindir}/install_compass
%{_mandir}/man1/mongo.1%{?ext_man}

%files mongos
%{_sbindir}/mongos
%{_mandir}/man1/mongos.1%{?ext_man}

%files mongoperf
%{_bindir}/mongoperf
%{_mandir}/man1/mongoperf.1%{?ext_man}

# TODO:
# * /var/lib/[mongodb] is NOT a subvolume in default BTRFS setup,
# which means system snapper snapshots will include mongodb database files!
# this is an issue with any database that's not PostgreSQL

%changelog
