#
# spec file for package postgresql15
#
# Copyright (c) 2025 SUSE LLC
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


%define pgversion 15.13
%define pgmajor 15
%define buildlibs 0
%define tarversion %{pgversion}
%define oldest_supported_llvm_ver 10
# To be able to use cmake(LLVM) < ...
%define latest_supported_llvm_ver_plus_one 19

### CUT HERE ###
%define pgname postgresql%pgmajor
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

%define requires_file() %( readlink -f '%*' | LC_ALL=C xargs -r rpm -q --qf 'Requires: %%{name} >= %%{epoch}:%%{version}\\n' -f | sed -e 's/ (none):/ /' -e 's/ 0:/ /' | grep -v "is not")

%if "@BUILD_FLAVOR@" == "mini"
%define devel devel-mini
%define mini 1
Name:           %pgname-mini
%else
%define devel devel
%define mini 0
Name:           %pgname
%endif

# Use Python 2 for for PostgreSQL 10 on SLE12.
# Use Python 3 for everything else.
%if 0%{?is_opensuse} || 0%{?sle_version} >= 150000 || %pgmajor > 10
%define python python3
%else
%define python python
%endif

%if %pgmajor >= 17
%bcond_with derived
%else
%bcond_without derived
%endif

%if 0%{?suse_version} >= 1500
%bcond_without liblz4
%endif

%if 0%{?sle_version} >= 150100 || 0%{?suse_version} >= 1550
%bcond_without libzstd
%endif

%if %{without derived}
BuildRequires:  bison
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  flex
BuildRequires:  perl
%endif
%if %mini
%bcond_with  selinux
%if %pgmajor >= 16
%bcond_without icu
%else
%bcond_with  icu
%endif
%else
BuildRequires:  %{python}-devel
BuildRequires:  docbook_4
BuildRequires:  gettext-devel
BuildRequires:  libuuid-devel
BuildRequires:  ncurses-devel
BuildRequires:  pam-devel
BuildRequires:  readline-devel
BuildRequires:  tcl-devel
BuildRequires:  timezone
BuildRequires:  zlib-devel
%if %{with liblz4}
BuildRequires:  pkgconfig(liblz4)
%endif

%if %{with libzstd}
BuildRequires:  pkgconfig(libzstd)
%endif

%bcond_without  selinux
%bcond_without  icu
%if  !%buildlibs
BuildRequires:  %libecpg
BuildRequires:  %libpq
%endif

%if 0%{?suse_version} >= 1500 && %pgmajor >= 11
%ifarch riscv64 loongarch64
%bcond_with     llvm
%else
%bcond_without  llvm
%endif
%else
%bcond_with     llvm
%endif
%endif

%ifnarch %arm
%bcond_without  check
%else
%bcond_with     check
%endif

%if %pgmajor >= 11 || %mini
%bcond_without server_devel
%else
%bcond_with server_devel
%endif

BuildRequires:  fdupes
%if %{with icu}
BuildRequires:  libicu-devel
%endif
%if %{with selinux}
BuildRequires:  libselinux-devel
%endif
%if %{with llvm}
BuildRequires:  gcc-c++
BuildRequires:  (cmake(Clang) >= %{oldest_supported_llvm_ver} with cmake(Clang) < %{latest_supported_llvm_ver_plus_one})
BuildRequires:  (cmake(LLVM)  >= %{oldest_supported_llvm_ver} with cmake(LLVM)  < %{latest_supported_llvm_ver_plus_one})
%endif
BuildRequires:  libxslt-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
#!BuildIgnore:  %pgname
#!BuildIgnore:  %pgname-server
#!BuildIgnore:  %pgname-devel
#!BuildIgnore:  %pgname-server-devel
#!BuildIgnore:  %pgname-llvmjit
#!BuildIgnore:  %pgname-llvmjit-devel
#!BuildIgnore:  %pgname-contrib
#!BuildIgnore:  %pgname-docs
#!BuildIgnore:  %pgname-test
#!BuildIgnore:  %pgname-pltcl
#!BuildIgnore:  %pgname-plperl
#!BuildIgnore:  %pgname-plpython
#!BuildIgnore:  postgresql-implementation
#!BuildIgnore:  postgresql-server-implementation
#!BuildIgnore:  postgresql-server-devel-implementation
#!BuildIgnore:  postgresql-llvmjit-devel-implementation
Summary:        Basic Clients and Utilities for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
Version:        %pgversion
Release:        0
Source0:        https://ftp.postgresql.org/pub/source/v%{tarversion}/postgresql-%{tarversion}.tar.bz2
Source1:        https://ftp.postgresql.org/pub/source/v%{tarversion}/postgresql-%{tarversion}.tar.bz2.sha256
Source2:        baselibs.conf
Source17:       postgresql-rpmlintrc
Patch1:         postgresql-conf.patch
Patch2:         postresql-pg_config_paths.patch
# PL/Perl needs to be linked with rpath (bsc#578053)
Patch4:         postgresql-plperl-keep-rpath.patch
Patch8:         postgresql-testsuite-keep-results-file.patch
Patch9:         postgresql-var-run-socket.patch
%if %{with llvm}
Patch10:        postgresql-llvm-optional.patch
Patch11:        0001-jit-Workaround-potential-datalayout-mismatch-on-s390.patch
%endif
URL:            https://www.postgresql.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       postgresql = %version-%release
Provides:       postgresql-implementation = %version-%release
Requires:       %libpq >= %version
Requires(post): postgresql-noarch >= %pgmajor
Requires(postun): postgresql-noarch >= %pgmajor
# At this point we changed the package layout on SLE and conflict with
# older releases to get a clean cut.
Conflicts:      postgresql-noarch < 12.0.1

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

%package -n %pgname-%devel
Summary:        PostgreSQL client development header files and libraries
Group:          Development/Libraries/C and C++
Provides:       postgresql-devel = %version-%release
Provides:       postgresql-devel-implementation = %version-%release
%if %mini
Requires:       this-is-only-for-build-envs
Provides:       %libecpg = %version-%release
Provides:       %libpq = %version-%release
Provides:       %pgname-devel = %version-%release
Conflicts:      %libecpg
Conflicts:      %libpq
Conflicts:      %pgname-devel
%else
Requires:       %libecpg >= %version
Requires:       %libpq >= %version
Requires:       postgresql-devel-noarch >= %pgmajor
%endif
# Installation of postgresql??-devel is exclusive
Provides:       postgresql-devel-exclusive = %pgmajor
Conflicts:      postgresql-devel-exclusive < %pgmajor

%if %{with server_devel}
%package server-devel
Summary:        PostgreSQL server development header files and utilities
Group:          Development/Libraries/C and C++
%else
Provides:       %pgname-server-devel = %version-%release
%endif
Provides:       postgresql-server-devel = %version-%release
Provides:       postgresql-server-devel-implementation = %version-%release
Requires(post): postgresql-server-devel-noarch >= %pgmajor
Requires(postun): postgresql-server-devel-noarch >= %pgmajor
Requires:       %pgname-devel = %version
Requires:       %pgname-server = %version-%release
# Installation of postgresql??-devel is exclusive
Provides:       postgresql-server-devel-exclusive = %pgmajor
Conflicts:      postgresql-server-devel-exclusive < %pgmajor
Requires:       libxslt-devel
Requires:       openssl-devel
Requires:       pam-devel
Requires:       readline-devel
Requires:       zlib-devel
Requires:       pkgconfig(krb5)
%if %{with selinux}
Requires:       libselinux-devel
%endif
%if %{with llvm}
Recommends:     %pgname-llvmjit-devel = %version-%release
%endif

%if %{with server_devel}
%description server-devel
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the header files and libraries needed to compile
C extensions that link into the PostgreSQL server. For building client
applications, see the postgresql%pgmajor-devel package.
%endif

%description -n %pgname-%devel
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

%package server
Summary:        The Programs Needed to Create and Run a PostgreSQL Server
Group:          Productivity/Databases/Servers
PreReq:         postgresql = %version
Requires:       glibc-locale
Requires:       timezone
%if %{with llvm}
Recommends:     %{name}-llvmjit
%endif
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

%package llvmjit-devel
Summary:        PostgreSQL development files for extensions with LLVM support
Group:          Development/Libraries/C and C++
Provides:       postgresql-llvmjit-devel = %version-%release
Provides:       postgresql-llvmjit-devel-implementation = %version-%release
Requires:       %pgname-server-devel = %version
%if %{with llvm}
Requires:       %pgname-llvmjit = %version
Requires(post): postgresql-llvmjit-devel-noarch >= %pgmajor
Requires(postun): postgresql-llvmjit-devel-noarch >= %pgmajor
%requires_file	%_bindir/llc
%requires_file	%_bindir/clang
%endif

%description llvmjit-devel
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, sub-queries, triggers, and user-defined
types and functions.

This package pulls in the right versions of llvm and clang to compile
PostgreSQL extensions that support just-in-time compilation with LLVM,
if llvm is supported. Otherwise it will just pull the
%{pgname}-server-devel package.

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
BuildArch:      noarch

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
Requires(post): %pgname >= %{version}
Requires:       %pgname >= %{version}
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
Requires:       %python
Requires:       postgresql-plpython-noarch >= %pgmajor

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

%prep
%setup -q -n postgresql-%tarversion
# Keep the timestamp of configure, because patching it would otherwise
# confuse PostgreSQL's build system
touch -r configure tmp
%patch -P 1
%patch -P 2
%patch -P 4
%patch -P 8
%patch -P 9
%if %{with llvm}
%patch -P 10
%patch -P 11
%endif
touch -r tmp configure
rm tmp
find src/test/ -name '*.orig' -delete
find -name .gitignore -delete

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export PYTHON=%python
%ifarch %arm
export USE_ARMV8_CRC32C=0
%endif
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
%if !%mini
        --with-python \
        --with-perl \
        --with-tcl \
        --with-tclconfig=%_libdir \
        --with-pam \
        --with-uuid=e2fs \
        --with-libxml \
        --with-libxslt \
%if %{with liblz4}
        --with-lz4 \
%endif
%if %{with libzstd}
        --with-zstd \
%endif
        --with-systemd \
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
%if %mini
make -C src/interfaces %{?_smp_mflags} PACKAGE_TARNAME=%pgname
%else
make %{?_smp_mflags} PACKAGE_TARNAME=%pgname world

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
VLANG=%pgmajor
%if %mini
make DESTDIR=%buildroot PACKAGE_TARNAME=%pgname -C src/include install
make DESTDIR=%buildroot PACKAGE_TARNAME=%pgname -C src/interfaces install
rm -rf %buildroot%pgincludedir/server
rm -rf %buildroot%pgdatadir
%else
make DESTDIR=%buildroot PACKAGE_TARNAME=%pgname install install-docs
%if 0
mv %buildroot%pgincludedir/{server,..}
make DESTDIR=%buildroot PACKAGE_TARNAME=%pgname -C src/interfaces uninstall
rm -rf %buildroot%pgincludedir/*
mv %buildroot%pgincludedir{/../server,}
%endif

# {{{ the test package
mkdir -p %buildroot%pgtestdir/regress
install -sm 0755 contrib/spi/{refint.so,autoinc.so} %buildroot%pgtestdir/regress
install -sm 0755 src/test/regress/{pg_regress,regress.so} %buildroot%pgtestdir/regress
for i in  src/test/regress/{data,expected,input,output,sql}; do
	test -d $i && cp -r $i %buildroot%pgtestdir/regress/
done
install -m 0644 src/test/regress/*_schedule %buildroot%pgtestdir/regress
# }}}
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

%if !%mini
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
install -d -m 755 %buildroot%pgdocdir
cp doc/KNOWN_BUGS doc/MISSING_FEATURES COPYRIGHT \
   README* HISTORY  %buildroot%pgdocdir
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

	# Package only binaries that exist in this version
        test -e %buildroot$PGBIN || continue

        touch %buildroot$ALTBIN
        ln -s $ALTBIN %buildroot$BIN

        echo "$PGBIN" >> $PKG.files
        echo "$BIN" >> $PKG.files
        echo "%ghost $ALTBIN" >> $PKG.files
        test -e %buildroot$MAN &&
            echo "%doc $MAN" >> $PKG.files
        %find_lang $f-$VLANG $PKG.files ||:
    done
}
%if !%mini
genlists main \
	createdb \
	clusterdb \
	createuser \
	dropdb \
	dropuser \
	pg_dump \
	pg_dumpall \
	pg_restore \
	pg_rewind \
	psql \
	vacuumdb \
	reindexdb \
	pg_basebackup \
	pg_isready \
	pg_recvlogical \
	createlang \
	droplang \
	pg_receivexlog \
	pg_receivewal \
	pg_verify_checksums \
	pg_checksums \
	pg_combinebackup \
	pg_verifybackup

%find_lang plpgsql-$VLANG main.files
%find_lang pgscripts-$VLANG main.files

genlists server \
	initdb \
	pg_ctl \
	pg_controldata \
	pg_resetwal \
	pg_createsubscriber \
	pg_walsummary \
	pg_waldump \
	pg_resetxlog \
%if %pgmajor >= 15
	pg_upgrade \
%endif
	postgres \
	postmaster

genlists contrib \
	pg_xlogdump \
	oid2name \
	pg_archivecleanup \
	pg_amcheck \
	pg_standby \
	pg_test_fsync \
%if %pgmajor < 15
	pg_upgrade \
%endif
        pgbench \
	vacuumlo \
	pg_test_timing
for pl in plperl plpython pltcl; do
    %find_lang $pl-$VLANG $pl.lang
done
ln -s /etc/alternatives/postgresql %buildroot/usr/lib/postgresql
touch %buildroot/etc/alternatives/postgresql

# Remove mostly unneeded buildtime requirements for server extensions
sed -i '/^LIBS = /s/= .*/=/' %buildroot/%pglibdir/pgxs/src/Makefile.global
%endif

# Make sure we can also link agaist newer versions
pushd %buildroot%_libdir
for f in *.so; do
    ln -sf $f.? $f
done
%if 0
for long in *.so.*.*; do
    short=${long%%.*}
    so=${short%%.*}
    ln -sf $long $short
    ln -sf $short $so
done
%endif
popd

%find_lang ecpg-$VLANG devel.files
# The devel subpackage is exclusive across versions
# and not handled by update-alternatives.
mv %buildroot%pgbindir/ecpg %buildroot%_bindir/ecpg

%if !%mini
%find_lang pg_config-$VLANG server-devel.files
ln -s %pgbindir/pg_config %buildroot%_bindir/pg_config
%endif

%if %{without server_devel}
cat server-devel.files >> devel.files
%endif

# Build up the file lists for the libpq and libecpg packages
cat > libpq.files <<EOF
%defattr(-,root,root)
%if !%mini
%dir %pgdatadir
%pgdatadir/pg_service.conf.sample
%endif
EOF
find %buildroot -name 'libpq*.so.*' -printf '/%%P\n' >> libpq.files
%find_lang libpq5-$VLANG libpq.files

cat > libecpg.files <<EOF
%defattr(-,root,root)
EOF
find %buildroot \( -name 'libecpg*.so.*' -o -name 'libpgtypes.so.*' \) -printf '/%%P\n' >> libecpg.files
%find_lang ecpglib6-$VLANG libecpg.files

%if !%buildlibs
# Delete the contents of the library packages, if we don't want to build them
awk -v P=%buildroot '/^(%lang|[^%])/{print P $NF}' libpq.files libecpg.files | xargs rm
%endif

%fdupes %buildroot

%post -n %pgname-%devel
/sbin/ldconfig

%postun -n %pgname-%devel
/sbin/ldconfig

%if %{with server_devel}
%post server-devel
/usr/share/postgresql/install-alternatives %pgmajor

%postun server-devel
/usr/share/postgresql/install-alternatives %pgmajor
%endif

%if !%mini

%postun
/usr/share/postgresql/install-alternatives %pgmajor

%post
/usr/share/postgresql/install-alternatives %pgmajor

%post server
/usr/share/postgresql/install-alternatives %pgmajor

%preun server
# Stop only when we are uninstalling the currently running version
test -x /usr/bin/systemctl &&
  MAINPID=$(/usr/bin/systemctl show postgresql.service --property=MainPID --value) ||:
if test -n "$MAINPID" && test "$MAINPID" -ne 0; then
  BIN=$(readlink -n /proc/$MAINPID/exe)
  DIR=$(dirname ${BIN% *})
  if test "$DIR" = "%pgbindir" -o "$DIR" = "%_bindir"; then
      %service_del_preun postgresql.service
  fi
fi

%postun server
/usr/share/postgresql/install-alternatives %pgmajor
# Restart only when we are updating the currently running version
test -x /usr/bin/systemctl &&
  MAINPID=$(/usr/bin/systemctl show postgresql.service --property=MainPID --value) ||:
if test -n "$MAINPID" && test "$MAINPID" -ne 0; then
  BIN=$(readlink -n /proc/$MAINPID/exe)
  DIR=$(dirname ${BIN% *})
  if test "$DIR" = "%pgbindir" -o "$DIR" = "%_bindir"; then
      %service_del_postun postgresql.service
  fi
fi

%post contrib
/usr/share/postgresql/install-alternatives %pgmajor

%postun contrib
/usr/share/postgresql/install-alternatives %pgmajor

%if %buildlibs
%post -n %libpq -p /sbin/ldconfig

%postun -n %libpq -p /sbin/ldconfig

%post -n %libecpg -p /sbin/ldconfig

%postun -n %libecpg -p /sbin/ldconfig
%endif

%files -f main.files
%defattr(-,root,root)
%dir %pgbindir
%doc %pgmandir/man7/*
%docdir %pgdocdir
%dir %pgdocdir
%pgdocdir/[[:upper:]]*
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
%pgdatadir/timezone*
%pgdatadir/*.*
%if %buildlibs
%exclude %pgdatadir/pg_service.conf.sample
%endif
%pglibdir/*_and_*.so
%pglibdir/euc2004_sjis2004.so
%pglibdir/libpqwalreceiver.so
%pgextensiondir/plpgsql*
%attr(750,postgres,postgres) %dir /var/lib/pgsql

%if %{with llvm}
%dir %pglibdir/bitcode

%files llvmjit
%defattr(-,root,root)
%pglibdir/llvm*
%pglibdir/bitcode/*
%endif

%files llvmjit-devel
%defattr(-,root,root)

%files pltcl -f pltcl.lang
%defattr(-,root,root)
%pgextensiondir/pltcl*
%pglibdir/pltcl.so

%files plperl -f plperl.lang
%defattr(-,root,root)
%pgextensiondir/plperl*
%pglibdir/plperl.so

%files plpython -f plpython.lang
%defattr(-,root,root)
%pgextensiondir/plpython*
%pglibdir/plpython*.so

%endif

%if %buildlibs && !%mini
%files -n %libpq -f libpq.files

%files -n %libecpg -f libecpg.files
%endif

%if %buildlibs && %mini
%files -n %pgname-%devel -f devel.files -f libpq.files -f libecpg.files
%defattr(-,root,root)
%else

%files -n %pgname-%devel -f devel.files
%defattr(-,root,root)
%endif

%dir %pgbasedir
%dir %pgbindir
%_bindir/ecpg
%_libdir/pkgconfig/*
%_libdir/lib*.so
%pgincludedir

%if %{with server_devel}
%exclude %pgincludedir/server
%endif

%if !%mini
%doc %pgmandir/man1/ecpg.1*
%if %{with server_devel}
%files server-devel -f server-devel.files
%endif
%defattr(-,root,root)
%ghost %_bindir/pg_config
%pgbindir/pg_config
%pgincludedir/server
%pglibdir/pgxs
%_libdir/lib*.a
%doc %pgmandir/man1/pg_config.1*
%endif

%changelog
