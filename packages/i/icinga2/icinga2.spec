#
# spec file for package icinga2
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

Name:           icinga2
Version:        2.14.3
Release:        0
Summary:        Network monitoring application
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://www.icinga.com/
Source:         https://github.com/Icinga/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        icinga2-rpmlintrc
# PATCH-FEATURE-OPENSUSE ecsos -- insert missing graphite tags as descriped in icingaweb2-module-graphite docs.
Patch0:         icinga2-graphite.patch
# PATCH-FIX-OPENSUSE lrupp -- fixing the syntax file for vim >= 8.x
Patch1:         icinga2-vim_syntax.patch
PreReq:         permissions
BuildRequires:  nagios-rpm-macros
Requires:       icinga2-bin = %{version}
Requires:       icinga2-common = %{version}
Conflicts:      icinga2-common < %{version}

%description
Meta package for Icinga 2 Core, DB IDO and Web.

%package bin
Summary:        Icinga 2 binaries and libraries
Group:          System/Monitoring
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex >= 2.5.35
BuildRequires:  gcc-c++
BuildRequires:  libboost_context-devel >= 1.66
BuildRequires:  libboost_coroutine-devel >= 1.66
BuildRequires:  libboost_filesystem-devel >= 1.66
BuildRequires:  libboost_iostreams-devel >= 1.66
BuildRequires:  libboost_program_options-devel >= 1.66
BuildRequires:  libboost_regex-devel >= 1.66
BuildRequires:  libboost_system-devel >= 1.66
BuildRequires:  libboost_test-devel >= 1.66
BuildRequires:  libboost_thread-devel >= 1.66
BuildRequires:  pkgconfig(libedit)
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(yajl)
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
Requires:       icinga2-bin = %{version}
Requires:       systemd
Recommends:     monitoring-plugins
Conflicts:      icinga2-libs <= 2.10.0
Provides:       monitoring_daemon
Obsoletes:      icinga2-libs <= 2.10.0

%description bin
Icinga 2 is a general-purpose network monitoring application.
This subpackage provides the binaries for Icinga 2 Core.

%package common
Summary:        Common Icinga 2 configuration
Group:          System/Monitoring
BuildRequires:  logrotate
BuildRequires:  monitoring-plugins-common
Requires:       monitoring-plugins-common
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         permissions
Requires(post): coreutils
Requires(post): shadow
Requires(pre):  coreutils
Requires(pre):  shadow
Recommends:     logrotate
Provides:       group(%{icinga_group})
Provides:       group(%{icinga_command_group})
Provides:       user(%{icinga_user})

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
BuildRequires:  libmysqlclient-devel
BuildRequires:  mysql-devel
Requires:       icinga2-bin = %{version}

%description ido-mysql
Icinga 2 IDO mysql database backend. Compatible with Icinga 1.x
IDOUtils schema >= 1.12

%package ido-pgsql
Summary:        IDO PostgreSQL database backend for Icinga 2
Group:          System/Monitoring
BuildRequires:  postgresql-devel
Requires:       icinga2-bin = %{version}

%description ido-pgsql
Icinga 2 IDO PostgreSQL database backend. Compatible with Icinga 1.x
IDOUtils schema >= 1.12

%package -n vim-icinga2
Summary:        Vim syntax highlighting for icinga2
Group:          Productivity/Text/Editors
BuildRequires:  vim
Requires:       vim

%description -n vim-icinga2
Provides Vim syntax highlighting for icinga2.

%package -n nano-icinga2
Summary:        Nano syntax highlighting for icinga2
Group:          Productivity/Text/Editors
Requires:       nano

%description -n nano-icinga2
Provides Nano syntax highlighting for icinga2.

%prep
%autosetup -p1
find . -type f -name '*.sh' -exec sed -i -e 's|\/usr\/bin\/env bash|\/bin\/bash|g' {} \;

%build
export CCACHE_BASEDIR="${CCACHE_BASEDIR:-$(pwd)}"

CMAKE_OPTS="-DCMAKE_INSTALL_PREFIX=%{_prefix} \
            -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
            -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir} \
            -DCMAKE_BUILD_TYPE=RelWithDebInfo \
            -DCMAKE_VERBOSE_MAKEFILE=ON \
            -DBoost_NO_BOOST_CMAKE=ON \
            -DICINGA2_PLUGINDIR=%{icinga2_plugindir} \
            -DICINGA2_RUNDIR=/run \
            -DICINGA2_SYSCONFIGFILE=%{_sysconfdir}/sysconfig/icinga2 \
            -DICINGA2_USER=%{icinga_user} \
            -DICINGA2_GROUP=%{icinga_group} \
            -DICINGA2_COMMAND_GROUP=%{icinga_command_group}"

CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_UNITY_BUILD=ON"

CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_LTO_BUILD=OFF"

CMAKE_OPTS="$CMAKE_OPTS -DINSTALL_SYSTEMD_SERVICE_AND_INITSCRIPT=OFF"
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_COMPAT=ON"
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_LIVESTATUS=ON"
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_NOTIFICATION=ON"
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_PERFDATA=ON"
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_TESTS=ON"
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_MYSQL=ON"
CMAKE_OPTS="$CMAKE_OPTS -DICINGA2_WITH_PGSQL=ON"

CMAKE_OPTS="$CMAKE_OPTS -DUSE_SYSTEMD=ON"

# FIXME: you should use the %%cmake macros
cmake $CMAKE_OPTS -DCMAKE_C_FLAGS:STRING="-O2 -g -m64 -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables " -DCMAKE_CXX_FLAGS:STRING="-O2 -g -m64 -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables " .

%make_build

%install
make install \
DESTDIR="%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.x86_64"
install -D -m 0644 etc/initsystem/icinga2.service.limits.conf %{buildroot}/%{_unitdir}/%{name}.service.d/limits.conf

rm -f %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.x86_64/%{_sysconfdir}/icinga2/features-enabled/*.conf

ln -sf %{_sbindir}/service %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.x86_64/usr/sbin/rcicinga2
mkdir -p "%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.x86_64/%{_fillupdir}"
mv "%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.x86_64%{_sysconfdir}/sysconfig/icinga2" "%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.x86_64/%{_fillupdir}/sysconfig.icinga2"

install -D -m 0644 tools/syntax/vim/syntax/icinga2.vim %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.x86_64/usr/share/vim/site/syntax/icinga2.vim
install -D -m 0644 tools/syntax/vim/ftdetect/icinga2.vim %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.x86_64/usr/share/vim/site/ftdetect/icinga2.vim

install -D -m 0644 tools/syntax/nano/icinga2.nanorc %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.x86_64/usr/share/nano/icinga2.nanorc

%check
export CTEST_OUTPUT_ON_FAILURE=1
%make_build test

%pre
%service_add_pre %{name}.service

%verifyscript

%{_bindir}/chkstat -n --warn --system -e /run/icinga2/cmd 1>&2

%post

if [ -x %{_bindir}/chkstat ]; then
%{_bindir}/chkstat -n --set --system /run/icinga2/cmd
fi

%fillup_only  %{name}
%service_add_post %{name}.service

if [ ${1:-0} -eq 1 ]
then
  # initial installation, enable default features
  for feature in checker notification mainlog; do
    ln -sf ../features-available/${feature}.conf %{_sysconfdir}/icinga2/features-enabled/${feature}.conf
  done
fi

exit 0

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service
if [ "$1" = "0" ]; then
rm -rf %{_sysconfdir}/icinga2/features-enabled
fi

exit 0

%pre common
getent group %{icinga_group} >/dev/null || %{_sbindir}/groupadd -r %{icinga_group}
getent group %{icinga_command_group} >/dev/null || %{_sbindir}/groupadd -r %{icinga_command_group}
getent passwd %{icinga_user} >/dev/null || %{_sbindir}/useradd -c "icinga" -s /sbin/nologin -r -d %{_localstatedir}/spool/icinga2 -G %{icinga_command_group} -g %{icinga_group} %{icinga_user}

%verifyscript common

%{_bindir}/chkstat -n --warn --system -e /run/icinga2/cmd 1>&2

%post common

if [ -x %{_bindir}/chkstat ]; then
%{_bindir}/chkstat -n --set --system /run/icinga2/cmd
fi

%post ido-mysql
if [ ${1:-0} -eq 1 ] && [ -e %{_sysconfdir}/icinga2/features-enabled/ido-mysql.conf ]
then
ln -sf ../features-available/ido-mysql.conf %{_sysconfdir}/icinga2/features-enabled/ido-mysql.conf
fi

exit 0

%postun ido-mysql
if [ "$1" = "0" ]; then
rm -f %{_sysconfdir}/icinga2/features-enabled/ido-mysql.conf
fi

exit 0

%post ido-pgsql
if [ ${1:-0} -eq 1 ] && [ -e %{_sysconfdir}/icinga2/features-enabled/ido-pgsql.conf ]
then
ln -sf ../features-available/ido-pgsql.conf %{_sysconfdir}/icinga2/features-enabled/ido-pgsql.conf
fi

exit 0

%postun ido-pgsql
if [ "$1" = "0" ]; then
rm -f %{_sysconfdir}/icinga2/features-enabled/ido-pgsql.conf
fi

exit 0

%files
%license COPYING

%config(noreplace) %{_sysconfdir}/logrotate.d/icinga2
%dir %{_unitdir}/%{name}.service.d
%attr(644,root,root) %{_unitdir}/%{name}.service
%{_unitdir}/%{name}.service.d/limits.conf
%{_sbindir}/rc%{name}
%{_fillupdir}/sysconfig.%{name}

%{_sbindir}/%{name}

%dir %{_prefix}/lib/icinga2
%{_prefix}/lib/icinga2/prepare-dirs
%{_prefix}/lib/icinga2/safe-reload

%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/icinga2
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/icinga2/conf.d
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/icinga2/features-available
%exclude %{_sysconfdir}/icinga2/features-available/ido-*.conf
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/icinga2/features-enabled
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/icinga2/scripts
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_sysconfdir}/icinga2/zones.d
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/icinga2/icinga2.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/icinga2/constants.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/icinga2/zones.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/icinga2/conf.d/*.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/icinga2/features-available/*.conf
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/icinga2/zones.d/*
%config(noreplace) %{_sysconfdir}/icinga2/scripts/*

%attr(0750,%{icinga_user},%{icinga_command_group}) %{_localstatedir}/cache/icinga2
%attr(0750,%{icinga_user},%{icinga_command_group}) %dir %{_localstatedir}/log/icinga2
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/log/icinga2/crash
%attr(0750,%{icinga_user},%{icinga_command_group}) %dir %{_localstatedir}/log/icinga2/compat
%attr(0750,%{icinga_user},%{icinga_command_group}) %dir %{_localstatedir}/log/icinga2/compat/archives
%attr(0750,%{icinga_user},%{icinga_group}) %{_localstatedir}/lib/icinga2
%attr(0750,%{icinga_user},%{icinga_command_group}) %ghost %dir /run/icinga2
%attr(2750,%{icinga_user},%{icinga_command_group}) %ghost /run/icinga2/cmd
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/spool/icinga2
%attr(0770,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/spool/icinga2/perfdata
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_localstatedir}/spool/icinga2/tmp

%files bin
%license COPYING
%doc README.md NEWS AUTHORS CHANGELOG.md
%dir %{_libdir}/icinga2
%dir %{_libdir}/icinga2/sbin
%{_libdir}/icinga2/sbin/icinga2
%{icinga2_plugindir}/check_nscp_api
%{_datadir}/icinga2
%exclude %{_datadir}/icinga2/include
%{_mandir}/man8/icinga2.8%{?ext_man}

%files common
%license COPYING
%doc README.md NEWS AUTHORS CHANGELOG.md tools/syntax
%{_sysconfdir}/bash_completion.d/icinga2
%attr(0750,%{icinga_user},%{icinga_group}) %dir %{_datadir}/icinga2/include
%{_datadir}/icinga2/include/*

%files doc
%{_datadir}/doc/icinga2
%docdir %{_datadir}/doc/icinga2

%files ido-mysql
%license COPYING
%doc README.md NEWS AUTHORS CHANGELOG.md
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/icinga2/features-available/ido-mysql.conf
%{_libdir}/icinga2/libmysql_shim*
%{_datadir}/icinga2-ido-mysql

%files ido-pgsql
%license COPYING
%doc README.md NEWS AUTHORS CHANGELOG.md
%config(noreplace) %attr(0640,%{icinga_user},%{icinga_group}) %{_sysconfdir}/icinga2/features-available/ido-pgsql.conf
%{_libdir}/icinga2/libpgsql_shim*
%{_datadir}/icinga2-ido-pgsql

%files -n vim-icinga2
%{_datadir}/vim/site/syntax/icinga2.vim
%{_datadir}/vim/site/ftdetect/icinga2.vim

%files -n nano-icinga2
%dir %{_datadir}/nano
%{_datadir}/nano/icinga2.nanorc

%changelog
