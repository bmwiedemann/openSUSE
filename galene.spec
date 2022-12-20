#
# spec file for package galene
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


# Remove stripping of Go binaries.
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true
# Project name when using go tooling.
%define project github.com/jech/galene

%bcond_without  apparmor

Name:           galene
Version:        0.6.1
Release:        0
Summary:        Galène videoconferencing server
License:        MIT
Group:          Development/Languages/Other
URL:            https://galene.org/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        %{name}.service
Source3:        %{name}.sysconfig
Source4:        ice-servers.json
Source5:        apparmor-usr.sbin.galene
Patch1:         galene-html-sendselect-default.patch
BuildRequires:  fdupes
BuildRequires:  filesystem
BuildRequires:  go >= 1.16
BuildRequires:  systemd-rpm-macros
Requires:       fdupes
Requires:       filesystem
Requires(pre):  %fillup_prereq
%if %{with apparmor}
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
Recommends:     apparmor-abstractions
%endif

%description
Galène is a videoconferencing server implemented in Go which can be
deployed with moderate server resources.

%prep
%setup -qa1
%patch1 -p1

%build
%ifarch ppc64
go build -mod=vendor
%else
go build -mod=vendor -buildmode=pie
%endif

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
%if %{with apparmor}
%apparmor_reload %{_sysconfdir}/apparmor.d/usr.sbin.galene
%endif

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc CHANGES
%doc INSTALL
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
%dir %attr(0755, root, root) %{_datadir}/%{name}/static/external/fontawesome
%dir %attr(0755, root, root) %{_datadir}/%{name}/static/external/fontawesome/css
%dir %attr(0755, root, root) %{_datadir}/%{name}/static/external/fontawesome/webfonts
%dir %attr(0755, root, root) %{_datadir}/%{name}/static/external/toastify
%dir %attr(0755, root, root) %{_datadir}/%{name}/static/external/contextual
%{_datadir}/%{name}/static/*
%{_datadir}/%{name}/static/external/fontawesome
%{_datadir}/%{name}/static/external/fontawesome/css/*.css
%{_datadir}/%{name}/static/external/fontawesome/webfonts/*
%{_datadir}/%{name}/static/external/toastify/*
%{_datadir}/%{name}/static/external/contextual/*
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%dir %attr(0750, root, %{name}) %{_sysconfdir}/%{name}
%config %attr(0640, root, %{name}) %{_sysconfdir}/%{name}/ice-servers.json.example
%if %{with apparmor}
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/usr.sbin.galene
%endif
%dir %attr(0750, root, %{name}) %{_sharedstatedir}/%{name}
%dir %attr(0570, %{name}, root) %{_sharedstatedir}/%{name}/groups
%dir %attr(0750, %{name}, %{name}) %{_sharedstatedir}/%{name}/recordings
%{_fillupdir}/sysconfig.%{name}

%changelog
