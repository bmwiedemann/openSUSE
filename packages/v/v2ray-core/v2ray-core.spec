#
# spec file for package v2ray-core
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define   provider        github
%define   provider_tld    com
%define   project         v2ray
%define   repo            v2ray-core
# https://github.com/shadowsocks/v2ray-plugin
%define   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%define   import_path     v2ray.com/core

Name:           v2ray-core
Version:        4.23.4
Release:        0
Summary:        Project V
Group:          Productivity/Networking/Web/Proxy
License:        MIT
URL:            https://github.com/v2ray/v2ray-core
Source0:        https://github.com/v2ray/v2ray-core/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        v2ray.service
Source3:        config.json
Source4:        vpoint_socks_vmess.json
Source5:        vpoint_vmess_freedom.json
Source99:       %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  golang-packaging
# This package can be built with go version < 1.13
BuildRequires:  golang(API) = 1.14
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
AutoReqProv:    Off
Provides:       %{project} = %{version}-%{release}
Obsoletes:      %{project} < %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_provides}
%{?systemd_ordering}

%description
Project V is a set of network tools that help you to build your own computer
network. It secures your network connections and thus protects your privacy. See
our website for more information.

%package -n golang-%{provider}-%{project}-%{repo}
Summary:        Additional mobile libraries
Group:          Development/Languages/Golang
BuildArch:      noarch
AutoReqProv:    On

%description -n golang-%{provider}-%{project}-%{repo}
Project V is a set of network tools that help you to build your own computer
network. It secures your network connections and thus protects your privacy. See
our website for more information.

This package provide source code for %{repo}

%prep
%setup -q -a1 -n %{repo}-%{version}
# %setup -q -D -T -a 1 -n %{repo}-%{version}
rm go.sum go.mod

%build
%goprep %{import_path}
%gobuild main...
mv %{_builddir}/go/bin/main %{_builddir}/go/bin/v2ray
%gobuild infra/control/main...
mv %{_builddir}/go/bin/main %{_builddir}/go/bin/v2ctl

%install
%goinstall
%gosrc
%gofilelist

install -d %{buildroot}%{_unitdir}/v2ray
install -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/v2ray/

install -d %{buildroot}%{_sysconfdir}/v2ray
install -m0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/v2ray/
install -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/v2ray/
install -m0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/v2ray/

install -d %{buildroot}%{_sbindir}/
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcv2ray

%fdupes %{buildroot}

%pre
%service_add_pre %{project}.service

%post
%service_add_post %{project}.service

%preun
%service_del_preun %{project}.service

%postun
%service_del_postun %{project}.service

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/v2ray
%{_bindir}/v2ctl
%{_unitdir}/v2ray
%dir %{_sysconfdir}/v2ray
%config(noreplace) %{_sysconfdir}/v2ray/*.json
%{_sbindir}/rcv2ray

%files -n golang-%{provider}-%{project}-%{repo} -f file.lst
%defattr(-,root,root)
%doc README.md
%license LICENSE

%changelog
