#
# spec file for package icinga2
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


%define revision 1

# make sure that _rundir is working on older systems
%if ! %{defined _rundir}
%define _rundir %{_localstatedir}/run
%endif
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif

%define _libexecdir %{_prefix}/lib/
%define plugindir %{_libdir}/nagios/plugins

%if "%{_vendor}" == "redhat"
%define apachename httpd
%define apacheconfdir %{_sysconfdir}/httpd/conf.d
%define apacheuser apache
%define apachegroup apache

%if 0%{?el5}%{?el6}%{?amzn}
%define use_systemd 0
%define use_selinux 0
%if %(uname -m) != "x86_64"
%define march_flag -march=i686
%endif
%else
# fedora and el>=7
%define use_systemd 1
%define use_selinux 1
%if 0%{?fedora} >= 24
# for installing limits.conf on systemd >= 228
%define configure_systemd_limits 1
%else
%define configure_systemd_limits 0
%endif
%endif
%endif

%if "%{_vendor}" == "suse"
%define plugindir %{icinga2_plugindir}
%define apachename apache2
%define apacheconfdir  %{_sysconfdir}/apache2/conf.d
%define apacheuser wwwrun
%define apachegroup www
%if 0%{?suse_version} >= 1310
%define use_systemd 1
%if 0%{?sle_version} >= 120200 || 0%{?suse_version} > 1320
# for installing limits.conf on systemd >= 228
%define configure_systemd_limits 1
%else
%define configure_systemd_limits 0
%endif
%else
%define use_systemd 0
%endif
%endif

%define icinga_user icinga
%define icinga_group icinga
%define icingacmd_group icingacmd

# enable unity builds by default for all architectures except arm32
%ifarch %{arm}
%bcond_with unity_build
%else
%bcond_without unity_build
%endif
# enable unity builds by default for all distribution except Tumbleweed
%if 0%{?suse_version} > 1500
%define unity_build 0
%else
%define unity_build 1
%endif

%define logmsg logger -t %{name}/rpm

Summary:        Network monitoring application
License:        GPL-2.0-or-later
Group:          System/Monitoring
%if "%{_vendor}" == "suse"
%else
%endif
Name:           icinga2
Version:        2.12.1
Release:        %{revision}%{?dist}
URL:            https://www.icinga.com/
Source:         https://github.com/Icinga/%{name}/archive/v%{version}.tar.gz

Source1:        icinga2-rpmlintrc
%if "%{_vendor}" == "suse"
# PATCH-FEATURE-OPENSUSE ecsos -- insert missing graphite tags as descriped in icingaweb2-module-graphite docs.
Patch0:         icinga2-graphite.patch
%if 0%{?suse_version} > 1500
# PATCH-FEATURE-OPENSUSE ecsos -- Boost in Tumbleweed is to new. Fix boost build error in Tumbleweed. Should be included in version 2.13.0
Patch1:         icinga2-boost-8185-8184.patch
Patch2:         icinga2-boost-8185-8190.patch
Patch3:         icinga2-boost-8185-8191.patch
%endif
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if "%{_vendor}" == "suse"
PreReq:         permissions
Requires:       logrotate
BuildRequires:  nagios-rpm-macros
%endif
Requires:       %{name}-bin = %{version}-%{release}
Requires:       %{name}-common = %{version}-%{release}

Conflicts:      %{name}-common < %{version}-%{release}

%description
Meta package for Icinga 2 Core, DB IDO and Web.

%package bin
Summary:        Icinga 2 binaries and libraries
Group:          System/Monitoring

Requires:       %{name}-bin = %{version}-%{release}

%if "%{_vendor}" == "suse"
Provides:       monitoring_daemon
Recommends:     monitoring-plugins
%if 0%{?suse_version} >= 1310
BuildRequires:  libyajl-devel
%endif
%endif
BuildRequires:  libedit-devel
BuildRequires:  ncurses-devel
%if "%{_vendor}" == "suse" && 0%{?suse_version} < 1210
BuildRequires:  gcc48-c++
BuildRequires:  libopenssl1-devel
BuildRequires:  libstdc++48-devel
%else
%if "%{_vendor}" == "redhat" && (0%{?el5} || 0%{?rhel} == 5 || "%{?dist}" == ".el5" || 0%{?el6} || 0%{?rhel} == 6 || "%{?dist}" == ".el6")
# Requires devtoolset-2 scl
BuildRequires:  devtoolset-2-binutils
BuildRequires:  devtoolset-2-gcc-c++
BuildRequires:  devtoolset-2-libstdc++-devel
%define scl_enable scl enable devtoolset-2 --
%else
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
%endif
BuildRequires:  openssl-devel
%endif
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex >= 2.5.35
BuildRequires:  make

%if 0%{?build_icinga_org} && "%{_vendor}" == "redhat" && (0%{?el5} || 0%{?rhel} == 5 || "%{?dist}" == ".el5" || 0%{?el6} || 0%{?rhel} == 6 || "%{?dist}" == ".el6")
# el5 and el6 require packages.icinga.com
BuildRequires:  boost166-devel
%else
%if 0%{?build_icinga_org} && "%{_vendor}" == "suse" && 0%{?suse_version} < 1310
# sles 11 sp3 requires packages.icinga.com
BuildRequires:  boost166-devel
%else
%if "%{_vendor}" == "suse" && 0%{?suse_version} > 1320
BuildRequires:  libboost_context-devel >= 1.66
BuildRequires:  libboost_coroutine-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_program_options-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_test-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
%else
%if (0%{?el5} || 0%{?rhel} == 5 || "%{?dist}" == ".el5" || 0%{?el6} || 0%{?rhel} == 6 || "%{?dist}" == ".el6")
# Requires EPEL repository
BuildRequires:  boost166-devel >= 1.66
%else
BuildRequires:  boost-devel >= 1.66
%endif
%endif
%endif
%endif

%if 0%{?use_systemd}
BuildRequires:  pkgconfig(libsystemd)
Requires:       systemd
%endif

Obsoletes:      %{name}-libs < %{version}
Provides:       %{name}-libs = %{version}
Conflicts:      %{name}-libs

%description bin
Icinga 2 is a general-purpose network monitoring application.
This subpackage provides the binaries for Icinga 2 Core.

%package common
Summary:        Common Icinga 2 configuration
Group:          System/Monitoring
%if (0%{?amzn} || 0%{?fedora} || 0%{?rhel})
Requires(pre):  shadow-utils
Requires(post): shadow-utils
%endif
BuildRequires:  logrotate
%if "%{_vendor}" == "suse"
PreReq:         permissions
Provides:       group(%{icinga_group})
Provides:       group(%{icingacmd_group})
Provides:       user(%{icinga_user})
Requires(pre):  shadow
Requires(post): shadow
# Coreutils is added because of autoyast problems reported
Requires(pre):  coreutils
Requires(post): coreutils
%if 0%{?suse_version} >= 1200
BuildRequires:  monitoring-plugins-common
Requires:       monitoring-plugins-common
%else
Recommends:     monitoring-plugins-common
%endif
Recommends:     logrotate
%endif

%description common
This subpackage provides common directories, and the UID and GUID definitions
among Icinga 2 related packages.


%package doc
Summary:        Documentation for Icinga 2
Group:          Documentation/Other

%description doc
This subpackage provides documentation for Icinga 2.


%package ido-mysql
Summary:        IDO MySQL database backend for Icinga 2
Group:          System/Monitoring
%if "%{_vendor}" == "suse"
BuildRequires:  libmysqlclient-devel
%if 0%{?suse_version} >= 1310
BuildRequires:  mysql-devel
%endif

%else
BuildRequires:  mysql-devel
%endif

Requires:       %{name}-bin = %{version}-%{release}

%description ido-mysql
Icinga 2 IDO mysql database backend. Compatible with Icinga 1.x
IDOUtils schema >= 1.12


%package ido-pgsql
Summary:        IDO PostgreSQL database backend for Icinga 2
Group:          System/Monitoring
%if "%{_vendor}" == "suse" && 0%{?suse_version} < 1210
BuildRequires:  postgresql-devel >= 8.4
%else
BuildRequires:  postgresql-devel
%endif
Requires:       %{name}-bin = %{version}-%{release}

%description ido-pgsql
Icinga 2 IDO PostgreSQL database backend. Compatible with Icinga 1.x
IDOUtils schema >= 1.12

%if 0%{?use_selinux}
%global selinux_variants mls targeted
%global selinux_modulename %{name}

%package selinux
Summary:        SELinux policy module supporting icinga2
Group:          System/Base
BuildRequires:  checkpolicy
BuildRequires:  hardlink
BuildRequires:  selinux-policy-devel
Requires:       %{name}-bin = %{version}-%{release}
Requires(post):   policycoreutils-python
Requires(postun): policycoreutils-python

%description selinux
SELinux policy module supporting icinga2.
%endif

%package -n vim-icinga2
Summary:        Vim syntax highlighting for icinga2
Group:          Productivity/Text/Editors
%if "%{_vendor}" == "suse"
BuildRequires:  vim
Requires:       vim
%else
Requires:       vim-filesystem
%endif

%description -n vim-icinga2
Provides Vim syntax highlighting for icinga2.


%package -n nano-icinga2
Summary:        Nano syntax highlighting for icinga2
Group:          Productivity/Text/Editors
Requires:       nano

%description -n nano-icinga2
Provides Nano syntax highlighting for icinga2.

%prep
%setup -q -n %{name}-%{version}
# use absolute shebang instead of env on SUSE distributions
%if "%{_vendor}" == "suse"
find . -type f -name '*.sh' -exec sed -i -e 's|\/usr\/bin\/env bash|\/bin\/bash|g' {} \;
%patch0 -p1
%if 0%{?suse_version} > 1500
# Fix boost biuld error in Tumbleed. Should be fixed in 2.13.0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%endif
%endif

%build
CMAKE_OPTS="-DCMAKE_INSTALL_PREFIX=/usr \
         -DCMAKE_INSTALL_SYSCONFDIR=/etc \
         -DCMAKE_INSTALL_LOCALSTATEDIR=/var \
         -DCMAKE_BUILD_TYPE=RelWithDebInfo \
         -DICINGA2_LTO_BUILD=ON \
         -DCMAKE_NO_BUILTIN_CHRPATH=ON \
         -DCMAKE_VERBOSE_MAKEFILE=ON \
         -DBoost_NO_BOOST_CMAKE=ON \
         -DICINGA2_PLUGINDIR=%{plugindir} \
         -DICINGA2_RUNDIR=%{_rundir} \
         -DICINGA2_SYSCONFIGFILE=/etc/sysconfig/icinga2 \
         -DICINGA2_USER=%{icinga_user} \
         -DICINGA2_GROUP=%{icinga_group} \
         -DICINGA2_COMMAND_GROUP=%{icingacmd_group}"
%if 0%{?fedora}
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_STUDIO=true"
%endif

%if %{unity_build}
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_UNITY_BUILD=ON "
%else
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_UNITY_BUILD=OFF "
%endif

%if "%{_vendor}" == "redhat"
%if 0%{?el5} || 0%{?rhel} == 5 || "%{?dist}" == ".el5" || 0%{?el6} || 0%{?rhel} == 6 || "%{?dist}" == ".el6"
%if 0%{?build_icinga_org}
# Boost_VERSION 1.41.0 vs 101400 - disable build tests
# details in https://dev.icinga.com/issues/5033
CMAKE_OPTS="$CMAKE_OPTS -DBOOST_LIBRARYDIR=%{_libdir}/boost153 \
 -DBOOST_INCLUDEDIR=/usr/include/boost153 \
 -DBoost_ADDITIONAL_VERSIONS='1.53;1.53.0'"
%else
CMAKE_OPTS="$CMAKE_OPTS -DBOOST_LIBRARYDIR=%{_libdir}/boost148 \
 -DBOOST_INCLUDEDIR=/usr/include/boost148 \
 -DBoost_ADDITIONAL_VERSIONS='1.48;1.48.0'"
%endif
CMAKE_OPTS="$CMAKE_OPTS \
 -DBoost_NO_SYSTEM_PATHS=TRUE \
 -DBUILD_TESTING=FALSE \
 -DBoost_NO_BOOST_CMAKE=TRUE"
%endif
%endif

%if "%{_vendor}" == "suse" && 0%{?suse_version} < 1310
CMAKE_OPTS="$CMAKE_OPTS -DBOOST_LIBRARYDIR=%{_libdir}/boost153 \
 -DBOOST_INCLUDEDIR=/usr/include/boost153 \
 -DBoost_ADDITIONAL_VERSIONS='1.53;1.53.0' \
 -DBoost_NO_SYSTEM_PATHS=TRUE \
 -DBUILD_TESTING=FALSE \
 -DBoost_NO_BOOST_CMAKE=TRUE"
%endif

%if 0%{?use_systemd}
CMAKE_OPTS="$CMAKE_OPTS -DUSE_SYSTEMD=ON"
%endif

%if "%{_vendor}" == "suse" && 0%{?suse_version} < 1210
# from package gcc48-c++
export CC=gcc-4.8
export CXX=g++-4.8
%endif

%if "%{?_buildhost}" != ""
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_BUILD_HOST_NAME:STRING=%_buildhost"
%endif

%{?scl_enable} cmake $CMAKE_OPTS -DCMAKE_C_FLAGS:STRING="%{optflags} %{?march_flag}" -DCMAKE_CXX_FLAGS:STRING="%{optflags} %{?march_flag}" .

make %{?_smp_mflags}

%if 0%{?use_selinux}
cd tools/selinux
for selinuxvariant in %{selinux_variants}
do
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile
  mv %{selinux_modulename}.pp %{selinux_modulename}.pp.${selinuxvariant}
  make NAME=${selinuxvariant} -f /usr/share/selinux/devel/Makefile clean
done
cd -
%endif

%install
make install \
  DESTDIR="%{buildroot}"

# install custom limits.conf for systemd
%if 0%{?configure_systemd_limits}
# for > 2.8 or > 2.7.2
%if "%{_vendor}" == "suse"
install -D -m 0644 etc/initsystem/icinga2.service.limits.conf %{buildroot}/%{_unitdir}/%{name}.service.d/limits.conf
%else
install -D -m 0644 etc/initsystem/icinga2.service.limits.conf %{buildroot}/etc/systemd/system/%{name}.service.d/limits.conf
%endif
%endif

# remove features-enabled symlinks
rm -f %{buildroot}/%{_sysconfdir}/%{name}/features-enabled/*.conf

# enable suse rc links
%if "%{_vendor}" == "suse"
%if 0%{?use_systemd}
  ln -sf /usr/sbin/service %{buildroot}%{_sbindir}/rc%{name}
%else
  ln -sf ../../%{_initrddir}/%{name} "%{buildroot}%{_sbindir}/rc%{name}"
%endif
mkdir -p "%{buildroot}%{_fillupdir}/"
mv "%{buildroot}%{_sysconfdir}/sysconfig/%{name}" "%{buildroot}%{_fillupdir}/sysconfig.%{name}"
%endif

%if 0%{?use_selinux}
cd tools/selinux
for selinuxvariant in %{selinux_variants}
do
  install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
  install -p -m 644 %{selinux_modulename}.pp.${selinuxvariant} \
    %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{selinux_modulename}.pp
done
cd -

# TODO: Fix build problems on Icinga, see https://github.com/Icinga/puppet-icinga_build/issues/11
#/usr/sbin/hardlink -cv %%{buildroot}%%{_datadir}/selinux
%endif

%if "%{_vendor}" == "suse"
install -D -m 0644 tools/syntax/vim/syntax/%{name}.vim %{buildroot}%{_datadir}/vim/site/syntax/%{name}.vim
install -D -m 0644 tools/syntax/vim/ftdetect/%{name}.vim %{buildroot}%{_datadir}/vim/site/ftdetect/%{name}.vim
%else
install -D -m 0644 tools/syntax/vim/syntax/%{name}.vim %{buildroot}%{_datadir}/vim/vimfiles/syntax/%{name}.vim
install -D -m 0644 tools/syntax/vim/ftdetect/%{name}.vim %{buildroot}%{_datadir}/vim/vimfiles/ftdetect/%{name}.vim
%endif

install -D -m 0644 tools/syntax/nano/%{name}.nanorc %{buildroot}%{_datadir}/nano/%{name}.nanorc

%pre
%if "%{_vendor}" == "suse"
%if 0%{?use_systemd}
  %service_add_pre %{name}.service
%endif

%verifyscript
%verify_permissions -e %{_rundir}/%{name}/cmd
%endif

%post
# suse
%if "%{_vendor}" == "suse"
%if 0%{?suse_version} >= 1310
%set_permissions %{_rundir}/%{name}/cmd
%endif

%if 0%{?use_systemd}
%fillup_only  %{name}
%service_add_post %{name}.service
%else
%fillup_and_insserv %{name}
%endif

if [ ${1:-0} -eq 1 ]
then
  # initial installation, enable default features
  for feature in checker notification mainlog; do
    ln -sf ../features-available/${feature}.conf %{_sysconfdir}/%{name}/features-enabled/${feature}.conf
  done
fi

exit 0

%else
# rhel

%if 0%{?use_systemd}
%systemd_post %{name}.service
%else
/sbin/chkconfig --add %{name}
%endif

if [ ${1:-0} -eq 1 ]
then
  # initial installation, enable default features
  for feature in checker notification mainlog; do
    ln -sf ../features-available/${feature}.conf %{_sysconfdir}/%{name}/features-enabled/${feature}.conf
  done
fi

exit 0

%endif
# suse/rhel

%preun
# suse
%if "%{_vendor}" == "suse"

%if 0%{?use_systemd}
  %service_del_preun %{name}.service
%else
  %stop_on_removal %{name}
%endif

exit 0

%else
# rhel

%if 0%{?use_systemd}
%systemd_preun %{name}.service
%else
if [ "$1" = "0" ]; then
  /sbin/service %{name} stop > /dev/null 2>&1 || :
  /sbin/chkconfig --del %{name} || :
fi
%endif

exit 0

%endif
# suse / rhel

%postun
# suse
%if "%{_vendor}" == "suse"
%if 0%{?use_systemd}
  %service_del_postun %{name}.service
%else
  %restart_on_update %{name}
  %insserv_cleanup
%endif

%else
# rhel

%if 0%{?use_systemd}
%systemd_postun_with_restart %{name}.service
%else
if [ "$1" -ge  "1" ]; then
  /sbin/service %{name} condrestart >/dev/null 2>&1 || :
fi
%endif

%endif
# suse / rhel

if [ "$1" = "0" ]; then
  # deinstallation of the package - remove enabled features
  rm -rf %{_sysconfdir}/%{name}/features-enabled
fi

exit 0

%pre common
getent group %{icinga_group} >/dev/null || %{_sbindir}/groupadd -r %{icinga_group}
getent group %{icingacmd_group} >/dev/null || %{_sbindir}/groupadd -r %{icingacmd_group}
getent passwd %{icinga_user} >/dev/null || %{_sbindir}/useradd -c "icinga" -s /sbin/nologin -r -d %{_localstatedir}/spool/%{name} -G %{icingacmd_group} -g %{icinga_group} %{icinga_user}

%if "%{_vendor}" == "suse"
%verifyscript common
%verify_permissions -e %{_rundir}/%{name}/cmd
%endif

%post common
%if "%{_vendor}" == "suse"
%if 0%{?suse_version} >= 1310
%set_permissions %{_rundir}/%{name}/cmd
%endif
%endif

%post ido-mysql
if [ ${1:-0} -eq 1 ] && [ -e %{_sysconfdir}/%{name}/features-enabled/ido-mysql.conf ]
then
  # initial installation, enable ido-mysql feature
  ln -sf ../features-available/ido-mysql.conf %{_sysconfdir}/%{name}/features-enabled/ido-mysql.conf
fi

exit 0

%postun ido-mysql
if [ "$1" = "0" ]; then
  # deinstallation of the package - remove feature
  rm -f %{_sysconfdir}/%{name}/features-enabled/ido-mysql.conf
fi

exit 0

%post ido-pgsql
if [ ${1:-0} -eq 1 ] && [ -e %{_sysconfdir}/%{name}/features-enabled/ido-pgsql.conf ]
then
  # initial installation, enable ido-pgsql feature
  ln -sf ../features-available/ido-pgsql.conf %{_sysconfdir}/%{name}/features-enabled/ido-pgsql.conf
fi

exit 0

%postun ido-pgsql
if [ "$1" = "0" ]; then
  # deinstallation of the package - remove feature
  rm -f %{_sysconfdir}/%{name}/features-enabled/ido-pgsql.conf
fi

exit 0

%if 0%{?use_selinux}
%post selinux
for selinuxvariant in %{selinux_variants}
do
  /usr/sbin/semodule -s ${selinuxvariant} -i \
    %{_datadir}/selinux/${selinuxvariant}/%{selinux_modulename}.pp &> /dev/null || :
done
/sbin/fixfiles -R icinga2-bin restore &> /dev/null || :
/sbin/fixfiles -R icinga2-common restore &> /dev/null || :
/sbin/semanage port -a -t icinga2_port_t -p tcp 5665 &> /dev/null || :

%postun selinux
if [ $1 -eq 0 ] ; then
  /sbin/semanage port -d -t icinga2_port_t -p tcp 5665 &> /dev/null || :
  for selinuxvariant in %{selinux_variants}
  do
     /usr/sbin/semodule -s ${selinuxvariant} -r %{selinux_modulename} &> /dev/null || :
  done
  /sbin/fixfiles -R icinga2-bin restore &> /dev/null || :
  /sbin/fixfiles -R icinga2-common restore &> /dev/null || :
fi
%endif

%files
%defattr(-,root,root,-)
%license COPYING

%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}

%if 0%{?use_systemd}
%attr(644,root,root) %{_unitdir}/%{name}.service
%if 0%{?configure_systemd_limits}
%if "%{_vendor}" == "suse"
%dir %{_unitdir}/%{name}.service.d
%{_unitdir}/%{name}.service.d/limits.conf
%else
%dir /etc/systemd/system/%{name}.service.d
%attr(644,root,root) %config(noreplace) /etc/systemd/system/%{name}.service.d/limits.conf
%endif
%endif
%else
%attr(755,root,root) %config(noreplace) %{_sysconfdir}/init.d/%{name}
%endif
%if "%{_vendor}" == "suse"
%{_sbindir}/rc%{name}
%{_fillupdir}/sysconfig.%{name}
%else
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%endif

%{_sbindir}/%{name}

%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/prepare-dirs
%{_libexecdir}/%{name}/safe-reload

%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/conf.d
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/features-available
%exclude %{_sysconfdir}/%{name}/features-available/ido-*.conf
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/features-enabled
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/scripts
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/%{name}/zones.d
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/constants.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/zones.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/conf.d/*.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/features-available/*.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/zones.d/*
%config(noreplace) %{_sysconfdir}/%{name}/scripts/*

%attr(0750,%{icinga_user},%{icingacmd_group}) %{_localstatedir}/cache/%{name}
%attr(0750,%{icinga_user},%{icingacmd_group}) %dir %{_localstatedir}/log/%{name}
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/log/%{name}/crash
%attr(0750,%{icinga_user},%{icingacmd_group}) %dir %{_localstatedir}/log/%{name}/compat
%attr(0750,%{icinga_user},%{icingacmd_group}) %dir %{_localstatedir}/log/%{name}/compat/archives
%attr(0750,%{icinga_user},%{icinga_group}) %{_localstatedir}/lib/%{name}
%attr(0750,%{icinga_user},%{icingacmd_group}) %ghost %dir %{_rundir}/%{name}
%attr(2750,%{icinga_user},%{icingacmd_group}) %ghost %{_rundir}/%{name}/cmd
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/spool/%{name}
%attr(0770,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/spool/%{name}/perfdata
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/spool/%{name}/tmp

%files bin
%defattr(-,root,root,-)
%license COPYING 
%doc README.md NEWS AUTHORS CHANGELOG.md
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/sbin
%{_libdir}/%{name}/sbin/%{name}
%{plugindir}/check_nscp_api
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/include
%{_mandir}/man8/%{name}.8.gz

%files common
%defattr(-,root,root,-)
%license COPYING 
%doc README.md NEWS AUTHORS CHANGELOG.md tools/syntax
%{_sysconfdir}/bash_completion.d/%{name}
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_datadir}/%{name}/include
%{_datadir}/%{name}/include/*

%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/%{name}
%docdir %{_datadir}/doc/%{name}

%files ido-mysql
%defattr(-,root,root,-)
%license COPYING 
%doc README.md NEWS AUTHORS CHANGELOG.md
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/features-available/ido-mysql.conf
%{_libdir}/%{name}/libmysql_shim*
%{_datadir}/icinga2-ido-mysql

%files ido-pgsql
%defattr(-,root,root,-)
%license COPYING 
%doc README.md NEWS AUTHORS CHANGELOG.md
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/%{name}/features-available/ido-pgsql.conf
%{_libdir}/%{name}/libpgsql_shim*
%{_datadir}/icinga2-ido-pgsql

%if 0%{?use_selinux}
%files selinux
%defattr(-,root,root,0755)
%doc tools/selinux/*
%{_datadir}/selinux/*/%{selinux_modulename}.pp
%endif

%files -n vim-icinga2
%defattr(-,root,root,-)
%if "%{_vendor}" == "suse"
%{_datadir}/vim/site/syntax/%{name}.vim
%{_datadir}/vim/site/ftdetect/%{name}.vim
%else
%{_datadir}/vim/vimfiles/syntax/%{name}.vim
%{_datadir}/vim/vimfiles/ftdetect/%{name}.vim
%endif

%files -n nano-icinga2
%defattr(-,root,root,-)
%if "%{_vendor}" == "suse"
%dir %{_datadir}/nano
%endif
%{_datadir}/nano/%{name}.nanorc

%changelog
