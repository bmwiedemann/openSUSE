#
# spec file for package kafka
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


# The scala version this package gets compiled for.
%define scala_version 2.11
%define username kafka
%define groupname kafka
%define src_install_dir /usr/src/%{name}

Name:           kafka
Version:        2.1.0
Release:        0
Summary:        Apache Kafka Server
License:        Apache-2.0
Group:          Productivity/Networking/Other
Url:            http://kafka.apache.org
Source0:        %{name}-%{version}.tar.xz
Source1:        build.sh
Source2:        kafka-wrapper
Source3:        %{name}.conf
Source4:        %{name}.service
Source5:        %{name}-zookeeper.service
Source6:        README.SUSE
Source7:        BUILD
Source8:        WORKSPACE
# PATCH-FIX-OPENSUSE rotate-gc-log.patch
Patch0:         rotate-gc-log.patch
# PATCH-FIX-OPENSUSE lock-down-jmxremote.patch
Patch1:         lock-down-jmxremote.patch
ExclusiveArch:  x86_64
BuildRequires:  java-1_8_0-openjdk
# Only required for Gradle build
BuildRequires:  java-1_8_0-openjdk-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# If you update Kafka, you will probably need to regenerate kafka-kit. At the
# very least you will need to bump its version. Refer to to the README.updating
# file in the kafka-kit package for instructions on rebuilding it.
BuildRequires:  kafka-kit == %{version}
BuildRequires:  openstack-suse-macros
BuildRequires:  tar
BuildRequires:  xz
BuildRequires:  systemd-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Requires(pre):  pwdutils

%package doc
Summary:        Apache Kafka Documentation
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description doc
Documentation for the Kafka distributed streaming platform.

%package zookeeper
Summary:        Zookeeper server for testing Kafka
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description zookeeper
This package contains a single node Zookeeper cluster for testing Kafka. This
is not meant for production use, only for testing.

%package source
Summary:        Source code of Apache Kafka

%description source
Source code of the Kafka distributed streaming platform.

%description
The %{name} package contains the Kafka distributed streaming platform.

%prep
%setup -q
pushd bin
for f in {connect,zookeeper}-*
  do
  mv $f "kafka-${f}"
  done
popd
%patch0
%patch1

%build

export KIT=%{_datadir}/tetra
sh %{SOURCE1}
pushd core/build/distributions/
tar -xzf %{name}_%{scala_version}-%{version}.tgz
popd

%pre
%openstack_pre_user_group_create %{username} %{groupname}
%service_add_pre %{name}.service

%pre zookeeper
%service_add_pre %{name}-zookeeper.service

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.service

%post zookeeper
%service_add_post %{name}-zookeeper.service

%preun
%service_del_preun %{name}.service

%preun zookeeper
%service_del_preun %{name}-zookeeper.service

%postun
%service_del_postun %{name}.service

%postun zookeeper
%service_del_postun %{name}-zookeeper.service

%install
# systemd units
mkdir -p %{buildroot}%{_sbindir} %{buildroot}%{_unitdir}
install -p -D -m 444 %{SOURCE4} %{buildroot}%{_unitdir}/
install -p -D -m 444 %{SOURCE5} %{buildroot}%{_unitdir}/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-zookeeper

# Directories
install -D -m 644 %{SOURCE3} %{buildroot}/%_tmpfilesdir/%name.conf
install -d -m 755 %{buildroot}%{_libdir}/%{name}
install -d -m 755 %{buildroot}%{_libdir}/%{name}/bin
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}
install -d -m 755 %{buildroot}%{_libdir}/%{name}/libs
install -d -m 755 %{buildroot}%{_docdir}/%{name}
install -d -m 755 %{buildroot}%{_bindir}

# Documentation
mkdir %{buildroot}%{_docdir}/%{name}/site-docs
cp -a docs/ %{buildroot}%{_docdir}/%{name}/site-docs
sed -e 's#__CONFDIR__#%{_sysconfdir}/%{name}#g' \
    -e 's#__LIBDIR__#%{_libdir}#g' \
    %{SOURCE6} > README.SUSE

# Wrapper for executables
install -m 755 %{SOURCE2} %{buildroot}%{_libdir}/%{name}/bin/kafka-wrapper
sed -i 's#__KAFKABIN__#%{_libdir}/%{name}/bin#g' %{buildroot}%{_libdir}/%{name}/bin/kafka-wrapper

### Distribution tarball contents

pushd core/build/distributions/%{name}_%{scala_version}-%{version}

# Executables
install -m 755 bin/*.sh %{buildroot}%{_libdir}/%{name}/bin

for f in %{buildroot}%{_libdir}/%{name}/bin/kafka-*
  do
  ln -sr %{buildroot}%{_libdir}/%{name}/bin/kafka-wrapper %{buildroot}%{_bindir}/$(basename $f)
  done

# Jars
install -m 644 libs/* %{buildroot}%{_libdir}/%{name}/libs

# Configuration
install -m 640 config/* %{buildroot}%{_sysconfdir}/%{name}
ln -sr %{buildroot}%{_sysconfdir}/%{name} %{buildroot}%{_libdir}/%{name}/config

mkdir -p %{buildroot}%{_localstatedir}/log/%{name}

popd

# Install sources and Bazel configuration files
mkdir -p %{buildroot}%{src_install_dir}
tar -xf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
cp %{SOURCE7} %{SOURCE8} %{buildroot}%{src_install_dir}

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/%{name}
%attr(0755, kafka, kafka) %dir %{_localstatedir}/log/%{name}
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/connect-console-sink.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/connect-console-source.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/connect-distributed.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/connect-file-sink.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/connect-file-source.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/connect-log4j.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/connect-standalone.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/consumer.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/producer.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/trogdor.conf
%config(noreplace) %attr(0640, root, kafka) %{_sysconfdir}/%{name}/log4j.properties
%config(noreplace) %attr(0640, root, kafka) %{_sysconfdir}/%{name}/server.properties
%config %attr(0640, root, kafka) %{_sysconfdir}/%{name}/tools-log4j.properties
%license LICENSE
%doc NOTICE
%doc README.SUSE
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
# SLE 12 SP2 the package needs to own this directory
%if 0%{?sle_version} == 120200 && !0%{?is_opensuse} 
%dir %_tmpfilesdir
%endif
%_tmpfilesdir/%name.conf
%{_libdir}/%{name}
%{_bindir}/kafka-broker-api-versions.sh
%{_bindir}/kafka-connect-distributed.sh
%{_bindir}/kafka-connect-standalone.sh
%{_bindir}/kafka-acls.sh
%{_bindir}/kafka-configs.sh
%{_bindir}/kafka-console-consumer.sh
%{_bindir}/kafka-console-producer.sh
%{_bindir}/kafka-consumer-groups.sh
%{_bindir}/kafka-consumer-perf-test.sh
%{_bindir}/kafka-mirror-maker.sh
%{_bindir}/kafka-preferred-replica-election.sh
%{_bindir}/kafka-producer-perf-test.sh
%{_bindir}/kafka-reassign-partitions.sh
%{_bindir}/kafka-replica-verification.sh
%{_bindir}/kafka-run-class.sh
%{_bindir}/kafka-server-start.sh
%{_bindir}/kafka-server-stop.sh
%{_bindir}/kafka-streams-application-reset.sh
%{_bindir}/kafka-topics.sh
%{_bindir}/kafka-verifiable-consumer.sh
%{_bindir}/kafka-verifiable-producer.sh
%{_bindir}/kafka-delegation-tokens.sh
%{_bindir}/kafka-delete-records.sh
%{_bindir}/kafka-dump-log.sh
%{_bindir}/kafka-log-dirs.sh
%{_bindir}/kafka-wrapper

%files zookeeper
%defattr(-,root,root)
%license LICENSE
%doc NOTICE
%doc README.SUSE
%attr(0640, root, kafka) %config %{_sysconfdir}/%{name}/zookeeper.properties
%{_unitdir}/%{name}-zookeeper.service
%{_sbindir}/rc%{name}-zookeeper
%{_bindir}/kafka-zookeeper-security-migration.sh
%{_bindir}/kafka-zookeeper-server-start.sh
%{_bindir}/kafka-zookeeper-server-stop.sh
%{_bindir}/kafka-zookeeper-shell.sh
%dir %{_localstatedir}/log/%{name}
%attr(0755, kafka, kafka) %{_localstatedir}/log/%{name}

%files doc
%defattr(-,root,root)
%license LICENSE
%doc NOTICE
# Leap 15.0+ and Tumbleweed need this directory declared explicitly. In Leap
# >= 42.3 and SLE, the docdir macro implies this declaration already.
%if 0%{?is_opensuse} && ( 0%{?sle_version} > 120300 || 0%{?suse_version} > 1500 )
%{_docdir}/%{name}/site-docs
%endif
%docdir %{_docdir}/%{name}/site-docs

%files source
%defattr(-,root,root)
%{src_install_dir}

%changelog
