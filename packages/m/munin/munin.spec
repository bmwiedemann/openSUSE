#
# spec file for package munin
#
# Copyright (c) 2024 SUSE LLC
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


%define	htmldir /srv/www/htdocs/munin
%define	cgidir /srv/www/cgi-bin
%define	dbdir %{_localstatedir}/lib/munin
%define	logdir %{_localstatedir}/log/munin
%define plugindir %{_prefix}/lib/munin/plugins
%define active_by_default 0
Name:           munin
Version:        2.0.72
Release:        0
Summary:        Network-wide graphing framework (grapher/gatherer)
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://munin-monitoring.org/
Source0:        https://codeload.github.com/munin-monitoring/munin/tar.gz/refs/tags/%{version}#/%{name}-%{version}.tar.gz
Source1:        Makefile.config
Source2:        munin-node.rc
Source3:        munin.cron.d
Source4:        munin.logrotate
Source5:        munin-node.logrotate
Source6:        munin-node.xml
Source7:        plugins.conf
Source8:        munin-node.tmpfiles
Source9:        munin-node.service
Source10:       munin-cgi-graph.service
Source11:       munin-cgi-html.service
# https://github.com/ifad/nginx-munin/archive/master.zip
Source12:       nginx-munin.zip
# https://github.com/ifad/gsa-munin/archive/master.zip
Source13:       gsa-munin.zip
Source14:       munin-cron.timer
Source15:       munin-cron.service
# Source16:       http://downloads.munin-monitoring.org/%{name}/stable/%{version}/%{name}-%{version}.tar.gz.asc
# 0x910846ADEE4C5D67C19B3E6F0A24C05998BA4133
Source17:       munin.keyring
Patch1:         perl526.patch
# PATCH-FIX-UPSTREAM Use IO::Socket::IP instead of IO::Socket::INET[6]
Patch2:         munin-remove-deprecated-INET6.patch
BuildRequires:  firewall-macros
BuildRequires:  html2text
BuildRequires:  htmldoc
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  shadow
BuildRequires:  unzip
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Net::SNMP)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(Net::Server)
BuildRequires:  pkgconfig(systemd)
Requires:       perl-base = %{perl_version}
Requires:       perl-rrdtool
Requires:       rrdtool
Requires:       shadow
Requires:       spawn-fcgi
Requires:       perl(Date::Manip)
Requires:       perl(FCGI)
Requires:       perl(File::Copy::Recursive)
Requires:       perl(HTML::Template)
Requires:       perl(IO::Socket::IP)
Requires:       perl(Log::Log4perl)
Requires:       perl(Munin::Common::Defaults)
Requires:       perl(Net::SNMP)
Requires:       perl(Net::SSLeay)
Requires:       perl(Net::Server)
Requires:       perl(URI)
Recommends:     logrotate
Provides:       group(munin)
Provides:       user(munin)
BuildArch:      noarch
%{?systemd_ordering}
%if 0%{?suse_version} <= 1510
Recommends:     cron
%endif

%description
Munin is a highly flexible and powerful solution used to create graphs of
virtually everything imaginable throughout your network, while still
maintaining a rattling ease of installation and configuration.

This package contains the grapher/gatherer. You will only need one instance of
it in your network. It will periodically poll all the nodes in your network
it's aware of for data, which it in turn will use to create graphs and HTML
pages, suitable for viewing with your graphical web browser of choice.

Munin is written in Perl, and relies heavily on Tobi Oetiker's excellent
RRDtool.

%package node
Summary:        Network-wide graphing framework (node)
# some scripts need logtail which is part of package logdigest in openSUSE
# problem with logdigest is that it installs a cronjob for itself which
# might be unwanted
Group:          System/Monitoring
Requires:       perl-HTML-Template
Requires:       perl-Log-Log4perl
Requires:       perl-Net-SNMP
Requires:       perl-Net-SSLeay
Requires:       perl-Net-Server
Requires:       perl-base = %{perl_version}
Requires:       perl-libwww-perl
Requires:       ps
Requires:       ruby
Requires:       shadow
Requires:       sysstat
Requires(pre):  group(nobody)
Requires(pre):  group(www)
Requires(pre):  user(nobody)
Recommends:     logdigest
Recommends:     logrotate
BuildArch:      noarch
%{?systemd_ordering}

%description node
Munin is a highly flexible and powerful solution used to create graphs of
virtually everything imaginable throughout your network, while still
maintaining a rattling ease of installation and configuration.

This package contains node software. You should install it on all the nodes
in your network. It will know how to extract all sorts of data from the
node it runs on, and will wait for the gatherer to request this data for
further processing.

It includes a range of plugins capable of extracting common values such as
cpu usage, network usage, load average, and so on. Creating your own plugins
which are capable of extracting other system-specific values is very easy,
and is often done in a matter of minutes. You can also create plugins which
relay information from other devices in your network that can't run Munin,
such as a switch or a server running another operating system, by using
SNMP or similar technology.

Munin is written in Perl, and relies heavily on Tobi Oetiker's excellent
RRDtool. To see a real example of Munin in action, take a peek at
<http://www.linpro.no/projects/munin/example/>.

%prep
%setup -q
cp %{SOURCE1} .
unzip %{SOURCE12}
unzip %{SOURCE13}
%patch -P 1 -p1
%patch -P 2 -p1

%build
%__make HOSTNAME=yourhostname

%install
%makeinstall
%__mkdir_p %{buildroot}/%{_sysconfdir}/munin/plugins
%__mkdir_p %{buildroot}/%{_sysconfdir}/munin/munin-conf.d

%__mkdir_p %{buildroot}%{_sysconfdir}/logrotate.d
%__install -m0644 %{SOURCE4} %{buildroot}/%{_sysconfdir}/logrotate.d/munin
%__install -m0644 %{SOURCE5} %{buildroot}/%{_sysconfdir}/logrotate.d/munin-node

%__install -m0644 %{SOURCE7} %{buildroot}/%{_sysconfdir}/munin/plugin-conf.d/munin-node

%__mkdir_p %{buildroot}%{_sbindir}
%__ln_s service %{buildroot}%{_sbindir}/rcmunin-node
%__ln_s service %{buildroot}%{_sbindir}/rcmunin-cgi-graph
%__ln_s service %{buildroot}%{_sbindir}/rcmunin-cgi-html

%__mkdir_p %{buildroot}/%{_prefix}/lib/tmpfiles.d
%__install -m0644 %{SOURCE8} %{buildroot}/%{_prefix}/lib/tmpfiles.d/munin.conf
%__install -m0644 %{SOURCE8} %{buildroot}/%{_prefix}/lib/tmpfiles.d/munin-node.conf
%__mkdir_p %{buildroot}/%{_unitdir}
%__install -m0644 %{SOURCE9} %{buildroot}/%{_unitdir}/munin-node.service
%__install -m0644 %{SOURCE10} %{buildroot}/%{_unitdir}/munin-cgi-graph.service
%__install -m0644 %{SOURCE11} %{buildroot}/%{_unitdir}/munin-cgi-html.service
%if 0%{?suse_version} > 1510
%__install -m0644 %{SOURCE14} %{buildroot}/%{_unitdir}/
%__install -m0644 %{SOURCE15} %{buildroot}/%{_unitdir}/
%else
%__mkdir_p %{buildroot}/%{_sysconfdir}/cron.d
%__install -m0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/cron.d/munin
%endif

%__mkdir_p %{buildroot}/%{logdir}
%__mkdir_p %{buildroot}/%{htmldir}
%__mkdir_p %{buildroot}/%{dbdir}
%__mkdir_p %{buildroot}/%{dbdir}/plugin-state

%__install -m0755 nginx-munin-master/nginx_* %{buildroot}/%{plugindir}
ln nginx-munin-master/README.org README.nginx

%__install -m0755 munin-gsa-master/snmp_* %{buildroot}/%{plugindir}
ln munin-gsa-master/README.md README.gsa

%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}/%{plugindir}/*
%endif

# Fix rpmlint warning: This script uses 'env' as an interpreter.
for F in \
	%{buildroot}/%{_prefix}/lib/munin/plugins/ipmi_sensor_ \
	%{buildroot}/%{_prefix}/lib/munin/plugins/smart_ \
	; do
	sed -i -e 's|^#!%{_bindir}/env python|#!%{_bindir}/python3|' $F
done
for F in \
	%{buildroot}/%{_prefix}/lib/munin/plugins/tomcat_ \
	; do
	sed -i -e 's|^#!%{_bindir}/env ruby|#!%{_bindir}/ruby|' $F
done

# firewalld
install -D -m 644 %{SOURCE6} %{buildroot}%{_prefix}/lib/firewalld/services/munin-node.xml

%pre
getent group munin >/dev/null || %{_sbindir}/groupadd -r munin
getent passwd munin > /dev/null || %{_sbindir}/useradd -r -c "munin monitoring" -d %{dbdir} -g munin munin
%service_add_pre munin-cgi-graph.service
%service_add_pre munin-cgi-html.service
%if 0%{?suse_version} > 1510
%service_add_pre munin-cron.timer
%service_add_pre munin-cron.service
%endif

%post
%tmpfiles_create munin.conf
%service_add_post munin-cgi-graph.service
%service_add_post munin-cgi-html.service
%if 0%{?suse_version} > 1510
%service_add_post munin-cron.timer
%service_add_post munin-cron.service
# update from cron based release
if [ -f  %{_sysconfdir}/cron.d/munin ]; then
  systemctl enable munin-cron.timer || :
  systemctl start munin-cron.timer || :
fi
%endif

%preun
%service_del_preun munin-cgi-graph.service
%service_del_preun munin-cgi-html.service
%if 0%{?suse_version} > 1510
%service_del_preun munin-cron.timer
%service_del_preun munin-cron.service
%endif

%postun
%service_del_postun munin-cgi-graph.service
%service_del_postun munin-cgi-html.service
%if 0%{?suse_version} > 1510
%service_del_postun munin-cron.timer
%service_del_postun munin-cron.service
%endif

## Node
%pre node
getent group munin >/dev/null || %{_sbindir}/groupadd -r munin
getent passwd munin > /dev/null || %{_sbindir}/useradd -r -c "munin monitoring" -d %{dbdir} -g munin munin
%service_add_pre munin-node.service

%post node
if [ $1 = 1 ]; then
%{_sbindir}/munin-node-configure --shell | sh
fi
%tmpfiles_create munin-node.conf
%service_add_post munin-node.service
%firewalld_reload

%preun node
%service_del_preun munin-node.service

%postun node
%service_del_postun munin-node.service

%files
%license COPYING
%doc ChangeLog README UPGRADING
%{_bindir}/munin-check
%{_bindir}/munin-cron
%{_bindir}/munindoc
%dir %{_prefix}/lib/munin
%{_prefix}/lib/munin/munin-graph
%{_prefix}/lib/munin/munin-html
%{_prefix}/lib/munin/munin-datafile2storable
%{_prefix}/lib/munin/munin-storable2datafile
%{_prefix}/lib/munin/munin-limits
%{_prefix}/lib/munin/munin-update
%{_prefix}/lib/munin/DejaVuSans.ttf
%{_prefix}/lib/munin/DejaVuSansMono.ttf
%{cgidir}/munin-cgi-graph
%{cgidir}/munin-cgi-html
%{_prefix}/lib/tmpfiles.d/munin.conf
%{_unitdir}/munin-cgi-graph.service
%{_unitdir}/munin-cgi-html.service
%{_sbindir}/rcmunin-cgi-graph
%{_sbindir}/rcmunin-cgi-html
%if 0%{?suse_version} > 1510
%{_unitdir}/munin-cron.*
%else
%dir %{_sysconfdir}/cron.d
%config %{_sysconfdir}/cron.d/munin
%endif
%attr(0755, munin, munin) %dir %{htmldir}
%attr(0444, munin, munin) %{htmldir}/.htaccess
%dir %{_sysconfdir}/munin
%dir %{_sysconfdir}/munin/munin-conf.d
%dir %{_sysconfdir}/munin/templates
%dir %{_sysconfdir}/munin/static
%config %{_sysconfdir}/munin/templates/*
%config %{_sysconfdir}/munin/static/*
%config(noreplace) %{_sysconfdir}/munin/munin.conf
%config %{_sysconfdir}/logrotate.d/munin
%dir %{perl_vendorlib}/Munin
%dir %{perl_vendorlib}/Munin/Master
%{perl_vendorlib}/Munin/Master/Config.pm
%{perl_vendorlib}/Munin/Master/GraphOld.pm
%{perl_vendorlib}/Munin/Master/Group.pm
%{perl_vendorlib}/Munin/Master/GroupRepository.pm
%{perl_vendorlib}/Munin/Master/HTMLConfig.pm
%{perl_vendorlib}/Munin/Master/HTMLOld.pm
%{perl_vendorlib}/Munin/Master/Host.pm
%{perl_vendorlib}/Munin/Master/LimitsOld.pm
%{perl_vendorlib}/Munin/Master/Logger.pm
%{perl_vendorlib}/Munin/Master/Node.pm
%{perl_vendorlib}/Munin/Master/ProcessManager.pm
%{perl_vendorlib}/Munin/Master/Update.pm
%{perl_vendorlib}/Munin/Master/UpdateWorker.pm
%{perl_vendorlib}/Munin/Master/Utils.pm
%{perl_vendorlib}/Munin/Master/Worker.pm
%{_mandir}/man3/Munin::Master::Config.3pm.gz
%{_mandir}/man3/Munin::Master::Group.3pm.gz
%{_mandir}/man3/Munin::Master::GroupRepository.3pm.gz
%{_mandir}/man3/Munin::Master::HTMLOld.3pm.gz
%{_mandir}/man3/Munin::Master::Host.3pm.gz
%{_mandir}/man3/Munin::Master::LimitsOld.3pm.gz
%{_mandir}/man3/Munin::Master::Logger.3pm.gz
%{_mandir}/man3/Munin::Master::Node.3pm.gz
%{_mandir}/man3/Munin::Master::ProcessManager.3pm.gz
%{_mandir}/man3/Munin::Master::Update.3pm.gz
%{_mandir}/man3/Munin::Master::UpdateWorker.3pm.gz
%{_mandir}/man3/Munin::Master::Utils.3pm.gz
%{_mandir}/man3/Munin::Master::Worker.3pm.gz
%{_mandir}/man5/munin-node.conf.5%{?ext_man}
%{_mandir}/man5/munin.conf.5%{?ext_man}
%{_mandir}/man8/munin-check.8%{?ext_man}
%{_mandir}/man8/munin-cron.8%{?ext_man}
%{_mandir}/man8/munin-graph.8%{?ext_man}
%{_mandir}/man8/munin-html.8%{?ext_man}
%{_mandir}/man8/munin-limits.8%{?ext_man}
%{_mandir}/man8/munin-update.8%{?ext_man}
%{_mandir}/man8/munin.8%{?ext_man}
%attr(0750, munin, munin) %dir %{logdir}
%attr(0755, munin, munin) %dir %{dbdir}
%ghost %attr(0644, munin, munin) %{logdir}/munin-graph.log
%ghost %attr(0644, munin, munin) %{logdir}/munin-html.log
%ghost %attr(0644, munin, munin) %{logdir}/munin-nagios.log
%ghost %attr(0644, munin, munin) %{logdir}/munin-limits.log
%ghost %attr(0644, munin, munin) %{logdir}/munin-update.log
%ghost /run/munin

%files node
%doc README.nginx README.gsa
%{_sbindir}/munin-run
%{_sbindir}/munin-node
%{_sbindir}/munin-node-configure
%{_bindir}/munin-get
%{_prefix}/lib/tmpfiles.d/munin-node.conf
%{_unitdir}/munin-node.service
%dir %{_prefix}/lib/munin
%{_prefix}/lib/munin/munin-async
%{_prefix}/lib/munin/munin-asyncd
%{_prefix}/lib/munin/plugins/
%{_sbindir}/rcmunin-node
%dir %{_sysconfdir}/munin/plugin-conf.d
%dir %{_sysconfdir}/munin/plugins
%config(noreplace) %{_sysconfdir}/munin/plugin-conf.d/munin-node
%config(noreplace) %{_sysconfdir}/munin/munin-node.conf
%config %{_sysconfdir}/logrotate.d/munin-node
%dir %{perl_vendorlib}/Munin/Common
%{perl_vendorlib}/Munin/Common/Config.pm
%{perl_vendorlib}/Munin/Common/Daemon.pm
%{perl_vendorlib}/Munin/Common/Defaults.pm
%{perl_vendorlib}/Munin/Common/TLS.pm
%{perl_vendorlib}/Munin/Common/TLSClient.pm
%{perl_vendorlib}/Munin/Common/TLSServer.pm
%{perl_vendorlib}/Munin/Common/Timeout.pm
%{perl_vendorlib}/Munin/Common/DictFile.pm
%{perl_vendorlib}/Munin/Common/SyncDictFile.pm
%dir %{perl_vendorlib}/Munin/Node
%{perl_vendorlib}/Munin/Node/Config.pm
%dir %{perl_vendorlib}/Munin/Node/Configure
%{perl_vendorlib}/Munin/Node/Configure/Debug.pm
%{perl_vendorlib}/Munin/Node/Configure/History.pm
%{perl_vendorlib}/Munin/Node/Configure/HostEnumeration.pm
%{perl_vendorlib}/Munin/Node/Configure/Plugin.pm
%{perl_vendorlib}/Munin/Node/Configure/PluginList.pm
%{perl_vendorlib}/Munin/Node/Logger.pm
%{perl_vendorlib}/Munin/Node/OS.pm
%{perl_vendorlib}/Munin/Node/SNMPConfig.pm
%{perl_vendorlib}/Munin/Node/Server.pm
%{perl_vendorlib}/Munin/Node/Service.pm
%{perl_vendorlib}/Munin/Node/Session.pm
%{perl_vendorlib}/Munin/Node/Utils.pm
%{perl_vendorlib}/Munin/Node/SpoolReader.pm
%{perl_vendorlib}/Munin/Node/SpoolWriter.pm
%{perl_vendorlib}/Munin/Plugin.pm
%dir %{perl_vendorlib}/Munin/Plugin
%{perl_vendorlib}/Munin/Plugin/Pgsql.pm
%{perl_vendorlib}/Munin/Plugin/SNMP.pm
%{_mandir}/man1/munin-node-configure.1%{?ext_man}
%{_mandir}/man1/munin-node.1%{?ext_man}
%{_mandir}/man1/munin-run.1%{?ext_man}
%{_mandir}/man1/munindoc.1%{?ext_man}
%{_mandir}/man1/munin-get.1%{?ext_man}
%{_mandir}/man3/Munin::Common::Config.3pm.gz
%{_mandir}/man3/Munin::Common::Daemon.3pm.gz
%{_mandir}/man3/Munin::Common::Defaults.3pm.gz
%{_mandir}/man3/Munin::Common::TLS.3pm.gz
%{_mandir}/man3/Munin::Common::TLSClient.3pm.gz
%{_mandir}/man3/Munin::Common::TLSServer.3pm.gz
%{_mandir}/man3/Munin::Common::Timeout.3pm.gz
%{_mandir}/man3/Munin::Node::Config.3pm.gz
%{_mandir}/man3/Munin::Node::Configure::Debug.3pm.gz
%{_mandir}/man3/Munin::Node::Configure::History.3pm.gz
%{_mandir}/man3/Munin::Node::Configure::HostEnumeration.3pm.gz
%{_mandir}/man3/Munin::Node::Configure::Plugin.3pm.gz
%{_mandir}/man3/Munin::Node::Configure::PluginList.3pm.gz
%{_mandir}/man3/Munin::Node::Logger.3pm.gz
%{_mandir}/man3/Munin::Node::OS.3pm.gz
%{_mandir}/man3/Munin::Node::SpoolReader.3pm.gz
%{_mandir}/man3/Munin::Node::SpoolWriter.3pm.gz
%{_mandir}/man3/Munin::Node::SNMPConfig.3pm.gz
%{_mandir}/man3/Munin::Node::Server.3pm.gz
%{_mandir}/man3/Munin::Node::Service.3pm.gz
%{_mandir}/man3/Munin::Node::Session.3pm.gz
%{_mandir}/man3/Munin::Node::Utils.3pm.gz
%{_mandir}/man3/Munin::Plugin.3pm.gz
%{_mandir}/man3/Munin::Plugin::Pgsql.3pm.gz
%{_mandir}/man3/Munin::Plugin::SNMP.3pm.gz
%attr(0750, munin, munin) %dir %{logdir}
%attr(0755, munin, munin) %dir %{dbdir}
%attr(0775, nobody, nobody) %dir %{dbdir}/plugin-state
%ghost %{logdir}/munin-node.log
%ghost /run/munin
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/munin-node.xml

%changelog
