#
# spec file for package gitlab-container-registry
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


Name:           gitlab-container-registry
Version:        4.30.0
Release:        0
Summary:        The GitLab Container Registry
License:        Apache-2.0
Group:          System/Management
URL:            https://gitlab.com/gitlab-org/container-registry
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}-configuration.yml
Source3:        %{name}.service
Source4:       system-user-%{name}.conf
BuildRequires:  golang(API) >= 1.23
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools

%description
The GitLab Container Registry originated as a fork of the Docker Distribution
Registry, now CNCF Distribution, both distributed under Apache License Version
2.0.

The first GitLab change on top of the upstream implementation was efe421fd, and
since then we have diverged enough to the point where we decided to detach from
upstream and proceed on our own path.

Since then, we have implemented and released several major performance
improvements and bug fixes. For a list of changes, please see differences from
upstream
(https://gitlab.com/gitlab-org/container-registry/-/blob/master/docs/upstream-differences.md).
These changes culminated on a new architecture based on a relational
metadata database and the original goal, enabling online garbage collection
(https://gitlab.com/gitlab-org/container-registry/-/blob/master/docs/spec/gitlab/online-garbage-collection.md).

%prep
%autosetup -p 1 -a 1

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %{_sourcedir}/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

go build \
   -mod=vendor \
   -buildmode=pie \
   -ldflags=" \
   -X github.com/docker/distribution/version.Version=%{version} \
   -X github.com/docker/distribution/version.Revision=${COMMIT_HASH} \
   -X github.com/docker/distribution/version.Package=github.com/docker/distribution \
   -X github.com/docker/distribution/version.BuildTime=${BUILD_DATE}" \
   -o bin/%{name} ./cmd/registry

%sysusers_generate_pre %{SOURCE4} %{name} system-user-%{name}.conf

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

#
# configuration directory in /etc/
#
install -D -m 644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name}/config.yml

#
# directory in /var/lib/
#
install -d  %{buildroot}%{_localstatedir}/lib/%{name}

#
# system user
#
install -d -m 755 %{buildroot}%{_sysusersdir}
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/

#
# systemd service
#
install -d -m 0755 %{buildroot}%{_sbindir}
install -D -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service

%check
%{buildroot}/%{_bindir}/%{name} --version

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_sysusersdir}/system-user-%{name}.conf
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.yml
%dir %attr(-,%{name},%{name}) %{_localstatedir}/lib/%{name}

%changelog
