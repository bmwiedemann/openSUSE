#
# spec file for package sysdig
#
# Copyright (c) 2026 SUSE LLC
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


%define falco_libs_version 0.21.0
%define falco_driver_version 8.1.0
Name:           sysdig
Version:        0.41.4
Release:        0
Summary:        System-level exploration
License:        Apache-2.0
URL:            https://github.com/draios/sysdig
Source0:        https://github.com/draios/%{name}/archive/%{version}/sysdig-%{version}.tar.gz
Source1:        https://github.com/falcosecurity/libs/archive/%{falco_libs_version}.tar.gz#/falco-libs-%{falco_libs_version}.tar.gz
Source2:        https://github.com/falcosecurity/libs/archive/%{falco_driver_version}+driver.tar.gz#/falco-driver-%{falco_driver_version}.tar.gz
# PATCH-FIX-OPENSUSE sysdig-disable-container-plugin.patch - the container plugin downloads a prebuilt binary at build time (offline build + prebuilt-binary policy); building it from source needs unpackaged deps (RE-flex, plugin-sdk-cpp)
Patch0:         sysdig-disable-container-plugin.patch
BuildRequires:  abseil-cpp-devel
BuildRequires:  bpftool
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libb64-devel
BuildRequires:  libbpf-devel
BuildRequires:  libjq-devel
BuildRequires:  nlohmann_json-devel
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  uthash-devel
BuildRequires:  valijson-devel
BuildRequires:  pkgconfig(grpc)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(zlib)
# Modern BPF ships a vendored vmlinux.h only for these arches
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

%description
Sysdig is open source, system-level exploration: capture system state and
activity from a running Linux instance, then save, filter and analyze.
Think of it as strace + tcpdump + lsof + awesome sauce. With a little Lua
cherry on top.

%package bash-completion
Summary:        Bash completion for %{name}
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -p1
# Pre-seed the bundled falcosecurity/libs + driver sources so cmake does not fetch them
mkdir -p build/falcosecurity-libs-repo/falcosecurity-libs-prefix/src/
cp %{SOURCE1} build/falcosecurity-libs-repo/falcosecurity-libs-prefix/src/%{falco_libs_version}.tar.gz
mkdir -p build/driver-repo/driver-prefix/src/
cp %{SOURCE2} build/driver-repo/driver-prefix/src/%{falco_driver_version}+driver.tar.gz

%build
%cmake \
  -DBUILD_SHARED_LIBS=OFF \
  -DUSE_BUNDLED_DEPS=OFF \
  -DUSE_BUNDLED_FALCOSECURITY_LIBS=ON \
  -DUSE_BUNDLED_JSONCPP=OFF \
  -DUSE_BUNDLED_TBB=OFF \
  -DUSE_BUNDLED_RE2=OFF \
  -DUSE_BUNDLED_VALIJSON=OFF \
  -DUSE_BUNDLED_LUAJIT=OFF \
  -DUSE_BUNDLED_NCURSES=OFF \
  -DUSE_BUNDLED_YAMLCPP=OFF \
  -DUSE_BUNDLED_NJSON=OFF \
  -DBUILD_DRIVER=OFF \
  -DBUILD_BPF=OFF \
  -DBUILD_SYSDIG_MODERN_BPF=ON \
  -DCREATE_TEST_TARGETS=OFF \
  -DDIR_ETC=%{_sysconfdir} \
  -DSYSDIG_VERSION=%{version} \
  -Wno-dev
%cmake_build

%install
%cmake_install
# sysdig embeds falcosecurity-libs statically; drop its development SDK (headers,
# static libs, pkgconfig) and the bundled scap driver/DKMS source tree (no kmod built)
rm -rf %{buildroot}%{_includedir}/sysdig
rm -f %{buildroot}%{_includedir}/libpman.h
rm -f %{buildroot}%{_libdir}/lib*.a
rm -f %{buildroot}%{_libdir}/pkgconfig/lib{pman,scap,sinsp}.pc
rm -rf %{buildroot}%{_prefix}/src/scap-*
# Ship bash completion in the modern location, not the forbidden /etc/bash_completion.d
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/sysdig %{buildroot}%{_datadir}/bash-completion/completions/sysdig
# Use a fixed interpreter instead of /usr/bin/env
sed -i '1s@^#!%{_bindir}/env bash@#!/bin/bash@' %{buildroot}%{_bindir}/scap-driver-loader
%fdupes -s %{buildroot}/%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/sysdig
%{_bindir}/csysdig
%{_bindir}/scap-driver-loader
%{_mandir}/man8/sysdig.8%{?ext_man}
%{_mandir}/man8/csysdig.8%{?ext_man}
%{_datadir}/%{name}

%files bash-completion
%{_datadir}/bash-completion/completions/sysdig

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%dir %{_datadir}/zsh/vendor-completions
%{_datadir}/zsh/site-functions/_sysdig
%{_datadir}/zsh/vendor-completions/_sysdig

%changelog
