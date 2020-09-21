#
# spec file for package apache2
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define src_name        httpd-%{version}
%define apache_mmn	%(test -s %{SOURCE0} && { echo -n apache_mmn_; bzcat %{SOURCE0} | awk '/^#define MODULE_MAGIC_NUMBER_MAJOR/ {printf "%d", $3}'; } || echo apache_mmn_notfound)
%define suse_maintenance_mmn  0
%define	default_mpm	prefork
%define mpms_to_build	prefork worker event
%define datadir		/srv/www
%define htdocsdir	%{datadir}/htdocs
%define manualdir	%{_datadir}/%{name}/manual
%define errordir	%{_datadir}/%{name}/error
%define iconsdir	%{_datadir}/%{name}/icons
%define cgidir		%{datadir}/cgi-bin
%define localstatedir	%{_localstatedir}/lib/%{name}
%define proxycachedir 	%{_localstatedir}/cache/%{name}
%define logfiledir	%{_localstatedir}/log/%{name}
%define sysconfdir	%{_sysconfdir}/%{name}
%define includedir 	%{_includedir}/%{name}
%define libexecdir	%{_libdir}/%{name}
%define installbuilddir	%{_datadir}/%{name}/build
%define userdir		public_html
%define suexec_safepath	%{_prefix}/local/bin:%{_prefix}/bin:/bin
%define platform_string	Linux/SUSE
%define httpduser wwwrun
%define httpdgroup www
#for some reason the parser barfs if not conditional
%{?requires_ge:%requires_ge libapr1}
%{?requires_ge:%requires_ge libapr-util1}
%if 0%{?suse_version} >= 1220
%define runtimedir /run
%define mods_static unixd systemd
%else
%define runtimedir	%{_localstatedir}/run
%define mods_static unixd
%endif
%if 0%{?suse_version} >= 1500
%define use_firewalld 1
%else
%define use_firewalld 0
%endif
%if 0%{?suse_version} >= 1500 || 0%{?is_opensuse}
%define build_http2 1
%else
%define build_http2 0
%endif
Name:           apache2
Version:        2.4.46
Release:        0
Summary:        The Apache Web Server
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            http://httpd.apache.org/
Source0:        http://www.apache.org/dist/httpd/%{src_name}.tar.bz2
Source1:        http://www.apache.org/dist/httpd/%{src_name}.tar.bz2.asc
Source2:        apache2.keyring
# Add file to take mtime from it in prep section
Source3:        apache2.changes
Source10:       SUSE-NOTICE
Source11:       rc.%{name}
Source13:       sysconfig.%{name}
Source18:       robots.txt
Source20:       favicon.ico
Source22:       apache2-README
Source23:       apache2-README.QUICKSTART
Source25:       gensslcert
Source26:       apache2-README-access_compat.txt
Source27:       %{name}.logrotate
Source28:       permissions.%{name}
Source29:       apache-ssl-stuff.tar.bz2
Source30:       deprecated-scripts.tar.xz
Source31:       apache2-README-instances.txt
# sysconf_addword is part of aaa_base.rpm starting with openSUSE 11.0
# we bring our own copy for the cases where it is not available
Source45:       sysconf_addword
Source46:       a2enflag
Source47:       a2enmod
#%%if %%{use_firewalld}
Source49:       apache2.firewalld
Source50:       apache2.ssl.firewalld
#%%else
Source51:       apache2.susefirewall
Source52:       apache2.ssl.susefirewall
#%%endif
Source100:      apache2-httpd.conf
Source101:      apache2-errors.conf
Source102:      apache2-default-server.conf
Source103:      apache2-listen.conf
Source104:      apache2-manual.conf
Source105:      apache2-mod_autoindex-defaults.conf
Source106:      apache2-mod_info.conf
Source107:      apache2-mod_log_config.conf
Source108:      apache2-mod_mime-defaults.conf
Source109:      apache2-mod_status.conf
Source110:      apache2-mod_userdir.conf
Source111:      apache2-server-tuning.conf
Source113:      apache2-ssl-global.conf
Source114:      apache2-mod_usertrack.conf
Source115:      apache2-mod_reqtimeout.conf
Source116:      apache2-loadmodule.conf
Source117:      apache2-global.conf
Source118:      apache2-mod_cgid-timeout.conf
Source119:      apache2-protocols.conf
Source130:      apache2-vhost.template
Source131:      apache2-vhost-ssl.template
Source140:      apache2-check_forensic
Source141:      apache-22-24-upgrade
Source142:      start_apache2
Source143:      apache2-systemd-ask-pass
Source144:      apache2.service
Source145:      apache2-find-directives
Source146:      apache2@.service
Source147:      apache2-script-helpers
Source148:      apache2.target
Source149:      %{name}-init.logrotate
Patch2:         httpd-2.1.3alpha-layout.dif
Patch23:        httpd-apachectl.patch
Patch66:        httpd-2.0.54-envvars.dif
Patch67:        httpd-2.2.0-apxs-a2enmod.dif
Patch68:        httpd-2.x.x-logresolve.patch
Patch69:        httpd-2.4.9-bnc690734.patch
Patch70:        httpd-implicit-pointer-decl.patch
Patch111:       httpd-visibility.patch
# PATCH-FEATURE-UPSTREAM kstreitova@suse.com -- backport of HttpContentLengthHeadZero and HttpExpectStrict
Patch115:       httpd-2.4.x-fate317766-config-control-two-protocol-options.diff
Patch116:       deprecated-scripts-arch.patch
# https://svn.apache.org/viewvc?view=revision
Patch117:       apache2-mod_proxy_uwsgi-fix-crash.patch
BuildRequires:  apache-rpm-macros-control
BuildRequires:  apr-util-devel
#Since 2.4.7 the event MPM requires apr 1.5.0 or later.
BuildRequires:  apr-devel >= 1.5.0
BuildRequires:  automake
%if %{use_firewalld}
BuildRequires:  firewall-macros
%endif
%if 0%{?suse_version} >= 1315
BuildRequires:  libbrotli-devel
%endif
BuildRequires:  db-devel
BuildRequires:  ed
BuildRequires:  libcap-devel
#for mod_proxy_html and mod_xml2enc
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel >= 0.9.8a
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  zlib-devel
Requires:       %{_sysconfdir}/mime.types
Requires:       %{name}-MPM
Requires:       logrotate
Recommends:     w3m
%if 0%{?suse_version} >= 1315
Requires:       which
%endif
%if 0%{?suse_version} < 1210
Requires(post): %insserv_prereq
%endif
Requires(post): %fillup_prereq
Requires(post): %{name}-utils
Requires(post): fileutils
Requires(post): grep
Requires(post): permissions
Requires(post): pwdutils
Requires(post): sed
Requires(post): textutils
%if 0%{?suse_version} > 1320
Requires(pre):  user(wwwrun)
Requires(pre):  group(www)
%endif
Suggests:       apache2-%{default_mpm}
Provides:       %{apache_mmn}
Provides:       %{name}-mod_macro = %{version}
Provides:       http_daemon
Provides:       httpd
Provides:       suse_help_viewer
Provides:       suse_maintenance_mmn_%{suse_maintenance_mmn}
Obsoletes:      %{name}-mod_macro <= 1.2.1
Provides:       apache = %{version}
Obsoletes:      apache < 1.3.29
Provides:       mod_ssl = %{version}
Obsoletes:      mod_ssl < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%endif
%if 0%{?suse_version} >= 1310
BuildRequires:  systemd-rpm-macros
%endif
%if 0%{?build_http2}
BuildRequires:  pkgconfig(libnghttp2) >= 1.2.1
%endif
%{?systemd_ordering}

%description
This version of httpd is a major release of the 2.4 stable branch,
and represents the best available version of Apache HTTP Server.
New features include Loadable MPMs, major improvements to OCSP support,
mod_lua, Dynamic Reverse Proxy configuration, Improved Authentication/
Authorization, FastCGI Proxy, New Expression Parser, and a Small Object
Caching API.

 See %{_docdir}/apache2/, http://httpd.apache.org/, and
http://httpd.apache.org/docs-2.4/upgrading.html.

%package worker
Summary:        Apache 2 worker MPM (Multi-Processing Module)
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
# the post scriptlet sources /usr/share/apache2/script-helpers
Requires(post): %{name} = %{version}
Provides:       %{name}-MPM

%package prefork
Summary:        Apache 2 "prefork" MPM (Multi-Processing Module)
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
# the post scriptlet sources /usr/share/apache2/script-helpers
Requires(post): %{name} = %{version}
Provides:       %{name}-MPM
Provides:       apache:%{_sbindir}/httpd

%package event
Summary:        Apache 2 event MPM (Multi-Processing Module)
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}
# the post scriptlet sources /usr/share/apache2/script-helpers
Requires(post): %{name} = %{version}
Provides:       %{name}-MPM

%description worker
The worker MPM (multi-Processing Module) implementing a hybrid
multi-threaded multi-process web server.

This combination offers a performance boost and retains some of the
stability of the multi-process model.

%description prefork
"prefork" MPM (Multi-Processing Module)

This MPM is basically the one that Apache 1.3.x used. It warrants the
maximum stability because each server runs in its own process. If a
process dies it will not affect other servers.

%description event
"event" MPM (multi-Processing Module)

It uses a separate thread to handle Keep Alive requests and accepting
connections. Keep Alive requests have traditionally required httpd to
dedicate a worker to handle it. This dedicated worker could not be used
again until the Keep Alive timeout was reached.

This MPM depends on APR's atomic compare-and-swap operations for thread
synchronization.

%package devel
Summary:        Apache 2 Header and Include Files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       %{name}-MPM
Requires:       apache-rpm-macros-control
Requires:       apache2-prefork
Requires:       apr-devel
Requires:       apr-util-devel
Requires:       gcc
Provides:       httpd-devel = %{version}

%description devel
This package contains header files and include files that are needed
for development using the Apache API.

%package doc
Summary:        Additional Package Documentation
Group:          Documentation/Other
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description doc
This package contains optional documentation provided in addition to
this package's base documentation.

%package example-pages
Summary:        Example Pages for the Apache 2 Web Server
Group:          Productivity/Networking/Web/Servers

%description example-pages
Some Example pages for Apache that show information about the installed
server.

%package utils
Summary:        Apache 2 utilities
Group:          Productivity/Networking/Web/Servers

%description utils
Utilities provided by the Apache 2 Web Server project which are useful
to administrators of web servers in general.

%prep
%setup -q -n %{src_name} -a30
%patch2 -p1
%patch23
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69
%patch70 -p1
%patch111 -p1
%patch115 -p1
%if 0%{?suse_version} == 1110
%patch116 -p1
%endif
%patch117 -p1
cat %{_sourcedir}/SUSE-NOTICE >> NOTICE
# install READMEs
a=$(basename %{SOURCE22})
cp %{SOURCE22} ./${a##%{name}-}
b=$(basename %{SOURCE23})
cp %{SOURCE23} ./${b##%{name}-}
c=$(basename %{SOURCE31})
cp %{SOURCE31} ./${c##%{name}-}
d=$(basename %{SOURCE26})
cp %{SOURCE26} ./${d##%{name}-}

#
# replace PLATFORM string that's seen in the "Server:" header
#
sed 's,(" PLATFORM "),(%{platform_string}),' server/core.c > tmp_file && mv tmp_file server/core.c
sed 's/public_html/%{userdir}/g' docs/conf/extra/httpd-userdir.conf.in > tmp_file && mv tmp_file docs/conf/extra/httpd-userdir.conf.in
# Use mtime of .changes for build time
CHANGES=`stat --format="%%y" %{SOURCE3}`
sed -i -e "s/__DATE__ \" \" __TIME__;/\"$CHANGES\";/" server/buildmark.c
#
# now configure Apache
#
autoreconf -fiv

%build
function configure {
	CFLAGS="%{optflags} -fPIC -Wall -DLDAP_DEPRECATED" \
	CPPFLAGS="-DSSL_EXPERIMENTAL_ENGINE -DMAX_SERVER_LIMIT=200000 -DLDAP_DEPRECATED -DMAXLINE=4096" \
	./configure \
		--enable-layout=SuSE81%(test "%{_lib}" = lib64 && echo -n _64) \
		--with-program-name=httpd$mpm_suffix \
		--with-apr=%{_bindir}/apr-1-config \
		--with-apr-util=%{_bindir}/apu-1-config \
		--with-mpm=$mpm \
%if "$mpm" == "worker" || "$mpm" == "event"
%ifarch %ix86
%ifnarch i386
		--enable-nonportable-atomics=yes \
%endif
%endif
%endif
		--enable-exception-hook \
		--with-pcre \
		--enable-pie \
		--enable-mods-shared=all \
		--enable-mods-static="%{mods_static}" \
		--enable-ssl=shared \
		--disable-isapi \
		--enable-deflate \
%if 0%{?suse_version} >= 1315
                --enable-brotli \
%endif
		--enable-echo \
		--enable-filter \
		--enable-ext-filter \
		--enable-charset-lite \
		--enable-file-cache \
		--enable-logio \
		--enable-dumpio \
		--enable-bucketeer \
		--enable-case_filter \
		--enable-case_filter_in \
		--enable-imagemap \
%if 0%{?build_http2}
                --enable-http2 \
%endif
		--with-ldap \
		--enable-ldap \
		--enable-authnz_ldap \
		--enable-authnz-fcgi \
		--enable-proxy \
		--enable-proxy-connect \
		--enable-proxy-ftp \
		--enable-proxy-http \
%if 0%{?build_http2}
                --enable-proxy-http2 \
%endif
		--enable-proxy-fdpass \
		--enable-cache \
		--enable-disk-cache \
		--enable-mem-cache \
		--enable-version \
		--enable-dav-lock \
		--enable-authn-alias \
		--enable-optional-hook-export \
		--enable-optional-hook-import \
		--enable-optional-fn-import \
 		--enable-optional-fn-export \
		--enable-suexec \
		--with-suexec-bin=%{_sbindir}/suexec \
		--with-suexec-caller=%{httpduser} \
		--with-suexec-docroot=%{datadir} \
		--with-suexec-logfile=%{logfiledir}/suexec.log \
		--with-suexec-userdir=%{userdir} \
		--with-suexec-uidmin=96 \
		--with-suexec-gidmin=96 \
		--with-suexec-safepath=%{suexec_safepath} \
		--disable-heartbeat
}

# build the 3 multi-processing modules (MPM) in a loop
#
for mpm in %{mpms_to_build}; do
	echo $mpm >> .status
	test -s Makefile && make clean >/dev/null
	echo -e "\n\n\n \e[01m***** Building $mpm MPM *****\e[00m\n\n\n"
	export mpm_suffix=-$mpm
	configure
	sed "s/-$mpm//" include/ap_config_auto.h > include/ap_config_auto.h.new
	mv include/ap_config_auto.h.new include/ap_config_auto.h
	sed -i -e "s@%{_localstatedir}/run@%{runtimedir}@g" include/ap_config_layout.h

	make CFLAGS="%{optflags} -fvisibility=hidden -fPIC -Wall -DDEFAULT_LISTENBACKLOG=APR_INT32_MAX -DDEFAULT_ERRORLOG='\"%{logfiledir}/error_log\"'" %{?_smp_mflags}
	make DESTDIR=%{buildroot} install -j1

	# show pathnames in config files
	echo;echo;echo; diff -U1 docs/conf/httpd-std.conf.in docs/conf/httpd-std.conf ||:
	echo;echo;echo; diff -U1 docs/conf/ssl-std.conf.in   docs/conf/ssl-std.conf ||:
	# show compile settings
	pwd
	printf "\n\n\n"; ./httpd$mpm_suffix -V
	printf "\n\n\n"; ./httpd$mpm_suffix -l
	#mv %{buildroot}/%{sysconfdir}/httpd-std.conf %{buildroot}/%{sysconfdir}/httpd-std.conf$mpm_suffix
	#mv %{buildroot}/%{sysconfdir}/httpd2-prefork.conf %{buildroot}/%{sysconfdir}/httpd-std.conf$mpm_suffix
	# fix up and rename config_vars file: remove references to the RPM build dir;
	# remove references to RPM build root; fix apr/apu includedir
	sed -e "/^EXTRA_INCLUDES/s|-I%{_builddir}[^ ]* ||g" \
	    -e "/^AP._INCLUDEDIR/s|%{builddir}.*$|%{includedir}$mpm_suffix|" \
	    -e "/abs_srcdir/d" \
	    -e "/AP_LIBS/d" \
	  < %{buildroot}/%{installbuilddir}/config_vars.mk \
	  > %{buildroot}/%{installbuilddir}/config_vars.mk$mpm_suffix
	rm %{buildroot}/%{installbuilddir}/config_vars.mk
	#rm -rf %{buildroot}.$mpm.post
	#cp -a %{buildroot}/ %{buildroot}.$mpm.post
done
mkdir -p %{buildroot}/%{libexecdir}

# remove references to mpm type in config_vars
sed -e "s^%{_libdir}/%{name}-%{default_mpm}^%{_libdir}/%{name}^" \
    -e "s/httpd$/httpd-%{default_mpm}/" \
    -e "s/%{name}-%{default_mpm}/%{name}/" \
  < %{buildroot}/%{installbuilddir}/config_vars.mk-%{default_mpm} \
  > %{buildroot}/%{installbuilddir}/config_vars.mk

# get rid of modules that do not differ between the MPMs (since most of them are the same)
# by putting them in /usr/lib/apache2
ldir=%{buildroot}/%{libexecdir}
for i in $(cd $ldir-%{default_mpm}; ls -1 *.so); do
	identical=true
	for mpm in %{mpms_to_build}; do
		if test -f $ldir-$mpm/$i -a -f $ldir-%{default_mpm}/$i; then
			objcopy --strip-debug $ldir-$mpm/$i $ldir-$mpm/$i.tst
			objcopy --strip-debug $ldir-%{default_mpm}/$i $ldir-%{default_mpm}/$i.tst
			ls -l $ldir-{%{default_mpm},$mpm}/$i*
			cmp -s $ldir-{%{default_mpm},$mpm}/$i.tst || identical=false
			rm -f $ldir-{%{default_mpm},$mpm}/$i.tst
		else
			identical=false
		fi
	done
	if $identical; then
		cp -dp $ldir-%{default_mpm}/$i $ldir
		for mpm in %{mpms_to_build}; do
			rm $ldir-$mpm/$i
			ln -s ../%{name}/$i $ldir-$mpm/$i
		done
	fi
done

# merge the three /usr/include/apache2-* directories
# by putting them in /usr/lib/apache2
idir=%{buildroot}/%{includedir}
mkdir -p $idir
for i in $(cd $idir-%{default_mpm}; ls -1); do
	identical=true
	for mpm in %{mpms_to_build}; do
		cmp -s $idir-{%{default_mpm},$mpm}/$i || identical=false
	done
	if $identical; then
		cp -dp $idir-%{default_mpm}/$i $idir
		for mpm in %{mpms_to_build}; do
			rm $idir-$mpm/$i
			ln -s ../%{name}/$i $idir-$mpm/$i
		done
	fi
done
for i in ap_config_auto.h ap_config_layout.h; do
	if [ ! -f $idir/$i ]; then
		sed 's/-%{default_mpm}//' $idir-%{default_mpm}/$i > $idir/$i
	fi
done

%install
# (most installation (to build root) has already been done in %%build)
#
# save MODULE_MAGIC_NUMBER
cat > %{buildroot}/%{_libdir}/%{name}_MMN <<-EOF
	#!/bin/sh
	echo %{apache_mmn}
EOF

cp -p %{buildroot}/%{sysconfdir}/httpd-%{default_mpm}.conf %{buildroot}/%{sysconfdir}/httpd.conf
cp -p %{buildroot}/%{sysconfdir}/httpd.conf ./httpd.conf.default
rm %{buildroot}/%{sysconfdir}/httpd-*.conf
#
# create directories
mkdir -p %{buildroot}/%{_fillupdir} \
	 %{buildroot}/%{proxycachedir} \
	 %{buildroot}/%{localstatedir}
#
# support files
install -m 755 support/log_server_status 	%{buildroot}/%{_bindir}/
install -m 755 support/split-logfile 		%{buildroot}/%{_bindir}/
install -m 755 support/logresolve.pl 		%{buildroot}/%{_sbindir}/
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 %{_sourcedir}/%{name}.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
%if 0%{?suse_version} == 1110
install -m 644 %{_sourcedir}/%{name}-init.logrotate %{buildroot}/%{_sysconfdir}/logrotate.d/%{name}
%endif
install -m 755 %{_sourcedir}/apache2-check_forensic %{buildroot}/%{_bindir}/check_forensic
install -m 755 %{_sourcedir}/apache2-find-directives %{buildroot}/%{_bindir}/
#
# ssl stuff
install -m 755 %{SOURCE25} %{buildroot}/%{_bindir}/
tar -xjf %{SOURCE29} -C %{buildroot}/%{sysconfdir}
#
# init script and friends
install -m 644 %{_sourcedir}/apache2-script-helpers %{buildroot}/%{_datadir}/%{name}/script-helpers
install -m 744 %{_sourcedir}/start_apache2 %{buildroot}/%{_sbindir}/
cp -r deprecated-scripts %{buildroot}/%{_datadir}/%{name}/
install -m 755 %{_sourcedir}/apache-22-24-upgrade %{buildroot}/%{_datadir}/%{name}/
%if 0%{?suse_version} >= 1210
mkdir -p %{buildroot}%{_unitdir}/
install -m 700 %{_sourcedir}/apache2-systemd-ask-pass %{buildroot}/%{_sbindir}/
install -m 644 %{_sourcedir}/apache2.service %{buildroot}/%{_unitdir}/
install -m 644 %{_sourcedir}/apache2@.service %{buildroot}/%{_unitdir}/
install -m 644 %{_sourcedir}/apache2.target %{buildroot}/%{_unitdir}/
ln -sf service %{buildroot}/%{_sbindir}/rcapache2
%else
mkdir -p %{buildroot}%{_sysconfdir}/init.d
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/sysconfig.d

install -m 744 %{_sourcedir}/rc.%{name} %{buildroot}/%{_initddir}/%{name}
ln -sf ../..%{_initddir}/%{name} %{buildroot}/%{_sbindir}/rcapache2
for file in find_mpm \
            get_includes \
            get_module_list \
            load_configuration
do
    ln -sf deprecated-scripts/$file %{buildroot}/%{_datadir}/%{name}/$file
    chmod +x %{buildroot}/%{_datadir}/%{name}/$file
done
%endif
install -m 755 %{_sourcedir}/sysconf_addword %{buildroot}/%{_datadir}/%{name}/
install -m 755 %{_sourcedir}/a2enflag %{buildroot}/%{_sbindir}
ln -s a2enflag %{buildroot}/%{_sbindir}/a2disflag
install -m 755 %{_sourcedir}/a2enmod %{buildroot}/%{_sbindir}
ln -s a2enmod %{buildroot}/%{_sbindir}/a2dismod
#
# directories for files from other packages and other configuration
mkdir -p %{buildroot}/%{sysconfdir}/vhosts.d
#
# install sysconfig template
install -m 644 %{_sourcedir}/sysconfig.%{name} \
	%{buildroot}/%{_fillupdir}/sysconfig.%{name}
#
# install configuration files:
mkdir -p %{buildroot}/%{runtimedir}
mkdir -p %{buildroot}/%{sysconfdir}/conf.d
for i in default-server.conf \
	 errors.conf \
	 global.conf \
	 httpd.conf \
	 listen.conf \
	 loadmodule.conf \
	 mod_autoindex-defaults.conf \
	 mod_info.conf \
	 mod_log_config.conf \
	 mod_mime-defaults.conf \
	 mod_status.conf \
	 mod_userdir.conf \
	 mod_usertrack.conf \
	 server-tuning.conf \
	 mod_reqtimeout.conf \
         mod_cgid-timeout.conf \
	 ssl-global.conf \
	 protocols.conf
do
	install -m 644 %{_sourcedir}/apache2-$i %{buildroot}/%{sysconfdir}/$i
done
cat > %{buildroot}/%{sysconfdir}/uid.conf <<-EOF
	User %{httpduser}
	Group %{httpdgroup}
EOF

# fixup libdir
%if "%{_lib}" != "lib64"
sed -e 's/lib64/%{_lib}/' -i \
  %{buildroot}/%{sysconfdir}/loadmodule.conf \
  %{buildroot}/%{_fillupdir}/sysconfig.%{name}
%endif

# remove configuration for mpms which have not been built
mpm_confs="$(awk '/IfModule .*\.c/ {print $2}' %{buildroot}/%{sysconfdir}/server-tuning.conf | cut -d. -f1 | tr '\n' ' ')"
for mpm_conf in $mpm_confs; do
	case "%{mpms_to_build}" in
	*$mpm_conf*) ;;
	*) sed "/^# $mpm_conf/, /^$/ d" %{buildroot}/%{sysconfdir}/server-tuning.conf > t
	   #diff -u %{buildroot}/%{sysconfdir}/server-tuning.conf t ||:
	   mv t %{buildroot}/%{sysconfdir}/server-tuning.conf
	   ;;
	esac
done
install -m 644 %{SOURCE130} %{buildroot}/%{sysconfdir}/vhosts.d/vhost.template
install -m 644 %{SOURCE131} %{buildroot}/%{sysconfdir}/vhosts.d/vhost-ssl.template
install -m 644 %{SOURCE104} %{buildroot}/%{sysconfdir}/conf.d/manual.conf
# for mod_auth_ldap
install -m 644 docs/conf/charset.conv %{buildroot}/%{sysconfdir}/

cp -p %{_sourcedir}/robots.txt .
cp -p %{_sourcedir}/favicon.ico %{buildroot}/%{htdocsdir}/
cat > %{buildroot}/%{htdocsdir}/robots.txt <<-EOF
	User-Agent: *
	Disallow: /
EOF

#
# use official mime.types (more complete)
#
ln -sf ../mime.types %{buildroot}/%{sysconfdir}/mime.types

mv %{buildroot}/%{cgidir}/printenv* .
mv %{buildroot}/%{cgidir}/test-cgi .

# fix up apxs
pushd %{buildroot}/%{_bindir}
	for mpm in %{mpms_to_build}; do
		cat <<-EOT_ED | ed -s apxs
			H
			,s/^\(.*\)config_vars.mk\(.*\)$/\1config_vars.mk\$mpm_suffix\2/
			/config_vars.mk
			-
			i
			my \$mpm_suffix = "-$mpm";
			.
			wq apxs-$mpm
		EOT_ED
		chmod 755 apxs-$mpm
	done
	cat <<-EOT_ED | ed -s apxs
		H
		/config_vars
		a
		my \$mpm_suffix = "";
		.
		wq
	EOT_ED
popd

# install firewall information file
%if %{use_firewalld}
install -D -m 644 %{SOURCE49} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}.xml
install -D -m 644 %{SOURCE50} %{buildroot}%{_prefix}/lib/firewalld/services/%{name}-ssl.xml
%else
install -d %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/
install -m 644 %{SOURCE51} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
install -m 644 %{SOURCE52} %{buildroot}%{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}-ssl
%endif
ln -sf %{_bindir}/apxs %{buildroot}%{_sbindir}
#
# compat symlinks apache2 -> apache
#
ln -s ab                  %{buildroot}/%{_bindir}/ab2
ln -s ab.1.gz             %{buildroot}/%{_mandir}/man1/ab2.1.gz
ln -s apxs                %{buildroot}/%{_bindir}/apxs2
ln -s apxs.1.gz           %{buildroot}/%{_mandir}/man1/apxs2.1.gz
ln -s apxs-prefork        %{buildroot}/%{_bindir}/apxs2-prefork
ln -s apxs-worker         %{buildroot}/%{_bindir}/apxs2-worker
ln -s apxs-event          %{buildroot}/%{_bindir}/apxs2-event
ln -s dbmmanage           %{buildroot}/%{_bindir}/dbmmanage2
ln -s dbmmanage.1.gz      %{buildroot}/%{_mandir}/man1/dbmmanage2.1.gz
ln -s htdbm               %{buildroot}/%{_bindir}/htdbm2
ln -s htdbm.1.gz          %{buildroot}/%{_mandir}/man1/htdbm2.1.gz
ln -s htdigest            %{buildroot}/%{_bindir}/htdigest2
ln -s htdigest.1.gz       %{buildroot}/%{_mandir}/man1/htdigest2.1.gz
ln -s htpasswd            %{buildroot}/%{_bindir}/htpasswd2
ln -s htpasswd.1.gz       %{buildroot}/%{_mandir}/man1/htpasswd2.1.gz
ln -s check_forensic      %{buildroot}/%{_bindir}/check_forensic2
ln -s logresolve          %{buildroot}/%{_bindir}/logresolve2
ln -s logresolve.1.gz     %{buildroot}/%{_mandir}/man1/logresolve2.1.gz
ln -s log_server_status   %{buildroot}/%{_bindir}/log_server_status2
ln -s split-logfile       %{buildroot}/%{_bindir}/split-logfile2
ln -s apachectl           %{buildroot}/%{_sbindir}/apache2ctl
ln -s apachectl.8.gz      %{buildroot}/%{_mandir}/man8/apache2ctl.8.gz
ln -s apxs                %{buildroot}/%{_sbindir}/apxs2
ln -s httpd-prefork       %{buildroot}/%{_sbindir}/httpd2-prefork
ln -s httpd-worker        %{buildroot}/%{_sbindir}/httpd2-worker
ln -s httpd-event         %{buildroot}/%{_sbindir}/httpd2-event
ln -s httpd.8.gz          %{buildroot}/%{_mandir}/man8/httpd2.8.gz
ln -s logresolve.pl       %{buildroot}/%{_sbindir}/logresolve.pl2
ln -s rotatelogs          %{buildroot}/%{_sbindir}/rotatelogs2
ln -s rotatelogs.8.gz     %{buildroot}/%{_mandir}/man8/rotatelogs2.8.gz
ln -s suexec              %{buildroot}/%{_sbindir}/suexec2
ln -s suexec.8.gz         %{buildroot}/%{_mandir}/man8/suexec2.8.gz
#
# filelists
#
>filelist; >filelist-devel
for mpm in %{mpms_to_build}; do
	echo %dir %{_libdir}/%{name}-$mpm >> filelist
	(
	echo %dir %{includedir}-$mpm
	echo %{_bindir}/apxs-$mpm
	echo %{_bindir}/apxs2-$mpm
	) >> filelist-devel
done
find %{buildroot}/%{includedir}/.. -type f -o -type l \
 | sed "s#%{buildroot}##" \
 >> filelist-devel
find %{buildroot}/%{installbuilddir} -type f \
 | sed "s#%{buildroot}##" \
 >> filelist-devel
#
# remove files from the build root that we won't package
#
rm -f %{buildroot}/%{_libdir}/%{name}-*/*.exp	# needed only on AIX
rm -f %{buildroot}/%{_libdir}/%{name}/*.exp		# needed only on AIX
rm -f %{buildroot}/%{_sbindir}/checkgid		# needed only for user installations from tarball
rm -r %{buildroot}/%{sysconfdir}/extra 		# it is already in the documentation directory
#
# do not ship example configuration files in
# /etc/apache2, but %doc them later
#
mv %{buildroot}/%{sysconfdir}/original .

%check
# now check wether httpd binary runs properly
# and validate httpd.conf file
#
pushd %{buildroot}/%{sysconfdir}
for i in *.conf; do
  cp $i $i.test;
done
sed -e 's+%{_libdir}+'%{buildroot}'%{_libdir}+' \
    -e 's+%{_localstatedir}/run+'%{buildroot}'%{_localstatedir}/run+' \
    -e 's+%{sysconfdir}+'%{buildroot}'%{sysconfdir}+' \
    -e 's+%{datadir}+'%{buildroot}'%{datadir}+' \
    -e 's+\.conf$+&.test+' \
    -e 's+%{_localstatedir}/log+'%{buildroot}'%{_localstatedir}/log+' \
		httpd.conf > httpd.conf.test
sed -e 's+%{sysconfdir}+'%{buildroot}'%{sysconfdir}+' \
		default-server.conf > default-server.conf.test
sed -i 's+%{_localstatedir}/log+'%{buildroot}'%{_localstatedir}/log+' \
		global.conf.test
sed -i 's+%{_libdir}+%{buildroot}/%{_libdir}+' loadmodule.conf.test
popd

LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
%{buildroot}/%{_sbindir}/httpd-%{default_mpm} \
	-e debug -t -f %{buildroot}/%{sysconfdir}/httpd.conf.test || exit 1
rm %{buildroot}/%{sysconfdir}/*.test

# taken from kdump/kdump.spec, thanks!
# Compatibility cruft
# there is no %%license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %{_defaultdocdir}
%endif
%endif
# End of compatibility cruft

%files -f filelist
%defattr(-,root,root)
%doc INSTALL READM* ABOUT_APACHE CHANGES
%license LICENSE
%doc support/SHA1
%{_mandir}/man?/apachectl.?.*
%{_mandir}/man?/apache2ctl.?.*
%{_mandir}/man?/htcacheclean.?.*
%{_mandir}/man?/httpd.?.*
%{_mandir}/man?/httpd2.?.*
%{_mandir}/man?/apxs.?.*
%{_mandir}/man?/apxs2.?.*
%{_mandir}/man?/suexec.?.*
%{_mandir}/man?/suexec2.?.*
%doc robots.txt
%doc printenv
%doc test-cgi
%doc httpd.conf.default
%doc original
%attr(750,root,root) %dir %{logfiledir}
%attr(750,%{httpduser},root) %dir %{proxycachedir}
%attr(750,%{httpduser},root) %dir %{localstatedir}
%dir %{sysconfdir}
%config %{sysconfdir}/magic
%config %{sysconfdir}/mime.types
%config (noreplace) %{sysconfdir}/*.conf
%config (noreplace) %{sysconfdir}/charset.conv
%{sysconfdir}/vhosts.d/*.template
%dir %{sysconfdir}/ssl.crl
%dir %{sysconfdir}/ssl.crt
%dir %{sysconfdir}/ssl.csr
%dir %attr(700,root,root) %{sysconfdir}/ssl.key
%dir %{sysconfdir}/ssl.prm
%{sysconfdir}/ssl.*/README*
%dir %{sysconfdir}/conf.d
%dir %{sysconfdir}/vhosts.d
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%if 0%{?suse_version} >= 1210
%{_unitdir}/apache2.service
%{_unitdir}/apache2@.service
%{_unitdir}/apache2.target
%{_sbindir}/apache2-systemd-ask-pass
%else
%{_initddir}/%{name}
%dir %{_sysconfdir}/%{name}/sysconfig.d
%endif
%{_sbindir}/rcapache2
%{_sbindir}/apachectl
%{_sbindir}/apache2ctl
%{_sbindir}/envvars
%{_sbindir}/envvars-std
%{_sbindir}/htcacheclean
%{_sbindir}/a2enflag
%{_sbindir}/a2enmod
%{_sbindir}/a2disflag
%{_sbindir}/a2dismod
%{_sbindir}/start_apache2
%{_bindir}/log_server_status
%{_bindir}/log_server_status2
%verify(not mode) %attr(0755,root,root) %{_sbindir}/suexec
%{_sbindir}/suexec2
%{iconsdir}
%{errordir}
%{_fillupdir}/sysconfig.%{name}
%attr(755,root,root) %{_libdir}/%{name}_MMN
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/mod_*.so
%dir %{installbuilddir}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/apache-22-24-upgrade
%{_datadir}/%{name}/deprecated-scripts
%{_datadir}/%{name}/script-helpers
%{_datadir}/%{name}/sysconf_addword
%if %{use_firewalld}
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_prefix}/lib/firewalld/services/%{name}.xml
%{_prefix}/lib/firewalld/services/%{name}-ssl.xml
%else
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}
%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/%{name}-ssl
%endif
%if 0%{?suse_version} == 1110
/usr/share/apache2/find_mpm
/usr/share/apache2/get_includes
/usr/share/apache2/get_module_list
/usr/share/apache2/load_configuration
%endif

%files prefork
%defattr(-,root,root)
%{_sbindir}/httpd-prefork
%{_sbindir}/httpd2-prefork
%dir %{_libdir}/%{name}-prefork
# hardcoded list so we do not lose mods by accident
%{_libdir}/%{name}-prefork/mod_access_compat.so
%{_libdir}/%{name}-prefork/mod_actions.so
%{_libdir}/%{name}-prefork/mod_alias.so
%{_libdir}/%{name}-prefork/mod_allowmethods.so
%{_libdir}/%{name}-prefork/mod_asis.so
%{_libdir}/%{name}-prefork/mod_auth_basic.so
%{_libdir}/%{name}-prefork/mod_auth_digest.so
%{_libdir}/%{name}-prefork/mod_auth_form.so
%{_libdir}/%{name}-prefork/mod_authn_anon.so
%{_libdir}/%{name}-prefork/mod_authn_core.so
%{_libdir}/%{name}-prefork/mod_authn_dbd.so
%{_libdir}/%{name}-prefork/mod_authn_dbm.so
%{_libdir}/%{name}-prefork/mod_authn_file.so
%{_libdir}/%{name}-prefork/mod_authn_socache.so
%{_libdir}/%{name}-prefork/mod_authnz_ldap.so
%{_libdir}/%{name}-prefork/mod_authnz_fcgi.so
%{_libdir}/%{name}-prefork/mod_authz_core.so
%{_libdir}/%{name}-prefork/mod_authz_dbd.so
%{_libdir}/%{name}-prefork/mod_authz_dbm.so
%{_libdir}/%{name}-prefork/mod_authz_groupfile.so
%{_libdir}/%{name}-prefork/mod_authz_host.so
%{_libdir}/%{name}-prefork/mod_authz_owner.so
%{_libdir}/%{name}-prefork/mod_authz_user.so
%{_libdir}/%{name}-prefork/mod_autoindex.so
%{_libdir}/%{name}-prefork/mod_bucketeer.so
%{_libdir}/%{name}-prefork/mod_buffer.so
%{_libdir}/%{name}-prefork/mod_cache.so
%{_libdir}/%{name}-prefork/mod_cache_disk.so
%{_libdir}/%{name}-prefork/mod_cache_socache.so
%{_libdir}/%{name}-prefork/mod_case_filter.so
%{_libdir}/%{name}-prefork/mod_case_filter_in.so
%{_libdir}/%{name}-prefork/mod_cgi.so
%{_libdir}/%{name}-prefork/mod_charset_lite.so
%{_libdir}/%{name}-prefork/mod_data.so
%{_libdir}/%{name}-prefork/mod_dav.so
%{_libdir}/%{name}-prefork/mod_dav_fs.so
%{_libdir}/%{name}-prefork/mod_dav_lock.so
%{_libdir}/%{name}-prefork/mod_dbd.so
%{_libdir}/%{name}-prefork/mod_deflate.so
%if 0%{?suse_version} >= 1315
%{_libdir}/%{name}-prefork/mod_brotli.so
%endif
%{_libdir}/%{name}-prefork/mod_dialup.so
%{_libdir}/%{name}-prefork/mod_dir.so
%{_libdir}/%{name}-prefork/mod_dumpio.so
%{_libdir}/%{name}-prefork/mod_echo.so
%{_libdir}/%{name}-prefork/mod_env.so
%{_libdir}/%{name}-prefork/mod_expires.so
%{_libdir}/%{name}-prefork/mod_ext_filter.so
%{_libdir}/%{name}-prefork/mod_file_cache.so
%{_libdir}/%{name}-prefork/mod_filter.so
%{_libdir}/%{name}-prefork/mod_headers.so
%{_libdir}/%{name}-prefork/mod_heartmonitor.so
%if 0%{?build_http2}
%{_libdir}/%{name}-prefork/mod_http2.so
%{_libdir}/%{name}-prefork/mod_proxy_http2.so
%endif
%{_libdir}/%{name}-prefork/mod_imagemap.so
%{_libdir}/%{name}-prefork/mod_include.so
%{_libdir}/%{name}-prefork/mod_info.so
%{_libdir}/%{name}-prefork/mod_lbmethod_bybusyness.so
%{_libdir}/%{name}-prefork/mod_lbmethod_byrequests.so
%{_libdir}/%{name}-prefork/mod_lbmethod_bytraffic.so
%{_libdir}/%{name}-prefork/mod_lbmethod_heartbeat.so
%{_libdir}/%{name}-prefork/mod_ldap.so
%{_libdir}/%{name}-prefork/mod_log_config.so
%{_libdir}/%{name}-prefork/mod_log_debug.so
%{_libdir}/%{name}-prefork/mod_log_forensic.so
%{_libdir}/%{name}-prefork/mod_logio.so
%{_libdir}/%{name}-prefork/mod_lua.so
%{_libdir}/%{name}-prefork/mod_macro.so
%{_libdir}/%{name}-prefork/mod_mime.so
%{_libdir}/%{name}-prefork/mod_mime_magic.so
%{_libdir}/%{name}-prefork/mod_negotiation.so
%{_libdir}/%{name}-prefork/mod_optional_fn_export.so
%{_libdir}/%{name}-prefork/mod_optional_fn_import.so
%{_libdir}/%{name}-prefork/mod_optional_hook_export.so
%{_libdir}/%{name}-prefork/mod_optional_hook_import.so
%{_libdir}/%{name}-prefork/mod_proxy.so
%{_libdir}/%{name}-prefork/mod_proxy_ajp.so
%{_libdir}/%{name}-prefork/mod_proxy_balancer.so
%{_libdir}/%{name}-prefork/mod_proxy_connect.so
%{_libdir}/%{name}-prefork/mod_proxy_express.so
%{_libdir}/%{name}-prefork/mod_proxy_fcgi.so
%{_libdir}/%{name}-prefork/mod_proxy_fdpass.so
%{_libdir}/%{name}-prefork/mod_proxy_ftp.so
%{_libdir}/%{name}-prefork/mod_proxy_hcheck.so
%{_libdir}/%{name}-prefork/mod_proxy_html.so
%{_libdir}/%{name}-prefork/mod_proxy_http.so
%{_libdir}/%{name}-prefork/mod_proxy_scgi.so
%{_libdir}/%{name}-prefork/mod_proxy_uwsgi.so
%{_libdir}/%{name}-prefork/mod_proxy_wstunnel.so
%{_libdir}/%{name}-prefork/mod_ratelimit.so
%{_libdir}/%{name}-prefork/mod_reflector.so
%{_libdir}/%{name}-prefork/mod_remoteip.so
%{_libdir}/%{name}-prefork/mod_reqtimeout.so
%{_libdir}/%{name}-prefork/mod_request.so
%{_libdir}/%{name}-prefork/mod_rewrite.so
%{_libdir}/%{name}-prefork/mod_sed.so
%{_libdir}/%{name}-prefork/mod_session.so
%{_libdir}/%{name}-prefork/mod_session_cookie.so
%{_libdir}/%{name}-prefork/mod_session_crypto.so
%{_libdir}/%{name}-prefork/mod_session_dbd.so
%{_libdir}/%{name}-prefork/mod_setenvif.so
%{_libdir}/%{name}-prefork/mod_slotmem_plain.so
%{_libdir}/%{name}-prefork/mod_slotmem_shm.so
%{_libdir}/%{name}-prefork/mod_socache_dbm.so
%{_libdir}/%{name}-prefork/mod_socache_memcache.so
%{_libdir}/%{name}-prefork/mod_socache_redis.so
%{_libdir}/%{name}-prefork/mod_socache_shmcb.so
%{_libdir}/%{name}-prefork/mod_speling.so
%{_libdir}/%{name}-prefork/mod_ssl.so
%{_libdir}/%{name}-prefork/mod_status.so
%{_libdir}/%{name}-prefork/mod_substitute.so
%{_libdir}/%{name}-prefork/mod_suexec.so
%{_libdir}/%{name}-prefork/mod_unique_id.so
%{_libdir}/%{name}-prefork/mod_userdir.so
%{_libdir}/%{name}-prefork/mod_usertrack.so
%{_libdir}/%{name}-prefork/mod_version.so
%{_libdir}/%{name}-prefork/mod_vhost_alias.so
%{_libdir}/%{name}-prefork/mod_watchdog.so
%{_libdir}/%{name}-prefork/mod_xml2enc.so

%files worker
%defattr(-,root,root)
%{_sbindir}/httpd-worker
%{_sbindir}/httpd2-worker
%dir %{_libdir}/%{name}-worker
# hardcoded list so we do not lose mods by accident
%{_libdir}/%{name}-worker/mod_access_compat.so
%{_libdir}/%{name}-worker/mod_actions.so
%{_libdir}/%{name}-worker/mod_alias.so
%{_libdir}/%{name}-worker/mod_allowmethods.so
%{_libdir}/%{name}-worker/mod_asis.so
%{_libdir}/%{name}-worker/mod_auth_basic.so
%{_libdir}/%{name}-worker/mod_auth_digest.so
%{_libdir}/%{name}-worker/mod_auth_form.so
%{_libdir}/%{name}-worker/mod_authn_anon.so
%{_libdir}/%{name}-worker/mod_authn_core.so
%{_libdir}/%{name}-worker/mod_authn_dbd.so
%{_libdir}/%{name}-worker/mod_authn_dbm.so
%{_libdir}/%{name}-worker/mod_authn_file.so
%{_libdir}/%{name}-worker/mod_authn_socache.so
%{_libdir}/%{name}-worker/mod_authnz_ldap.so
%{_libdir}/%{name}-worker/mod_authnz_fcgi.so
%{_libdir}/%{name}-worker/mod_authz_core.so
%{_libdir}/%{name}-worker/mod_authz_dbd.so
%{_libdir}/%{name}-worker/mod_authz_dbm.so
%{_libdir}/%{name}-worker/mod_authz_groupfile.so
%{_libdir}/%{name}-worker/mod_authz_host.so
%{_libdir}/%{name}-worker/mod_authz_owner.so
%{_libdir}/%{name}-worker/mod_authz_user.so
%{_libdir}/%{name}-worker/mod_autoindex.so
%{_libdir}/%{name}-worker/mod_bucketeer.so
%{_libdir}/%{name}-worker/mod_buffer.so
%{_libdir}/%{name}-worker/mod_cache.so
%{_libdir}/%{name}-worker/mod_cache_disk.so
%{_libdir}/%{name}-worker/mod_cache_socache.so
%{_libdir}/%{name}-worker/mod_case_filter.so
%{_libdir}/%{name}-worker/mod_case_filter_in.so
%{_libdir}/%{name}-worker/mod_cgid.so
%{_libdir}/%{name}-worker/mod_charset_lite.so
%{_libdir}/%{name}-worker/mod_data.so
%{_libdir}/%{name}-worker/mod_dav.so
%{_libdir}/%{name}-worker/mod_dav_fs.so
%{_libdir}/%{name}-worker/mod_dav_lock.so
%{_libdir}/%{name}-worker/mod_dbd.so
%{_libdir}/%{name}-worker/mod_deflate.so
%if 0%{?suse_version} >= 1315
%{_libdir}/%{name}-worker/mod_brotli.so
%endif
%{_libdir}/%{name}-worker/mod_dialup.so
%{_libdir}/%{name}-worker/mod_dir.so
%{_libdir}/%{name}-worker/mod_dumpio.so
%{_libdir}/%{name}-worker/mod_echo.so
%{_libdir}/%{name}-worker/mod_env.so
%{_libdir}/%{name}-worker/mod_expires.so
%{_libdir}/%{name}-worker/mod_ext_filter.so
%{_libdir}/%{name}-worker/mod_file_cache.so
%{_libdir}/%{name}-worker/mod_filter.so
%{_libdir}/%{name}-worker/mod_headers.so
%{_libdir}/%{name}-worker/mod_heartmonitor.so
%if 0%{?build_http2}
%{_libdir}/%{name}-worker/mod_http2.so
%{_libdir}/%{name}-worker/mod_proxy_http2.so
%endif
%{_libdir}/%{name}-worker/mod_imagemap.so
%{_libdir}/%{name}-worker/mod_include.so
%{_libdir}/%{name}-worker/mod_info.so
%{_libdir}/%{name}-worker/mod_lbmethod_bybusyness.so
%{_libdir}/%{name}-worker/mod_lbmethod_byrequests.so
%{_libdir}/%{name}-worker/mod_lbmethod_bytraffic.so
%{_libdir}/%{name}-worker/mod_lbmethod_heartbeat.so
%{_libdir}/%{name}-worker/mod_ldap.so
%{_libdir}/%{name}-worker/mod_log_config.so
%{_libdir}/%{name}-worker/mod_log_debug.so
%{_libdir}/%{name}-worker/mod_log_forensic.so
%{_libdir}/%{name}-worker/mod_logio.so
%{_libdir}/%{name}-worker/mod_lua.so
%{_libdir}/%{name}-worker/mod_macro.so
%{_libdir}/%{name}-worker/mod_mime.so
%{_libdir}/%{name}-worker/mod_mime_magic.so
%{_libdir}/%{name}-worker/mod_negotiation.so
%{_libdir}/%{name}-worker/mod_optional_fn_export.so
%{_libdir}/%{name}-worker/mod_optional_fn_import.so
%{_libdir}/%{name}-worker/mod_optional_hook_export.so
%{_libdir}/%{name}-worker/mod_optional_hook_import.so
%{_libdir}/%{name}-worker/mod_proxy.so
%{_libdir}/%{name}-worker/mod_proxy_ajp.so
%{_libdir}/%{name}-worker/mod_proxy_balancer.so
%{_libdir}/%{name}-worker/mod_proxy_connect.so
%{_libdir}/%{name}-worker/mod_proxy_express.so
%{_libdir}/%{name}-worker/mod_proxy_fcgi.so
%{_libdir}/%{name}-worker/mod_proxy_fdpass.so
%{_libdir}/%{name}-worker/mod_proxy_ftp.so
%{_libdir}/%{name}-worker/mod_proxy_hcheck.so
%{_libdir}/%{name}-worker/mod_proxy_html.so
%{_libdir}/%{name}-worker/mod_proxy_http.so
%{_libdir}/%{name}-worker/mod_proxy_scgi.so
%{_libdir}/%{name}-worker/mod_proxy_uwsgi.so
%{_libdir}/%{name}-worker/mod_proxy_wstunnel.so
%{_libdir}/%{name}-worker/mod_ratelimit.so
%{_libdir}/%{name}-worker/mod_reflector.so
%{_libdir}/%{name}-worker/mod_remoteip.so
%{_libdir}/%{name}-worker/mod_reqtimeout.so
%{_libdir}/%{name}-worker/mod_request.so
%{_libdir}/%{name}-worker/mod_rewrite.so
%{_libdir}/%{name}-worker/mod_sed.so
%{_libdir}/%{name}-worker/mod_session.so
%{_libdir}/%{name}-worker/mod_session_cookie.so
%{_libdir}/%{name}-worker/mod_session_crypto.so
%{_libdir}/%{name}-worker/mod_session_dbd.so
%{_libdir}/%{name}-worker/mod_setenvif.so
%{_libdir}/%{name}-worker/mod_slotmem_plain.so
%{_libdir}/%{name}-worker/mod_slotmem_shm.so
%{_libdir}/%{name}-worker/mod_socache_dbm.so
%{_libdir}/%{name}-worker/mod_socache_memcache.so
%{_libdir}/%{name}-worker/mod_socache_redis.so
%{_libdir}/%{name}-worker/mod_socache_shmcb.so
%{_libdir}/%{name}-worker/mod_speling.so
%{_libdir}/%{name}-worker/mod_ssl.so
%{_libdir}/%{name}-worker/mod_status.so
%{_libdir}/%{name}-worker/mod_substitute.so
%{_libdir}/%{name}-worker/mod_suexec.so
%{_libdir}/%{name}-worker/mod_unique_id.so
%{_libdir}/%{name}-worker/mod_userdir.so
%{_libdir}/%{name}-worker/mod_usertrack.so
%{_libdir}/%{name}-worker/mod_version.so
%{_libdir}/%{name}-worker/mod_vhost_alias.so
%{_libdir}/%{name}-worker/mod_watchdog.so
%{_libdir}/%{name}-worker/mod_xml2enc.so

%files event
%defattr(-,root,root)
%{_sbindir}/httpd-event
%{_sbindir}/httpd2-event
%dir %{_libdir}/%{name}-event
# hardcoded list so we do not lose mods by accident
%{_libdir}/%{name}-event/mod_access_compat.so
%{_libdir}/%{name}-event/mod_actions.so
%{_libdir}/%{name}-event/mod_alias.so
%{_libdir}/%{name}-event/mod_allowmethods.so
%{_libdir}/%{name}-event/mod_asis.so
%{_libdir}/%{name}-event/mod_auth_basic.so
%{_libdir}/%{name}-event/mod_auth_digest.so
%{_libdir}/%{name}-event/mod_auth_form.so
%{_libdir}/%{name}-event/mod_authn_anon.so
%{_libdir}/%{name}-event/mod_authn_core.so
%{_libdir}/%{name}-event/mod_authn_dbd.so
%{_libdir}/%{name}-event/mod_authn_dbm.so
%{_libdir}/%{name}-event/mod_authn_file.so
%{_libdir}/%{name}-event/mod_authn_socache.so
%{_libdir}/%{name}-event/mod_authnz_ldap.so
%{_libdir}/%{name}-event/mod_authnz_fcgi.so
%{_libdir}/%{name}-event/mod_authz_core.so
%{_libdir}/%{name}-event/mod_authz_dbd.so
%{_libdir}/%{name}-event/mod_authz_dbm.so
%{_libdir}/%{name}-event/mod_authz_groupfile.so
%{_libdir}/%{name}-event/mod_authz_host.so
%{_libdir}/%{name}-event/mod_authz_owner.so
%{_libdir}/%{name}-event/mod_authz_user.so
%{_libdir}/%{name}-event/mod_autoindex.so
%{_libdir}/%{name}-event/mod_bucketeer.so
%{_libdir}/%{name}-event/mod_buffer.so
%{_libdir}/%{name}-event/mod_cache.so
%{_libdir}/%{name}-event/mod_cache_disk.so
%{_libdir}/%{name}-event/mod_cache_socache.so
%{_libdir}/%{name}-event/mod_case_filter.so
%{_libdir}/%{name}-event/mod_case_filter_in.so
%{_libdir}/%{name}-event/mod_cgid.so
%{_libdir}/%{name}-event/mod_charset_lite.so
%{_libdir}/%{name}-event/mod_data.so
%{_libdir}/%{name}-event/mod_dav.so
%{_libdir}/%{name}-event/mod_dav_fs.so
%{_libdir}/%{name}-event/mod_dav_lock.so
%{_libdir}/%{name}-event/mod_dbd.so
%if 0%{?suse_version} >= 1315
%{_libdir}/%{name}-event/mod_brotli.so
%endif
%{_libdir}/%{name}-event/mod_deflate.so
%{_libdir}/%{name}-event/mod_dialup.so
%{_libdir}/%{name}-event/mod_dir.so
%{_libdir}/%{name}-event/mod_dumpio.so
%{_libdir}/%{name}-event/mod_echo.so
%{_libdir}/%{name}-event/mod_env.so
%{_libdir}/%{name}-event/mod_expires.so
%{_libdir}/%{name}-event/mod_ext_filter.so
%{_libdir}/%{name}-event/mod_file_cache.so
%{_libdir}/%{name}-event/mod_filter.so
%{_libdir}/%{name}-event/mod_headers.so
%if 0%{?build_http2}
%{_libdir}/%{name}-event/mod_http2.so
%{_libdir}/%{name}-event/mod_proxy_http2.so
%endif
%{_libdir}/%{name}-event/mod_heartmonitor.so
%{_libdir}/%{name}-event/mod_imagemap.so
%{_libdir}/%{name}-event/mod_include.so
%{_libdir}/%{name}-event/mod_info.so
%{_libdir}/%{name}-event/mod_lbmethod_bybusyness.so
%{_libdir}/%{name}-event/mod_lbmethod_byrequests.so
%{_libdir}/%{name}-event/mod_lbmethod_bytraffic.so
%{_libdir}/%{name}-event/mod_lbmethod_heartbeat.so
%{_libdir}/%{name}-event/mod_ldap.so
%{_libdir}/%{name}-event/mod_log_config.so
%{_libdir}/%{name}-event/mod_log_debug.so
%{_libdir}/%{name}-event/mod_log_forensic.so
%{_libdir}/%{name}-event/mod_logio.so
%{_libdir}/%{name}-event/mod_lua.so
%{_libdir}/%{name}-event/mod_macro.so
%{_libdir}/%{name}-event/mod_mime.so
%{_libdir}/%{name}-event/mod_mime_magic.so
%{_libdir}/%{name}-event/mod_negotiation.so
%{_libdir}/%{name}-event/mod_optional_fn_export.so
%{_libdir}/%{name}-event/mod_optional_fn_import.so
%{_libdir}/%{name}-event/mod_optional_hook_export.so
%{_libdir}/%{name}-event/mod_optional_hook_import.so
%{_libdir}/%{name}-event/mod_proxy.so
%{_libdir}/%{name}-event/mod_proxy_ajp.so
%{_libdir}/%{name}-event/mod_proxy_balancer.so
%{_libdir}/%{name}-event/mod_proxy_connect.so
%{_libdir}/%{name}-event/mod_proxy_express.so
%{_libdir}/%{name}-event/mod_proxy_fcgi.so
%{_libdir}/%{name}-event/mod_proxy_fdpass.so
%{_libdir}/%{name}-event/mod_proxy_ftp.so
%{_libdir}/%{name}-event/mod_proxy_hcheck.so
%{_libdir}/%{name}-event/mod_proxy_html.so
%{_libdir}/%{name}-event/mod_proxy_http.so
%{_libdir}/%{name}-event/mod_proxy_scgi.so
%{_libdir}/%{name}-event/mod_proxy_uwsgi.so
%{_libdir}/%{name}-event/mod_proxy_wstunnel.so
%{_libdir}/%{name}-event/mod_ratelimit.so
%{_libdir}/%{name}-event/mod_reflector.so
%{_libdir}/%{name}-event/mod_remoteip.so
%{_libdir}/%{name}-event/mod_reqtimeout.so
%{_libdir}/%{name}-event/mod_request.so
%{_libdir}/%{name}-event/mod_rewrite.so
%{_libdir}/%{name}-event/mod_sed.so
%{_libdir}/%{name}-event/mod_session.so
%{_libdir}/%{name}-event/mod_session_cookie.so
%{_libdir}/%{name}-event/mod_session_crypto.so
%{_libdir}/%{name}-event/mod_session_dbd.so
%{_libdir}/%{name}-event/mod_setenvif.so
%{_libdir}/%{name}-event/mod_slotmem_plain.so
%{_libdir}/%{name}-event/mod_slotmem_shm.so
%{_libdir}/%{name}-event/mod_socache_dbm.so
%{_libdir}/%{name}-event/mod_socache_memcache.so
%{_libdir}/%{name}-event/mod_socache_redis.so
%{_libdir}/%{name}-event/mod_socache_shmcb.so
%{_libdir}/%{name}-event/mod_speling.so
%{_libdir}/%{name}-event/mod_ssl.so
%{_libdir}/%{name}-event/mod_status.so
%{_libdir}/%{name}-event/mod_substitute.so
%{_libdir}/%{name}-event/mod_suexec.so
%{_libdir}/%{name}-event/mod_unique_id.so
%{_libdir}/%{name}-event/mod_userdir.so
%{_libdir}/%{name}-event/mod_usertrack.so
%{_libdir}/%{name}-event/mod_version.so
%{_libdir}/%{name}-event/mod_vhost_alias.so
%{_libdir}/%{name}-event/mod_watchdog.so
%{_libdir}/%{name}-event/mod_xml2enc.so

%files devel -f filelist-devel
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%dir %{installbuilddir}
%dir %{includedir}
%{_bindir}/apxs
%{_sbindir}/apxs
%{_bindir}/apxs2
%{_sbindir}/apxs2

%files doc
%defattr(-,root,root)
%doc %{manualdir}
%dir %{sysconfdir}
%dir %{sysconfdir}/conf.d
%config %{sysconfdir}/conf.d/manual.conf

%files example-pages
%defattr(-,root,root)
%config(noreplace) %{htdocsdir}/index.htm*
%config(noreplace) %{htdocsdir}/favicon.ico
%config(noreplace) %{htdocsdir}/robots.txt

%files utils
%defattr(-,root,root)
%{_mandir}/man?/ab.?.*
%{_mandir}/man?/ab2.?.*
%{_mandir}/man?/dbmmanage.?.*
%{_mandir}/man?/dbmmanage2.?.*
%{_mandir}/man?/htdbm.?.*
%{_mandir}/man?/htdbm2.?.*
%{_mandir}/man?/htdigest.?.*
%{_mandir}/man?/htdigest2.?.*
%{_mandir}/man?/htpasswd.?.*
%{_mandir}/man?/htpasswd2.?.*
%{_mandir}/man?/httxt2dbm.?.*
%{_mandir}/man?/logresolve.?.*
%{_mandir}/man?/logresolve2.?.*
%{_mandir}/man?/rotatelogs.?.*
%{_mandir}/man?/rotatelogs2.?.*
%{_sbindir}/fcgistarter
%{_mandir}/man8/fcgistarter.8.*
%{_bindir}/check_forensic
%{_bindir}/check_forensic2
%{_bindir}/dbmmanage
%{_bindir}/dbmmanage2
%{_bindir}/apache2-find-directives
%{_bindir}/gensslcert
%{_bindir}/htdbm
%{_bindir}/htdbm2
%{_bindir}/htdigest
%{_bindir}/htdigest2
%{_bindir}/htpasswd
%{_bindir}/htpasswd2
%{_bindir}/split-logfile
%{_bindir}/split-logfile2
%{_bindir}/ab
%{_bindir}/ab2
%{_bindir}/httxt2dbm
%{_sbindir}/logresolve.pl
%{_sbindir}/logresolve.pl2
%{_bindir}/logresolve
%{_bindir}/logresolve2
%{_sbindir}/rotatelogs
%{_sbindir}/rotatelogs2

%define install_httpd_link() \
( \
  # it might happen that apache2 including \
  # %{_datadir}/apache2/script-helpers is not installed \
  # yet even if apache2-<MPM> has Requires(post): apache2 \
  # because of circular dependency between apache2 \
  # and apache2-MPM \
  if [ -f %{_datadir}/apache2/script-helpers ]; then \
    . %{_datadir}/apache2/script-helpers \
    find_mpm \
    # when this is run in %post(apache2), it may happen \
    # no MPM is installed so far \
    if [ -n "$HTTPD_MPM" ]; then \
      ln -sf $HTTPD_SBIN_BASE-$HTTPD_MPM $HTTPD_SBIN_BASE \
    fi \
  fi \
)

%post prefork -p /bin/bash
%install_httpd_link
exit 0

%postun prefork -p /bin/bash
if [ "$1" = 1 ]; then
  %apache_request_restart
fi
%install_httpd_link
exit 0

%posttrans prefork
%apache_restart_if_needed
exit 0

%post worker -p /bin/bash
%install_httpd_link
exit 0

%postun worker -p /bin/bash
if [ "$1" = 1 ]; then
  %apache_request_restart
fi
%install_httpd_link
exit 0

%posttrans worker
%apache_restart_if_needed
exit 0

%post event -p /bin/bash
%install_httpd_link
exit 0

%postun event -p /bin/bash
if [ "$1" = 1 ]; then
  %apache_request_restart
fi
%install_httpd_link
exit 0

%posttrans event
%apache_restart_if_needed
exit 0

%pre
%if 0%{?suse_version} >= 1210
%service_add_pre apache2.service
%endif

%preun
%if 0%{?suse_version} >= 1210
%service_del_preun apache2.target
%endif
# removing the symlink in case of uninstall (not upgrade) [bsc#1041830]
if [ "$1" = 0 ]; then
  for i in %{_sbindir}/httpd \
    %{installbuilddir}/config_vars.mk
  do
    test -L $i && rm $i
  done
fi
exit 0

%postun
%if 0%{?suse_version} >= 1210
%service_del_postun_without_restart apache2.target
if [ "$1" = 1 ]; then
  %apache_request_restart
fi
%else
%insserv_cleanup
%endif

%post
%if 0%{?suse_version} <= 1130
%run_permissions
%else
%set_permissions %{_sbindir}/suexec || echo "Please check %{_sysconfdir}/permissions.local for settings of %{_sbindir}/suexec2 ."
%endif
# wwwadmin group existed in past remove after openSUSE-13.2 out of support scope
if grep -q "^wwwadmin:" %{_sysconfdir}/group; then
	groupmod -n www wwwadmin 2>/dev/null ||:
	usermod -g %{httpdgroup} %{httpduser} 2>/dev/null ||:
	usermod -s /bin/false %{httpduser} 2>/dev/null ||:
fi
%{fillup_only apache2}
%if 0%{?suse_version} >= 1210
%service_add_post apache2.service
%else
%{fillup_and_insserv apache2}
%endif
%if %{use_firewalld}
%firewalld_reload
%endif
exit 0

%posttrans
%{_datadir}/%{name}/apache-22-24-upgrade
%apache_restart_if_needed

%verifyscript
%verify_permissions -e %{_sbindir}/suexec

%changelog
