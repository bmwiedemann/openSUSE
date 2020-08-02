#
# spec file for package nagios
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


%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} >= 1230
%bcond_without systemd
%else
%bcond_with systemd
%endif

Name:           nagios
Version:        4.4.6
Release:        0
Summary:        The Nagios Network Monitor
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://www.nagios.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        rc%{name}
Source2:        %{name}-exec-start-pre
Source3:        %{name}.sysconfig
Source4:        suse.de-nagios
Source5:        nagios.8
Source6:        nagiosstats.8
Source8:        upgrade_nagios.sh
Source9:        upgrade_nagios.8
Source10:       %{name}-README.SuSE
Source11:       %{name}-html-pages.tar.bz2
Source12:       %{name}.service
Source13:       %{name}.tmpfiles
Source14:       %{name}-archive.timer
Source15:       %{name}-archive.service
Source20:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM unescape hex characters in CGI input - avoid addional '+'
Patch3:         nagios-fix_encoding_trends.cgi.patch
# PATCH-FIX-UPSTREAM return 1 in int main()
Patch4:         nagios-random_data.patch
# PATCH-FIX-OPENSUSE disable Nagios online update checks for distributed packages
Patch11:        nagios-disable_phone_home.patch
# PATCH-FIX-OPENSUSE fake compile time in json sources to avoid problems in OBS
Patch14:        nagios-4.0.6-remove-date-time.patch
# PATCH-FIX-OPENSUSE patch to not truncate performance data
Patch16:        nagios-output-length.patch
# PATCH-FIX-OPENSUSE use KOHANNA if available
Patch17:        nagios-4.1.0-add_KOHANNA.conf
# PATCH-FIX-UPSTREAM allow ppc64le builds in contrib Makefile
Patch18:        nagios-4.4.3-enable-ppc64le.patch
BuildRequires:  doxygen
# yes: we still build for SLE10
%if 0%{?suse_version} > 1020
BuildRequires:  fdupes
%endif
BuildRequires:  bzip2
BuildRequires:  freetype2-devel
BuildRequires:  gd-devel
BuildRequires:  gperf
BuildRequires:  iputils
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  mailx
BuildRequires:  nagios-rpm-macros
BuildRequires:  net-tools
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  unzip
BuildRequires:  zlib-devel
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
Source100:      nagios_systemd
%{?systemd_ordering}
%else
Recommends:     cron
%endif
Provides:       monitoring_daemon
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(pre):  /bin/logger
Requires(pre):  coreutils
Requires(pre):  grep
%if 0%{?suse_version} 
Requires(pre):  %fillup_prereq
%if 0%{?suse_version} < 01200
Requires(pre):  %insserv_prereq
Requires:       cron
%endif
Requires(pre):  shadow
Recommends:     %{name}-www
# this package contains shared tools with icinga
Recommends:     monitoring-tools
Recommends:     icinga-monitoring-tools
Recommends:     %{name}-plugins
%else
Requires(pre):  shadow-utils
%endif
Requires(pre):  permissions
Requires(pre):  sed
Requires:       mailx
%define         nslockfile_dir /var/run/%{name}
%define         nslockfile %nslockfile_dir/%{name}.pid
%define         apache2_sysconfdir %{_sysconfdir}/apache2/conf.d
# Macro that print mesages to syslog at package (un)install time
%define         nnmmsg logger -t %{name}/rpm

%description
Nagios is a program that will monitor hosts and services on your
network. It has the ability to email or page you when a problem arises
and when a problem is resolved. Nagios is written in C and is designed
to run under Linux (and some other *NIX variants) as a background
process, intermittently running checks on various services that you
specify.

The actual service checks are performed by separate "plugin" programs
which return the status of the checks to Nagios. The plugins are
available at http://sourceforge.net/projects/nagiosplug

This package provides core programs for Nagios. The web interface,
documentation, and development files are built as separate packages

%package www
Summary:        Provides the HTML and CGI files for the Nagios web interface
Group:          System/Monitoring
Requires:       %{name} = %{version}
Requires:       gd
Requires:       mod_php_any
Requires:       php
Provides:       monitoring_webfrontend
Requires(pre):  /bin/logger
Requires(pre):  coreutils
Requires(pre):  gawk
Requires(pre):  grep
Requires(pre):  sed
%if 0%{?suse_version}
Requires(pre):  apache2
Requires(pre):  shadow
%else
Requires(pre):  httpd
Requires(pre):  shadow-utils
%endif

%description www
Nagios is a program that will monitor hosts and services on your
network. It has the ability to email or page you when a problem arises
and when a problem is resolved. Nagios is written in C and is designed
to run under Linux (and some other *NIX variants) as a background
process, intermittently running checks on various services that you
specify.

Several CGI programs are included with Nagios in order to allow you to
view the current service status, problem history, notification history,
and log file via the web. This package provides the HTML and CGI files
for the Nagios web interface. In addition, HTML documentation is
included in this package.

%package theme-exfoliation
Summary:        Nagios Core web interface
Group:          System/Monitoring
Requires(pre):  nagios-theme-switcher
Requires:       nagios-www >= 3.0
%if 0%{?suse_version} >= 01210
BuildArch:      noarch
%endif

%description theme-exfoliation
Exfoliation is a simple makeover for the Nagios Core web interface. It consists
of two folders that overlay on a stock Nagios installation.

%package www-dch
Summary:        HTML and CGI files that do not call home
Group:          System/Monitoring
Requires:       %{name}-www = %{version}

%description www-dch
Several CGI programs are included with Nagios in order to allow you to
view the current service status, problem history, notification history,
and log file via the web.

Since Version 3.1, some of those CGI files and the Nagios process itself
try to detect the latest version and fetching news feeds from the upstream
server www.nagios.org.

This additional package provides simply HTML files that do not "call
home" and also allow to run the web interface without PHP support.

There is also an offline version of the documentation included in this
package.

Note: The HTML pages use 'side' and 'main' and frame targets.

%package contrib
Summary:        Files from the contrib directory
Group:          Development/Tools/Other
Requires:       %{name} = %{version}

%description contrib
This package contains all the files from the contrib directory

%package devel
Summary:        Development files for Nagios
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       gcc

%description devel
Nagios is a program that will monitor hosts and services on your
network. It has the ability to email or page you when a problem arises
and when a problem is resolved. Nagios is written in C and is designed
to run under Linux (and some other *NIX variants) as a background
process, intermittently running checks on various services that you
specify.

This package provides include files that Nagios-related applications
may compile against.

%prep
%setup -q -n nagioscore-%{name}-%{version}
%patch3 -p1
%patch4 -p1
%patch11 -p1
%patch14 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
find -name ".gitignore" | xargs rm
# fixing permissions the dirty way....
chmod 644 Changelog LEGAL LICENSE README.md sample-config/README sample-config/template-object/README
# README.SuSE file
sed -e 's@DATADIR@%{_datadir}/%{name}@g' -e 's@SYSCONFDIR@%{nagios_sysconfdir}@g' %{SOURCE10} > README.SUSE
# we do not use /usr/local ...
pushd contrib/eventhandlers 1>/dev/null
for f in $(find . -type f) ; do
    F=$(mktemp temp.XXXXXX)
    sed "s=/usr/local/nagios/var/rw/=%{nagios_spooldir}/=; \
         s=NscaBin\=\"/usr/local/nagios/libexec/send_nsca\"=NscaBin\=\"%{_bindir}/send_nsca\"=; \
         s=NscaCfg\=\"/usr/local/nagios/etc/send_nsca.cfg\"=NscaCfg\=\"%{_sysconfdir}/nsca.cfg\"=; \
         s=/usr/local/nagios/libexec/eventhandlers/=%{nagios_eventhandlerdir}/=; \
         s=/var/nagios/rw/nagios.qh=%{nagios_localstatedir}/nagios.qh=; \
         s=/usr/local/nagios/libexec/=%{nagios_plugindir}/=" ${f} > ${F}
    mv ${F} ${f}
done
popd 1>/dev/null

%build
%configure \
	--prefix=%{_prefix} \
	--exec-prefix=%{_sbindir} \
	--bindir=%{_sbindir} \
	--sbindir=%{nagios_cgidir} \
	--libexecdir=%{nagios_plugindir} \
	--datadir=%{nagios_datadir} \
	--sysconfdir=%{nagios_sysconfdir} \
	--with-init-dir=%{_sysconfdir}/init.d \
	--localstatedir=%{nagios_localstatedir} \
	--with-cgibindir=%{nagios_cgidir} \
	--with-cgiurl=/%{name}/cgi-bin \
	--with-htmurl=/%{name} \
	--with-httpd-conf=%{apache2_sysconfdir} \
	--with-checkresult-dir=%{nagios_spooldir} \
	--with-lockfile=%{nslockfile} \
	--with-nagios-user=%{nagios_user} \
	--with-nagios-group=%{nagios_group} \
	--with-command-user=%{nagios_command_user} \
	--with-command-group=%{nagios_command_group} \
	--with-gd-lib=%{_libdir} \
	--with-gd-inc=%{_includedir} \
	--with-template-objects \
	--with-template-extinfo \
	--with-perlcache \
	--enable-event-broker
#
# make daemonchk.cgi and event handlers
#
make %{?_smp_mflags} all
#
# Build documentation
#
make dox
#
# Build contrib stuff
#
make %{?_smp_mflags} -C contrib

%install
mkdir -p %{buildroot}/%{nagios_logdir}/archives
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%apache2_sysconfdir/
mkdir -p %{buildroot}%nslockfile_dir
make install install-commandmode install-config install-webconf install-classicui\
    DESTDIR=%{buildroot} \
    INSTALL_OPTS="" \
    COMMAND_OPTS="" \
    INIT_OPTS=""
make install -C contrib \
    DESTDIR=%{buildroot} \
    INSTALL_OPTS=""
# install event handlers
install -d -m0755 %{buildroot}/%{nagios_eventhandlerdir}
cp -afpv contrib/eventhandlers/* %{buildroot}%{nagios_eventhandlerdir}/
find %{buildroot}%{nagios_eventhandlerdir}/ -type f -exec chmod +x {} +
# install directory for event brokers like ndoutils
install -d -m0755 %{buildroot}%{nagios_localstatedir}/brokers
# install headers for development package
mkdir -p %{buildroot}%{_includedir}/%{name}/lib
install -p -m644 include/*.h %{buildroot}%{_includedir}/%{name}/
install -m644 lib/*.h %{buildroot}/%{_includedir}/%{name}/lib
#
# cleanup sample-conf dir for including in docdir
#
find sample-config/ -name "*.in" -delete
find sample-config/ -name "*.in.orig" -delete
sed -e 's|command_file=.*|command_file=%{nagios_command_file}|g' \
    -e 's|log_file=/var/lib/nagios/nagios.log|log_file=%{nagios_logdir}/nagios.log|g' \
    -e 's|log_archive_path=/var/lib/nagios/archives|log_archive_path=%{nagios_logdir}/archives|g' \
    -e 's|#query_socket=/var/lib/nagios/rw/nagios.qh|query_socket=%{nagios_localstatedir}/nagios.qh|g' \
    -e 's|^lock_file=.*|lock_file=%nslockfile|g' \
    %{buildroot}/%{nagios_sysconfdir}/nagios.cfg > %{buildroot}%{_sysconfdir}/%{name}/nagios.cfg.tmp
mv %{buildroot}/%{nagios_sysconfdir}/nagios.cfg.tmp %{buildroot}%{_sysconfdir}/%{name}/nagios.cfg
#
# Install documentation
#
cp -fr Documentation/html/* %{buildroot}%{nagios_datadir}/docs/
#
# Install libnagios
#
install -Dm644 lib/libnagios.a %{buildroot}%{_libdir}/libnagios.a
#
# install SuSE specials
#
# init-script
%if %{with systemd}
install -D -m0755 %{SOURCE100} %{buildroot}%{_sbindir}/rc%{name}
install -D -m0755 %{SOURCE2}  %{buildroot}/%{nagios_libdir}/%{name}-exec-start-pre
install -D -m0644 %{SOURCE12} %{buildroot}/%{_unitdir}/%{name}.service
install -D -m0644 %{SOURCE13} %{buildroot}/%{_prefix}/lib/tmpfiles.d/%{name}.conf
%else
install -D -m 0755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/%{name}
ln -sf ../../etc/init.d/%{name} %{buildroot}%{_sbindir}/rc%{name}
touch %{buildroot}%{nslockfile}
%endif
# sysconfig script
install -D -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}
# install cronjob (gzip' the logfiles)
%if %{with systemd}
sed -e 's|__NAGIOS_USER__|%{nagios_user}|g' \
    -e 's|__NAGIOS_GROUP__|%{nagios_group}|g' %{SOURCE4} > %{buildroot}%{_sbindir}/nagios-archive
install -Dm0644 %{SOURCE14} %{buildroot}/%{_unitdir}/nagios-archive.timer
install -Dm0644 %{SOURCE15} %{buildroot}/%{_unitdir}/nagios-archive.service
%else
mkdir %{buildroot}%{_sysconfdir}/cron.weekly
sed -e 's|__NAGIOS_USER__|%{nagios_user}|g' \
    -e 's|__NAGIOS_GROUP__|%{nagios_group}|g' %{SOURCE4} > %{buildroot}%{_sysconfdir}/cron.weekly/%{name}
%endif
# install empty htpasswd file (boo#961115)
touch %{buildroot}%{_sysconfdir}/%{name}/htpasswd.users
# important ghost files
touch %{buildroot}%{nagios_state_retention_file}
touch %{buildroot}%{nagios_status_file}
touch %{buildroot}%{nagios_logdir}/config.err
# install manpages
install -Dm644 %{SOURCE5} %{buildroot}%{_mandir}/man8/%{name}.8
install -Dm644 %{SOURCE6} %{buildroot}%{_mandir}/man8/nagiostats.8
# we use nagios_spooldir for this
test -d %{buildroot}%{nagios_localstatedir}/rw && rmdir %{buildroot}%{nagios_localstatedir}/rw
# install plain html files to allow users to use Nagios without internet connection
# and without PHP at all
pushd %{buildroot}%{nagios_datadir} >/dev/null
tar -xf %{SOURCE11}
sed -i "s|3.4.3|%{version}|g" main.html
popd >/dev/null
# install upgrade script
install -m755 %{SOURCE8} %{buildroot}%{_sbindir}/upgrade_nagios
install -m644 %{SOURCE9} %{buildroot}%{_mandir}/man8/upgrade_nagios.8
# delete monitoring-tools because they are provided by monitoring-tools package
rm -f %{buildroot}/%{_sbindir}/convertcfg
rm -f %{buildroot}/%{_sbindir}/mini_epn
rm -f %{buildroot}/%{_sbindir}/new_mini_epn
# move exfoliation theme to separate folder
mkdir -p %{buildroot}%{_datadir}/nagios-themes/exfoliation
mv %{buildroot}%{nagios_datadir}/{stylesheets,images} %{buildroot}%{_datadir}/nagios-themes/exfoliation/
%if 0%{?suse_version} > 1020
%fdupes %{buildroot}%{_datadir}/nagios-themes/exfoliation/
%endif
mkdir -p %{buildroot}%{nagios_datadir}/{stylesheets,images}
cp -rf html/stylesheets/* %{buildroot}%{nagios_datadir}/stylesheets/
cp -rf html/images/* %{buildroot}%{nagios_datadir}/images/

%pre
# Create user and group on the system if necessary
%nagios_user_group_add
%nagios_command_user_group_add
# update?
if [ ${1:-0} -gt 1 ]; then
  # in the past, group www was used as nagios_command_group - now we use the default: nagcmd
  if id -Gn %{nagios_user} 2>/dev/null | grep -q %{nagios_command_group} >/dev/null 2>&1 ; then
    : # %%{nagios_user} is already in %%nagios_command_group group
  else
    # Add %%{nagios_user} to %%nagios_command_group.
    %if 0%{?suse_version} > 1220
      usermod -a -G %{nagios_command_group} %{nagios_user}
    %else
      groupmod -A %{nagios_user} %{nagios_command_group} 2>/dev/null
    %endif
    %{nnmmsg} "Added %{nagios_user} to %{nagios_command_group}"
  fi
fi
%if %{with systemd}
%service_add_pre %{name}.service %{name}-archive.service %{name}-archive.timer
%endif

%post
# Update ?
if [ ${1:-0} -gt 1 ]; then
  if [ -f %{nagios_sysconfdir}/nagios.cfg ]; then
    %{nnmmsg} "Please run %{_sbindir}/upgrade_nagios %{nagios_sysconfdir}/nagios.cfg to upgrade your installation."
  fi
else
  # First installation: create an alias for the default nagiosadmin user
  if [ -r etc/aliases ]; then
    if ! grep -q "^nagiosadmin:" etc/aliases; then
        echo -e "nagiosadmin:\troot" >> etc/aliases
	    %{nnmmsg} "Added alias for user nagiosadmin to /etc/aliases"
        if [ -x usr/bin/newaliases ]; then
            usr/bin/newaliases &>/dev/null || true
        fi
    fi
  fi
fi
%if %{with systemd}
%service_add_post %{name}.service %{name}-archive.service %{name}-archive.timer
systemd-tmpfiles --create %{_prefix}/lib/tmpfiles.d/%{name}.conf
%fillup_only
%else
%{fillup_and_insserv %{name}}
%if 0%{?sles_version} != 11
%set_permissions /etc/cron.weekly/
%endif
%endif
%if 0%{?sles_version} != 11
%set_permissions /var/spool/nagios/
%endif

%preun
%if %{with systemd}
%service_del_preun %{name}.service %{name}-archive.service %{name}-archive.timer
%else
%stop_on_removal %{name}
%endif

%postun
%if %{with systemd}
%service_del_postun %{name}.service %{name}-archive.service %{name}-archive.timer
%else
%restart_on_update %{name}
%{insserv_cleanup}
%endif

%verifyscript
%if ! %{with systemd}
%verify_permissions -e /etc/cron.weekly/
%endif
%verify_permissions -e /var/spool/nagios/

%post www
wwwusr=%{nagios_command_user}
if [ -f etc/apache2/uid.conf ]; then
    # If apache is installed, and we can find the apache user, set a shell var
    wwwusr=$(awk '/^[ \t]*User[ \t]+[a-zA-Z0-9]+/ {print $2}' etc/apache2/uid.conf)
fi
# if apache user is not in nagios_command_group, add it
if id -Gn $wwwusr 2>/dev/null | grep -q %{nagios_command_group} >/dev/null 2>&1 ; then
    : # $wwwusr (default: %%nagios_command_user) is already in Nagios cmd group
else
    # modify apache user, adding it to nagios_command_group
  %if 0%{?suse_version} > 1220
    usermod -a -G %{nagios_command_group} $wwwusr
  %else
    groupmod -A $wwwusr %{nagios_command_group} 2>/dev/null
  %endif
  %{nnmmsg} "User $wwwusr added to group %{nagios_command_group} so sending commands to Nagios from the CGI is possible."
fi
# Update ?
if [ ${1:-0} -eq 1 ]; then
  if [ -x %{_sbindir}/a2enmod ]; then
    # enable authentification in apache config
      %{_sbindir}/a2enmod authn_file >/dev/null 
      %{_sbindir}/a2enmod auth_basic >/dev/null
      %{_sbindir}/a2enmod authz_user >/dev/null 
      %{_sbindir}/a2enmod version >/dev/null 
      # enable php in apache config
      %if 0%{?sle_version} == 120000 
        %{_sbindir}/a2enmod php5 >/dev/null || :
      %else
        %{_sbindir}/a2enmod php >/dev/null || :
      %endif
  fi
  %if %{with systemd}
  %{_bindir}/systemctl try-restart apache2
  %else
  %restart_on_update apache2
  %endif
fi

%post www-dch
# Update ?
if [ ${1:-0} -eq 1 ]; then
%if %{with systemd}
%{_bindir}/systemctl try-restart apache2
%else
%restart_on_update apache2
%endif
fi

%post theme-exfoliation
if [ ${1:-0} -eq 1 ]; then
    # Only switch the theme if we're not in update mode.
    if [ -x %{_sbindir}/switch-nagios-theme ]; then
        %{_sbindir}/switch-nagios-theme -f exfoliation || :
    fi
fi

%postun theme-exfoliation
if [ ${1:-0} -eq 1 ]; then
    # Only switch the theme if we're not in update mode.
    if [ -x %{_sbindir}/switch-nagios-theme ]; then
        %{_sbindir}/switch-nagios-theme exfoliation || :
    fi
fi

%files
%defattr(0644,root,root,0755)
%doc Changelog LEGAL LICENSE README.md README.SUSE UPGRADING THANKS sample-config/
%dir %{nagios_libdir}
%dir %{nagios_plugindir}
%exclude %{nagios_cgidir}/*
%{_mandir}/man8/%{name}*
%attr(0755,root,root) %{_sbindir}/rc%{name}
%attr(0755,root,root) %{_sbindir}/upgrade_nagios
%{_mandir}/man8/upgrade_nagios.8*
%{_fillupdir}/sysconfig.%{name}
%if %{with systemd}
%attr(0755,root,root) %{nagios_libdir}/%{name}-exec-start-pre
%{_unitdir}/%{name}.service
%{_prefix}/lib/tmpfiles.d/%{name}.conf
%attr(0755,root,root) %{_sbindir}/nagios-archive
%{_unitdir}/nagios-archive.timer
%{_unitdir}/nagios-archive.service
%else
%attr(0755,root,root) %{_sysconfdir}/init.d/%{name}
%ghost %dir %{nslockfile_dir}
%attr(0644,%{nagios_user},%{nagios_group}) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %{nslockfile}
%if 0%{?sles_version} != 11
%dir %{_sysconfdir}/cron.weekly
%endif
%attr(0755,root,root) %{_sysconfdir}/cron.weekly/*
%endif
%config(noreplace) %{nagios_sysconfdir}/*.cfg
%config(noreplace) %{nagios_sysconfdir}/objects/*.cfg
%ghost %config(missingok,noreplace) %{nagios_logdir}/config.err
# directories with special handling:
%attr(0755,root,%{nagios_command_group})           %dir %{nagios_sysconfdir}
%attr(0755,root,%{nagios_command_group})           %dir %{nagios_sysconfdir}/objects
%attr(2775,%{nagios_user},%{nagios_command_group}) %dir %{nagios_spooldir}
%attr(0775,%{nagios_user},%{nagios_command_group}) %dir %{nagios_localstatedir}
%attr(0755,%{nagios_user},%{nagios_group})         %dir %{nagios_logdir}
%attr(0755,%{nagios_user},%{nagios_group})         %dir %{nagios_logdir}/archives
# files with special handling
%config(noreplace) %attr(0640,root,%{nagios_group}) %{nagios_sysconfdir}/resource.cfg
%attr(0600,%{nagios_user},%{nagios_group}) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %{nagios_state_retention_file}
%attr(0664,%{nagios_user},%{nagios_group}) %verify(not md5 size mtime) %ghost %config(missingok,noreplace) %{nagios_status_file}
%attr(0750,root,%{nagios_command_group}) %{_sbindir}/%{name}
%attr(0750,root,%{nagios_command_group}) %{_sbindir}/nagiostats

%files www
%defattr(0644,root,root,0755)
%dir %{nagios_cgidir}
%dir %{nagios_datadir}
%attr(0755,root,root) %{nagios_cgidir}/*
%{nagios_datadir}/*
%config(noreplace) %{apache2_sysconfdir}/%{name}.conf
%attr(0640,root,%nagios_command_group) %config(missingok,noreplace) %{_sysconfdir}/%{name}/htpasswd.users
%exclude %{nagios_datadir}/index.html
%exclude %{nagios_datadir}/main.html
%exclude %{nagios_datadir}/side.html

%files theme-exfoliation
%defattr(0644,root,root,0755)
%dir %{_datadir}/nagios-themes
%{_datadir}/nagios-themes/exfoliation/

%files www-dch
%defattr(0644,root,root,0755)
%{nagios_datadir}/index.html
%{nagios_datadir}/main.html
%{nagios_datadir}/side.html

%files contrib 
%defattr(-,root,root)
%doc contrib/README
%dir %{nagios_eventhandlerdir}
%attr(0755,root,root) %{nagios_eventhandlerdir}/*

%files devel
%defattr(644,root,root,0755)
%{_includedir}/%{name}/
%{_libdir}/libnagios.a

%changelog
