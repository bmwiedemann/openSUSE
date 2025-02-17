#
# spec file for package postgis
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


%define         pg_name  @BUILD_FLAVOR@%{nil}
%define         ext_name postgis
%{pg_version_from_name}
%define         main_version 3.5

Name:           %{pg_name}-%{ext_name}
Version:        3.5.0
Release:        0
Summary:        Geographic Information Systems Extensions to PostgreSQL
License:        GPL-2.0-or-later
Group:          Productivity/Databases/Servers
URL:            https://postgis.net/
Source0:        https://download.osgeo.org/postgis/source/%{ext_name}-%{version}.tar.gz
Source1:        https://postgis.net/stuff/%{ext_name}-%{version}.tar.gz.md5
BuildRequires:  %{pg_name}-llvmjit-devel
BuildRequires:  %{pg_name}-server-devel
BuildRequires:  cgal-devel
BuildRequires:  cunit-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel >= 3.0
BuildRequires:  gtk2-devel
BuildRequires:  libgeos-devel >= 3.8.0
BuildRequires:  libjson-c-devel
BuildRequires:  libprotobuf-c-devel
BuildRequires:  proj-devel >= 6.1.0
# proj.db is required for ST_ functions and tests boo#1188129
BuildRequires:  proj
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxml2-devel
BuildRequires:  libxml2-tools
# building doc but would add 350 texlive packages
# BuildRequires:  dblatex
# BuildRequires:  ImageMagick
%ifarch %{ix86}
%define with_sfcgal 0
%else
%define with_sfcgal 1
BuildRequires:  sfcgal-devel >= 1.4.1
%endif
BuildRequires:  update-alternatives
%pg_server_requires
%if "%{pg_name}" == ""
Name:           %{ext_name}
ExclusiveArch:  do_not_build
%endif
# proj.db is required for ST_ functions and tests boo#1188129
Requires:       proj
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      postgis2
Provides:       postgis
Conflicts:      %{pg_name}-address_standardizer
Provides:       %{pg_name}-address_standardizer

%description
PostGIS is a spatial database extender for PostgreSQL object-relational
database. It adds support for geographic objects allowing location queries
to be run in SQL.

%package utils
Summary:        The utils for PostGIS
Group:          Productivity/Databases/Tools
Requires:       %{name} = %{version}
Requires:       perl-DBD-Pg
Provides:       postgis-utils
BuildArch:      noarch

%description utils
The postgis-utils package provides utilities for PostGIS.

%prep
%autosetup -p1 -n %{ext_name}-%{version}
echo "pg_version is %{pg_version}"

%build
# since 3.4.0, we need to move again those to pg_config_bindir for alternatives
%configure \
    --bindir=%{pg_config_bindir} \
    --datarootdir=%{pg_config_sharedir} \
    --datadir=%{pg_config_sharedir} \
    --with-protobuf \
    --with-raster \
    --with-topology \
    --with-gui \
    --with-json \
%if %{with_sfcgal}
    --with-sfcgal=%{_bindir}/sfcgal-config \
%endif
    --disable-rpath \
    --disable-gtktest \
    --with-interrupt-tests \
    --with-raster-dblwarning

%make_build soname="%{ext_name}-%{main_version}.so"

%install
install -d -m 755 %{buildroot}%{pg_config_bindir}
%make_install

# install manpages format them as our pg packages
install -d -m 755 %{buildroot}%{_mandir}/man1
# fix shebang and install utils
sed -i 's,^#!/usr/bin/env perl,#!/usr/bin/perl,g' utils/*.pl regress/*.pl %{buildroot}%{pg_config_bindir}/postgis_restore
rm utils/postgis_restore.pl
install -m 755 utils/*.pl %{buildroot}%{pg_config_bindir}
# remove .a and .la files
rm -f %{buildroot}/%{_libdir}/*.la
rm -f %{buildroot}/%{_libdir}/*.a

# Temporary fix we re-add the readme with doc macro
rm -fr %{buildroot}%{_docdir}/%{pg_name}

%fdupes -s %{buildroot}%{pg_config_sharedir}/extension
%fdupes -s %{buildroot}%{pg_config_sharedir}/contrib

find %{buildroot}/%{_mandir}/man1/ -type f -printf "mv %%p %%ppg%{pg_version}\n" | bash -x

%check
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export PGDATA=/home/abuild/postgis_tests/data
export PGHOST=/tmp
export PGPORT=5454
mkdir -p "${PGDATA}"
initdb --pgdata=${PGDATA} --auth=peer --auth-host=scram-sha-256 --auth-local=peer --encoding=UTF-8 --locale=en_US.UTF-8 --lc-message=en_US.UTF-8
pg_ctl -D "${PGDATA}" -l logfile -o "-p ${PGPORT} -k ${PGHOST} -B 1024" start
psql -d postgres -c "\dx"

# Manually try to create a databse and the 4 postgis extensions
# As extension are not installed system wide we use the old sql method
# Need access to $libdir/postgis not installed
#export LD_LIBRARY_PATH=%%{_libdir}:%%{buildroot}/%%{pg_libdir}
#export libdir=%%{buildroot}/%%{pg_libdir}
#psql -d postgres -c "create database %%{sname};"
#psql -d %%{sname} -f %%{buildroot}/%%{pg_share}/contrib/%%{sname}-%%{main_version}/postgis.sql
#psql -d %%{sname} -f %%{buildroot}/%%{pg_share}/contrib/%%{sname}-%%{main_version}/postgis_sfcgal.sql
#psql -d %%{sname} -f %%{buildroot}/%%{pg_share}/contrib/%%{sname}-%%{main_version}/postgis_raster.sql
#psql -d %%{sname} -f %%{buildroot}/%%{pg_share}/contrib/%%{sname}-%%{main_version}/postgis_topology.sql
#psql -d %%{sname} -c "\dx"
#psql -d %%{sname} -c "select postgis_full_version();"
# Don't fail test yet, we have a different result for mvt between Leap and TW
# Tests often failed one time, then retry.
make check || make check || :
pg_ctl -D "${PGDATA}" --mode="fast" stop

%postun
%{_datadir}/postgresql/install-alternatives %pg_version

%post
%{_datadir}/postgresql/install-alternatives %pg_version

%postun utils
%{_datadir}/postgresql/install-alternatives %pg_version

%post utils
%{_datadir}/postgresql/install-alternatives %pg_version

%files
%license COPYING LICENSE.TXT
%doc ChangeLog CODE_OF_CONDUCT.md CONTRIBUTING.md NEWS README.postgis SECURITY.md extensions/address_standardizer/README.address_standardizer
%{pg_config_pkglibdir}/*
%{_mandir}/man1/pgsql2shp.1pg%{pg_version}.gz
%{_mandir}/man1/pgtopo_export.1pg%{pg_version}.gz
%{_mandir}/man1/pgtopo_import.1pg%{pg_version}.gz
%{_mandir}/man1/postgis.1pg%{pg_version}.gz
%{_mandir}/man1/postgis_restore.1pg%{pg_version}.gz
%{_mandir}/man1/shp2pgsql.1pg%{pg_version}.gz
%{pg_config_bindir}/pgtopo_export
%{pg_config_bindir}/pgtopo_import
%{pg_config_bindir}/pgsql2shp
%{pg_config_bindir}/postgis
%{pg_config_bindir}/postgis_restore
%{pg_config_bindir}/raster2pgsql
%{pg_config_bindir}/shp2pgsql
%{pg_config_bindir}/shp2pgsql-gui
%dir %{pg_config_sharedir}/applications
%{pg_config_sharedir}/applications/shp2pgsql-gui.desktop
%dir %{pg_config_sharedir}/icons
%{pg_config_sharedir}/icons/*
%dir %{pg_config_sharedir}/contrib
%{pg_config_sharedir}/contrib/postgis*
%{pg_config_sharedir}/extension/postgis*
%{pg_config_sharedir}/extension/address_standardizer*

%files utils
%license COPYING LICENSE.TXT
%{pg_config_bindir}/create_extension_unpackage.pl
%{pg_config_bindir}/create_or_replace_to_create.pl
%{pg_config_bindir}/create_skip_signatures.pl
%{pg_config_bindir}/create_spatial_ref_sys_config_dump.pl
%{pg_config_bindir}/create_uninstall.pl
%{pg_config_bindir}/create_unpackaged.pl
%{pg_config_bindir}/create_upgrade.pl
%{pg_config_bindir}/profile_intersects.pl
%{pg_config_bindir}/read_scripts_version.pl
%{pg_config_bindir}/repo_revision.pl
%{pg_config_bindir}/test_estimation.pl
%{pg_config_bindir}/test_geography_estimation.pl
%{pg_config_bindir}/test_geography_joinestimation.pl
%{pg_config_bindir}/test_joinestimation.pl

%changelog
