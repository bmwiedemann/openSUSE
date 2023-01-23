#
# spec file for package EternalTerminal
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


%global _firewalld_dir %{_prefix}/lib/firewalld
Name:           EternalTerminal
Version:        6.2.4
Release:        0
Summary:        Remote shell that survives IP roaming and disconnect
License:        Apache-2.0
URL:            https://mistertea.github.io/EternalTerminal/
Source0:        https://github.com/MisterTea/EternalTerminal/archive/et-v%{version}.tar.gz
Source1:        et.xml
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  firewall-macros
BuildRequires:  firewalld
%if 0%{?sle_version} >= 150300
BuildRequires:  gcc10-c++
%define forced_gcc_version -10
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  gflags-devel
BuildRequires:  libopenssl-1_1-devel
BuildRequires:  libsodium-devel
BuildRequires:  ncurses-devel
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel
BuildRequires:  utempter-devel
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

%description
Eternal Terminal (ET) is a remote shell that automatically reconnects without
interrupting the session.

%prep
%autosetup -n EternalTerminal-et-v%{version} -p1

%build

%if 0%{?forced_gcc_version:1}
export CC=gcc%{?forced_gcc_version}
export CXX=g++%{?forced_gcc_version}
%endif
export CXXFLAGS="%{optflags} -std=c++17"
# see https://github.com/MisterTea/EternalTerminal/issues/403
%cmake -DDISABLE_VCPKG:BOOL=ON -DProtobuf_LITE_LIBRARY=%{_libdir}/libprotobuf-lite.so
make %{?_smp_mflags}

%install
%cmake_install

mkdir -p \
  %{buildroot}%{_unitdir} \
  %{buildroot}%{_sysconfdir} \
  %{buildroot}%{_firewalld_dir}/services
install -m 0644 -p systemctl/et.service %{buildroot}%{_unitdir}/et.service
install -m 0644 -p etc/et.cfg %{buildroot}%{_sysconfdir}/et.cfg
install -m 0644 %{SOURCE1} %{buildroot}%{_firewalld_dir}/services/et.xml

%pre
%service_add_pre et.service

%post
%service_add_post et.service
%firewalld_reload

%preun
%service_del_preun et.service

%postun
%service_del_postun et.service
%firewalld_reload

%files
%license LICENSE
%doc README.md
%{_bindir}/et
%{_bindir}/etserver
%{_bindir}/etterminal
%{_bindir}/htm
%{_bindir}/htmd
%dir %{_firewalld_dir}
%dir %{_firewalld_dir}/services
%{_firewalld_dir}/services/et.xml
%config(noreplace) %{_sysconfdir}/et.cfg
%{_unitdir}/et.service

%changelog
