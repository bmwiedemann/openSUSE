#
# spec file for package postgresql-plr
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


%define pgname @BUILD_FLAVOR@
%if "%{pgname}" == ""
%define pgname postgresql
%endif
# Thanks upstream :-)
%define sname plr
%define sversion REL8_4_7
# Make our path like what postgresql packager decide

%define pgshare %(pg_config --sharedir)
%define pkglibs %(pg_config --pkglibdir)
%define extensiondir %{pgshare}/extension

Summary:        PL/R - R Procedural Language for PostgreSQL
License:        GPL-2.0-or-later
Group:          Productivity/Databases/Servers
Name:           %{pgname}-%{sname}
Version:        8.4.7
Release:        1.0
Source:         https://github.com/postgres-plr/plr/archive/%{sversion}.tar.gz
Source1:        readme.SUSE
Source2:        plr-US.pdf
Source99:       series
Patch0:         patch-Makefile-ldflags.patch
URL:            https://github.com/postgres-plr/plr/
BuildRequires:  %{pgname}-server
BuildRequires:  %{pgname}-server-devel
BuildRequires:  R-base
BuildRequires:  R-base-devel
BuildRequires:  pkg-config
BuildRequires:  post-build-checks
Requires:       %{pgname}-server
Requires:       R-base
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if "%{pgname}" == "postgresql"
ExclusiveArch:  do_not_build
%endif
%if ("%{pgname}" == "postgresql95" || "%{pgname}" == "postgresql96") && 0%{?suse_version} >= 1550
ExclusiveArch:  do_not_build
%endif

%description
PL/R is a loadable procedural language that enables you to write PostgreSQL
functions and triggers in the R programming language. PL/R offers most (if
not all) of the capabilities a function writer has in the R language.

Commands are available to access the database via the PostgreSQL Server
Programming Interface (SPI) and to raise messages via elog() . There is no
way to access internals of the database backend. However the user is able
to gain OS-level access under the permissions of the PostgreSQL user ID,
as with a C function. Thus, any unprivileged database user should not be
permitted to use this language. It must be installed as an untrusted
procedural language so that only database superusers can create functions
in it. The writer of a PL/R function must take care that the function cannot
be used to do anything unwanted, since it will be able to do anything that
could be done by a user logged in as the database administrator.

An implementation restriction is that PL/R procedures cannot be used to
create input/output functions for new data types.

%package doc
Summary:        Documentation for PL/R - R Procedural Language for PostgreSQL
Group:          Productivity/Databases/Servers

%description doc
PL/R is a loadable procedural language that enables you to write PostgreSQL
functions and triggers in the R programming language. PL/R offers most (if
not all) of the capabilities a function writer has in the R language.

This package contain the associated documentation

%prep
# plr.so know where R is located
%autosetup -p1 -n %{sname}-%{sversion}

# Need to fix spurious rights in doc and root
find ./ -type f -exec chmod 0644 {} \;
cp -v %{S:2} .

%build
export PATH="$PATH:/usr/lib/%{pgname}/bin"
# Picked from main obs postgresql
export CFLAGS="%optflags $SP"
# uncomment the following line to enable the stack protector
CFLAGS="$CFLAGS -fstack-protector"

#Rpath?
LDFLAGS="$LDFLAGS -Wl,-rpath,%_libdir/R/lib"
USE_PGXS=1 %__make %{?extension} %{?_smp_mflags};

%install
export PATH="$PATH:/usr/lib/%{pgname}/bin"
mkdir -p %{buildroot}/etc/ld.so.conf.d/
# okay keep this method until using rpath is completed
cat  > %{buildroot}/etc/ld.so.conf.d/%{name}.conf <<EOF
# postgresql-plr need to find where R is installed
%{_libdir}/R
%{_libdir}/R/lib
EOF

# All the right location could be found with pg_config
# USE_PGXS=1 make install
install -d -m 0755 %{buildroot}/%{pkglibs}
install -m 755 %{sname}.so %{buildroot}/%{pkglibs}/%{sname}.so
install -d -m 0755 %{buildroot}/%{extensiondir}
install -p -m 644 %{sname}*.sql %{buildroot}%{extensiondir}/
install -p -m 644 %{sname}.control %{buildroot}%{extensiondir}/%{sname}.control

cp -a %{S:1} .

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 0755)
%doc README.md
%doc readme.SUSE
%dir %{extensiondir}/
%{extensiondir}/%{sname}.control
%{extensiondir}/%{sname}*.sql
%config /etc/ld.so.conf.d/%{name}.conf
%defattr(755, root, root, 0755)
%dir %{pkglibs}
%{pkglibs}/%{sname}.so

%files doc
%defattr(644, root, root, 0755)
%doc *pdf
%doc expected/plr.out

%changelog
