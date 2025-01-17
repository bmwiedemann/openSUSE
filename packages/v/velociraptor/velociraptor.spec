#
# spec file for package velociraptor
#
# Copyright (c) 2025 SUSE LLC
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
%define name_suffix -client
%define make_target linux_bare
%define config_perms 0600, root, root
%define state_dir_perms 0700, root, root
%else
%define build_server 1
%define build_client 0
%define name_suffix %{nil}
%define make_target linux
%define config_perms 0640, root, velociraptor
%define state_dir_perms 0700, velociraptor, velociraptor
%endif

%define projname velociraptor
%define vmlinux_h_version 5.14.21150400.22-150400-default

# SLE 15 SP3 / Leap 15.3 or newer gets eBPF
# Earlier versions don't have a usable eBPF and the
# release doesn't easily build llvm13
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150200
%bcond_without bpf
%endif
%if "%{_vendor}" == "debbuild"
%bcond_without bpf
%endif
%if 0%{?rhel}
# RHEL can do BPF but we need llvm for it
%bcond_without bpf
%endif

%if "%{_vendor}" == "debbuild"
%define _unitdir /usr/lib/systemd/system
%endif

# Older SLE releases and debbuild don't support uppercase VERSION macro
%if "%{_vendor}" == "debbuild" || 0%{?sle_version} < 150000
%global VERSION %{version}
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
Version:        0.7.0.4.git142.862ef23
Release:        0
%if %{build_server}
Summary:        Endpoint visibility and collection tool
%else
Summary:        Endpoint visibility and collection tool (endpoint only)
%endif
Group:          System/Monitoring
License:        AGPL-3.0-only
URL:            https://github.com/Velocidex/velociraptor
Source:         %{projname}-%{version}.tar.gz
Source1:        velociraptor-go_modules.tar.gz
Source2:        vmlinux.h-%{vmlinux_h_version}.tar.xz
Source3:        velociraptor.service
Source4:        velociraptor-server.config.placeholder
Source5:        velociraptor-client.service
Source6:        velociraptor-client.config.placeholder
Source7:        sysconfig.velociraptor
Source8:        sysconfig.velociraptor-client
Source9:        %{projname}.obsinfo
Source10:       system-user-velociraptor.sysusers
Source11:       velociraptor-nodejs.spec.inc
Source12:       package-lock.json

%include %{_sourcedir}/velociraptor-nodejs.spec.inc

Patch1:         vendor-build-fixes-for-SLE12.patch
Patch2:         sdjournal-build-fix-for-SLE12.patch
Patch3:         velociraptor-reproducible-timestamp.diff
BuildRequires:  fileb0x
%if 0%{?suse_version}
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.19
BuildRequires:  pkgconfig(libsystemd)
%endif
%if "%{_vendor}" == "debbuild"
BuildRequires:  golang >= 2:1.19~0
BuildRequires:  libsystemd-dev
BuildRequires:  pkg-config
%endif
%if 0%{?rhel}
BuildRequires:  golang >= 1.19
BuildRequires:  python3
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(libsystemd)
%endif
%if %{build_server}
BuildRequires:  local-npm-registry
BuildRequires:  nodejs >= 18
BuildRequires:  npm >= 18
%endif
%if %{with bpf}
%if 0%{?suse_version}
%if 0%{?suse_version} > 1500 || 0%{?sle_version} == 150600
BuildRequires:  clang17
BuildRequires:  llvm17
%else
%if 0%{?sle_version} >= 150300
BuildRequires:  clang16
BuildRequires:  llvm16
%if 0%{?sle_version} > 150400
BuildRequires:  llvm16-libclang13
%endif
%else
BuildRequires:  clang13
BuildRequires:  llvm13
%endif
%endif
BuildRequires:  libelf-devel
BuildRequires:  libzstd-devel
BuildRequires:  zlib-devel
%endif
%if "%{_vendor}" == "debbuild"
BuildRequires:  clang
BuildRequires:  libelf-dev
BuildRequires:  libzstd-dev
BuildRequires:  llvm
BuildRequires:  zlib1g-dev
%endif
%if 0%{?rhel}
BuildRequires:  clang >= 13
BuildRequires:  libelf-devel
BuildRequires:  libzstd-devel
BuildRequires:  llvm >= 13
BuildRequires:  zlib-devel
%endif
%endif
%if %{build_server}
BuildRequires:  group(velociraptor)
Requires:       group(velociraptor)
Requires:       user(velociraptor)
Obsoletes:      velociraptor-kafka-humio-gateway < %{version}
%else
%if 0%{?suse_version}
BuildRequires:  sysuser-tools
%{?sysusers_requires}
%endif
%endif

%if 0%{?suse_version}
# SLE12 doesn't support sysusers
%if 0%{?sle_version} >= 120000 && 0%{?sle_version} < 150000
Requires(pre):  pwdutils
%define pre_create_group 1
%else
Requires:       group(velociraptor)
%endif
%endif

%if %{build_server}
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150400
ExclusiveArch:  x86_64
%else
ExclusiveArch:  do_not_build
%endif
%else
ExclusiveArch:  x86_64 ppc64le aarch64 s390x
%endif

%if 0%{?rhel}
# RHEL builds aren't working yet
ExclusiveArch:  do_not_build
%endif

# Not *required* but without it, we spam the system log
Recommends:     auditd

%if 0%{?_project:1} && (0%{?suse_version} > 1500 || 0%{?sle_version} > 150000)
Provides:       %{name}(project:%_project)
%endif

%if "%{vendor}" == "debbuild"
%define mtag Packager: https://www.suse.com
%mtag
%endif

%if %{build_server}
%description
Velociraptor is a tool for collecting host based state information
using The Velociraptor Query Language (VQL) queries.

To learn more about Velociraptor, read the documentation on:

https://docs.velociraptor.app/

This package contains the velociraptor server and full console GUI.
For just the endpoint agent, please install the 'velociraptor-client' package.

%endif
%if %{build_client}
%description
Velociraptor is a tool for collecting host based state information
using The Velociraptor Query Language (VQL) queries.

To learn more about Velociraptor, read the documentation on:

https://docs.velociraptor.app/

This package contains only the endpoint agent.  For the full server and GUI
console, please install the 'velociraptor' package.

%if 0%{?suse_version}
%package -n system-user-velociraptor
Summary:        System user and group 'velociraptor'
Version:        1.0.0
License:        Apache-2.0
Group:          System/Monitoring
Provides:       group(velociraptor)
Provides:       user(velociraptor)
BuildArch:      noarch

%description -n system-user-velociraptor
This package provides a shared system user for all velociraptor components
%endif
%endif

%prep
%setup -q -a 1 -a 2 -n %{projname}-%{VERSION}
%autopatch -p1

# Set the version to something more specific than <next-tag>-dev
sed -ie "s/\([[:space:]]VERSION *= \).*/\1 \"%{VERSION}\"/" constants/constants.go

%if %{with bpf}
mkdir -p third_party/libbpfgo/output

arch=%{_arch}
if test "$arch" = "amd64"; then
	arch=x86_64
fi

cp vmlinux.h-%{vmlinux_h_version}/vmlinux-${arch}.h \
   third_party/libbpfgo/output/vmlinux.h
%endif

# These just clutter the GUI and we don't have Windows clients
# Note: There are dependencies on these that need to be resolved before
# removing them outright.
# rm -rf artifacts/definitions/Windows
%if %{build_server}
pushd gui/velociraptor
rm -f package-lock.json
local-npm-registry %{_sourcedir} install --include=dev --legacy-peer-deps
popd
%endif

%build

# Reproducible builds need stable timestamps
timestamp=$(date -Iseconds --utc --date=@$(grep mtime: %{SOURCE9}|sed -e 's/mtime: //'))
git_commit=$(grep commit: %{SOURCE9}|sed -e 's/commit: //g')

export VELOCIRAPTOR_BUILD_TIME=$timestamp
export VELOCIRAPTOR_GIT_HEAD=$git_commit

%if %{build_server}
(cd gui/velociraptor ; npm run build)
%else
%if 0%{?suse_version}
%sysusers_generate_pre %{SOURCE10} velociraptor-user
%endif
%endif

%if 0%{?suse_version}
LLVM_STRIP=llvm-strip
%else
LLVM_STRIP=llvm-strip
%endif

CLANG=clang

PATH=$PATH:/usr/sbin make %{make_target} BUILD_BPF_PLUGINS=%{with bpf} CLANG=$CLANG STRIP=$LLVM_STRIP

%install
install -D -d -m 0750 %buildroot/%{_sysconfdir}/velociraptor
install -D -d -m 0700 %buildroot/%{_sharedstatedir}/%{name}/data
install -D -d -m 0700 %buildroot/%{_sharedstatedir}/%{name}/logs
install -D -d -m 0700 %buildroot/%{_sharedstatedir}/%{name}/tmp

%if %{build_server}
service_file_source=%{SOURCE3}
config_file_source=%{SOURCE4}
sysconfig_file_source=%{SOURCE7}
config_file=server.config

%else
%if 0%{?suse_version}
install -D -m 0644 %{SOURCE10} %{buildroot}%{_sysusersdir}/system-user-velociraptor.conf
%endif
service_file_source=%{SOURCE5}
config_file_source=%{SOURCE6}
sysconfig_file_source=%{SOURCE8}
config_file=client.config
%endif

%if 0%{?suse_version}
install -D -m 0644 "$sysconfig_file_source" %{buildroot}%{_fillupdir}/sysconfig.%{name}
%endif
%if "%{vendor}" == "debbuild"
install -D -m 0644 "$sysconfig_file_source" %{buildroot}/%{_sysconfdir}/default/%{name}
%endif

install -D -m 0644 "$service_file_source" %{buildroot}%{_unitdir}/%{name}.service
install -D -m 0640 "$config_file_source" "%{buildroot}%{_sysconfdir}/velociraptor/$config_file"
install -D -m 0755 output/velociraptor-v%{VERSION}-linux-* %buildroot/%{_bindir}/%{name}

%files
%defattr(-, root, root)
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.%{name}
%endif
%if "%{vendor}" == "debbuild"
%{_sysconfdir}/default/%{name}
%endif

%dir %attr(-, root, velociraptor) %{_sysconfdir}/velociraptor

%config(noreplace) %attr(%{config_perms}) %{_sysconfdir}/velociraptor/*.config
%dir %attr(%{state_dir_perms}) %{_sharedstatedir}/%{name}
%dir %attr(%{state_dir_perms}) %{_sharedstatedir}/%{name}/data
%dir %attr(%{state_dir_perms}) %{_sharedstatedir}/%{name}/logs
%dir %attr(%{state_dir_perms}) %{_sharedstatedir}/%{name}/tmp

%if %{build_client}
%if 0%{?suse_version}
%files -n system-user-velociraptor
%defattr(-, root, root)
%{_sysusersdir}/system-user-velociraptor.conf

%pre -n system-user-velociraptor -f velociraptor-user.pre
%endif
%endif

%if 0%{?suse_version}
%pre
%if 0%{?pre_create_group}
# create velociraptor group if it doesn't exist
groupadd -f -r velociraptor  2>/dev/null || :
%endif
%service_add_pre %{name}.service

%post
%{fillup_only}
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service
%endif

%if "%{_vendor}" == "debbuild"
%postun
# Automatically added by dh_installsystemd/13.11.4
if [ "$1" = remove ] && [ -d /run/systemd/system ] ; then
	systemctl --system daemon-reload >/dev/null || true
fi
# End automatically added section
# Automatically added by dh_installsystemd/13.11.4
if [ "$1" = "purge" ]; then
	if [ -x "/usr/bin/deb-systemd-helper" ]; then
		deb-systemd-helper purge 'velociraptor-client.service' >/dev/null || true
	fi
fi
# End automatically added section
%endif

%changelog
