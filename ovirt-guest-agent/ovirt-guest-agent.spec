#
# spec file for package ovirt-guest-agent
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} >= 1210
%define withprefix %_prefix
%else
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
%{!?_initddir: %{expand: %%global _initddir %{_initrddir}}}
%{!?_rundir: %{expand: %%global _rundir %{_localstatedir}/run}}
%{!?_udevrulesdir: %{expand: %%global _udevrulesdir %{?withprefix}/lib/udev/rules.d}}

%global release_version 1
%define         major_version 1.0.14
Name:           ovirt-guest-agent
Version:        %major_version
Release:        %{release_version}%{?dist}
Summary:        The oVirt Guest Agent
License:        Apache-2.0
Group:          System/Monitoring
Url:            http://wiki.ovirt.org/wiki/Category:Ovirt_guest_agent
Source0:        http://resources.ovirt.org/pub/src/ovirt-guest-agent/ovirt-guest-agent-%{major_version}.tar.bz2

%if 0%{?suse_version} >= 1210
BuildRequires:  fdupes
BuildRequires:  systemd
%endif
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  python-devel
BuildRequires:  sudo
BuildRequires:  udev
Requires:       %{name}-common = %{version}-%{release}

%package common
Summary:        Commonly used files of the oVirt Guest Agent
Group:          System/Monitoring
BuildArch:      noarch
%if %{?suse_version} >= 1210
BuildRequires:  python-pep8
%endif
Requires:       python-ethtool >= 0.4-1
Requires:       rpm-python
Requires:       sudo
Requires:       udev >= 095-14.23
Provides:       %{name} = %{version}-%{release}

%description
This is the oVirt management agent running inside the guest. The agent
interfaces with the oVirt manager, supplying heart-beat info as well as
run-time data from within the guest itself. The agent also accepts
control commands to be run executed within the OS (like: shutdown and
restart).

%description common
This is the oVirt management agent running inside the guest. The agent
interfaces with the oVirt manager, supplying heart-beat info as well as
run-time data from within the guest itself. The agent also accepts
control commands to be run executed within the OS (like: shutdown and
restart).

%prep
%setup -q -n ovirt-guest-agent-%{version}
sed "s@/run/ovirt-guest-agent.pid@%{_rundir}/ovirt-guest-agent.pid@g" -i ovirt-guest-agent/ovirt-guest-agent.py

%build

autoreconf -ivf

%configure \
    --with-sudohelper=sudo \
    --without-sso

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

install -d -m 755 -p %{buildroot}%{_sbindir}
%if %{?suse_version} >= 1210
install -d 644 %{buildroot}%{_unitdir}
install -m 644 ovirt-guest-agent/ovirt-guest-agent.service %{buildroot}%{_unitdir}/ovirt-guest-agent.service
ln -s service %{buildroot}%{_sbindir}/rcovirt-guest-agent
%else
install -d -p -m 755 %{buildroot}%{_initrddir}
install -D -m 755 ovirt-guest-agent/ovirt-guest-agent.sles %{buildroot}%{_initrddir}/ovirt-guest-agent
ln -s %{_initddir}/ovirt-guest-agent %{buildroot}%{_sbindir}/rcovirt-guest-agent
%endif
install -d -m 755 -p %{buildroot}%{_udevrulesdir}
/bin/mv %{buildroot}/%{_sysconfdir}/udev/rules.d/55-ovirt-guest-agent.rules %{buildroot}%{_udevrulesdir}/55-ovirt-guest-agent.rules
%if 0%{?suse_version} >= 1210
%fdupes %{buildroot}%{_datadir}/ovirt-guest-agent
%endif

%pre common
# include the sudoers.d directory in /etc/sudoers if it does not already exist
grep "^#includedir %{_sysconfdir}/sudoers.d$" %{_sysconfdir}/sudoers > /dev/null || echo "#includedir %{_sysconfdir}/sudoers.d" >> %{_sysconfdir}/sudoers ||:

getent group ovirtagent >/dev/null || groupadd -r -g 175 ovirtagent
getent passwd ovirtagent > /dev/null || \
    /usr/sbin/useradd -u 175 -g 175 -o -r ovirtagent \
    -c "oVirt Guest Agent" -d %{_datadir}/ovirt-guest-agent -s /sbin/nologin
%if 0%{?suse_version} >= 1210
%service_add_pre ovirt-guest-agent.service
%endif
exit 0

%post common
/sbin/udevadm trigger --subsystem-match="virtio-ports" \
    --attr-match="name=com.redhat.rhevm.vdsm"

%if 0%{?suse_version} >= 1210
%service_add_post ovirt-guest-agent.service
%endif
exit 0

%preun common
if [ "$1" -eq 0 ]
then
%if 0%{?suse_version} >= 1210
    %service_del_preun ovirt-guest-agent.service
%else
    %stop_on_removal ovirt-guest-agent
%endif
    # /bin/systemctl stop ovirt-guest-agent.service > /dev/null 2>&1

    # Send an "uninstalled" notification to vdsm.
    VIRTIO=`grep "^device" %{_sysconfdir}/ovirt-guest-agent.conf | awk '{ print $3; }'`
    if [ -w $VIRTIO ]
    then
        # Non blocking uninstalled notification
        echo -e '{"__name__": "uninstalled"}\n' | dd of=$VIRTIO \
            oflag=nonblock status=noxfer conv=nocreat 1>& /dev/null || :
    fi
fi
exit 0

%postun common
if [ "$1" -eq 0 ]
then
%if 0%{?suse_version} >= 1210
    %service_del_postun ovirt-guest-agent.service
%else
    %insserv_cleanup
%endif
    # Let udev clear access rights
    /sbin/udevadm trigger --subsystem-match="virtio-ports" \
        --attr-match="name=com.redhat.rhevm.vdsm"
fi

if [ "$1" -ge 1 ]; then
%if 0%{?suse_version} >= 1210
    /bin/systemctl try-restart ovirt-guest-agent.service >/dev/null 2>&1 || :
%else
    true
%endif
fi
exit 0

%files common
%defattr(644,root,root,755)

%dir %attr (755,ovirtagent,ovirtagent) %{_localstatedir}/log/ovirt-guest-agent
%dir %attr (755,root,root) %{_datadir}/ovirt-guest-agent
%dir %attr (750,root,root) %{_sysconfdir}/sudoers.d

# Hook configuration directories
%dir %attr (755,root,root) %{_sysconfdir}/ovirt-guest-agent
%dir %attr (755,root,root) %{_sysconfdir}/ovirt-guest-agent/hooks.d
%dir %attr (755,root,root) %{_sysconfdir}/ovirt-guest-agent/hooks.d/before_migration
%dir %attr (755,root,root) %{_sysconfdir}/ovirt-guest-agent/hooks.d/after_migration
%dir %attr (755,root,root) %{_sysconfdir}/ovirt-guest-agent/hooks.d/before_hibernation
%dir %attr (755,root,root) %{_sysconfdir}/ovirt-guest-agent/hooks.d/after_hibernation

# Hook installation directories
%dir %attr (755,root,root) %{_datadir}/ovirt-guest-agent/scripts
%dir %attr (755,root,root) %{_datadir}/ovirt-guest-agent/scripts/hooks/
%dir %attr (755,root,root) %{_datadir}/ovirt-guest-agent/scripts/hooks/defaults
%dir %attr (755,root,root) %{_datadir}/ovirt-guest-agent/scripts/hooks/before_migration
%dir %attr (755,root,root) %{_datadir}/ovirt-guest-agent/scripts/hooks/after_migration
%dir %attr (755,root,root) %{_datadir}/ovirt-guest-agent/scripts/hooks/before_hibernation
%dir %attr (755,root,root) %{_datadir}/ovirt-guest-agent/scripts/hooks/after_hibernation

%config(noreplace) %{_sysconfdir}/ovirt-guest-agent.conf
%config(noreplace) %attr (440,root,root) %{_sysconfdir}/sudoers.d/50_ovirt-guest-agent
%attr (644,root,root) %{_udevrulesdir}/55-ovirt-guest-agent.rules

%doc AUTHORS COPYING NEWS README

%{_datadir}/ovirt-guest-agent/default.conf
%{_datadir}/ovirt-guest-agent/default-logger.conf

%attr (755,root,root) %{_datadir}/ovirt-guest-agent/ovirt-guest-agent.py*
%{_datadir}/ovirt-guest-agent/OVirtAgentLogic.py*
%{_datadir}/ovirt-guest-agent/VirtIoChannel.py*
%{_datadir}/ovirt-guest-agent/GuestAgentLinux2.py*
%{_datadir}/ovirt-guest-agent/timezone.py*
%{_datadir}/ovirt-guest-agent/hooks.py*
%{_datadir}/ovirt-guest-agent/ovirt-locksession
%{_datadir}/ovirt-guest-agent/ovirt-logout
%{_datadir}/ovirt-guest-agent/ovirt-shutdown
%{_datadir}/ovirt-guest-agent/ovirt-hibernate
%{_datadir}/ovirt-guest-agent/ovirt-flush-caches
%{_datadir}/ovirt-guest-agent/ovirt-container-list

# We don't provide single-sign-on support on this distribution
%exclude %{_datadir}/ovirt-guest-agent/CredServer.py*
%exclude %{_sysconfdir}/dbus-1/system.d/org.ovirt.vdsm.Credentials.conf

%{_datadir}/ovirt-guest-agent/scripts/hooks/defaults/55-flush-caches
%attr (755,root,root) %{_datadir}/ovirt-guest-agent/scripts/hooks/defaults/55-flush-caches.sudo
%attr (755,root,root) %{_datadir}/ovirt-guest-agent/scripts/hooks/defaults/flush-caches

# SUDO support script
%attr (755, root, root) %{_datadir}/ovirt-guest-agent/ovirt-hibernate-wrapper.sh
%attr (755, root, root) %{_datadir}/ovirt-guest-agent/ovirt-locksession-wrapper.sh
%attr (755, root, root) %{_datadir}/ovirt-guest-agent/ovirt-logout-wrapper.sh
%attr (755, root, root) %{_datadir}/ovirt-guest-agent/ovirt-shutdown-wrapper.sh
%attr (755, root, root) %{_datadir}/ovirt-guest-agent/ovirt-sudo-wrapper.sh
%attr (755, root, root) %{_datadir}/ovirt-guest-agent/ovirt-container-list-wrapper.sh
%attr (755, root, root) %{_datadir}/ovirt-guest-agent/ovirt-flush-caches-wrapper.sh

# Helper scripts for the daemon
%attr (755,root,root) %{_datadir}/ovirt-guest-agent/LockActiveSession.py*
%attr (755,root,root) %{_datadir}/ovirt-guest-agent/LogoutActiveUser.py*
%attr (755,root,root) %{_datadir}/ovirt-guest-agent/hibernate
%attr (755,root,root) %{_datadir}/ovirt-guest-agent/diskmapper
%attr (755,root,root) %{_datadir}/ovirt-guest-agent/ovirt-osinfo
%attr (755,root,root) %{_datadir}/ovirt-guest-agent/container-list

%config(noreplace) %{_datadir}/ovirt-guest-agent/scripts/hooks/before_hibernation/55_flush-caches
%config(noreplace) %{_datadir}/ovirt-guest-agent/scripts/hooks/before_migration/55_flush-caches
%config(noreplace) %{_sysconfdir}/ovirt-guest-agent/hooks.d/before_hibernation/55_flush-caches
%config(noreplace) %{_sysconfdir}/ovirt-guest-agent/hooks.d/before_migration/55_flush-caches

%if 0%{?suse_version} >= 1210
# systemd service
%{_unitdir}/ovirt-guest-agent.service
%else
# init script
%attr (755,root,root) %{_initddir}/ovirt-guest-agent
%endif
# *suse helper link
%{_sbindir}/rcovirt-guest-agent

%changelog
