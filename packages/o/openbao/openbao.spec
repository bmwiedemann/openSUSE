#
# spec file for package openbao
#
# Copyright (c) 2024 SUSE LLC
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


%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%define server_service_name openbao.service
%define agent_service_name openbao-agent.service
%define configdir_name openbao
%define statedir_name openbao

Name:           openbao
Version:        2.0.3
Release:        0
Summary:        Manage, store, and distribute sensitive data
License:        MPL-2.0
URL:            https://github.com/openbao/openbao
Group:          Productivity/Security
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source3:        %{name}-agent.service
Source4:        %{name}-agent.hcl.sample
BuildRequires:  go >= 1.22
BuildRequires:  user(openbao)

%description
OpenBao exists to provide a software solution to manage, store, and distribute
sensitive data including secrets, certificates, and keys. The OpenBao community
intends to provide this software under an OSI-approved open-source license, led
by a community run under open governance principles.

A modern system requires access to a multitude of secrets: database
credentials, API keys for external services, credentials for service-oriented
architecture communication, etc. Understanding who is accessing what secrets is
already very difficult and platform-specific. Adding on key rolling, secure
storage, and detailed audit logs is almost impossible without a custom
solution. This is where OpenBao steps in.

The key features of OpenBao are:

* Secure Secret Storage: Arbitrary key/value secrets can be stored in OpenBao.
  OpenBao encrypts these secrets prior to writing them to persistent storage,
  so gaining access to the raw storage isn't enough to access your secrets.
  OpenBao can write to disk, Consul, and more.
* Dynamic Secrets: OpenBao can generate secrets on-demand for some systems,
  such as AWS or SQL databases. For example, when an application needs to
  access an S3 bucket, it asks OpenBao for credentials, and OpenBao will
  generate an AWS keypair with valid permissions on demand. After creating
  these dynamic secrets, OpenBao will also automatically revoke them after the
  lease is up.
* Data Encryption: OpenBao can encrypt and decrypt data without storing it.
  This allows security teams to define encryption parameters and developers to
  store encrypted data in a location such as a SQL database without having to
  design their own encryption methods.
* Leasing and Renewal: All secrets in OpenBao have a lease associated with
  them. At the end of the lease, OpenBao will automatically revoke that secret.
  Clients are able to renew leases via built-in renew APIs.
* Revocation: OpenBao has built-in support for secret revocation. OpenBao can
  revoke not only single secrets, but a tree of secrets, for example, all
  secrets read by a specific user, or all secrets of a particular type.
  Revocation assists in key rolling as well as locking down systems in the case
  of an intrusion.

%package -n %{name}-server
Summary:        OpenBao server
BuildArch:      noarch
Requires:       %{name} = %{version}
# Require the system user and group
Requires(pre):  user(openbao)
Requires(pre):  group(openbao)
# agent and server conflict
Conflicts:      %{name}-agent

%description -n %{name}-server
Files required to run a OpenBao server

%package -n %{name}-agent
Summary:        OpenBao agent
BuildArch:      noarch
Requires:       %{name} = %{version}
# Require the system user and group
Requires(pre):  user(openbao)
Requires(pre):  group(openbao)
# agent and server conflict
Conflicts:      %{name}-server

%description -n %{name}-agent
Files required to run a OpenBao agent

%package -n %{name}-mysql-database-plugin
Summary:        OpenBao database plugin for MySQL

%description -n %{name}-mysql-database-plugin
OpenBao database plugin for MySQL

%package -n %{name}-mysql-legacy-database-plugin
Summary:        OpenBao database plugin for MySQL Legacy

%description -n %{name}-mysql-legacy-database-plugin
OpenBao database plugin for MySQL Legacy

%package -n %{name}-cassandra-database-plugin
Summary:        OpenBao database plugin for Cassandra

%description -n %{name}-cassandra-database-plugin
OpenBao database plugin for Cassandra

%package -n %{name}-influxdb-database-plugin
Summary:        OpenBao database plugin for InfluxDB

%description -n %{name}-influxdb-database-plugin
OpenBao database plugin for InfluxDB

%package -n %{name}-postgresql-database-plugin
Summary:        OpenBao database plugin for PostgreSQL

%description -n %{name}-postgresql-database-plugin
OpenBao database plugin for PostgreSQL

%prep
%autosetup -p 1 -a 1

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

%ifarch i586 armv7hl-suse-linux s390x armv7hl armv7l armv7l:armv6l:armv5tel
CGO_ENABLED=1
%else
CGO_ENABLED=0
%endif

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
    -X github.com/openbao/openbao/version.GitCommit=v%{version} \
    -X github.com/openbao/openbao/version.BuildDate=${BUILD_DATE}" \
   -o bin/openbao .

#
# database plugins
#

go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/mysql-database-plugin ./plugins/database/mysql/mysql-database-plugin

go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/mysql-legacy-database-plugin ./plugins/database/mysql/mysql-legacy-database-plugin

go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/cassandra-database-plugin ./plugins/database/cassandra/cassandra-database-plugin

go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/influxdb-database-plugin ./plugins/database/influxdb/influxdb-database-plugin

go build \
   -mod=vendor \
   -buildmode=pie \
   -o bin/postgresql-database-plugin ./plugins/database/postgresql/postgresql-database-plugin

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# server systemd unit file
install -D -m 0644 .release/linux/package/usr/lib/systemd/system/%{server_service_name} %{buildroot}%{_unitdir}/%{server_service_name}

# fix for https://github.com/openbao/openbao/issues/274
sed -i '/EnvironmentFile/ s/openbao\.d/openbao/' %{buildroot}%{_unitdir}/%{server_service_name}

# agent systemd unit file
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{agent_service_name}

# configuration in /etc/openbao/
install -d -m 0750 %{buildroot}%{_sysconfdir}/%{configdir_name}/
install -D -m 0640 .release/linux/package/etc/%{configdir_name}/%{name}.env %{buildroot}%{_sysconfdir}/%{configdir_name}/%{name}.env
install -D -m 0640 .release/linux/package/etc/%{configdir_name}/%{name}.env %{buildroot}%{_sysconfdir}/%{configdir_name}/%{name}-agent.env

# touch configuration files
touch %{buildroot}%{_sysconfdir}/%{configdir_name}/%{name}.hcl
touch %{buildroot}%{_sysconfdir}/%{configdir_name}/%{name}-agent.hcl

# agent configuration example
cp %{SOURCE4} .

# fix path in sample configuration
cp .release/linux/package/etc/%{configdir_name}/%{name}.hcl %{name}.hcl.sample
sed -i 's|/opt/%{name}|/var/lib/%{name}|g' %{name}.hcl.sample

# directory in /var/lib/
install -d -m 0755 %{buildroot}%{_sharedstatedir}/%{statedir_name}

# database plugins
for plugin in \
        mysql-database-plugin \
        mysql-legacy-database-plugin \
        cassandra-database-plugin \
        influxdb-database-plugin \
        postgresql-database-plugin
do
        install -D -m 0755 bin/${plugin} %{buildroot}/%{_bindir}/%{name}-${plugin}
done

%pre -n %{name}-server
%service_add_pre %{server_service_name}

%pre -n %{name}-agent
%service_add_pre %{agent_service_name}

%post -n %{name}-server
%service_add_post %{server_service_name}

%post -n %{name}-agent
%service_add_post %{agent_service_name}

%preun -n %{name}-server
%service_del_preun %{server_service_name}

%preun -n %{name}-agent
%service_del_preun %{agent_service_name}

%postun -n %{name}-server
%service_del_postun %{server_service_name}

%postun -n %{name}-agent
%service_del_postun %{agent_service_name}

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%files -n %{name}-server
%{_unitdir}/%{server_service_name}
%dir %attr(750,%{name}, %{name}) %{_sysconfdir}/%{configdir_name}/
%defattr(0640, root, %{name})
%config(noreplace) %ghost %{_sysconfdir}/%{configdir_name}/%{name}.hcl
%config(noreplace) %{_sysconfdir}/%{configdir_name}/%{name}.env
%doc %{name}.hcl.sample
%dir %attr(750,%{name}, %{name}) %{_sharedstatedir}/%{statedir_name}/

%files -n %{name}-agent
%{_unitdir}/%{agent_service_name}
%dir %attr(750,%{name}, %{name}) %{_sysconfdir}/%{configdir_name}/
%defattr(0640, root, %{name})
%ghost %{_sysconfdir}/%{configdir_name}/%{name}-agent.hcl
%config(noreplace) %{_sysconfdir}/%{configdir_name}/%{name}-agent.env
%doc %{name}-agent.hcl.sample

%files -n %{name}-mysql-database-plugin
%{_bindir}/%{name}-mysql-database-plugin

%files -n %{name}-mysql-legacy-database-plugin
%{_bindir}/%{name}-mysql-legacy-database-plugin

%files -n %{name}-cassandra-database-plugin
%{_bindir}/%{name}-cassandra-database-plugin

%files -n %{name}-influxdb-database-plugin
%{_bindir}/%{name}-influxdb-database-plugin

%files -n %{name}-postgresql-database-plugin
%{_bindir}/%{name}-postgresql-database-plugin

%changelog
