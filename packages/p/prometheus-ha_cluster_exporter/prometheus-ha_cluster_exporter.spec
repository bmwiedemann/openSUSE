#
# Copyright (c) 2019 SUSE LLC
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
Name:           prometheus-ha_cluster_exporter
# Version will be processed via set_version source service
Version:        1.0.0beta6
Release:        0
License:        Apache-2.0
Summary:        Prometheus exporter for Pacemaker HA clusters metrics
Group:          System/Monitoring
Url:            https://github.com/ClusterLabs/ha_cluster_exporter
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
ExclusiveArch:  aarch64 x86_64 ppc64le s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  go >= 1.11
Provides:       ha_cluster_exporter = %{version}-%{release}
Provides:       prometheus(ha_cluster_exporter) = %{version}-%{release}
# Unlike C/C++ packages, Golang packages do not have header files. They are statically built so the main package is also the devel package.
Provides:       %{name}-devel = %{version}
Provides:       %{name}-devel-static = %{version}

# Make sure that the binary is not getting stripped.
%undefine _build_create_debug
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true

%description
Prometheus exporter for Pacemaker HA clusters metrics

%prep
%setup -q            # unpack project sources
%setup -q -T -D -a 1 # unpack go dependencies in vendor.tar.gz, which was prepared by the source services

%define shortname ha_cluster_exporter

%build

# s390x GOARCH doesn't support PIE
%ifnarch s390x
export GOFLAGS="-buildmode=pie"
%endif

go build -mod=vendor -ldflags="-s -w -X main.version=%{version}" -o %{shortname}

%install

# Install the binary.
install -D -m 0755 %{shortname} "%{buildroot}%{_bindir}/%{shortname}"

# Install the systemd unit
install -D -m 0644 %{shortname}.service %{buildroot}%{_unitdir}/%{name}.service

# Install compat wrapper for legacy init systems
install -Dd -m 0755 %{buildroot}%{_sbindir}
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
%defattr(-,root,root)
%doc *.md
%doc doc/*
%if 0%{?suse_version} >= 1500
%license LICENSE
%else
%doc LICENSE
%endif
%{_bindir}/%{shortname}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}

%changelog
