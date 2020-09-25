#
# spec file for package cscreen
#
# Copyright (c) 2020 SUSE LLC
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


%define GROUPNAME _cscreen
%define USERNAME _cscreen
%define HOMEDIR %{_localstatedir}/lib/cscreen
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?suse_version} > 1210
%define has_systemd 1
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%else
%define has_systemd 0
Requires(pre):  %insserv_prereq
%endif
Name:           cscreen
Version:        0.8
Release:        0
Summary:        Console screen
License:        BSD-4-Clause
Group:          System/Management
URL:            https://github.com/openSUSE/cscreen
Source:         %{name}-%{version}.tar.xz
Recommends:     logrotate
Requires:       mailx
Requires:       screen
Requires:       sudo
Requires(postun): /usr/bin/rm
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         %fillup_prereq
PreReq:         shadow
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package allows to run multiple consoles in one 'screen' and
to start the screen automatically during boot.

%prep
%setup
#
%build
#
%install
mkdir -p %{buildroot}/%{_sbindir}

%if %{?has_systemd}
install -Dm644 systemd/cscreen.service %{buildroot}/%{_unitdir}/%{name}d.service
pushd %{buildroot}/%{_sbindir}
ln -sf service %{buildroot}%{_sbindir}/rc%{name}d
popd
%else
install -Dm755 systemd/cscreen.init %{buildroot}/%{_sysconfdir}/init.d/cscreend
pushd %{buildroot}/%{_sbindir}
ln -s %{_sysconfdir}/init.d/%{name}d rc%{name}d
popd
%endif

install -Dm640 configs/%{name}.config %{buildroot}/%{_sysconfdir}/%{name}rc
install -Dm644 configs/%{name}.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
install -Dm644 configs/%{name}.sudoers %{buildroot}%{_sysconfdir}/sudoers.d/cscreen
install -Dm644 configs/%{name}.sysconfig %{buildroot}/%{_fillupdir}/sysconfig.%{name}
install -Dm755 src/%{name} %{buildroot}/%{_bindir}/%{name}
install -Dm755 src/%{name}_update_config.sh %{buildroot}/%{_bindir}/cscreen_update_config.sh

mkdir -p %{buildroot}%{_localstatedir}/log/screen/old
mkdir -pm700 %{buildroot}/%{HOMEDIR}
mkdir -pm700 %{buildroot}/%{HOMEDIR}/.ssh

%pre
%if %{?has_systemd}
%service_add_pre %{name}d.service
%endif
getent group %{GROUPNAME} >/dev/null || groupadd -r %{GROUPNAME}
if getent group tty >/dev/null;then
    TTY_GROUP="-G tty"
    if getent group dialout >/dev/null;then
	TTY_GROUP="$TTY_GROUP,dialout"
    fi
else
    TTY_GROUP=""
    echo "WARNING: Could not find tty group"
fi
getent passwd %{USERNAME} >/dev/null || \
    useradd -r -g %{GROUPNAME} -d %{HOMEDIR} -s /bin/bash \
	    -c "cscreen daemon user" %{USERNAME} $TTY_GROUP

%post
%if %{?has_systemd}
%service_add_post %{name}d.service
%else
%{fillup_and_insserv %{name}d }
%endif
%fillup_only %{name}

%preun
%if %{?has_systemd}
%service_del_preun %{name}d.service
%else
%stop_on_removal %{name}d
%endif

%postun
%if %{?has_systemd}
%if %{defined service_del_postun_without_restart}
%service_del_postun_without_restart %{name}d.service
%else
DISABLE_RESTART_ON_UPDATE=yes
%service_del_postun %{name}d.service
%endif
%else
%restart_on_update %{name}d
%insserv_cleanup
%endif
if [ -d /run/uscreens/S-cscreen ];then
    if [ "$1" = "0" ];then
	# Only delete on uninstall
	rm -rf /run/uscreens/S-cscreen
    fi
fi

%files
%defattr(-,root,root)
%doc docs/motd_example
%if 0%{?suse_version} > 1315
%license License
%endif
%{_bindir}/%{name}
%{_bindir}/cscreen_update_config.sh
%if %{?has_systemd}
%{_unitdir}/cscreend.service
%else
%{_sysconfdir}/init.d/cscreend
%endif
%{_sbindir}/rc%{name}d

%attr(0750,root,root) %dir %{_sysconfdir}/sudoers.d
%attr(0640,root,root) %config %{_sysconfdir}/sudoers.d/cscreen
%attr(755,%{USERNAME}, %{GROUPNAME}) %dir %{_localstatedir}/log/screen
%attr(755,%{USERNAME}, %{GROUPNAME}) %dir %{_localstatedir}/log/screen/old
%attr(644,%{USERNAME}, %{GROUPNAME}) %{_fillupdir}/sysconfig.%{name}
%attr(700,%{USERNAME}, %{GROUPNAME}) %dir %{HOMEDIR}
%attr(700,%{USERNAME}, %{GROUPNAME}) %dir %{HOMEDIR}/.ssh
%attr(644,%{USERNAME}, %{GROUPNAME}) %config(noreplace) %{_sysconfdir}/%{name}rc
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%changelog
