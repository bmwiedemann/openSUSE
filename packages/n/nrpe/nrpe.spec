#
# spec file for package nrpe
#
# Copyright (c) 2023 SUSE LLC
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


%define nnmmsg logger -t %{name}/rpm
%define nrpeport 5666
%if ! %{defined _rundir}
  %define _rundir %{_localstatedir}/run
%endif
%{!?_tmpfilesdir:%global _tmpfilesdir %{_prefix}/lib/tmpfiles.d}
%if 0%{?suse_version} >= 1210 || 0%{?centos_version} >= 600
  %bcond_without systemd
%else
  %bcond_with systemd
%endif
%if 0%{?suse_version} >= 01500
  %bcond_without firewalld
%else
  %bcond_with firewalld
%endif
%if 0%{?suse_version} >= 01500
%bcond_without reproducable
%else
%bcond_with reproducable
%endif
Name:           nrpe
Version:        4.0.3
Release:        0
Summary:        Nagios Remote Plug-In Executor
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://www.nagios.org/
Source0:        nrpe-%{version}.tar.bz2
Source1:        nrpe.init
Source2:        nrpe-rpmlintrc
Source3:        nrpe-SuSEfirewall2
Source4:        nrpe.8
Source5:        check_nrpe.cfg
Source10:       README.SUSE
Source11:       README.SUSE.systemd-addon
Source12:       usr.sbin.nrpe
Source13:       nrpe.xml
Source14:       nrpe-dh.h
# PATCH-FIX-UPSTREAM improve help output of nrpe and check_nrpe
Patch2:         nrpe-improved_help.patch
# PATCH-FIX-openSUSE fix pathnames for nrpe_check_control command
Patch4:         nrpe_check_control.patch
# PATCH-FIX-UPSTREAM using implicit definitions of functions
Patch5:         nrpe-implicit_declaration.patch
# PATCH-FIX-openSUSE patch used to NOT re-calculate dh.h parameters (for reproducable builds)
Patch6:         nrpe-static_dh_parameters.patch
# PATCH-FIX-openSUSE disable chkconfig call in Makefile
Patch7:         nrpe-disable-chkconfig_in_Makefile.patch
# PATCH-FIX-UPSTREAM this fills up the logs on the clients without real need
Patch8:         nrpe-4.0.4-silence_wrong_package_version_messages.patch
BuildRequires:  nagios-rpm-macros
Requires(pre):  grep
Requires(pre):  sed
Provides:       nagios-nrpe = %{version}
Obsoletes:      nagios-nrpe < 2.14
Provides:       nagios-nrpe-client = %{version}
Obsoletes:      nagios-nrpe-client < %{version}
PreReq:         %fillup_prereq
%if 0%{?suse_version} < 1200
PreReq:         %insserv_prereq
PreReq:         /bin/logger
%else
Requires(pre):  %{_bindir}/logger
%endif
%if 0%{?suse_version} > 1130
%if 0%{?suse_version} <= 1230
Requires(pre):  sysvinit(network)
Requires(pre):  sysvinit(syslog)
%endif
%endif
BuildRequires:  krb5-devel
%if 0%{?suse_version}
Requires(pre):  netcfg
Requires(pre):  pwdutils
BuildRequires:  libopenssl-devel
BuildRequires:  monitoring-plugins-common
BuildRequires:  tcpd-devel
%endif
%if 0%{?fedora_version}
Requires(pre):  shadow-utils
BuildRequires:  nagios-plugins-all
BuildRequires:  openssl-devel
BuildRequires:  tcp_wrappers-devel
%endif
BuildRequires:  openssl
Recommends:     inet-daemon
Recommends:     monitoring-plugins-disk
Recommends:     monitoring-plugins-load
Recommends:     monitoring-plugins-procs
Recommends:     monitoring-plugins-users
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
NRPE can be used to run Nagios plugins on a remote machine for
executing local checks.
This package contains the software for NRPE server.
It could be run by an inetd, or as a standalone daemon.

%package doc
Summary:        Nagios Remote Plug-In Executor documentation
Group:          Documentation/Other
Provides:       nagios-nrpe-doc = %{version}
Obsoletes:      nagios-nrpe-doc < 2.14
%if 0%{?suse_version} >= 1230
BuildArch:      noarch
%endif

%description doc
This package contains the README files, OpenOffice and PDF
documentation for the remote plugin executor (NRPE) for Nagios.

%package -n monitoring-plugins-nrpe
Summary:        NRPE plugin
Group:          System/Monitoring
Provides:       nagios-nrpe-server = %{version}-%{release}
Obsoletes:      nagios-nrpe-server < 2.14
Provides:       nagios-plugins-nrpe = %{version}-%{release}
Obsoletes:      nagios-plugins-nrpe < 2.15-%{release}
%if 0%{?suse_version} > 1020
Recommends:     monitoring_daemon
%endif

%description -n monitoring-plugins-nrpe
This package contains the plugin for the host runing the Nagios
daemon.

It is used to contact the NRPE process on remote hosts. The plugin
requests that a plugin be executed on the remote host and wait for the
NRPE process to execute the plugin and return the result.

The plugin then uses the output and return code from the plugin
execution on the remote host for its own output and return code.

%prep
%setup -q -n %{name}-%{version}
%patch2 -p1
%patch4 -p1
%patch5 -p1
%if %{with reproducable}
%patch6 -p1
install -m644 %{SOURCE14} include/dh.h
%endif
%patch7 -p1
%patch8 -p1
cp -a %{SOURCE10} .
cp -a %{SOURCE12} .
%if 0%{?suse_version} >= 1210
cat %{SOURCE11} >> README.SUSE
%endif
chmod -x contrib/README.nrpe_check_control
# increase the number of 'allowed' processes on newer systems:
sed -i "s|check_procs -w 150 -c 200|check_procs -w 350 -c 400|g" sample-config/nrpe.cfg.in
# add the new include directory
sed -i "s|#include_dir=<someotherdirectory>|#include_dir=<someotherdirectory>\ninclude_dir=%{_sysconfdir}/nrpe.d|g" sample-config/nrpe.cfg.in

%build
%configure \
    --sbindir=%{nagios_cgidir} \
    --libexecdir=%{nagios_plugindir} \
    --datadir=%{nagios_datadir} \
    --sysconfdir=%{_sysconfdir} \
    --with-pkgsysconfdir=%{_sysconfdir} \
    --localstatedir=%{nagios_logdir} \
    --exec-prefix=%{_sbindir} \
    --bindir=%{_sbindir} \
    --sbindir=%{_sbindir} \
    --with-logdir=%{nagios_logdir} \
    --with-piddir=%{_rundir}/%{name} \
    --with-pluginsdir=%{nagios_plugindir} \
    --enable-install-method=os \
    --with-dist-type=suse \
%if %{with systemd}
    --with-init-type=systemd \
%else
    --with-init-type=sysv \
%endif
    --with-inetd-type=xinetd \
    --with-log_facility=daemon \
    --with-kerberos-inc=%{_includedir} \
    --with-nagios-user=%{nagios_user} \
    --with-nagios-group=%{nagios_group} \
    --with-nrpe-user=%{nagios_user} \
    --with-nrpe-group=%{nagios_group} \
    --with-nrpe-port=%{nrpeport} \
    --enable-command-args \
    --enable-bash-command-substitution \
    --enable-ssl
make %{?_smp_mflags} all

gcc %{optflags} -o contrib/nrpe_check_control contrib/nrpe_check_control.c

%install
install -d %{buildroot}%{_sysconfdir}/xinetd.d
install -d %{buildroot}%{_rundir}/%{name}
%if %{with systemd}
install -d %{buildroot}%{_tmpfilesdir}/
install -d %{buildroot}%{_unitdir}/
%else
install -d %{buildroot}%{_sysconfdir}/init.d/
%endif
install -d %{buildroot}%{_sysconfdir}/nrpe.d
make install install-config install-inetd install-daemon install-init \
    DESTDIR=%{buildroot} \
    CGICFGDIR="%{_sysconfdir}" \
    NAGIOS_INSTALL_OPTS="" \
    INSTALL_OPTS="" \
    COMMAND_OPTS="" \
    NRPE_INSTALL_OPTS="" \
    INIT_OPTS=""

install -Dm 644 %{SOURCE4} %{buildroot}%{_mandir}/man8/nrpe.8

%if %{with systemd}
  sed -i -e "/User=/s/\(User=\).*/\1%{nagios_user}/" -e "/Group=/s/\(Group=\).*/\1%{nagios_group}/" %{buildroot}%{_unitdir}/%{name}.service
  install -Dm644 startup/default-socket %{buildroot}%{_unitdir}/%{name}.socket
  ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rcnrpe
%else
  %if 0%{?suse_version} <= 1230
    # openSUSE uses own nrpe init script
    rm %{buildroot}%{_sysconfdir}/init.d/nrpe
    install -Dm 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/nrpe
    ln -s -f ../..%{_initddir}/nrpe %{buildroot}%{_sbindir}/rcnrpe
  %endif
%endif

%if %{without firewalld}
  # install SuSEfirewall2 script
  install -Dm644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/nrpe
%endif

# fix pid_file in nrpe.cfg
sed -i -e "s,^\(pid_file=\).*,\1%{_rundir}/%{name}/nrpe.pid," %{buildroot}/%{_sysconfdir}/nrpe.cfg

# create directory and pidfile (package them as ghost)
%if 0%{?suse_version} <= 1230
mkdir -p %{buildroot}%{_rundir}/%{name}
touch %{buildroot}%{_rundir}/%{name}/nrpe.pid
%endif

# create home directory of nagios user
mkdir -p %{buildroot}%{nagios_localstatedir}

# create contrib plugin
install -m0755 contrib/nrpe_check_control %{buildroot}%{nagios_plugindir}/nrpe_check_control
cat > nrpe_check_control.cfg <<'EOF'
define command {
    command_name    nrpe_check_control
    command_line    %{nagios_plugindir}/nrpe_check_control $SERVICESTATE$ $SERVICESTATETYPE$ $SERVICEATTEMPT$ "$HOSTNAME$"
}
EOF
install -Dm0644 nrpe_check_control.cfg %{buildroot}%{nagios_sysconfdir}/objects/nrpe_check_control.cfg

# install simple nrpe.cfg for the Nagios server in the objects directory
install -Dm644 %{SOURCE5} %{buildroot}%{nagios_sysconfdir}/objects/check_nrpe.cfg

install -Dm755 update-cfg.pl %{buildroot}/%{_defaultdocdir}/%{name}/examples/update-cfg.pl
# ...and also the files we want in the main package
install -m644 CHANGELOG.md README.SUSE README.md usr.sbin.nrpe %{buildroot}/%{_defaultdocdir}/%{name}/
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/local
echo "# Site-specific additions and overrides for 'usr.sbin.nrpe'" > %{buildroot}/%{_defaultdocdir}/%{name}/local/usr.sbin.nrpe
# remove the uninstall script: this is done by RPM
rm %{buildroot}/%{_sbindir}/nrpe-uninstall

%if 0%{?suse_version} >= 1599
# remove xinetd snipplets on newer distribution, where we do not support xinetd any longer
rm -rf %{buildroot}%{_sysconfdir}/xinetd.d
%endif

%pre
# Create user and group on the system if necessary
%nagios_user_group_add
%nagios_command_user_group_add
# check if the port for nrpe is already defined in /etc/services
if getent services nrpe >/dev/null ; then
    : OK - port already defined
else
    %{nnmmsg} "Adding port %{nrpeport} to %{_sysconfdir}/services"
	echo "nrpe            %{nrpeport}/tcp # Nagios nrpe" >> etc/services
fi
%if %{with systemd}
  %service_add_pre nrpe.service nrpe.socket
%endif

%preun
%if %{with systemd}
  %service_del_preun nrpe.service nrpe.socket
%else
  %stop_on_removal %{name}
%endif

%post
%if 0%{?suse_version} <= 1230
  %{fillup_and_insserv -fy %{name}}
%else
  %fillup_only %{name}
%endif

%if %{with systemd}
  %service_add_post nrpe.service nrpe.socket
  %tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%endif

%pre -n monitoring-plugins-nrpe
# Create user and group on the system if necessary
%nagios_user_group_add

%triggerun -- nagios-nrpe < 2.14
STATUS='%{_localstatedir}/adm/update-scripts/nrpe'
%if %{with systemd}
  if systemctl -q is-enabled nrpe.service ; then
    echo "systemctl -q restart nrpe.service" >> "$STATUS"
  elif systemctl -q is-enabled xinetd.service ; then
    echo "systemctl -q reload xinetd.service" >> "$STATUS"
  else
    # JFYI: no need to restart the nrpe.socket
    touch "$STATUS"
  fi
%else
  if [ -x %{_sysconfdir}/init.d/nrpe ]; then
    %{_sysconfdir}/init.d/nrpe status >/dev/null
    if test $? = 0; then
        echo "%{_sysconfdir}/init.d/nrpe restart" >> "$STATUS"
    else
        touch "$STATUS"
    fi
  fi
  if [ -x %{_sysconfdir}/init.d/xinetd ]; then
    %{_sysconfdir}/init.d/xinetd status >/dev/null
    if test $? = 0; then
        echo "%{_sysconfdir}/init.d/xinetd try-restart" >> "$STATUS"
    fi
  else
    touch "$STATUS"
  fi
%endif
chmod +x "$STATUS"

%triggerpostun -- nagios-nrpe < 2.14
# Move /etc/nagios/nrpe.cfg to /etc/nrpe.cfg when updating from an old version
# and inform the admin about the rename.
if test -e %{nagios_sysconfdir}/nrpe.cfg.rpmsave -a ! -e %{_sysconfdir}/nrpe.cfg.rpmnew; then
    mv %{_sysconfdir}/nrpe.cfg %{_sysconfdir}/nrpe.cfg.rpmnew
    mv %{nagios_sysconfdir}/nrpe.cfg.rpmsave %{_sysconfdir}/nrpe.cfg
    echo "# %{nagios_sysconfdir}/nrpe.cfg has been moved to %{_sysconfdir}/nrpe.cfg" > %{nagios_sysconfdir}/nrpe.cfg
    echo "# This file can be removed." >> %{nagios_sysconfdir}/nrpe.cfg
    echo "include=%{_sysconfdir}/nrpe.cfg" >> %{nagios_sysconfdir}/nrpe.cfg
fi
sed -i "s|%{nagios_sysconfdir}/nrpe.cfg|%{_sysconfdir}/nrpe.cfg|g" %{_sysconfdir}/xinetd.d/nrpe || :
%if %{without firewalld}
sed -i "s|nrpe-service|%{name}|g" %{_sysconfdir}/sysconfig/SuSEfirewall2 || :
%endif
if [ -e %{_localstatedir}/adm/update-scripts/nrpe ]; then
    /bin/sh %{_localstatedir}/adm/update-scripts/nrpe
    rm %{_localstatedir}/adm/update-scripts/nrpe
fi

%postun
%if %{with systemd}
  %service_del_postun nrpe.service nrpe.socket
 %else
  %restart_on_update nrpe
  %if 0%{?suse_version}
    %insserv_cleanup
  %endif
%endif

%files
%defattr(-,root,root)
%dir %{_defaultdocdir}/%{name}/
%dir %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/README.SUSE
%doc %{_defaultdocdir}/%{name}/README.md
%doc %{_defaultdocdir}/%{name}/CHANGELOG.md
%doc %{_defaultdocdir}/%{name}/usr.sbin.nrpe
%dir %{_defaultdocdir}/%{name}/local
%doc %{_defaultdocdir}/%{name}/local/usr.sbin.nrpe
%doc %{_defaultdocdir}/%{name}/examples/update-cfg.pl
%{_mandir}/man8/nrpe.8%{?ext_man}
%dir %{_sysconfdir}/nrpe.d
%config(noreplace) %{_sysconfdir}/nrpe.cfg
%if 0%{?suse_version} > 1315 && 0%{?suse_version} < 1599
%dir %{_sysconfdir}/xinetd.d
%config(noreplace) %{_sysconfdir}/xinetd.d/nrpe
%endif
%if %{without firewalld}
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/nrpe
%endif
%if 0%{?suse_version} <= 1230
%ghost %{_rundir}/%{name}/nrpe.pid
%endif
%if %{with systemd}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_tmpfilesdir}/%{name}.conf
%else
%{_sysconfdir}/init.d/nrpe
%endif
%ghost %dir %{_rundir}/%{name}
%attr(0755,root,root) %{_sbindir}/nrpe
%{_sbindir}/rcnrpe

%files doc
%defattr(-,root,root)
%defattr(0644,root,root,0755)
%doc CHANGELOG.md LEGAL *.md docs/*.pdf

%files -n monitoring-plugins-nrpe
%defattr(-,root,root)
%doc contrib/README.nrpe_check_control
%dir %{nagios_libdir}
%attr(0755,root,%{nagios_command_group}) %dir %{nagios_sysconfdir}
%attr(0755,root,%{nagios_command_group}) %dir %{nagios_sysconfdir}/objects
%config(noreplace) %{nagios_sysconfdir}/objects/nrpe_check_control.cfg
%config(noreplace) %{nagios_sysconfdir}/objects/check_nrpe.cfg
%{nagios_plugindir}/check_nrpe
%{nagios_plugindir}/nrpe_check_control

%changelog
