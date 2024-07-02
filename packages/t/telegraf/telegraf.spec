#
# spec file for package telegraf
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


%define _config_dir %{_sysconfdir}/%{name}
Name:           telegraf
Version:        1.31.1
Release:        0
Summary:        The plugin-driven server agent for collecting & reporting metrics
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/influxdata/telegraf
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Patch0:         harden_telegraf.service.patch
BuildRequires:  git-core
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  golang(API) >= 1.22
%{?systemd_ordering}

%description
Telegraf is an agent written in Go for collecting, processing, aggregating, and writing metrics.

Design goals are to have a minimal memory footprint with a plugin system so that developers in the community can
easily add support for collecting metrics from local or remote services.

%prep
%setup -q
%setup -q -T -D -a 1
%patch -P 0 -p1

%build
# Build the binary.
go build \
   -mod=vendor \
%ifnarch ppc64 ppc64le
   -buildmode=pie \
%endif
   ./cmd/telegraf;
./telegraf config > etc/telegraf.conf

%install
# Install the binary.
install -D -m 0755 %{name} "%{buildroot}/%{_bindir}/%{name}"

mkdir -p %{buildroot}/%{_config_dir}
mkdir -p %{buildroot}/%{_config_dir}/%{name}.d
install -m644 etc/%{name}.conf %{buildroot}/%{_config_dir}

install -D -m 644 scripts/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
sed -i '/User=/d' %{buildroot}%{_unitdir}/%{name}.service
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

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
%doc CHANGELOG.md CONTRIBUTING.md README.md
%license LICENSE
%dir %{_config_dir}
%config(noreplace) %{_config_dir}/%{name}.conf
%{_bindir}/%{name}

%changelog
