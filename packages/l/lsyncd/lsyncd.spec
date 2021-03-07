#
# spec file for package lsyncd
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           lsyncd
Version:        2.2.3
Release:        0
Summary:        Live Syncing (Mirror) Daemon
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            https://github.com/axkibe/lsyncd
Source0:        https://github.com/axkibe/lsyncd/archive/release-%{version}.tar.gz
Source1:        %{name}.conf
Source2:        rsync_sudo.sh
Source3:        %{name}.service
Source4:        %{name}.sysconfig
Source5:        %{name}.logrotate
Patch0:         lsyncd-lua.patch
Patch1:         lsyncd-man.patch
BuildRequires:  asciidoc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(lua) >= 5.2
BuildRequires:  pkgconfig(systemd)
Requires:       logrotate
Requires:       rsync >= 3.1
%{?systemd_requires}

%description
Lsyncd (Live Syncing (Mirror) Daemon) uses rsync to synchronize local directories with a remote machine running rsyncd. It watches multiple directory trees through inotify. The first step after adding the watches is to rsync all directories with the remote host, and then the software synchronizes single files by collecting the inotify events. lsyncd is a lightweight live mirror solution that should be easy to install and use while blending well with your system.

%prep
%setup -q -n %{name}-release-%{version}
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags}"
%cmake \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_MANDIR=%{_mandir}
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/%{_sbindir} \
   %{buildroot}/%{_sysconfdir}/%{name} \
   %{buildroot}/%{_localstatedir}/log/lsyncd
install -Dm 644 %{SOURCE3} %{buildroot}%{_unitdir}/lsyncd.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}
install -Dm 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/logrotate.d/lsyncd
install -Dm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/lsyncd/lsyncd.conf
install -Dm 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/lsyncd/rsync_sudo.sh
install -Dm 644 %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.%{name}

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc ChangeLog
%{_bindir}/lsyncd
%{_sbindir}/rc%{name}
%{_mandir}/man1/lsyncd.1%{?ext_man}
%{_unitdir}/lsyncd.service
%config(noreplace) %{_sysconfdir}/logrotate.d/lsyncd
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/lsyncd.conf
%config(noreplace) %{_sysconfdir}/%{name}/rsync_sudo.sh
%dir %{_localstatedir}/log/%{name}
%{_fillupdir}/sysconfig.%{name}

%changelog
