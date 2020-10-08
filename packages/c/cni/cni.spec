#
# spec file for package cni
#
# Copyright (c) 2020 SUSE LLC
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


%define         cni_etc_dir  %{_sysconfdir}/cni
%define         cni_bin_dir  %{_libexecdir}/cni
%define         cni_doc_dir  %{_docdir}/cni

Name:           cni
Version:        0.8.0
Release:        0
Summary:        Container Network Interface - networking for Linux containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/containernetworking/cni
Source:         %{name}-%{version}.tar.xz
Source1:        99-loopback.conf
Source2:        build.sh
BuildRequires:  golang-packaging
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Recommends:     cni-plugins
Requires(post): %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
# Make sure that the binary is not getting stripped.
%{go_nostrip}

%description
The CNI (Container Network Interface) project consists of a
specification and libraries for writing plugins to configure
network interfaces in Linux containers, along with a number of
supported plugins. CNI concerns itself only with network
connectivity of containers and removing allocated resources when
the container is deleted. Because of this focus, CNI has a wide
range of support and the specification is simple to implement.

%prep
%setup -q
cp %{SOURCE2} build.sh

%build
sh ./build.sh

%install

# install the plugins
install -m 755 -d "%{buildroot}%{cni_bin_dir}"
cp bin/noop "%{buildroot}%{cni_bin_dir}/"
cp bin/sleep "%{buildroot}%{cni_bin_dir}/"

# undo a copy: cnitool must go to sbin/
install -m 755 -d "%{buildroot}%{_sbindir}"
cp bin/cnitool  "%{buildroot}%{_sbindir}/"

# config
install -m 755 -d "%{buildroot}%{cni_etc_dir}"
install -m 755 -d "%{buildroot}%{cni_etc_dir}/net.d"
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{cni_etc_dir}/net.d/99-loopback.conf.sample

# documentation
install -m 755 -d "%{buildroot}%{cni_doc_dir}"

%post
%{fillup_only -n %{name}}

%files
%defattr(-,root,root)
%doc CONTRIBUTING.md README.md DCO
%license LICENSE
%dir %{cni_etc_dir}
%dir %{cni_etc_dir}/net.d
%config %{cni_etc_dir}/net.d/*
%dir %{cni_bin_dir}
%dir %{cni_doc_dir}
%{cni_bin_dir}/*
%{cni_etc_dir}/net.d/*
%{_sbindir}/cnitool

%changelog
