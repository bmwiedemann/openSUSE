#
# spec file for package telegraf
#
# Copyright (c) 2018 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           telegraf
Version:        1.8.3
Release:        0
License:        MIT
Summary:        The plugin-driven server agent for collecting & reporting metrics
Url:            https://github.com/influxdata/telegraf
Group:          System/Monitoring
Source:         %{name}-%{version}.tar.gz
Source1:        %{name}-deps.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  go >= 1.7
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}

## Features ##

Patch0:         0001-Generic-SQL-output-plugin-for-Telegraf.patch

## /Features ##

%define _influxdata_dir %{_builddir}/src/github.com/influxdata
%define _telegraf_dir %{_influxdata_dir}/%{name}
%define _config_dir %{_sysconfdir}/%{name}

%description
Telegraf is an agent written in Go for collecting, processing, aggregating, and writing metrics.

Design goals are to have a minimal memory footprint with a plugin system so that developers in the community can
easily add support for collecting metrics from local or remote services.

%prep
mkdir -p %{_influxdata_dir}
tar -C %{_builddir}/src -xJf %{SOURCE1}
tar -C %{_influxdata_dir} -xzf %{SOURCE0}
cd %{_influxdata_dir}
# If there is allready telegraf then remove it
rm -rf %{name}
ln -sf %{name}-%{version} %{name}
cd %{name}
%patch0 -p1

%build
export GOPATH="%{_builddir}:$GOPATH"
export LDFLAGS="-buildmode=pie"
cd %{_telegraf_dir}
make %{name}

%install
mkdir -p %{buildroot}%{_bindir}
install -m755 %{_telegraf_dir}/%{name} %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}/%{_config_dir}
install -m644 %{_telegraf_dir}/etc/%{name}.conf %{buildroot}/%{_config_dir}

install -D -m 644 %{_telegraf_dir}/scripts/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
sed -i '/User=/d' %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%doc src/github.com/influxdata/%{name}/CHANGELOG.md
%doc src/github.com/influxdata/%{name}/CONTRIBUTING.md
%license src/github.com/influxdata/%{name}/LICENSE
%doc src/github.com/influxdata/%{name}/README.md
%dir %{_config_dir}
%config %{_config_dir}/%{name}.conf
%{_bindir}/%{name}

%changelog
