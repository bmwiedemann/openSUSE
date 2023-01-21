#
# spec file for package velociraptor-client
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


%define projname velociraptor
%define vendor_version 0.6.7.4~git41.678ed56
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

Name:           velociraptor-client
Version:        0.6.7.4~git53.0e85855
Release:        0
Summary:        Endpoint visibility and collection tool (endpoint only)
Group:          System/Monitoring
License:        AGPL-3.0-only
URL:            https://github.com/Velocidex/velociraptor
Source:         %{projname}-%{version}.tar.xz
Source1:        vendor-golang-%{vendor_version}.tar.xz
Source2:        %{name}.service
Source3:        %{name}.config.placeholder
Source4:        vmlinux.h-%{vmlinux_h_version}.tar.xz
Source5:        update-vendoring.sh
Source6:        sysconfig.%{name}
Patch1:         velociraptor-golang-mage-vendoring.diff
Patch2:         velociraptor-skip-git-submodule-import-for-OBS-build.patch
Patch3:         vendor-build-fixes-for-SLE12.patch
Patch4:         sdjournal-build-fix-for-SLE12.patch
BuildRequires:  fileb0x
BuildRequires:  golang-packaging
BuildRequires:  mage
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.19
BuildRequires:  pkgconfig(libsystemd)
%ifarch x86_64
BuildRequires:  libtsan0
%endif
%if %{with bpf}
# clang15 causes libbpfo to crash immediately
BuildRequires:  clang13
BuildRequires:  libelf-devel
BuildRequires:  llvm13
BuildRequires:  zlib-devel-static
%endif
Conflicts:      velociraptor
ExclusiveArch:  x86_64 ppc64le aarch64 s390x

%description
Velociraptor is a tool for collecting host based state information
using The Velociraptor Query Language (VQL) queries.

To learn more about Velociraptor, read the documentation on:

https://docs.velociraptor.app/

This package contains only the endpoint agent.  For the full console, please
install the 'velociraptor' package.

%prep
%setup -q -a 1 -a 4 -n %{projname}-%{version}
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
PATH=$PATH:/usr/sbin make linux_bare BUILD_LIBBPFGO=%{with bpf}

%install
mkdir -p %buildroot/%{_bindir}
mkdir -p %buildroot/%{_sysconfdir}/velociraptor
mkdir -p %buildroot/%{_unitdir}
mkdir -p %buildroot/%{_sharedstatedir}/velociraptor-client
install -m 0755 output/velociraptor-v%{version}-linux-* %buildroot/%{_bindir}/velociraptor
install -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -m 0600 %{SOURCE3} %{buildroot}%{_sysconfdir}/velociraptor/client.config
install -d -m 755 %{buildroot}%{_fillupdir}
install -m 0644 %{SOURCE6} %{buildroot}%{_fillupdir}

%files
%defattr(-, root, root)
%license LICENSE
%doc README.md
%dir %{_sysconfdir}/velociraptor
%{_bindir}/velociraptor
%config(noreplace) %{_sysconfdir}/velociraptor/client.config
%{_unitdir}/%{name}.service
%dir %{_sharedstatedir}/velociraptor-client
%{_fillupdir}/sysconfig.%{name}

%pre
%service_add_pre %{name}.service

%post
%{fillup_only}
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%changelog
