#
# spec file for package cadvisor
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
# nodebuginfo


%global goipath github.com/google/cadvisor
Name:           cadvisor
Version:        0.46.0
Release:        0
Summary:        A Simple and Comprehensive Vulnerability Scanner for Containers
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/google/cadvisor
Source:         %{name}-%{version}.tar.zst
Source1:        vendor-cmd.tar.zst
Source2:        cadvisor.service
Source3:        sysconfig.cadvisor
BuildRequires:  golang-packaging
BuildRequires:  systemd-rpm-macros
BuildRequires:  zstd
BuildRequires:  golang(API) = 1.19
Requires:       ca-certificates
Requires:       git-core
Requires:       rpm
Requires(post): %fillup_prereq

%description
cAdvisor (Container Advisor) provides container users an understanding of the
resource usage and performance characteristics of their running containers. It
is a running daemon that collects, aggregates, processes, and exports
information about running containers. Specifically, for each container it keeps
resource isolation parameters, historical resource usage, histograms of
complete historical resource usage and network statistics. This data is
exported by container and machine-wide.

cAdvisor has native support for Docker containers and should support just about
any other container type out of the box. We strive for support across the board
so feel free to open an issue if that is not the case.  cAdvisor's container
abstraction is based on lmctfy's so containers are inherently nested
hierarchically.

%prep
%setup -qa1
%autopatch -p1

%build
%{goprep} %{goipath}

pushd cmd
%{gobuild} -tags netgo -ldflags '-X github.com/google/cadvisor/version.Version=%{version}' ./cmd
popd

%install
%{goinstall}
mv %{buildroot}%{_bindir}/{cmd,cadvisor}

#
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}

%pre
%service_add_pre cadvisor.service

%post
%service_add_post cadvisor.service
%{fillup_only -n cadvisor}

%preun
%service_del_preun cadvisor.service

%postun
%service_del_postun cadvisor.service

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/cadvisor
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}

%changelog
