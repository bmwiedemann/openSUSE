#
# Copyright (c) 2021 SUSE LLC
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

# Remove stripping of Go binaries.
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
# Project name when using go tooling.
%define project github.com/jech/galene

%if 0%{?suse_version} > 1320
%bcond_without  apparmor_reload
%else
%bcond_with     apparmor_reload
%endif
%bcond_without  apparmor

Name:           galene
Version:        0.2
Release:        0
License:        MIT
Summary:        Galène videoconferencing server
Url:            https://galene.org/
Group:          Development/Languages/Other
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}.service
Source3:        %{name}.sysconfig
Source4:        ice-servers.json
Source5:        apparmor-usr.sbin.galene
BuildRequires:  filesystem
BuildRequires:  fdupes
BuildRequires:  go >= 1.14
BuildRequires:  systemd-rpm-macros
Requires:       filesystem
Requires:       fdupes
Requires(pre): %fillup_prereq
%if %{with apparmor}
%if 0%{?suse_version} <= 1315
BuildRequires:  apparmor-profiles
Recommends:     apparmor-profiles
%else
BuildRequires:  apparmor-abstractions
Recommends:     apparmor-abstractions
%endif
%if %{with apparmor_reload}
BuildRequires:  apparmor-rpm-macros
%endif
%endif

%description
Galène is a videoconferencing server implemented in Go which can be
deployed with moderate server resources.
 
%prep
%setup -qa1

%build
go build \
   -mod=vendor \
   -buildmode=pie ;

%install
%fdupes %{buildroot}/%{_prefix}
# Install the binary
mkdir -p %{buildroot}%{_sbindir}
install -D -m 0755 %{name} "%{buildroot}%{_sbindir}/%{name}"
# Install static web content
for file in $(find static -type f); do
  install -D -m 0644 $file %{buildroot}%{_datadir}/%{name}/$file
done
# Install systemd unit and symbolic link
mkdir -p %{buildroot}%{_unitdir}
install -p -m644 %{SOURCE2} %{buildroot}%{_unitdir}/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
# create config directory and create example config files
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/%{name}/ice-servers.json.example
%if %{with apparmor}
# AppArmor profile
mkdir -p %{buildroot}%{_sysconfdir}/apparmor.d
install -m 0644 %{SOURCE5} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.galene
%endif
# create service directories
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}/groups %{buildroot}%{_sharedstatedir}/%{name}/recordings
# create sysconfig file
mkdir -p %{buildroot}%{_fillupdir}
install -D -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}

%pre
# creating group and user galene
%{_bindir}/getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name}
%{_bindir}/getent passwd %{name} >/dev/null || \
  %{_sbindir}/useradd -r -g %{name} -d / -s /sbin/nologin \
  -c "%{name} service user" %{name}
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only galene}
%if %{with apparmor} && %{with apparmor_reload}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.sbin.galene
%endif

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README
%doc README.FRONTEND
%doc README.PROTOCOL
%if 0%{?suse_version} < 1500
%doc LICENCE
%else
%license LICENCE
%endif
%{_sbindir}/%{name}
%dir %{_datadir}/%{name}
%dir %attr(0755, root, root) %{_datadir}/%{name}/static
%dir %attr(0755, root, root) %{_datadir}/%{name}/static/css
%dir %attr(0755, root, root) %{_datadir}/%{name}/static/scripts
%dir %attr(0755, root, root) %{_datadir}/%{name}/static/webfonts
%{_datadir}/%{name}/static/*
%{_datadir}/%{name}/static/css/*.css
%{_datadir}/%{name}/static/scripts/*.js
%{_datadir}/%{name}/static/webfonts/*
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%dir %attr(0750, root, %{name}) %{_sysconfdir}/%{name}
%config %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/ice-servers.json.example
%config %{_sysconfdir}/apparmor.d/usr.sbin.galene
%dir %attr(0750, root, %{name}) %{_sharedstatedir}/%{name}
%dir %attr(0570, %{name}, root) %{_sharedstatedir}/%{name}/groups
%dir %attr(0750, %{name}, %{name}) %{_sharedstatedir}/%{name}/recordings
%{_fillupdir}/sysconfig.%{name}

%changelog
