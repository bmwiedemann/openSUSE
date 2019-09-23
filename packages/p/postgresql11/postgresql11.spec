#
# spec file for package postgresql11
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
%bcond_without  llvm
%else
%bcond_with     systemd_notify
%bcond_with     llvm
%endif

%bcond_without  selinux
%bcond_without  icu
%ifnarch %arm
%bcond_without  check
%else
%bcond_with     check
%endif

%define pgmajor 11
%define pgname postgresql%pgmajor
%define priority %{pgmajor}
%define libpq libpq5
%define libecpg libecpg6
%define libpq_so libpq.so.5
%define libecpg_so libecpg.so.6
%define pgbasedir %_prefix/lib/%pgname
%define pgtestdir %pgbasedir/test
%define pgbindir %pgbasedir/bin
%define pglibdir %pgbasedir/%_lib
%define pgincludedir %_includedir/pgsql
%define pgdatadir %_datadir/%pgname
%define pgdocdir %_docdir/%pgname
%define pgextensiondir %pgdatadir/extension
%define pgcontribdir %pgdatadir/contrib
%define pgmandir %_mandir

%if "@BUILD_FLAVOR@" == "libs"
Name:           %pgname-libs
%define buildmain 0
%define buildlibs 1
%define builddevel 1
%else
Name:           %pgname
%define buildmain 1
%define buildlibs 0
%define builddevel 0
%endif

%if %buildmain
BuildRequires:  docbook_4
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
%if %{with llvm}
BuildRequires:  clang-devel
BuildRequires:  gcc-c++
BuildRequires:  llvm-devel
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
#!BuildIgnore:  %pgname
#!BuildIgnore:  %pgname-server
#!BuildIgnore:  postgresql-implementation
Summary:        Basic Clients and Utilities for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
Version:        11.5
Release:        0
Source0:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2
Source1:        https://ftp.postgresql.org/pub/source/v%{version}/postgresql-%{version}.tar.bz2.sha256
Source2:        baselibs.conf
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
%package -n %pgname-devel
Summary:        PostgreSQL client development header files and libraries
Group:          Development/Libraries/C and C++
Provides:       postgresql-devel-implementation = %version-%release
Requires:       %libecpg >= %version
Requires:       %libpq >= %version
Requires(post): postgresql-noarch >= %pgmajor
Requires(postun): postgresql-noarch >= %pgmajor
# Installation of postgresql??-devel is exclusive
Provides:       postgresql-devel-exclusive = %pgmajor
Conflicts:      postgresql-devel-exclusive < %pgmajor

%description -n %pgname-devel
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the header files and libraries needed to compile
C applications which will directly interact with a PostgreSQL database
management server and the ECPG Embedded C Postgres preprocessor. You
need to install this package if you want to develop applications in C
which will interact with a PostgreSQL server.

For building PostgreSQL server extensions, see the
postgresql%pgmajor-server-devel package.

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

%package server-devel
Summary:        PostgreSQL server development header files and utilities
Group:          Development/Libraries/C and C++
Provides:       postgresql-server-devel = %version-%release
Provides:       postgresql-server-devel-implementation = %version-%release
Requires(post): postgresql-server-noarch >= %pgmajor
Requires(postun): postgresql-server-noarch >= %pgmajor
Requires:       %pgname-devel = %version
Requires:       %pgname-server = %version-%release
# Installation of postgresql??-devel is exclusive
Provides:       postgresql-server-devel-exclusive = %pgmajor
Conflicts:      postgresql-server-devel-exclusive < %pgmajor
%if %{with llvm}
Requires:       clang-devel
%endif

%description server-devel
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the header files and libraries needed to compile
C extensions that link into the PostgreSQL server. For building client
applications, see the postgresql%pgmajor-devel package.

%if %{with llvm}
%package llvmjit
Summary:        Just-in-time compilation support for PostgreSQL
Group:          Productivity/Databases/Servers
Provides:       postgresql-llvmjit-implementation = %version-%release
Requires:       %pgname-server = %version-%release
Requires:       postgresql-llvmjit-noarch >= %pgmajor

%description llvmjit
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, sub-queries, triggers, and user-defined
types and functions.

This package contains support for just-in-time compiling parts of
PostgreSQL queries. Using LLVM it compiles e.g. expressions and tuple
deforming into native code, with the goal of accelerating analytics
queries.
%endif

%package test
Summary:        The test suite for PostgreSQL
Group:          Productivity/Databases/Servers
Provides:       postgresql-test-implementation = %version-%release
Requires:       %pgname-server = %version
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
page is: file:///usr/share/doc/packages/%pgname/html/index.html .
Manual pages for the PostgreSQL SQL statements can be found in the
postgresql package.

%package contrib
Summary:        Contributed Extensions and Additions to PostgreSQL
Group:          Productivity/Databases/Tools
Provides:       postgresql-contrib-implementation = %version-%release
Requires:       postgresql-contrib-noarch >= %pgmajor
Requires(post): %pgname >= %pgmajor
Requires:       %pgname >= %pgmajor
PreReq:         %pgname-server = %version-%release

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
Requires:       %pgname-server = %version-%release
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
Requires:       %pgname-server = %version-%release
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
Requires:       %pgname-server = %version
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
%patch9
touch -r tmp configure
rm tmp
find src/test/ -name '*.orig' -delete
find -name .gitignore -delete

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export PYTHON=python3
PACKAGE_TARNAME=%pgname %configure \
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
%if %{with llvm}
	--with-llvm \
%endif
%else
        --without-readline \
%endif
        --with-openssl \
        --with-ldap \
        --with-gssapi \
        --with-krb5 \
        --with-system-tzdata=/usr/share/zoneinfo
%if !%buildmain
make -C src/interfaces %{?_smp_mflags}
%else
make %{?_smp_mflags} PACKAGE_TARNAME=%pgname

%if %{with check}

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

%install
%if %buildmain
make DESTDIR=%buildroot PACKAGE_TARNAME=%pgname install install-docs
mv %buildroot%pgincludedir/{server,..}
make DESTDIR=%buildroot PACKAGE_TARNAME=%pgname -C src/interfaces uninstall
rm -rf %buildroot%pgincludedir/*
mv %buildroot%pgincludedir{/../server,}

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
%if %builddevel || %buildlibs
make DESTDIR=%buildroot PACKAGE_TARNAME=%pgname -C src/include install
make DESTDIR=%buildroot PACKAGE_TARNAME=%pgname -C src/interfaces install
rm -rf %buildroot%pgincludedir/server
%endif

# The client libraries go to libdir
mkdir -p %buildroot/%_libdir
ls %buildroot%pglibdir/lib* |
   grep -v walreceiver |
   xargs mv -t %buildroot/%_libdir
mv %buildroot%pglibdir/pkgconfig %buildroot%_libdir
find %buildroot%_libdir/pkgconfig -type f -exec sed -i 's, -L%pglibdir,,' '{}' +

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
     grep -v -e %_docdir -e %pgbindir -e %pgincludedir -e %pglibdir/bitcode \
     > contrib.files
rm flag
install -d -m 750 %buildroot/var/lib/pgsql
install -d -m755 %buildroot%pgdocdir
cp doc/KNOWN_BUGS doc/MISSING_FEATURES COPYRIGHT \
   README HISTORY doc/bug.template %buildroot%pgdocdir
cp -a %SOURCE3 %buildroot%pgdocdir/README.SUSE
# Use versioned names for the man pages:
for f in %buildroot%pgmandir/man*/*; do
        mv $f ${f}pg%pgmajor
done
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
        reindexdb pg_basebackup pg_receivewal pg_isready pg_recvlogical pg_verify_checksums
%find_lang plpgsql-%pgmajor main.files
%find_lang pgscripts-%pgmajor main.files

genlists server \
        initdb pg_ctl pg_controldata pg_resetwal pg_waldump  postgres postmaster

genlists server-devel \
        pg_config

genlists contrib \
        oid2name pg_archivecleanup pg_standby pg_test_fsync pg_upgrade \
        pgbench vacuumlo pg_test_timing
for pl in plperl plpython pltcl; do
    %find_lang $pl-%{pgmajor} $pl.lang
done
ln -s /etc/alternatives/postgresql %buildroot/usr/lib/postgresql
touch %buildroot/etc/alternatives/postgresql

# Remove mostly unneeded buildtime requirements for server extensions
sed -i '/^LIBS = /s/= .*/=/' %buildroot/%pglibdir/pgxs/src/Makefile.global
%endif

%if %builddevel
# Make sure we can also link agaist newer versions
pushd %buildroot%_libdir
for f in *.so; do
    ln -sf $f.? $f
done
popd
mkdir -p %buildroot%pgmandir/man1
cp -a doc/src/sgml/man1/ecpg.1 %buildroot%pgmandir/man1/ecpg.1pg%pgmajor
genlists devel ecpg

# Build up the file lists for the libpq and libecpg packages
cat > libpq.files <<EOF
%defattr(-,root,root)
%dir %pgdatadir
%_libdir/libpq.so.5
%_libdir/libpq.so.5.%pgmajor
%pgdatadir/pg_service.conf.sample 
EOF
%find_lang libpq5-%{pgmajor} libpq.files

cat > libecpg.files <<EOF
%defattr(-,root,root)
%_libdir/libecpg.so.6
%_libdir/libecpg.so.6.%pgmajor
%_libdir/libecpg_compat.so.3
%_libdir/libecpg_compat.so.3.%pgmajor
%_libdir/libpgtypes.so.3
%_libdir/libpgtypes.so.3.%pgmajor
EOF
%find_lang ecpglib6-%{pgmajor} libecpg.files

%if !%buildlibs
# Delete the contents of the libs and devel packages, if we don't want to build them
awk -v P=%buildroot '/^(%lang|[^%])/{print P $NF}' libpq.files libecpg.files | xargs rm
%endif
%else # !devel
rm -f %buildroot%pgmandir/man1/ecpg.*
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
  %if %{with systemd}
    %define stop %_stop_on_removal postgresql.service
    eval $(systemctl show postgresql --property=MainPID)
  %else
    %define stop /sbin/init.d postgresql stop
    MainPID=$(pidof -s postgres) || :
  %endif
  if test -n "$MainPID" && test "$MainPID" -ne 0; then
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
  %if %{with systemd}
    %define restart %_restart_on_update postgresql.service
    eval $(systemctl show postgresql --property=MainPID)
  %else
    %define restart /sbin/init.d postgresql restart
    MainPID=$(pidof -s postgres) || :
  %endif
  if test -n "$MainPID" && test "$MainPID" -ne 0 &&
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

%post -n %pgname-server-devel
/usr/share/postgresql/install-alternatives %priority

%postun -n %pgname-server-devel
/usr/share/postgresql/install-alternatives %priority
%endif

%if %builddevel

%post -n %pgname-devel
/usr/share/postgresql/install-alternatives %priority

%postun -n %pgname-devel
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
%if %{with llvm}
%dir %pglibdir/bitcode
%endif
%pgextensiondir/plpgsql*
%attr(750,postgres,postgres) %dir /var/lib/pgsql

%if %{with llvm}
%files llvmjit
%pglibdir/llvm*
%pglibdir/bitcode/*
%endif

%files server-devel -f server-devel.files
%defattr(-,root,root)
%pgincludedir
%pglibdir/pgxs
%_libdir/lib*.a

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

%files -n %libpq -f libpq.files

%files -n %libecpg -f libecpg.files

%endif

%if %builddevel

%files -n %pgname-devel -f devel.files
%defattr(-,root,root)
%dir %pgbasedir
%dir %pgbindir
%_libdir/pkgconfig/*
%_libdir/lib*.so
%pgincludedir

%endif

%changelog
