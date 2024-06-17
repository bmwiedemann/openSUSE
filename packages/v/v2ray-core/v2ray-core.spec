#
# spec file for package v2ray-core
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


%define   provider        github
%define   provider_tld    com
%define   project         v2fly
%define   repo            v2ray-core
# https://github.com/v2fly/v2ray-core
%define   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%define   import_path     github.com/v2fly/v2ray-core/v5

Name:           v2ray-core
Version:        5.16.1
Release:        0
Summary:        Network tools for building a computer network
License:        MIT
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/v2fly/v2ray-core
Source0:        https://github.com/v2fly/v2ray-core/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        v2ray.service
Source3:        v2ray@.service
Source4:        https://github.com/v2fly/geoip/raw/release/geoip.dat
Source5:        https://github.com/v2fly/domain-list-community/raw/release/dlc.dat
Source6:        https://github.com/v2fly/v2ray-core/releases/download/v%{version}/v2ray-extra.zip
Source99:       %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  unzip
BuildRequires:  pkgconfig(systemd)
AutoReqProv:    Off
Provides:       v2ray = %{version}-%{release}
Obsoletes:      v2ray < %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{go_provides}
%{?systemd_ordering}

%description
Project V is a set of network tools for building a computer network.
It secures network connections and protects privacy.

%package -n golang-%{provider}-%{project}-%{repo}
Summary:        Additional mobile libraries
Group:          Development/Languages/Golang
BuildArch:      noarch

%description -n golang-%{provider}-%{project}-%{repo}
Project V is a set of network tools for building a computer network.
It secures network connections and protects privacy.

This package provide source code for %{repo}

%prep
%setup -q -a1 -a6 -n %{repo}-%{version}

%build
export GO111MODULE=off
%goprep %{import_path}
%gobuild main...
mv %{_builddir}/go/bin/main %{_builddir}/go/bin/v2ray

%install
%goinstall
%gosrc
rm -rf %{buildroot}%{go_contribsrcdir}/%{import_path}/vendor
%gofilelist

install -d %{buildroot}%{_datadir}/v2ray
install -m0644 %{SOURCE4} %{buildroot}%{_datadir}/v2ray/geoip.dat
install -m0644 %{SOURCE5} %{buildroot}%{_datadir}/v2ray/geosite.dat

install -d %{buildroot}%{_unitdir}
install -m0644 %{SOURCE2} %{buildroot}%{_unitdir}/
install -m0644 %{SOURCE3} %{buildroot}%{_unitdir}/

install -d %{buildroot}%{_sysconfdir}/v2ray
install -m0644 release/config/*.json %{buildroot}%{_sysconfdir}/v2ray/

install -d %{buildroot}%{_sbindir}/
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rcv2ray

install -d %{buildroot}%{_datadir}/v2ray/browserforwarder
install -m0644 browserforwarder/index.js %{buildroot}%{_datadir}/v2ray/browserforwarder/
install -m0644 browserforwarder/index.html %{buildroot}%{_datadir}/v2ray/browserforwarder/

%fdupes %{buildroot}

%pre
%service_add_pre v2ray.service v2ray@.service

%post
%service_add_post v2ray.service v2ray@.service

%preun
%service_del_preun v2ray.service v2ray@.service

%postun
%service_del_postun v2ray.service v2ray@.service

%files
%doc README.md
%license LICENSE
%{_bindir}/v2ray
%{_bindir}/v2api
%{_unitdir}/v2ray.service
%{_unitdir}/v2ray@.service
%dir %{_sysconfdir}/v2ray
%dir %{_datadir}/v2ray
%{_datadir}/v2ray/*
%config(noreplace) %{_sysconfdir}/v2ray/*.json
%{_sbindir}/rcv2ray
%{_datadir}/v2ray/browserforwarder/

%files -n golang-%{provider}-%{project}-%{repo} -f file.lst
%doc README.md
%license LICENSE

%changelog
