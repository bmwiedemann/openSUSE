#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == "client"
%define build_client 1
%define build_server 0
%define build_kafka_humio_gateway 0
%define name_suffix -client
%define make_target linux_bare
%define config_perms %attr(0600, root, root)
%define state_dir_perms %attr(0700, root, root)
%else
%define build_kafka_humio_gateway 1
%define build_server 1
%define build_client 0
%define name_suffix %{nil}
%define make_target linux
%define config_perms %attr(0640, root, velociraptor)
%define state_dir_perms %attr(0700, velociraptor, velociraptor)
%endif

%define projname velociraptor
%define vendor_version 0.6.7.5~git77.997aa73
%define vmlinux_h_version 5.14.21150400.22-150400-default

# SLE 15 SP2 / Leap 15.2 or newer gets eBPF
# Earlier versions don't have a usable eBPF and the
# release doesn't easily build llvm13
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%bcond_without bpf
%else
%bcond_with bpf
%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

# SLE12 has _sharedstatedir in an odd place
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
%define _sharedstatedir /var/lib
%endif

Name:           velociraptor%{name_suffix}
Version:        0.6.7.5~git78.2bef6fc
Release:        0
%if %{build_server}
Summary:        Endpoint visibility and collection tool
%else
Summary:        Endpoint visibility and collection tool (endpoint only)
%endif
Group:          System/Monitoring
License:        AGPL-3.0-only
URL:            https://github.com/Velocidex/velociraptor
Source:         %{projname}-%{version}.tar.xz
Source1:        vendor-golang-%{vendor_version}.tar.xz
Source2:        vendor-golang-kafka-humio-gateway-%{vendor_version}.tar.xz
Source3:        vendor-nodejs-%{vendor_version}.tar.xz
Source4:        vmlinux.h-%{vmlinux_h_version}.tar.xz
Source5:        velociraptor.service
Source6:        velociraptor-server.config.placeholder
Source7:        velociraptor-client.service
Source8:        velociraptor-client.config.placeholder
Source9:        update-vendoring.sh
Source10:       sysconfig.velociraptor
Source11:       sysconfig.velociraptor-client
Source12:       %{projname}.obsinfo
Source13:       system-user-velociraptor.sysusers
Source14:       velociraptor-kafka.sysusers
Source15:       velociraptor-kafka-humio-gateway.service
Source16:       sysconfig.velociraptor-kafka-humio-gateway
Patch1:         velociraptor-golang-mage-vendoring.diff
Patch2:         vendor-build-fixes-for-SLE12.patch
Patch3:         sdjournal-build-fix-for-SLE12.patch
Patch4:         velociraptor-reproducible-timestamp.diff
BuildRequires:  fileb0x
BuildRequires:  golang-packaging
BuildRequires:  mage
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.18
BuildRequires:  pkgconfig(libsystemd)
%if %{build_server}
BuildRequires:  nodejs >= 16
BuildRequires:  npm >= 16
%endif
%if %{with bpf}
# clang15 causes libbpfgo to crash immediately
BuildRequires:  clang16
BuildRequires:  libelf-devel
BuildRequires:  libzstd-devel
BuildRequires:  libzstd-devel
BuildRequires:  llvm16
BuildRequires:  zlib-devel
%endif
Requires:       group(velociraptor)
Requires:       user(velociraptor)
ExclusiveArch:  x86_64 ppc64le aarch64 s390x
%if %{build_server}
BuildRequires:  sysuser-tools
%{?sysusers_requires}
%endif

%if %{build_server}
%description
Velociraptor is a tool for collecting host based state information
using The Velociraptor Query Language (VQL) queries.

To learn more about Velociraptor, read the documentation on:

https://docs.velociraptor.app/

This package contains the velociraptor server and full console GUI.
For just the endpoint agent, please install the 'velociraptor-client' package.

%package -n system-user-velociraptor
Summary:        System user and group 'velociraptor'
Version:        1.0.0
License:        Apache-2.0
Group:          System/Monitoring
Provides:       group(velociraptor)
Provides:       user(velociraptor)

%description -n system-user-velociraptor
This package provides a shared system user for all velociraptor components

%endif

%if %{build_kafka_humio_gateway}
%package kafka-humio-gateway
Summary:        Gateway between Kafka and Humio for Velociraptor Artifacts
Version:        0.6.7.5~git78.2bef6fc
Requires:       group(velociraptor-kafka)
Requires:       user(velociraptor-kafka)

%description kafka-humio-gateway
This tool is used to consume events generated by the Kafka Velociraptor plugin
and post them to a Humio cluster.
%endif

%if %{build_client}
%description
Velociraptor is a tool for collecting host based state information
using The Velociraptor Query Language (VQL) queries.

To learn more about Velociraptor, read the documentation on:

https://docs.velociraptor.app/

This package contains only the endpoint agent.  For the full server and GUI
console, please install the 'velociraptor' package.
%endif

%prep
%setup -q -a 1 -a 2 -a 3 -a 4 -n %{projname}-%{version}
%autopatch -p1

# Set the version to something more specific than <next-tag>-dev
sed -ie "s/\(VERSION *= \).*/\1 \"%{version}\"/" constants/constants.go

%if %{with bpf}
mkdir -p third_party/libbpfgo/output

cp vmlinux.h-%{vmlinux_h_version}/vmlinux-%{_arch}.h \
   third_party/libbpfgo/output/vmlinux.h
%endif

# These just clutter the GUI and we don't have Windows clients
# Note: There are dependencies on these that need to be resolved before
# removing them outright.
# rm -rf artifacts/definitions/Windows

%build

# Reproductible builds need stable timestamps
timestamp=$(date -Iseconds --utc --date=@$(grep mtime: %{SOURCE12}|sed -e 's/mtime: //'))
git_commit=$(grep commit: %{SOURCE12}|sed -e 's/commit: //g')

export VELOCIRAPTOR_BUILD_TIME=$timestamp
export VELOCIRAPTOR_GIT_HEAD=$git_commit

%if %{build_server}
(cd gui/velociraptor ; npm run build)
%sysusers_generate_pre %{SOURCE13} velociraptor-user
%endif

make %{make_target} BUILD_LIBBPFGO=%{with bpf} GIT=echo

%if %{build_kafka_humio_gateway}
(cd contrib/kafka-humio-gateway; go build -o %{name}-kafka-humio-gateway)
%sysusers_generate_pre %{SOURCE16} kafka-user
%endif

%install
install -D -d -m 0750 %buildroot/%{_sysconfdir}/velociraptor
install -D -d -m 0700 %buildroot/%{_sharedstatedir}/%{name}/data
install -D -d -m 0700 %buildroot/%{_sharedstatedir}/%{name}/logs
install -D -d -m 0700 %buildroot/%{_sharedstatedir}/%{name}/tmp

%if %{build_server}
service_file_source=%{SOURCE5}
config_file_source=%{SOURCE6}
sysconfig_file_source=%{SOURCE10}
config_file=server.config

install -D -m 0644 %{SOURCE13} %{buildroot}%{_sysusersdir}/system-user-velociraptor.conf
%else
service_file_source=%{SOURCE7}
config_file_source=%{SOURCE8}
sysconfig_file_source=%{SOURCE11}
config_file=client.config
%endif

install -D -m 0644 "$service_file_source" %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0644 "$sysconfig_file_source" %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -D -m 0640 "$config_file_source" "%{buildroot}%{_sysconfdir}/velociraptor/$config_file"
install -D -m 0755 output/velociraptor-v%{version}-linux-* %buildroot/%{_bindir}/%{name}

%if %{build_kafka_humio_gateway}
install -D -m 0644 %{SOURCE15} %{buildroot}%{_unitdir}/
install -D -m 0644 %{SOURCE16} %{buildroot}%{_fillupdir}/
install -D -m 0755 contrib/kafka-humio-gateway/velociraptor-kafka-humio-gateway %buildroot/%{_bindir}
install -D -m 0644 contrib/kafka-humio-gateway/sample-config.yml \
		   %buildroot/%{_datadir}/velociraptor-kafka-humio-gateway/sample-config.yml
install -D -m 0644 %{SOURCE14} %{buildroot}%{_sysusersdir}/velociraptor-kafka.conf
install -D -d -m 0750 %{buildroot}%{_sysconfdir}/velociraptor-kafka-humio-gateway
install -D -m 0640 contrib/kafka-humio-gateway/sample-config.yml \
		   %buildroot/%{_sysconfdir}/velociraptor-kafka-humio-gateway/transport.yml
%endif

%files
%defattr(-, root, root)
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}

%dir %attr(-, root, velociraptor) %{_sysconfdir}/velociraptor

%config(noreplace) %{config_perms} %{_sysconfdir}/velociraptor/*.config
%dir %{state_dir_perms} %{_sharedstatedir}/%{name}
%dir %{state_dir_perms} %{_sharedstatedir}/%{name}/data
%dir %{state_dir_perms} %{_sharedstatedir}/%{name}/logs
%dir %{state_dir_perms} %{_sharedstatedir}/%{name}/tmp

%pre
%service_add_pre %{name}.service

%post
%{fillup_only}
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%if %{build_server}
%pre -n system-user-velociraptor -f velociraptor-user.pre

%files -n system-user-velociraptor
%defattr(-, root, root)
%{_sysusersdir}/system-user-velociraptor.conf
%endif

%if %{build_kafka_humio_gateway}
%files kafka-humio-gateway
%defattr(-, root, root)
%license LICENSE
%doc contrib/kafka-humio-gateway/README.md
%{_bindir}/velociraptor-kafka-humio-gateway
%dir %{_datadir}/velociraptor-kafka-humio-gateway
%{_datadir}/velociraptor-kafka-humio-gateway/sample-config.yml
%{_sysusersdir}/velociraptor-kafka.conf
%{_unitdir}/velociraptor-kafka-humio-gateway.service
%{_fillupdir}/sysconfig.velociraptor-kafka-humio-gateway
%dir %attr(750, root, velociraptor-kafka) %{_sysconfdir}/velociraptor-kafka-humio-gateway
%config(noreplace) %attr(0640, root, velociraptor-kafka) %{_sysconfdir}/velociraptor-kafka-humio-gateway/transport.yml

%pre kafka-humio-gateway -f kafka-user.pre
%service_add_pre velociraptor-kafka-humio-gateway.service

%post kafka-humio-gateway
%{fillup_only -s kafka-humio-gateway}
%service_add_post velociraptor-kafka-humio-gateway.service

%preun kafka-humio-gateway
%service_del_preun velociraptor-kafka-humio-gateway.service

%postun kafka-humio-gateway
%service_del_postun velociraptor-kafka-humio-gateway.service

%endif

%changelog
