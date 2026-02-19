#
# spec file for package semaphore
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           semaphore
Version:        2.17.8
Release:        0
Summary:        Modern UI for Ansible
License:        MIT
URL:            https://github.com/semaphoreui/semaphore
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        web-%{version}.tar.gz
Source3:        Makefile
Source4:        PACKAGING_README.md
Source11:       %{name}.service
Source12:       server-config.json.example
Source21:       %{name}-runner.service
Source22:       runner-config.json.example
BuildRequires:  go >= 1.24
Requires:       ansible-core
Requires:       git-core

%description
Ansible Semaphore is a modern UI for Ansible. It lets you easily run Ansible
playbooks, get notifications about fails, control access to deployment system.

If your project has grown and deploying from the terminal is no longer for you
then Ansible Semaphore is what you need.

%prep
%autosetup -p 1 -a 1
tar xvf %{SOURCE2}

%build
# hash will be shortened by COMMIT_HASH:0:8 later
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

go build \
   -mod=vendor \
   -buildmode=pie \
   -tags "netgo" \
   -ldflags=" \
   -X github.com/semaphoreui/semaphore/util.Ver=v%{version} \
   -X github.com/semaphoreui/semaphore/util.Commit=${COMMIT_HASH:0:8} \
   -X github.com/semaphoreui/semaphore/util.Date=$BUILD_DATE" \
   -o bin/semaphore ./cli/main.go

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

# create the configuration directory
install -d -m 0755 %{buildroot}/%{_sysconfdir}/%{name}/
install -d -m 0755 %{buildroot}/%{_sysconfdir}/%{name}-runner/

# Install the systemd service unit
install -d -m 755 %{buildroot}%{_unitdir}
install -D -m 0644 %{SOURCE11} %{buildroot}/%{_unitdir}/
install -D -m 0644 %{SOURCE21} %{buildroot}/%{_unitdir}/
install -d -m 755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}-runner

cp %{SOURCE12} .
cp %{SOURCE22} .

%pre
%service_add_pre %{name}.service %{name}-runner.service

%post
%service_add_post %{name}.service %{name}-runner.service

%preun
%service_del_preun %{name}.service %{name}-runner.service

%postun
%service_del_postun %{name}.service %{name}-runner.service

%files
%doc README.md server-config.json.example runner-config.json.example
%license LICENSE
%dir %{_sysconfdir}/%{name}/
%ghost %config(noreplace) %attr(0644,root,root) %{_sysconfdir}/%{name}/config.json
%dir %{_sysconfdir}/%{name}-runner/
%ghost %config(noreplace) %attr(0644,root,root) %{_sysconfdir}/%{name}-runner/config.json
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}-runner.service
%{_sbindir}/rc%{name}
%{_sbindir}/rc%{name}-runner

%changelog
