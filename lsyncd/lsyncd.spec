#
# spec file for package lsyncd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} > 1230
%bcond_without systemd
%else
%bcond_with    systemd
%endif

Name:           lsyncd
Version:        2.2.3
Release:        0
Url:            https://github.com/axkibe/lsyncd
Source0:        https://github.com/axkibe/lsyncd/archive/release-%{version}.tar.gz
Source1:        %{name}-init.d
Source2:        %{name}.conf
Source3:        rsync_sudo.sh
Source4:        %{name}.service
Source5:        %{name}.sysconfig
Source6:        %{name}.logrotate
Patch0:         lsyncd-lua.patch
Patch1:         lsyncd-man.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(lua) >= 5.2
%if %{with systemd}
%{?systemd_requires}
BuildRequires:  systemd-rpm-macros
%else
PreReq:         %insserv_prereq 
%endif
PreReq:         %fillup_prereq
Requires:       logrotate
Requires:       rsync >= 3.1
Summary:        Live Syncing (Mirror) Daemon
License:        GPL-2.0-only
Group:          Productivity/Networking/Other

%description
Lsyncd (Live Syncing (Mirror) Daemon) uses rsync to synchronize local directories with a remote machine running rsyncd. It watches multiple directory trees through inotify. The first step after adding the watches is to rsync all directories with the remote host, and then the software synchronizes single files by collecting the inotify events. lsyncd is a lightweight live mirror solution that should be easy to install and use while blending well with your system.

%prep
%setup -q -n %{name}-release-%{version}
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%optflags"
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_INSTALL_MANDIR=%{_mandir}
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}/%{_sbindir} \
   %{buildroot}/%{_sysconfdir}/%{name} \
   %{buildroot}/%{_localstatedir}/log/lsyncd
%if %{with systemd}
install -Dm 644 %{S:4} %{buildroot}%{_unitdir}/lsyncd.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}
install -Dm 644 %{S:6} %{buildroot}%{_sysconfdir}/logrotate.d/lsyncd
%else
install -Dm 755 %{S:1} %{buildroot}/%{_initrddir}/lsyncd
ln -fs %{_sysconfdir}/init.d/lsyncd %{buildroot}%{_sbindir}/rc%{name}
%endif
install -Dm 644 %{S:2} %{buildroot}%{_sysconfdir}/lsyncd/lsyncd.conf
install -Dm 755 %{S:3} %{buildroot}%{_sysconfdir}/lsyncd/rsync_sudo.sh
install -Dm 644 %{S:5} %{buildroot}%{_fillupdir}/sysconfig.%{name}

%if %{with systemd}
%pre
%service_add_pre lsyncd.service
%endif

%post
%if %{with systemd}
%service_add_post lsyncd.service
%{fillup_only}
%else
%{fillup_and_insserv}
%endif

%if %{with systemd}
%preun
%service_del_preun lsyncd.service
%endif

%postun
%if %{with systemd}
%service_del_postun lsyncd.service
%else
%{restart_on_update}
%{insserv_cleanup}
%endif

%files
%defattr(-,root,root)
%doc ChangeLog COPYING
%{_bindir}/lsyncd
%{_mandir}/man1/lsyncd.1.gz
%if %{with systemd}
%{_unitdir}/lsyncd.service
%config(noreplace) %{_sysconfdir}/logrotate.d/lsyncd
%else
%{_initrddir}/lsyncd
%endif
%{_sbindir}/rc%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/lsyncd.conf
%config(noreplace) %{_sysconfdir}/%{name}/rsync_sudo.sh
%dir %{_localstatedir}/log/%{name}
%{_fillupdir}/sysconfig.%{name}

%changelog
