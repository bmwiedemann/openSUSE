#
# spec file for package cni
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


%global         provider_prefix github.com/containernetworking/cni
%global         import_path     %{provider_prefix}
%define         cni_etc_dir  %{_sysconfdir}/cni
%define         cni_bin_dir  %{_libexecdir}/cni
%define         cni_doc_dir  %{_docdir}/cni
Name:           cni
Version:        1.1.2
Release:        0
Summary:        Container Network Interface - networking for Linux containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/containernetworking/cni
Source0:        %{name}-%{version}.tar.gz
Source1:        99-loopback.conf
Source2:        vendor.tar.gz
# PATCH-FIX-UPSTREAM bsc#1206711
Patch0:         0001-fix-upstream-CVE-2021-38561.patch
BuildRequires:  golang-packaging
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.14
Requires(post): %fillup_prereq
Recommends:     cni-plugins
%{?systemd_requires}

%description
The CNI (Container Network Interface) project consists of a
specification and libraries for writing plugins to configure
network interfaces in Linux containers, along with a number of
supported plugins. CNI concerns itself only with network
connectivity of containers and removing allocated resources when
the container is deleted. Because of this focus, CNI has a wide
range of support and the specification is simple to implement.

%prep
%autosetup -a2 -N
pushd vendor/golang.org/x/text
%autopatch -p1
popd

%build
export GOFLAGS=-mod=vendor
%goprep %{import_path}
%gobuild libcni
%gobuild cnitool
for d in plugins/test/*; do
  if [ -d $d ]; then
    %gobuild $d
  fi
done

%install
# install the plugins
install -m 755 -d %{buildroot}%{cni_bin_dir}
install -D %{_builddir}/go/bin/noop %{buildroot}%{cni_bin_dir}/
install -D %{_builddir}/go/bin/sleep %{buildroot}%{cni_bin_dir}/

# undo a copy: cnitool must go to sbin/
install -m 755 -d %{buildroot}%{_sbindir}
install -D %{_builddir}/go/bin/cnitool %{buildroot}%{_sbindir}/

# config
install -m 755 -d %{buildroot}%{cni_etc_dir}
install -m 755 -d %{buildroot}%{cni_etc_dir}/net.d
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{cni_etc_dir}/net.d/99-loopback.conf.sample

# documentation
install -m 755 -d "%{buildroot}%{cni_doc_dir}"

%post
%{fillup_only -n %{name}}

%files
%doc CONTRIBUTING.md README.md DCO
%license LICENSE
%dir %{cni_etc_dir}
%dir %{cni_etc_dir}/net.d
%config %{cni_etc_dir}/net.d/*
%dir %{cni_bin_dir}
%dir %{cni_doc_dir}
%{cni_bin_dir}/{noop,sleep}
%{_sbindir}/cnitool

%changelog
