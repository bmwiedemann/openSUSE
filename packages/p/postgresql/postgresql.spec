#
# spec file for package postgresql
#
# Copyright (c) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define pgmajor 15
%define defaultpackage postgresql%pgmajor

%if ! %{defined _rpmmacrodir}
%define _rpmmacrodir %{_rpmconfigdir}/macros.d
%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version} >= 1300
%bcond_without  systemd
%else
%bcond_with     systemd
%endif

# We do not need the pgmajor comparison here as it is irrelevant which version this package has
%if 0%{?suse_version} >= 1500
%bcond_without  llvm
%else
%bcond_with     llvm
%endif

# On SLE-15 up to SP3 sysusers does not support shells
# other than /bin/nologin
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%bcond_without sysusers
%else
%bcond_with sysusers
%endif

Name:           postgresql
Summary:        Basic Clients and Utilities for PostgreSQL
License:        PostgreSQL
Group:          Productivity/Databases/Tools
Version:        %pgmajor
Release:        0
Url:            https://www.postgresql.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       postgresql-noarch = %version-%release
Requires:       postgresql-implementation
Requires:       update-alternatives
Recommends:     %defaultpackage
# In June 2020 we changed the package layout for PostgreSQL and
# conflict with older releases to get a clean cut-over.
Conflicts:      postgresql < 9
Conflicts:      postgresql90
Conflicts:      postgresql91
Conflicts:      postgresql92
Conflicts:      postgresql93
Conflicts:      postgresql94 < 9.4.26
Conflicts:      postgresql95 < 9.5.22
Conflicts:      postgresql96 < 9.6.18
Conflicts:      postgresql10 < 10.13
Conflicts:      postgresql11 < 11.8
Conflicts:      postgresql12 < 12.3
BuildArch:      noarch
Source0:        postgresql-init
Source1:        postgresql-sysconfig
Source2:        postgresql-firewall
Source3:        postgresql-tmpfiles.conf
Source4:        postgresql.service
Source5:        postgresql-bashprofile
Source6:        postgresql-script
Source7:        postgresql-install-alternatives
Source8:        postgresql-extensions-macros
Source9:        postgresql.sysusers

%if 0%{?suse_version} > 1100
    %define fwdir /etc/sysconfig/SuSEfirewall2.d/services
    %define fwname postgresql
%else
    %define fwdir /etc/sysconfig/scripts
    %define fwname SuSEfirewall2-postgresql
%endif

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

%package server
Summary:        The Programs Needed to Create and Run a PostgreSQL Server
Group:          Productivity/Databases/Servers
Provides:       postgresql-server-noarch = %version-%release
Requires:       postgresql-server-implementation
Requires:       postgresql = %version-%release
Recommends:     %defaultpackage-server
%if 0%{?suse_version} >= 1315
%if %{with sysusers}
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  shadow
%endif
%else
Requires(pre):  pwdutils
%endif
Provides:       postgresql-init = %version.0-%release
Obsoletes:      postgresql-init < %version.0-%release
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%else
Requires(postun): %insserv_prereq
%endif


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
Provides:       postgresql-server-devel-noarch = %version-%release
Requires:       postgresql-server-devel-implementation
Recommends:     %defaultpackage-server-devel

%description server-devel
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the header files and libraries needed to compile
C extensions that link into the PostgreSQL server. For building client
applications, see the %defaultpackage-devel package.

%package llvmjit
Summary:        Just-in-time compilation support for PostgreSQL
Group:          Productivity/Databases/Servers
Provides:       postgresql-llvmjit-noarch = %version-%release
Requires:       postgresql-llvmjit-implementation
Recommends:     %defaultpackage-llvmjit

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
Summary:        Helper package to pull all dependencies to build with llvm support
Group:          Productivity/Databases/Servers
Provides:       postgresql-llvmjit-devel-noarch = %version-%release
Requires:       postgresql-server-devel-noarch
Requires:       postgresql-llvmjit-devel-implementation

%description llvmjit-devel
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, sub-queries, triggers, and user-defined
types and functions.

This package will pull all the dependencies to build extensions with llvm
support if the base distro has llvm enabled.

Otherwise it will just pull the postgresqlXY-server-devel package

%package test
Summary:        The test suite for PostgreSQL
Group:          Productivity/Databases/Servers
Provides:       postgresql-test-noarch = %version-%release
Requires:       postgresql-test-implementation
Recommends:     %defaultpackage-implementation

%description test
This package contains the sources and pre-built binaries of various
tests for the PostgreSQL database management system, including
regression tests and benchmarks.

%package docs
Summary:        HTML Documentation for PostgreSQL
Group:          Productivity/Databases/Tools
Provides:       postgresql-docs-noarch = %version-%release
Requires:       postgresql-docs-implementation
Recommends:     %defaultpackage-docs

%description docs
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the HTML documentation for PostgreSQL. The start
page is: file:///usr/share/doc/packages/postgresql/html/index.html .
Manual pages for the PostgreSQL SQL statements can be found in the
postgresql package.

%package contrib
Summary:        Contributed Extensions and Additions to PostgreSQL
Group:          Productivity/Databases/Tools
Provides:       postgresql-contrib-noarch = %version-%release
Requires:       postgresql-contrib-implementation
Recommends:     %defaultpackage-contrib

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

%package devel
Summary:        PostgreSQL development header files and libraries
Group:          Development/Libraries/C and C++
Provides:       postgresql-devel-noarch = %version-%release
Provides:       pkgconfig(libecpg) = %{version}-%{release}
Provides:       pkgconfig(libecpg_compat) = %{version}-%{release}
Provides:       pkgconfig(libpgtypes) = %{version}-%{release}
Provides:       pkgconfig(libpq) = %{version}-%{release}
Requires:       postgresql-devel-implementation
Recommends:     %defaultpackage-devel

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

%package plperl
Summary:        The PL/Tcl, PL/Perl, and  PL/Python procedural languages for PostgreSQL
Group:          Productivity/Databases/Servers
Provides:       postgresql-plperl-noarch = %version-%release
Requires:       postgresql-plperl-implementation
Recommends:     %defaultpackage-plperl

%description plperl
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the PL/Perl procedural language for PostgreSQL.
With this module one can use Perl to write stored procedures,
functions, and triggers.

%package plpython
Summary:        The PL/Python Procedural Languages for PostgreSQL
Group:          Productivity/Databases/Servers
Provides:       postgresql-plpython-noarch = %version-%release
Requires:       postgresql-plpython-implementation
Recommends:     %defaultpackage-plpython

%description plpython
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the PL/Python procedural language for PostgreSQL.
With this module one can use Python to write stored procedures,
functions, and triggers.

%package pltcl
Summary:        PL/Tcl Procedural Language for PostgreSQL
Group:          Productivity/Databases/Tools
Provides:       postgresql-pltcl-noarch = %version-%release
Requires:       postgresql-pltcl-implementation
Recommends:     %defaultpackage-pltcl

%description pltcl
PostgreSQL is an advanced object-relational database management system
that supports an extended subset of the SQL standard, including
transactions, foreign keys, subqueries, triggers, and user-defined
types and functions.

This package contains the PL/Tcl procedural language for PostgreSQL.
With thie module one can use Tcl to write stored procedures, functions,
and triggers.

%prep

%build
%if %{with sysusers}
%sysusers_generate_pre %{SOURCE9} %{name}-server %{name}-server.conf
%endif
echo "This is a dummy package to provide a dependency on the default PostgreSQL version." > README

%install
mkdir -p %buildroot/var/lib/pgsql/

install -m755 -d %buildroot%{_fillupdir}
install -m644 %{S:1} %buildroot%{_fillupdir}/sysconfig.postgresql

%if 0%{?suse_version} < 1550
install -m755 -d %buildroot%fwdir
install -m644 %{S:2} %buildroot%fwdir/%fwname
%endif

install -m755 -d %buildroot/usr/sbin

install -m755 -d %buildroot/usr/share/postgresql
install -m755 %{S:7} %buildroot/usr/share/postgresql/install-alternatives

%if %{with systemd}
install -m644 %{S:5} %buildroot/usr/share/postgresql/bash_profile
install -m755 -d %buildroot/%_tmpfilesdir
install -m644 %{S:3} %buildroot%_tmpfilesdir/postgresql.conf
install -m755 %{S:6} %buildroot/usr/share/postgresql

install -m755 -d %buildroot%_unitdir
install -m444 %{S:4} %buildroot%_unitdir

ln -sf service %buildroot/usr/sbin/rcpostgresql
%else
install -m640 %{S:5} %buildroot/var/lib/pgsql/.bash_profile
install -m755 -d %buildroot/etc/init.d
install -m755 %{S:0} %buildroot/etc/init.d/postgresql
ln -sf /etc/init.d/postgresql %buildroot/usr/sbin/rcpostgresql
%endif

install -D -m 0644 %{SOURCE8} %{buildroot}%{_rpmmacrodir}/macros.%{name}

# sysusers.d
%if %{with sysusers}
install -Dm0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/%{name}-server.conf
%endif


%define eflag /run/postgresql-was-enabled
%define aflag /run/postgresql-was-running

%if %{with sysusers}
%pre server -f %{name}-server.pre
%else
%pre server
getent group postgres > /dev/null ||
	groupadd -g 26 -o -r postgres
getent passwd postgres > /dev/null ||
	useradd -g postgres -o -r -d /var/lib/pgsql -s /bin/bash \
	-c "PostgreSQL Server" -u 26 postgres
%endif
%if %{with systemd}
%service_add_pre postgresql.service

# Save the "enabled" and "active" state across the transition of
# ownership of postgresql.service from postgresql-init to
# postgresql-server.
if [ $1 -ge 1 ]; then \
	if [ x$(systemctl is-enabled postgresql.service 2>/dev/null ||:) = "xenabled" ]; then
		touch %eflag
	fi
	systemctl is-active postgresql.service &>/dev/null && touch %aflag ||:
fi
%endif

%post server
%fillup_only -n postgresql
%if %{with systemd}
PROFILE="/var/lib/pgsql/.bash_profile"
if test -r "$PROFILE" && test "`cat $PROFILE`" = "/usr/share/postgresql/bash_profile"
then
	# Correct a mistake in /usr/lib/tmpfiles.d/postgresql.conf
	# that created /var/lib/pgsql/.bash_profile with invalid
	# content (bsc#1159335).
	rm "$PROFILE"
fi
%tmpfiles_create %_tmpfilesdir/postgresql.conf
%service_add_post postgresql.service
%endif

%preun server
%if %{with systemd}
# Cannot use systemd macros here, because they're doing too much
/usr/bin/systemctl --no-reload disable postgresql.service || :
%else
%stop_on_removal postgresql
%endif

%postun server
%if %{with systemd}
# Cannot use systemd macros here, because they're doing too much
rm -f "/var/lib/systemd/migrated/postgresql"
/usr/bin/systemctl daemon-reload || :

%else
%insserv_cleanup
%endif

%if %{with systemd}
%posttrans server
# Save the "enabled" and "active" state across the transition of
# ownership of postgresql.service from postgresql-init to
# postgresql-server.
if test -f %eflag; then
	rm -f %eflag
	systemctl enable postgresql.service
fi
if test -f %aflag; then
	rm -f %aflag
	systemctl start postgresql.service
fi
%endif

%files
%defattr(-,root,root,-)
%doc README
%dir /usr/share/postgresql
/usr/share/postgresql/install-alternatives

%files server
%defattr(-,root,root,-)
%doc README
%attr(750,postgres,postgres) %dir /var/lib/pgsql
%if %{with systemd}
%attr(644,root,root) /usr/share/postgresql/bash_profile
%ghost %config %attr(640,postgres,postgres) /var/lib/pgsql/.bash_profile
%else
%config %attr(640,postgres,postgres) /var/lib/pgsql/.bash_profile
%endif

%if 0%{?suse_version} < 1550
%if 0%{?suse_version} > 1110
%dir %fwdir
%endif
%config %fwdir/%fwname
%endif

%{_fillupdir}/sysconfig.postgresql
/usr/sbin/rcpostgresql
%if %{with systemd}
%_tmpfilesdir/postgresql.conf
%_unitdir/
/usr/share/postgresql/postgresql-script
%ghost %dir %attr(1775,postgres,postgres) /run/postgresql
%else
%config /etc/init.d/postgresql
%dir %attr(1775,postgres,postgres) /var/run/postgresql
%endif
%if %{with sysusers}
%{_sysusersdir}/%{name}-server.conf
%endif

%files test
%defattr(-,root,root,-)
%doc README

%files docs
%defattr(-,root,root,-)
%doc README

%files contrib
%defattr(-,root,root,-)
%doc README

%files devel
%defattr(-,root,root,-)
%doc README

%files server-devel
%defattr(-,root,root,-)
%doc README
%{_rpmmacrodir}/macros.%{name}

%if %{with llvm}
%files llvmjit
%defattr(-,root,root,-)
%doc README

%files llvmjit-devel
%defattr(-,root,root,-)
%doc README
%endif

%files plperl
%defattr(-,root,root,-)
%doc README

%files plpython
%defattr(-,root,root,-)
%doc README

%files pltcl
%defattr(-,root,root,-)
%doc README

%changelog
