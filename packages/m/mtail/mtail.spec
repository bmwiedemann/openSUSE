#
# spec file for package mtail
#
# Copyright (c) 2022 SUSE LLC
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


%{go_nostrip}
# Project name when using go tooling.
%define project github.com/google/mtail

%bcond_without  apparmor

Name:           mtail
Version:        3.0.0rc51
Release:        0
Summary:        Tool for extracting metrics from application logs
License:        Apache-2.0
Group:          System/Management
URL:            https://%{project}
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}.service
Source3:        %{name}.sysconfig
Source4:        apparmor-usr.sbin.%{name}
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.17
Requires(post): %fillup_prereq
Requires(pre):  shadow
%if %{with apparmor}
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
Recommends:     apparmor-abstractions
%endif

%description
mtail is a tool for extracting metrics from application logs to be exported
into a timeseries database or timeseries calculator for alerting and
dashboarding.

%prep
%autosetup -n %{name}-%{version} -a1

%build
%ifarch ppc64
go build -mod=vendor -o mtail cmd/mtail/main.go
%else
go build -mod=vendor -buildmode=pie -o mtail cmd/mtail/main.go
%endif

%install
# Install the binary
mkdir -p %{buildroot}%{_sbindir}
install -D -m 0755 %{name} "%{buildroot}%{_sbindir}/%{name}"
# Install systemd unit and symbolic link
mkdir -p %{buildroot}%{_unitdir}
install -p -m644 %{SOURCE2} %{buildroot}%{_unitdir}/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
# create config directory and create example config files
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
# create sysconfig file
mkdir -p %{buildroot}%{_fillupdir}
install -D -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}
%if %{with apparmor}
# AppArmor profile
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.%{name}
%endif

%pre
# creating group and user mtail
%{_bindir}/getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name}
%{_bindir}/getent passwd %{name} >/dev/null || \
  %{_sbindir}/useradd -r -g %{name} -d / -s /sbin/nologin \
  -c "%{name} service user" %{name}
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only mtail}
%if %{with apparmor}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.sbin.mtail
%endif

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md
%license LICENSE
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%dir %attr(0750, root, %{name}) %{_sysconfdir}/%{name}
%if %{with apparmor}
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/usr.sbin.%{name}
%endif
%{_fillupdir}/sysconfig.%{name}

%changelog
