#
# spec file for package firebird
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


%define up_stage 0

Name:           firebird
Version:        3.0.6.33328
Release:        0
Summary:        Database system (common files)
License:        SUSE-IDPL-1.0 AND SUSE-IBPL-1.0
Group:          Productivity/Databases/Servers
URL:            https://www.firebirdsql.org/
# https://github.com/FirebirdSQL/firebird/releases/ - fetch and run firebird-clean-tar.sh
Source:         Firebird-%{version}-%{up_stage}.tar.xz
Source1:        README.SUSE
Source2:        50-server.conf
Source3:        firebird-clean-tar.sh
Source999:      baselibs.conf
BuildRequires:  autoconf >= 2.67
BuildRequires:  gcc-c++
BuildRequires:  libedit-devel
BuildRequires:  libicu-devel
BuildRequires:  libtommath-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  zlib-devel
Requires(pre):  pwdutils
Requires(pre):  %insserv_prereq

%if 0%{?suse_version} < 1130
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif

Patch1:         fbguard-allow-creating-a-guard-pidfile.patch
Patch2:         use-killproc-in-stop-branch-of-SuSE-init-script.patch
Patch3:         disable-xinetd-service-by-default.patch
Patch4:         add-pkgconfig-files.patch
Patch5:         Provide-sized-global-delete-operators-when-compiled-.patch
Patch6:         unicode-handle-new-SUSE-ICU-version-hack.patch
# work around problems with old g++
Patch91:        work-around-g-problem-in-SLE11.patch
Patch92:        use-C-98-on-SLE11.patch

%description
This package provides common files needed by both client and server
installations of Firebird RDBMS.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%prep
%setup -q -n Firebird-%{version}-%{up_stage}
# check for files with unclear licensing (bsc#763446)
if [ -d extern/SfIO ]; then
    echo "please repack the tarball without extern/SfIO directory (see bsc#763446)" >&2
    exit 1
fi
# --
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
# --
# work around a problem with old g++
%if 0%{?suse_version} < 1140
%patch91 -p1
%patch92 -p1
%endif

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="${CFLAGS} -fno-delete-null-pointer-checks"
./autogen.sh --prefix=%{_prefix} \
  --with-system-editline \
  --with-fbbin=%{_bindir} \
  --with-fbsbin=%{_sbindir} \
  --with-fbconf=%{_sysconfdir}/%{name} \
  --with-fblib=%{_libdir} \
  --with-fbinclude=%{_includedir} \
  --with-fbdoc=%{_docdir}/%{name} \
  --with-fbudf=%{_libdir}/%{name}/udf \
  --with-fbsample=%{_docdir}/%{name}/sample \
  --with-fbsample-db=%{_localstatedir}/lib/%{name}/sample \
  --with-fbhelp=%{_libdir}/%{name}/lib \
  --with-fbintl=%{_libdir}/%{name}/intl \
  --with-fbmisc=%{_datadir}/%{name}/misc \
  --with-fbsecure-db=%{_localstatedir}/lib/%{name}/secdb \
  --with-fbmsg=%{_libdir}/%{name}/lib \
  --with-fblog=%{_localstatedir}/log/%{name} \
  --with-fbglock=%{_localstatedir}/run/%{name} \
  --with-fbplugins=%{_libdir}/%{name}/plugins
make %{?_smp_mflags}
cd gen
make %{?_smp_mflags} -f Makefile.install buildRoot
chmod -R u+w buildroot%{_docdir}/%{name}
cat >>buildroot%{_sysconfdir}/%{name}/firebird.conf <<EOT

# allow additional config files
include \$(dir_conf)/firebird.conf.d/*.conf
EOT

%install
chmod u+rw,a+rx gen/buildroot/usr/include/firebird/impl
cp -r gen/buildroot/* %{buildroot}/
mkdir -p %{buildroot}%{_initddir}
install -m 755 gen/install/misc/firebird.init.d.suse \
  %{buildroot}%{_initddir}/firebird
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cp -v gen/install/misc/*.pc %{buildroot}%{_libdir}/pkgconfig/
cd %{buildroot}
mkdir -p .%{_libdir}/%{name}/utils
mv -v .%{_sbindir}/*.sh .%{_libdir}/%{name}/utils/
mv -v .%{_sbindir}/fb_config .%{_libdir}/%{name}/utils/
rm -vf .%{_libdir}/libicu*.so
mv -vi .%{_bindir}/isql .%{_bindir}/isql-fb
mv -vi .%{_bindir}/gstat .%{_bindir}/gstat-fb
mv -vi .%{_includedir}/ibase.h .%{_includedir}/%{name}/
mv -vi .%{_includedir}/iberror.h .%{_includedir}/%{name}/
mv -vi .%{_includedir}/ib_util.h .%{_includedir}/%{name}/
rm -vf .%{_includedir}/*.h
chmod -R u+w .%{_docdir}/%{name}
rm -vf .%{_datadir}/%{name}/misc/firebird.init.*
rm -vf .%{_datadir}/%{name}/misc/rc.config.firebird
%if 0%{?suse_version} < 1500 || 0%{?is_opensuse}
mkdir -p .%{_sysconfdir}/xinetd.d
mv -v .%{_datadir}/%{name}/misc/firebird.xinetd \
  .%{_sysconfdir}/xinetd.d/%{name}
%endif
mv -v .%{_sysconfdir}/%{name}/README .%{_sysconfdir}/%{name}/WhatsNew \
  .%{_docdir}/%{name}/
mv -v .%{_sysconfdir}/%{name}/IDPLicense.txt .%{_docdir}/%{name}/
mv -v .%{_sysconfdir}/%{name}/IPLicense.txt .%{_docdir}/%{name}/
chmod -R go+rX .%{_datadir}/%{name}/misc
cp -vi %{SOURCE1} .%{_docdir}/%{name}/
mkdir -p .%{_sysconfdir}/%{name}/firebird.conf.d
cp -v %{SOURCE2} .%{_sysconfdir}/%{name}/firebird.conf.d/
mkdir -p srv/%{name}
ln -s %{_initddir}/firebird usr/sbin/rcfirebird

%files
%defattr(-,root,root)
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/firebird.conf
%dir %{_sysconfdir}/%{name}/firebird.conf.d
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_libdir}/%{name}/intl
%{_libdir}/%{name}/lib
%{_libdir}/%{name}/plugins/libEngine12.so
%{_datadir}/%{name}/misc
%if 0%{?suse_version} >= 1500 && !0%{?is_opensuse}
%exclude %{_datadir}/%{name}/misc/firebird.xinetd
%endif
%{_docdir}/%{name}/IDPLicense.txt
%{_docdir}/%{name}/IPLicense.txt
%{_docdir}/%{name}/README.SUSE
%dir %{_localstatedir}/lib/%{name}
%dir %{_localstatedir}/lib/%{name}/secdb
%attr(0750,firebird,firebird) %{_localstatedir}/log/%{name}
%dir %attr(0750,firebird,firebird) /srv/firebird

%pre
getent group firebird >/dev/null || groupadd -r firebird || :
getent passwd firebird >/dev/null \
  || %{_sbindir}/useradd -r -g firebird -c 'Firebird SQL server' \
       -d /srv/firebird firebird \
  || :
exit 0

# ----------------------------------------------------------------------------

%package server
Summary:        Server files of Firebird RDBMS
Group:          Productivity/Databases/Servers
Requires:       %{name} = %{version}
Recommends:     %{name}-utils
# replaces these two from Leap 42.x and older
Provides:       firebird-classic = %{version}
Provides:       firebird-superserver = %{version}
Obsoletes:      firebird-classic < 3
Obsoletes:      firebird-superserver < 3

%description server
This package provides files needed to run Firebird RDBMS as a server.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%files server
%defattr(-,root,root)
%{_sbindir}/fb_lock_print
%{_sbindir}/fbguard
%{_sbindir}/firebird
%{_sbindir}/rcfirebird
%config(noreplace) %{_sysconfdir}/%{name}/databases.conf
%config(noreplace) %{_sysconfdir}/%{name}/fbtrace.conf
%config(noreplace) %{_sysconfdir}/%{name}/plugins.conf
%config(noreplace) %{_sysconfdir}/%{name}/firebird.conf.d/50-server.conf
%if 0%{?suse_version} < 1500 || 0%{?is_opensuse}
%if 0%{?suse_version} >= 1500
%dir %{_sysconfdir}/xinetd.d
%endif
%config(noreplace) %{_sysconfdir}/xinetd.d/%{name}
%else
%{_datadir}/%{name}/misc/firebird.xinetd
%endif
%exclude %{_libdir}/%{name}/plugins/libEngine12.so
%{_libdir}/%{name}/plugins
%{_libdir}/%{name}/udf
%{_libdir}/%{name}/utils
%attr(0600,firebird,firebird) %config(noreplace) %{_localstatedir}/lib/%{name}/secdb/security3.fdb
%attr(755,root,root) %{_initddir}/firebird

%post server
%restart_on_update %{_initddir}/firebird

%preun server
%stop_on_removal %{_initddir}/firebird

%postun server
%restart_on_update %{_initddir}/firebird
%insserv_cleanup

# ----------------------------------------------------------------------------

%package utils
Summary:        Firebird RDBMS management utilities
Group:          Productivity/Databases/Servers
Requires:       %{name} = %{version}
# split out of firebird after 42.x
Provides:       %{name}-superserver:%{_bindir}/gbak

%description utils
This package provides for Firebird RDBMS management.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%files utils
%defattr(-,root,root)
%{_bindir}/fbsvcmgr
%{_bindir}/fbtracemgr
%{_bindir}/gbak
%{_bindir}/gfix
%{_bindir}/gpre
%{_bindir}/gsec
%{_bindir}/gsplit
%{_bindir}/gstat-fb
%{_bindir}/isql-fb
%{_bindir}/nbackup
%{_bindir}/qli

# ----------------------------------------------------------------------------

%package -n libfbclient2
Summary:        Firebird RDBMS client library
Group:          System/Libraries
Requires:       %{name} >= 3.0
Requires:       libib_util
Provides:       libfbembed2_5 = %{version}
Obsoletes:      libfbembed2_5 < 3

%description -n libfbclient2
Shared client library for Firebird SQL server. Can be used both to
connect to remote servers and to access local databases in embedded
mode.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%files -n libfbclient2
%defattr(-,root,root)
%{_libdir}/libfbclient.so.*

%post -n libfbclient2 -p /sbin/ldconfig

%postun -n libfbclient2
/sbin/ldconfig

# ----------------------------------------------------------------------------

%package -n libfbclient-devel
Summary:        Development files for Firebird RDBMS client library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libfbclient2 = %{version}
Suggests:       %{name}-examples
Provides:       libfbclient2-devel = %{version}
Obsoletes:      libfbclient2-devel < 3
Provides:       firebird-devel = %{version}
Obsoletes:      firebird-devel < 3
# temporary workaround for LibreOffice build
# once FB3 is in Factory, libreoffice buildrequires will be fixed
# and this can be removed
Provides:       libfbembed-devel

%description -n libfbclient-devel
This package is needed for development of client applications accessing
Firebird RDBMS.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%files -n libfbclient-devel
%defattr(-,root,root)
%exclude %{_includedir}/%{name}/ib_util.h
%{_includedir}/%{name}
%{_libdir}/libfbclient.so
%{_libdir}/pkgconfig/fbclient.pc

# ----------------------------------------------------------------------------

%package -n libib_util
Summary:        Firebird RDBMS UDF support library
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n libib_util
Library providing utility functions for Firebird RDBMS user defined
functions (UDF).

Note: this library may be also loaded via dlopen() by Engine12
plugin as it's also needed for embedded connections (as long as UDFs
are used).

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%files -n libib_util
%defattr(-,root,root)
%{_libdir}/libib_util.so

%post -n libib_util -p /sbin/ldconfig

%postun -n libib_util
/sbin/ldconfig

# ----------------------------------------------------------------------------

%package -n libib_util-devel
Summary:        Development files for Firebird RDBMS
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libfbclient2 = %{version}
Requires:       libib_util = %{version}
Suggests:       %{name}-examples
Provides:       firebird-devel:%{_includedir}/firebird/ib_util.h

%description -n libib_util-devel
This package provides header files for libib_util, support library for
user defined functions (UDF) for Firebird RDBMS.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%files -n libib_util-devel
%defattr(-,root,root)
%{_includedir}/%{name}/ib_util.h

# ----------------------------------------------------------------------------

%package doc
Summary:        Documentation for Firebird RDBMS
Group:          Documentation/Other
Requires:       %{name} = %{version}
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description doc
Documentation for Firebird RDBMS.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%files doc
%defattr(-,root,root)
%{_docdir}/%{name}
%exclude %{_docdir}/%{name}/sample
%exclude %{_docdir}/%{name}/IDPLicense.txt
%exclude %{_docdir}/%{name}/IPLicense.txt
%exclude %{_docdir}/%{name}/README.SUSE

# ----------------------------------------------------------------------------

%package examples
Summary:        Example files for Firebird RDBMS
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description examples
This package provides an example database and API usage examples for
Firebird RDBMS.

Firebird is a relational database offering many ANSI SQL standard
features that runs on Linux, Windows, and a variety of Unix platforms.
Firebird offers excellent concurrency, high performance, and powerful
language support for stored procedures and triggers. It has been used
in production systems, under a variety of names, since 1981.


%files examples
%defattr(-,root,root)
%{_docdir}/%{name}/sample
%dir %{_localstatedir}/lib/%{name}/sample
%attr(0640,firebird,firebird) %{_localstatedir}/lib/%{name}/sample/*

# ----------------------------------------------------------------------------

%changelog
