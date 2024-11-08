#
# spec file for package mailgraph
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define cgi_dir %{apache_serverroot}/cgi-bin
%define css_dir %{apache_serverroot}/htdocs/css

Name:           mailgraph
Version:        1.14
Release:        0
Summary:        RRDtool frontend for Mail statistics
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            http://mailgraph.schweikert.ch/
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.init
Source2:        %{name}.service
Source3:        %{name}.logrotate
Source4:        %{name}.sysconfig
Source5:        rrdtool.gif
# PATCH-FIX-openSUSE -- rsyslog support, adapt pathnames for daemon_logfile and daemon_rrd_dir to openSUSE
Patch0:         %{name}-1.14-pl.patch
# PATCH-FIX-openSUSE -- adapt/enhance css usage and skip $uri in ref
Patch1:         %{name}-1.14-cgi.patch
# PATCH-FIX-UPSTREAM -- fix font for a tag
Patch2:         %{name}-1.14-css.patch
# PATCH-FIX-openSUSE -- integrate patch from nagios-plugins-mailgraph
Patch3:         mailgraph_for_nagios-plugins-mailgraph.patch
# PATCH-FIX-UPSTREAM -- do not get an image from http://oss.oetiker.ch every time the mailgraph.cgi is called
Patch4:         mailgraph-1.14-tracking.patch
# PATCH-FIX-UPSTREAM -- include postgrey and greylisting graphs in output (and add corresponding options)
Patch5:         mailgraph-1.14-add_postgrey_and_greylisting_support.patch
# PATCH-FIX-UPSTREAM -- handle postscreen in the same way as smtpd
Patch6:         mailgraph-1.14-add_postscreen_support.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
Requires(pre):  %fillup_prereq
Requires:       logrotate
Requires:       postfix
Requires:       rrdtool
Requires:       perl(File::Tail)
Requires:       perl(RRDs)
#
%if 0%{?suse_version} > 1100
Provides:       %{css_dir}
%endif
#
%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%define has_systemd 1
%else
Requires(pre):  %insserv_prereq
%endif

%description
Mailgraph is a very simple mail statistics RRDtool frontend for Postfix
that produces daily, weekly, monthly and yearly graphs of received/sent
and bounced/rejected mail (SMTP traffic).

%package apache
Summary:        Files and dependencies to show mailgraph stats in apache
Group:          Productivity/Networking/Diagnostic
Requires:       %name = %version
Requires:       apache2-mod_perl

%description apache
This package contains files (and dependencies) to show the generated
mailgraph statistics in an apache webserver.

Mailgraph is a very simple mail statistics RRDtool frontend for Postfix
that produces daily, weekly, monthly and yearly graphs of received/sent
and bounced/rejected mail (SMTP traffic).

%prep
%autosetup -p1

%build

%install
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/img
install -d -m 755 %{buildroot}%{_localstatedir}/log/%{name}

install -D -m 755 %{name}.pl %{buildroot}%{_bindir}/%{name}.pl
install -D -m 755 %{name}.cgi %{buildroot}%{cgi_dir}/%{name}.cgi
install -D -m 644 %{name}.css %{buildroot}%{css_dir}/%{name}.css
install -D -m 644 %{S:3} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
install -D -m 644 %{S:4} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -D -m 644 %{S:5} %{buildroot}%{css_dir}/rrdtool.gif

# systemd vs SysVinit
%if 0%{?has_systemd}
install -D -m 0644 %{S:2} %{buildroot}%{_unitdir}/%{name}.service
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}
%else #SysVinit
install -D -m 0755 %{S:1} %{buildroot}/%{_sysconfdir}/init.d/%{name}
ln -sf %{_sysconfdir}/init.d/%{name} %{buildroot}/%{_sbindir}/rc%{name}
%endif

%pre
if [[ -f %{_sysconfdir}/sysconfig/%{name} ]]; then
  sed -i -e 's#^MAILGRAPH_OPTS=" -d -v"$#MAILGRAPH_OPTS=" -v"#'\
    -e 's#^MAILGRAPH_LOG_TYPE=""$#MAILGRAPH_LOG_TYPE="syslog"#'\
    -e 's#^MAILGRAPH_LOG_FILE=""#MAILGRAPH_LOG_FILE="/var/log/mail"#'\
    %{_sysconfdir}/sysconfig/%{name}
fi
%if 0%{?has_systemd}
%service_add_pre %{name}.service
%endif

%preun
%if 0%{?has_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal %{name}
%endif

%post
%if 0%{?has_systemd}
%service_add_post %{name}.service
%{fillup_only mailgraph}
%else
%{fillup_and_insserv mailgraph}
install -d %{_localstatedir}/run/%{name}
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update %{name}
%{insserv_cleanup}
%endif

%files
%defattr(-,root,root)
%doc CHANGES README
%if 0%{?suse_version} >= 01200
%license COPYING
%else
%doc COPYING
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{_fillupdir}/sysconfig.%{name}
%dir %{_localstatedir}/lib/%{name}
%attr(755,wwwrun,www) %dir %{_localstatedir}/lib/%{name}/img
%dir %{_localstatedir}/log/%{name}
%{_bindir}/%{name}.pl
%{_sbindir}/rc%{name}
%if 0%{?has_systemd}
%{_unitdir}/%{name}.service
%else
%{_sysconfdir}/init.d/%{name}
%endif

%files apache
%defattr(-,root,root)
%dir %{apache_serverroot}
%dir %{apache_serverroot}/htdocs
%dir %{cgi_dir}
%{cgi_dir}/%{name}.cgi
%{css_dir}/%{name}.css
%{css_dir}/rrdtool.gif

%changelog
