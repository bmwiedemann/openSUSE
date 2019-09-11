#
# spec file for package postgresql10
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} >= 1300
%bcond_without  systemd
%else
%bcond_with     systemd
%endif
%if 0%{?suse_version} >= 1500
%bcond_without  systemd_notify
%else
%bcond_with     systemd_notify
%endif
%bcond_without  selinux
%bcond_without  icu

%define pgmajor 10
%define priority %{pgmajor}
%define libpq libpq5
%define libecpg libecpg6
%define libpq_so libpq.so.5
%define libecpg_so libecpg.so.6
%if "@BUILD_FLAVOR@" == "libs"
%define buildmain 0
%define buildlibs 0
%define builddevel 1
%else
%define buildmain 1
%define buildlibs 0
%define builddevel 0
%endif
%define pgbasedir %_prefix/lib/%name
%define pgtestdir %pgbasedir/test
%define pgbindir %pgbasedir/bin
%define pglibdir %pgbasedir/%_lib
%define pgincludedir %_includedir/pgsql
%define pgdatadir %_datadir/%name
%define pgdocdir %_docdir/%name
%define pgextensiondir %pgdatadir/extension
%define pgcontribdir %pgdatadir/contrib
%define pgmandir %_mandir

Name:           postgresql%pgmajor

%if %buildmain
BuildRequires:  gettext-devel
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  tcl-devel
BuildRequires:  timezone
BuildRequires:  zlib-devel
# 
%endif

BuildRequires:  fdupes
%if %{with icu}
BuildRequires:  libicu-devel
%endif
%if %{with selinux}
BuildRequires:  libselinux-devel
%endif
BuildRequires:  libxslt-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
%if 0%{?suse_version} == 1110
BuildRequires:  krb5-devel
%else
BuildRequires:  pkgconfig(krb5)
%endif
%if %{with systemd_notify}
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%endif
#!BuildIgnore:  %name
#!BuildIgnore:  %name-server
#!BuildIgnore:  postgresql-implementation
Summary:        Basic Clients and Utilities for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
Version:        10.9
Release:        0
Source0:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source1:        baselibs.conf
Source3:        postgresql-README.SUSE
Source17:       postgresql-rpmlintrc
Patch1:         postgresql-conf.patch
Patch2:         postgresql-regress.patch
# PL/Perl needs to be linked with rpath (bsc#578053)
Patch4:         postgresql-plperl-keep-rpath.patch
Patch6:         postgresql-testsuite-int8.sql.patch
Patch8:         postgresql-testsuite-keep-results-file.patch
Patch9:         postgresql-var-run-socket.patch
Url:            https://www.postgresql.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       postgresql = %version-%release
Provides:       postgresql-implementation = %version-%release
Requires:       %libpq >= %version
Requires(post): postgresql-noarch >= %pgmajor
Requires(postun): postgresql-noarch >= %pgmajor

%description
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the basic utility and client programs necessary
to maintain and work with local or remote PostgreSQL databases as well
as manual pages for the SQL commands that PostgreSQL supports. Full
HTML documentation for PostgreSQL can be found in the postgresql-docs
package.

%package -n %libpq
Summary:        Shared Libraries Required for PostgreSQL Clients
Group:          Productivity/Databases/Clients
Provides:       postgresql-libs:%_libdir/libpq.so.5
Obsoletes:      postgresql-libs < %version
# bug437293
%if "%_lib" == "lib64"
Conflicts:      %libpq-32bit < %version
%endif
%ifarch ia64
Conflicts:      %libpq-x86 < %version
%endif
%ifarch ppc64
Obsoletes:      postgresql-libs-64bit
%endif

%description -n %libpq

PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, user-defined types
and functions.

This package provides the client library that most PostgreSQL client
program or language bindings are using.

%package -n %libecpg

Summary:        Shared Libraries Required for PostgreSQL Clients
Group:          Productivity/Databases/Clients
Provides:       postgresql-libs:%_libdir/libecpg.so.6

%description -n %libecpg
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, user-defined types
and functions.

This package provides the runtime library of the embedded SQL C
preprocessor for PostgreSQL.

%if %builddevel
%package devel
Summary:        PostgreSQL development header files and libraries
Group:          Development/Libraries/C and C++
Provides:       postgresql%pgmajor-server-devel = %version-%release
Provides:       postgresql-devel-implementation = %version-%release
Provides:       postgresql-server-devel = %version-%release
Provides:       postgresql-server-devel-implementation = %version-%release
Requires:       %libecpg >= %version
Requires:       %libpq >= %version
Requires(post): postgresql-noarch >= %pgmajor
Requires(postun): postgresql-noarch >= %pgmajor
# Installation of postgresql??-devel is exclusive
Provides:       postgresql-devel-exclusive = %pgmajor
Conflicts:      postgresql-devel-exclusive < %pgmajor
Provides:       postgresql-server-devel-exclusive = %pgmajor
Conflicts:      postgresql-server-devel-exclusive < %pgmajor

%description devel
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the header files and libraries needed to compile
C applications which will directly interact with a PostgreSQL database
management server and the ECPG Embedded C Postgres preprocessor. You
need to install this package if you want to develop applications in C
which will interact with a PostgreSQL server.

%endif

%if %buildmain

%package server
Summary:        The Programs Needed to Create and Run a PostgreSQL Server
Group:          Productivity/Databases/Servers
PreReq:         /sbin/chkconfig
PreReq:         postgresql = %version
Requires:       glibc-locale
Requires:       timezone
Provides:       postgresql-server-implementation = %version-%release
Requires:       %libpq >= %version
Requires(pre):  postgresql-server-noarch >= %pgmajor
Requires(preun): postgresql-server-noarch >= %pgmajor
Requires(postun): postgresql-server-noarch >= %pgmajor
Requires(post): postgresql-noarch >= %pgmajor
Requires(postun): postgresql-noarch >= %pgmajor

%description server
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, sub-queries, triggers, and user-defined
types and functions.

This package includes the programs needed to create and run a
PostgreSQL server, which will in turn allow you to create and maintain
PostgreSQL databases.

%package test
Summary:        The test suite for PostgreSQL
Group:          Productivity/Databases/Servers
Provides:       postgresql-test-implementation = %version-%release
Requires:       %name-server = %version
Requires:       postgresql-test-noarch >= %pgmajor

%description test
This package contains the sources and pre-built binaries of various
tests for the PostgreSQL database management system, including
regression tests and benchmarks.

%package docs
Summary:        HTML Documentation for PostgreSQL
Group:          Productivity/Databases/Tools
Provides:       postgresql-docs-implementation = %version-%release
Requires:       postgresql-docs-noarch >= %pgmajor
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description docs
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the HTML documentation for PostgreSQL. The start
page is: file:///usr/share/doc/packages/%name/html/index.html .
Manual pages for the PostgreSQL SQL statements can be found in the
postgresql package.

%package contrib
Summary:        Contributed Extensions and Additions to PostgreSQL
Group:          Productivity/Databases/Tools
Provides:       postgresql-contrib-implementation = %version-%release
Requires:       postgresql-contrib-noarch >= %pgmajor
Requires(post): postgresql >= %pgmajor
PreReq:         %name-server = %version-%release

%description contrib
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

The postgresql-contrib package includes extensions and additions that
are distributed along with the PostgreSQL sources, but are not (yet)
officially part of the PostgreSQL core.

Documentation for the modules contained in this package can be found in
/usr/share/doc/packages/postgresql/contrib.

%package plperl
Summary:        The PL/Tcl, PL/Perl, and  PL/Python procedural languages for PostgreSQL
Group:          Productivity/Databases/Servers
Provides:       postgresql-plperl-implementation = %version-%release
Requires:       %name-server = %version-%release
Requires:       perl = %perl_version
Requires:       postgresql-plperl-noarch >= %pgmajor

%description plperl
This package contains the the PL/Tcl, PL/Perl, and PL/Python procedural
languages for the back-end.  With these modules one can use Perl,
Python, and Tcl to write stored procedures, functions and triggers.

PostgreSQL also offers the builtin procedural language PL/SQL.

%package plpython
Summary:        The PL/Python Procedural Languages for PostgreSQL
Group:          Productivity/Databases/Servers
Provides:       postgresql-plpython-implementation = %version-%release
Requires:       %name-server = %version-%release
Requires:       postgresql-plpython-noarch >= %pgmajor
Requires:       python

%description plpython
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the PL/Python procedural language for PostgreSQL.
With this module one can use Python to write stored procedures,
functions, and triggers.

PostgreSQL also offers the built-in procedural language PL/SQL which is
included in the postgresql-server package.

%package pltcl
Summary:        PL/Tcl Procedural Language for PostgreSQL
Group:          Productivity/Databases/Tools
Provides:       postgresql-pltcl-implementation = %version-%release
Requires:       %name-server = %version
Requires:       postgresql-pltcl-noarch >= %pgmajor
Requires:       tcl

%description pltcl
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the PL/Tcl procedural language for PostgreSQL. 
With thie module one can use Tcl to write stored procedures, functions,
and triggers.

PostgreSQL also offers the built-in procedural language PL/SQL which is
included in the postgresql-server package.

%endif

%prep
%setup -q -n postgresql-%version
# Keep the timestamp of configure, because patching it would otherwise
# confuse PostgreSQL's build system
touch -r configure tmp
%patch1
%patch2
%patch4
%patch6 -p1
%patch8 -p1
%patch9 -p1
touch -r tmp configure
rm tmp
find src/test/ -name '*.orig' -delete
find -name .gitignore -delete

%build
export PYTHON=python3
PACKAGE_TARNAME=%name %configure \
        --bindir=%pgbindir \
        --libdir=%pglibdir \
        --includedir=%pgincludedir \
        --datadir=%pgdatadir \
        --docdir=%pgdocdir \
        --mandir=%pgmandir \
        --disable-rpath \
        --enable-nls \
        --enable-thread-safety \
        --enable-integer-datetimes \
%if %buildmain
        --with-python \
        --with-perl \
        --with-tcl \
        --with-tclconfig=%_libdir \
        --with-pam \
        --with-uuid=e2fs \
        --with-libxml \
        --with-libxslt \
%if %{with systemd_notify}
        --with-systemd \
%endif
%if %{with selinux}
        --with-selinux \
%endif
%if %{with icu}
        --with-icu \
%endif
%else
        --without-readline \
%endif
        --with-openssl \
        --with-ldap \
%if 0%{?suse_version} > 910
        --with-gssapi \
        --with-krb5 \
%endif
        --with-system-tzdata=/usr/share/zoneinfo
%if !%buildmain
make -C src/backend %{?_smp_mflags} libpq-recursive
%if %builddevel
make -C src/port %{?_smp_mflags} libpgport.a
make -C src/common %{?_smp_mflags} libpgcommon.a
make -C src/interfaces/ecpg/preproc %{?_smp_mflags}
make -C src/bin/pg_config %{?_smp_mflags} pg_config
%endif
%if %buildlibs || %builddevel
make -C src/interfaces %{?_smp_mflags}
%endif
%else
# {{{ build the test package
#make -C src/test/regress all
# }}}
make %{?_smp_mflags} PACKAGE_TARNAME=%name world
%ifnarch %arm
%if 0%{?suse_version} > 910

%check
#
# Run the regression tests.
#
make check || {
  for f in src/test/regress/log/* {,src/test/regress/}regression.diffs; do
    if test -f $f; then
	cat $f
    fi
  done
  exit 1
}
%endif
%endif
%endif

%install
%if %buildmain
make DESTDIR=%buildroot PACKAGE_TARNAME=%name install install-docs
# {{{ the test package
mkdir -p %buildroot%pgtestdir/regress
install -sm 0755 contrib/spi/{refint.so,autoinc.so} %buildroot%pgtestdir/regress
install -sm 0755 src/test/regress/{pg_regress,regress.so} %buildroot%pgtestdir/regress
for i in  src/test/regress/{data,expected,input,output,sql}; do
	cp -r $i %buildroot%pgtestdir/regress/
done
install -m 0644 src/test/regress/{serial,parallel}_schedule %buildroot%pgtestdir/regress
# }}}
%endif
%if %builddevel && !%buildmain
SUBINSTALL=install
install -d %buildroot%pgmandir/man1
install -m644 doc/src/sgml/man1/{ecpg,pg_config}.1 %buildroot%pgmandir/man1
%else
SUBINSTALL=uninstall
rm -f %buildroot%pgmandir/*/ecpg*
rm -f %buildroot%pgmandir/*/pg_config*
%endif
# Install them for postgresql-libs and uninstall them for postgresql
make -C src DESTDIR=%buildroot $SUBINSTALL-local
make -C src/pl/plpgsql/src DESTDIR=%buildroot $SUBINSTALL-headers
for dir in \
        config \
        src/bin/pg_config \
        src/interfaces \
        src/include \
        src/makefiles \
        src/port \
        src/common \
        src/test/regress
do
        make -C $dir DESTDIR=%buildroot $SUBINSTALL
done

%if %builddevel
# The client libraries go to libdir
mkdir -p %buildroot/%_libdir
ls %buildroot%pglibdir/lib* |
   grep -v walreceiver |
   xargs mv -t %buildroot/%_libdir
mv %buildroot%pglibdir/pkgconfig %buildroot%_libdir
sed -i 's, -L%pglibdir,,' %buildroot%_libdir/pkgconfig/*.pc
%endif
# Don't ship static libraries,
# libpgport.a and libpgcommon.a are needed, though.
rm -f $(ls %buildroot/%_libdir/*.a %buildroot%pglibdir/*.a | grep -F -v -e libpgport.a -e libpgcommon.a)
%if %buildmain
#
# Install and collect the contrib stuff
#
touch flag; sleep 1 # otherwise we have installed files that are not newer than flag
make DESTDIR=%buildroot -C contrib install
find %buildroot -type f -cnewer flag -printf "/%%P\n" |
     grep -v -e %_docdir -e %pgbindir > contrib.files
rm flag
install -d -m 750 %buildroot/var/lib/pgsql
install -d -m755 %buildroot%pgdocdir
cp doc/KNOWN_BUGS doc/MISSING_FEATURES COPYRIGHT \
   README HISTORY doc/bug.template %buildroot%pgdocdir
cp -a %SOURCE3 %buildroot%pgdocdir/README.SUSE
%endif
# Use versioned names for the man pages:
for f in %buildroot%pgmandir/man*/*; do
        mv $f ${f}pg%pgmajor
done

%if %builddevel
# Make sure we can also link agaist newer versions
pushd %buildroot%_libdir
for f in *.so; do
    ln -sf $f.? $f
done
popd
# Remove mostly unneeded buildtime requirements for server extensions
sed -i '/^LIBS = /s/= .*/=/' %buildroot/%pglibdir/pgxs/src/Makefile.global
%if %buildlibs
%find_lang libpq5-%{pgmajor} libpq.lang
%find_lang ecpglib6-%{pgmajor} libecpg.lang
%else
rm %buildroot/usr/share/locale/*/*/libpq5*
rm %buildroot/usr/share/locale/*/*/ecpglib6*
rm %buildroot%_libdir/lib*.so.*
rm %buildroot%pgdatadir/pg_service.conf.sample
%endif
%endif
mkdir -p %buildroot{%_bindir,%_mandir/man1}
mkdir -p %buildroot/etc/alternatives
genlists ()
{
    # usage: genlists packagename basenames
    PKG=$1
    shift
    for f in $@
    do
        BIN=%_bindir/$f
        ALTBIN=/etc/alternatives/$f
        PGBIN=%pgbindir/$f
        MAN=%pgmandir/man1/$f.1*

        touch %buildroot$ALTBIN
        ln -s $ALTBIN %buildroot$BIN

        echo "$PGBIN" >> $PKG.files
        echo "$BIN" >> $PKG.files
        echo "%ghost $ALTBIN" >> $PKG.files
        test -e %buildroot$MAN &&
            echo "%doc $MAN" >> $PKG.files
        %find_lang $f-%pgmajor $PKG.files ||:
    done
}
%if %buildmain
genlists main \
        createdb clusterdb createuser dropdb \
        dropuser pg_dump pg_dumpall pg_restore pg_rewind psql vacuumdb \
        reindexdb pg_basebackup pg_receivewal pg_isready pg_recvlogical
%find_lang plpgsql-%pgmajor main.files
%find_lang pgscripts-%pgmajor main.files

genlists server \
        initdb pg_ctl pg_controldata pg_resetwal pg_waldump  postgres postmaster

genlists contrib \
        oid2name pg_archivecleanup pg_standby pg_test_fsync pg_upgrade \
        pgbench vacuumlo pg_test_timing
for pl in plperl plpython pltcl; do
    %find_lang $pl-%{pgmajor} $pl.lang
done

%endif
ln -s /etc/alternatives/postgresql %buildroot/usr/lib/postgresql
touch %buildroot/etc/alternatives/postgresql
%if %builddevel
genlists devel \
        pg_config ecpg
%endif
%fdupes %buildroot

%if %buildmain

%postun
/usr/share/postgresql/install-alternatives %priority

%post
/usr/share/postgresql/install-alternatives %priority

%post server
/usr/share/postgresql/install-alternatives %priority

%preun server
# Stop only when we are uninstalling the currently running version
test -n "$FIRST_ARG" || FIRST_ARG="$1"
if [ "$FIRST_ARG" -eq 0 -a -x /usr/bin/systemctl ]; then
  MainPID=0
  %if %{with systemd}
    %define stop %_stop_on_removal postgresql.service
    eval $(systemctl show postgresql --property=MainPID)
  %else
    %define stop /sbin/init.d postgresql stop
    MainPID=$(pidof -s postgres) || :
  %endif
  if test "$MainPID" -ne 0; then
    BIN=$(readlink -n /proc/$MainPID/exe)
    DIR=$(dirname ${BIN% *})
    if test "$DIR" = "%pgbindir" -o "$DIR" = "%_bindir"; then
        %stop
    fi
  fi
fi

%postun server
/usr/share/postgresql/install-alternatives %priority
# Restart only when we are updating the currently running version
# or from the old packaging scheme
test -n "$FIRST_ARG" || FIRST_ARG="$1"
if [ "$FIRST_ARG" -ge 1 ]; then
  MainPID=0
  %if %{with systemd}
    %define restart %_restart_on_update postgresql.service
    eval $(systemctl show postgresql --property=MainPID)
  %else
    %define restart /sbin/init.d postgresql restart
    MainPID=$(pidof -s postgres) || :
  %endif
  if test "$MainPID" -ne 0 &&
    readlink -n /proc/$MainPID/exe | grep -Fq " (deleted)"
  then
    BIN=$(readlink -n /proc/$MainPID/exe)
    DIR=$(dirname ${BIN% *})
    if test "$DIR" = "%pgbindir" -o "$DIR" = "%_bindir"; then
        %restart
    fi
  fi
fi

%post contrib
/usr/share/postgresql/install-alternatives %priority

%postun contrib
/usr/share/postgresql/install-alternatives %priority

%endif

%if %builddevel

%post devel
/usr/share/postgresql/install-alternatives %priority

%postun devel
/usr/share/postgresql/install-alternatives %priority
%endif

%if %buildlibs
%post -n %libpq -p /sbin/ldconfig

%postun -n %libpq -p /sbin/ldconfig

%post -n %libecpg -p /sbin/ldconfig

%postun -n %libecpg -p /sbin/ldconfig
%endif

%if %buildmain

%files -f main.files
%defattr(-,root,root)
%dir %pgbindir
%doc %pgmandir/man7/*
%docdir %pgdocdir
%dir %pgdocdir
%pgdocdir/[[:upper:]]*
%pgdocdir/bug.template
%dir %pglibdir
/usr/lib/postgresql
%ghost /etc/alternatives/postgresql

%files test
%defattr(-,root,root,-)
%pgtestdir

%files docs
%defattr(-,root,root)
%doc %pgmandir/man3/*
%docdir %pgdocdir
%dir %pgdocdir
%pgdocdir/html

%files contrib -f contrib.files
%defattr(-,root,root)
%docdir %pgdocdir
%dir %pgdocdir
%pgdocdir/extension
%dir %pgdatadir
%dir %pgcontribdir
/usr/lib/postgresql

%files server -f server.files
%defattr(-,root,root)
%dir %pgbasedir
%dir %pgextensiondir
%dir %pglibdir
%pglibdir/pgoutput.so
%pglibdir/plpgsql.so
%pglibdir/dict_snowball.so
%pgdatadir/tsearch_data
%exclude %pgdatadir/tsearch_data/*.rules
%dir %pgdatadir
/usr/lib/postgresql
%pgdatadir/timezone*
%pgdatadir/*.*
%if %buildlibs
%exclude %pgdatadir/pg_service.conf.sample
%endif
#exclude %pgdatadir/*.pltcl
%pglibdir/*_and_*.so
%pglibdir/euc2004_sjis2004.so
%pglibdir/libpqwalreceiver.so
%pgextensiondir/plpgsql*
%attr(750,postgres,postgres) %dir /var/lib/pgsql

%files pltcl -f pltcl.lang
%defattr(-,root,root)
%pgextensiondir/pltcl*
%pglibdir/pltcl.so
#pgdatadir/*.pltcl
#pgbindir/pltcl*

%files plperl -f plperl.lang
%defattr(-,root,root)
%pgextensiondir/plperl*
%pglibdir/plperl.so

%files plpython -f plpython.lang
%defattr(-,root,root)
%pgextensiondir/plpython*
%pglibdir/plpython*.so

%endif
%if %buildlibs

%files -n %libpq -f libpq.lang
%defattr(-,root,root)
%dir %pgbasedir
%dir %pgdatadir
%_libdir/libpq.so.*
%pgdatadir/pg_service.conf.sample

%files -n %libecpg -f libecpg.lang
%defattr(-,root,root)
%_libdir/libecpg*.so.*
%_libdir/libpgtypes.so.*

%endif

%if %builddevel

%files devel -f devel.files
%defattr(-,root,root)
%dir %pgbasedir
%dir %pgbindir
%dir %pglibdir
%_libdir/pkgconfig/*
%_libdir/lib*.a
%_libdir/lib*.so
%pglibdir/pgxs
%pgincludedir
/usr/lib/postgresql
%ghost /etc/alternatives/postgresql

%endif

%changelog
