#
# spec file for package nrpe
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# Macro that print mesages to syslog at package (un)install time
%define nnmmsg logger -t %{name}/rpm
%define nrpeport 5666
%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif

%if 0%{?suse_version} >= 1210 || 0%{?centos_version} >= 600
%bcond_without systemd
%else
%bcond_with systemd
%endif

Name:           nrpe
Version:        3.2.1
Release:        0
Summary:        Nagios Remote Plug-In Executor
License:        GPL-2.0-or-later
Group:          System/Monitoring
Url:            http://www.nagios.org/
Source0:        nrpe-%{version}.tar.bz2
Source1:        nrpe.init
Source2:        nagios-nrpe-rpmlintrc
Source3:        nagios-nrpe-SuSEfirewall2
Source4:        nrpe.8
Source5:        check_nrpe.cfg
Source6:        nrpe.service
Source8:        nrpe.socket
Source10:       README.SUSE
Source11:       README.SUSE.systemd-addon
# apparmor profile
Source12:       usr.sbin.nrpe
# PATCH-FIX-UPSTREAM improve help output of nrpe and check_nrpe
Patch2:         nrpe-improved_help.patch
# PATCH-FIX-openSUSE fix pathnames for nrpe_check_control command
Patch4:         nrpe_check_control.patch
# PATCH-FIX-UPSTREAM using implicit definitions of functions
Patch5:         nrpe-implicit_declaration.patch
%if 0%{?suse_version}
PreReq:         %fillup_prereq
PreReq:         %insserv_prereq
%endif
%if 0%{?suse_version} < 1200
PreReq:         /bin/logger
%else
PreReq:         /usr/bin/logger
%endif
PreReq:         coreutils
PreReq:         grep
%if 0%{?suse_version}
PreReq:         netcfg
PreReq:         pwdutils
%endif
PreReq:         sed
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1130
%if 0%{?suse_version} <= 1230
PreReq:         sysvinit(network)
PreReq:         sysvinit(syslog)
%endif
%endif
#
BuildRequires:  monitoring-plugins-common
BuildRequires:  nagios-rpm-macros
%if 0%{?fedora_version} ||  0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  tcp_wrappers-devel
%else
BuildRequires:  tcpd-devel
%endif
#
%if 0%{?suse_version} > 1000 || 0%{?fedora_version} ||  0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  krb5-devel
%else
BuildRequires:  heimdal-devel
%endif
#
%if 0%{?suse_version} > 1020
BuildRequires:  libopenssl-devel
BuildRequires:  openssl
%else
BuildRequires:  openssl-devel
%endif
#
%if 0%{?suse_version} > 1020
Recommends:     inet-daemon
Recommends:     monitoring-plugins-users
Recommends:     monitoring-plugins-load
Recommends:     monitoring-plugins-disk
Recommends:     monitoring-plugins-procs
%else
%if 0%{?suse_version}
Requires:       inet-daemon
%endif
Requires:       monitoring-plugins
%endif
#
Provides:       nagios-nrpe = %{version}
Obsoletes:      nagios-nrpe < 2.14
Provides:       nagios-nrpe-client = %{version}
Obsoletes:      nagios-nrpe-client < %{version}

%if %{with systemd}
BuildRequires:  systemd
%{?systemd_requires}
%endif

%{!?_tmpfilesdir:%global _tmpfilesdir /usr/lib/tmpfiles.d}

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

%description doc
This package contains the README files, OpenOffice and PDF
documentation for the remote plugin executor (NRPE) for Nagios.

%package -n monitoring-plugins-nrpe
Summary:        NRPE plugin
Group:          System/Monitoring
%if 0%{?suse_version} > 1020
Recommends:     monitoring_daemon
%endif
Provides:       nagios-nrpe-server = %{version}-%{release}
Obsoletes:      nagios-nrpe-server < 2.14
Provides:       nagios-plugins-nrpe = %{version}-%{release}
Obsoletes:      nagios-plugins-nrpe < 2.15-%{release}

%description -n monitoring-plugins-nrpe
This package contains the plugin for the host runing the Nagios
daemon.

It is used to contact the NRPE process on remote hosts. The plugin
requests that a plugin be executed on the remote host and wait for the
NRPE process to execute the plugin and return the result.

The plugin then uses the output and return code from the plugin
execution on the remote host for its own output and return code.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch2 -p1
%patch4 -p1
%patch5 -p1
cp -a %{SOURCE10} .
cp -a %{SOURCE12} .
%if 0%{?suse_version} >= 1210
cat %{SOURCE11} >> README.SUSE
%endif
chmod -x contrib/README.nrpe_check_control
%if 0%{?suse_version} > 01110
# increase the number of 'allowed' processes on newer systems:
sed -i "s|check_procs -w 150 -c 200|check_procs -w 250 -c 300|g" sample-config/nrpe.cfg.in  
%endif
# add the new include directory
sed -i "s|#include_dir=<someotherdirectory>|#include_dir=<someotherdirectory>\ninclude_dir=/etc/nrpe.d|g" sample-config/nrpe.cfg.in

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
    --with-piddir=/var/run/nrpe \
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
	--with-nrpe-port=%nrpeport \
	--enable-command-args \
	--enable-bash-command-substitution \
	--enable-ssl
make %{?_smp_mflags} all

gcc %{optflags} -o contrib/nrpe_check_control contrib/nrpe_check_control.c

%install
%nagios_command_user_group_add
install -d %{buildroot}%{_sysconfdir}/xinetd.d
install -d %{buildroot}%{_rundir}/%{name}
%if %{with systemd}
install -d %{buildroot}/usr/lib/tmpfiles.d
%endif
install -d %{buildroot}%{_sysconfdir}/nrpe.d
make install install-config install-inetd install-daemon \
    DESTDIR=%{buildroot} \
    CGICFGDIR="%{_sysconfdir}" \
    NAGIOS_INSTALL_OPTS="" \
    INSTALL_OPTS="" \
    COMMAND_OPTS="" \
    NRPE_INSTALL_OPTS="" \
    INIT_OPTS=""

install -Dm 644 %{SOURCE4} %{buildroot}%{_mandir}/man8/nrpe.8
%if 0%{?suse_version} <= 1230
install -Dm 755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/nrpe
ln -s -f ../../etc/init.d/nrpe %{buildroot}%{_sbindir}/rcnrpe
%else
ln -s -f %{_sbindir}/service %{buildroot}%{_sbindir}/rcnrpe
%endif

# install SuSEfirewall2 script
%if 0%{?suse_version} > 1020
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

%if %{with systemd}
# install systemd specific files
install -Dm644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}.service
%if 0%{?centos_version}
sed -i -e "/User=/s/\(User=\).*/\1%{nagios_user}/" -e "/Group=/s/\(Group=\).*/\1%{nagios_group}/" -e "/Requires=var-run.mount/d" %{buildroot}%{_unitdir}/%{name}.service
%else
sed -i -e "/User=/s/\(User=\).*/\1%{nagios_user}/" -e "/Group=/s/\(Group=\).*/\1%{nagios_group}/" %{buildroot}%{_unitdir}/%{name}.service
%endif
install -Dm644 %{SOURCE8} %{buildroot}%{_unitdir}/%{name}.socket
install -d -m 0755 %{buildroot}/%{_tmpfilesdir}
echo "d %{_rundir}/%{name} 0755 %{nagios_user} %{nagios_group} -" > %{buildroot}/%{_tmpfilesdir}/%{name}.conf
chmod 644 %{buildroot}/%{_tmpfilesdir}/%{name}.conf
%endif

# install config update script in doc dir...
install -Dm755 update-cfg.pl %{buildroot}/%{_defaultdocdir}/%{name}/examples/update-cfg.pl
# ...and also the files we want in the main package
install -m644 CHANGELOG.md README.SUSE README.md usr.sbin.nrpe %{buildroot}/%{_defaultdocdir}/%{name}/
# remove the uninstall script: this is done by RPM
rm %{buildroot}/%{_sbindir}/nrpe-uninstall

%pre
# Create user and group on the system if necessary
%nagios_user_group_add
%nagios_command_user_group_add
# check if the port for nrpe is already defined in /etc/services
if grep -q %nrpeport /etc/services ; then
    : OK - port already defined
else
    %nnmmsg "Adding port %nrpeport to /etc/services"
	echo "nrpe            %nrpeport/tcp # Nagios nrpe" >> etc/services
fi
%if %{with systemd}
 %if 0%{?centos_version}
  #systemd_pre nrpe.service nrpe.socket
 %else
  %service_add_pre nrpe.service nrpe.socket
 %endif
%endif

%preun
%if %{with systemd}
 %if 0%{?centos_version}
  %systemd_preun nrpe.service nrpe.socket
 %else
  %service_del_preun nrpe.service nrpe.socket
 %endif
%else
%stop_on_removal %{name}
%endif

%post
%if 0%{?suse_version} 
 %if 0%{?suse_version} <= 1230
  %{fillup_and_insserv -fy %{name}}
 %else
  %fillup_only %{name}
 %endif
%endif

%if %{with systemd}
 %if 0%{?centos_version}
  %systemd_post nrpe.service nrpe.socket
 %else
  %service_add_post nrpe.service nrpe.socket
  %tmpfiles_create %{_tmpfilesdir}/%{name}.conf
 %endif
%endif

%pre -n monitoring-plugins-nrpe
# Create user and group on the system if necessary
%nagios_user_group_add

%triggerun -- nagios-nrpe < 2.14
STATUS='/var/adm/update-scripts/nrpe'
if [ -x %{_sysconfdir}/init.d/nrpe ]; then
    %{_sysconfdir}/init.d/nrpe status >/dev/null
    if test $? = 0; then
        echo "%{_sysconfdir}/init.d/nrpe restart" >> "$STATUS"
    else
        touch "$STATUS"
    fi
    chmod +x "$STATUS"
fi
if [ -x %{_sysconfdir}/init.d/xinetd ]; then
    %{_sysconfdir}/init.d/xinetd status >/dev/null
    if test $? = 0; then
        echo "%{_sysconfdir}/init.d/xinetd try-restart" >> "$STATUS"
    else
        touch "$STATUS"
    fi
    chmod +x "$STATUS"
fi

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
sed -i "s|nrpe-service|%{name}|g" %{_sysconfdir}/sysconfig/SuSEfirewall2 || :
if [ -e /var/adm/update-scripts/nrpe ]; then
    /bin/sh /var/adm/update-scripts/nrpe
    rm /var/adm/update-scripts/nrpe
fi

%postun
%if 0%{?suse_version}
 %insserv_cleanup
 %if %{with systemd}
  %service_del_postun nrpe.service nrpe.socket
 %else
  %restart_on_update nrpe
 %endif
%endif
%if 0%{?centos_version}
 %systemd_postun_with_restart nrpe.service nrpe.socket
%endif

%files
%defattr(-,root,root)
%dir %{_defaultdocdir}/%{name}/
%dir %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/README.SUSE
%doc %{_defaultdocdir}/%{name}/README.md
%doc %{_defaultdocdir}/%{name}/CHANGELOG.md
%doc %{_defaultdocdir}/%{name}/usr.sbin.nrpe
%doc %{_defaultdocdir}/%{name}//examples/update-cfg.pl
%{_mandir}/man8/nrpe.8*
%dir %{_sysconfdir}/nrpe.d
%config(noreplace) %{_sysconfdir}/nrpe.cfg
%if 0%{?suse_version} > 1315
%dir %{_sysconfdir}/xinetd.d
%endif
%config(noreplace) %{_sysconfdir}/xinetd.d/nrpe
%if 0%{?suse_version} > 1020
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/nrpe
%endif
%if 0%{?suse_version} <= 1230
%{_sysconfdir}/init.d/nrpe
%ghost %dir %{_rundir}/%{name}
%ghost %{_rundir}/%{name}/nrpe.pid
%endif
%if %{with systemd}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.socket
%{_tmpfilesdir}/%{name}.conf
%ghost %dir %{_rundir}/%{name}
%endif
%attr(0755,root,root) %{_sbindir}/nrpe
%{_sbindir}/rcnrpe

%files doc
%defattr(0644,root,root,0755)
%doc CHANGELOG.md LEGAL *.md docs/*.pdf

%files -n monitoring-plugins-nrpe
%defattr(-,root,root)
%doc contrib/README.nrpe_check_control
%dir %{nagios_libdir}
%attr(0755,root,%{nagios_command_group})           %dir %{nagios_sysconfdir}
%attr(0755,root,%{nagios_command_group})           %dir %{nagios_sysconfdir}/objects
%config(noreplace) %{nagios_sysconfdir}/objects/nrpe_check_control.cfg
%config(noreplace) %{nagios_sysconfdir}/objects/check_nrpe.cfg
%{nagios_plugindir}/check_nrpe
%{nagios_plugindir}/nrpe_check_control

%changelog
