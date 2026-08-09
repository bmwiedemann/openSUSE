#
# spec file for package grass
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# Notice to maintainer : move this package to real lfhs
%define         shortver 85

Name:           grass
Version:        8.5.0
Release:        0
Summary:        Geographic Resources Analysis Support System
License:        GPL-2.0-or-later
URL:            https://grass.osgeo.org/
Source0:        https://github.com/OSGeo/grass/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/OSGeo/grass/releases/download/%{version}/%{name}-%{version}.tar.gz.sha256
BuildRequires:  PDAL-devel >= 1.7.1
BuildRequires:  bison
BuildRequires:  blas-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel
BuildRequires:  libgdal-devel >= 3.7
BuildRequires:  libgeos-devel >= 3
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  man
BuildRequires:  mysql-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  proj >= 9
BuildRequires:  python3-dateutil
BuildRequires:  python3-numpy
BuildRequires:  python3-opengl
BuildRequires:  python3-wxPython
BuildRequires:  python3-xml
BuildRequires:  readline-devel
BuildRequires:  sqlite-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cblas)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(lapack)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(ncurses) >= 5.5
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(openblas)
BuildRequires:  pkgconfig(proj) >= 9
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(zlib)
# proj contains the required common data files
Requires:       proj >= 9
Requires:       python3-dateutil
Requires:       python3-numpy
Requires:       python3-opengl
Requires:       python3-wxPython
Requires:       python3-xml
Requires:       sqlite >= 3
Requires:       unixODBC
Requires:       xterm
Recommends:     grass-doc

%package doc
Summary:        Documentation for GRASS GIS

%package devel
Summary:        Development files for GRASS GIS
Requires:       grass = %{version}

%description
GRASS (Geographic Resources Analysis Support System), commonly
referred to as GRASS, is a Geographic Information System
(GIS) used for geospatial data management and analysis, image
processing, graphics/maps production, spatial modeling, and
visualization. GRASS is currently used in academic and commercial
settings around the world, as well as by many governmental agencies
and environmental consulting companies.

%description devel
This package contains the development files for GRASS GIS

%description doc
This package contains the HTML documentation files for GRASS GIS

%prep
%autosetup -n grass-%{version}

%define grasver -@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@.@GRASS_VERSION_RELEASE@
%define grasver2 '-${GRASS_VERSION_MAJOR}.${GRASS_VERSION_MINOR}.${GRASS_VERSION_RELEASE}'

sed -i s/%{grasver}//g include/Make/Platform.make.in
sed -i s/%{grasver}//g grass.pc.in
sed -i s/%{grasver2}//g configure
sed -i s/%{grasver2}//g Makefile
sed -i -e "/GRASS_HEADERS_/ s/@GRASS_HEADERS_GIT_.*@/"$(date -d @${SOURCE_DATE_EPOCH} -u +%%FT%%T%%:z)"/" include/grass/version.h.in
cat include/grass/version.h.in

%define grassprefix %{_libdir}
%define grassdir %{grassprefix}/%{name}%{shortver}
%define grasslib %{grassprefix}/%{name}%{shortver}/lib

# configure with shared libs:
export CFLAGS="%{optflags} -Werror=implicit-function-declaration"
export CXXFLAGS="%{optflags} -std=c++17"

./configure \
	--prefix=%{grassprefix} \
	--enable-shared \
	--enable-socket \
	--enable-largefile \
	--with-blas \
	--with-bzlib \
	--with-cairo --with-cairo-ldflags=-lfontconfig \
	--with-curses \
	--with-cxx \
	--with-fftw \
	--with-freetype --with-freetype-includes=%{_includedir}/freetype2 \
	--with-gdal=%{_bindir}/gdal-config \
	--with-geos \
	--with-lapack \
	--with-motif \
	--with-mysql --with-mysql-includes=%{_includedir}/mysql \
	--with-netcdf \
	--with-nls \
	--with-odbc \
	--with-opengl \
	--with-openmp \
	--with-pdal \
	--with-png \
	--with-postgres --with-postgres-includes=%{_includedir}/pgsql \
	--with-proj-share=%{_datadir}/proj \
	--with-pthread \
	--with-python \
	--with-readline \
	--with-regex \
	--with-sqlite \
	--with-tiff \
	--with-wxwidgets \
	--with-x \
	--with-zstd

# rpmlint: wrong-script-interpreter /usr/bin/env python3
find . -type f -exec sed -i -e 's:#!%{_bindir}/env python3:#!%{_bindir}/python3:g' {} +

%build
# Make builds reproducible (e.g. "random" colortable example in documentation)
export GRASS_RANDOM_SEED=1234
%make_build prefix=%{grassprefix} PREFIX=%{grassprefix}

%install
make prefix=%{buildroot}%{grassprefix} PREFIX=%{buildroot}%{grassprefix} install

# don't create a non-standard-directory for a single file
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{grassprefix}/bin/grass %{buildroot}%{_bindir}
rmdir %{buildroot}%{grassprefix}/bin

# changing GISBASE in startup script (deleting %%{buildroot} from path)
sed -i s:%{buildroot}::g %{buildroot}%{_bindir}/grass
sed -i s:%{buildroot}::g %{buildroot}%{grassdir}/include/Make/Grass.make
sed -i s:%{buildroot}::g %{buildroot}%{grassdir}/include/Make/Platform.make
sed -i s:%{buildroot}::g %{buildroot}%{grassdir}%{_sysconfdir}/fontcap
sed -i s:%{buildroot}::g %{buildroot}%{grassdir}%{_sysconfdir}/python/grass/app/resource_paths.py

# make grass libraries available on the system
install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{grasslib} >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/grass-%{version}.conf

mkdir -p %{buildroot}%{_datadir}/applications
cp  %{buildroot}%{grassdir}/share/applications/grass.desktop %{buildroot}%{_datadir}/applications/grass.desktop
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s %{grassdir}/share/icons/hicolor/192x192/apps/grass.png %{buildroot}%{_datadir}/pixmaps/grass.png

# The blanket shebang rewrite in %%prep lands #!/usr/bin/python3 on library
# modules that are not executable and are never run directly
# (rpmlint: non-executable-script). This must come BEFORE byte-compiling:
# editing the sources afterwards would invalidate the fresh bytecode again.
find %{buildroot}%{grassdir} -name '*.py' ! -perm -u+x -exec sed -i '1{/^#!\/usr\/bin\/python3$/d}' {} +

# Byte-compile with hash-based invalidation (PEP 552). Timestamp-based .pyc
# cannot work here: the mtimes of the installed sources are clamped to
# SOURCE_DATE_EPOCH for reproducibility after %%install has run, so any
# timestamp we record is stale by the time the package is assembled
# (rpmlint: python-bytecode-inconsistent-mtime).
find %{buildroot}%{grassdir} -name __pycache__ -type d -prune -exec rm -rf {} +
python3 -m compileall -q --invalidation-mode checked-hash \
    -s %{buildroot} %{buildroot}%{grassdir} >/dev/null || :

rm -rf %{buildroot}%{_libdir}/grass%{shortver}/utils/__pycache__

echo %{grassdir} >%{buildroot}/%{_sysconfdir}/GRASSDIR

%fdupes -s %{buildroot}%{grassdir}

# Generate the translation file list instead of hardcoding it: the .mo files
# are compiled from locale/po/ at build time, so a hand-maintained list rots
# silently as upstream adds languages -- si and uk were both mistagged as
# %%lang(sl), and hi and sv were missing entirely.
: > %{_builddir}/grass.lang
for _mo in %{buildroot}%{grassdir}/locale/*/LC_MESSAGES; do
    [ -d "$_mo" ] || continue
    _lang=$(basename "$(dirname "$_mo")")
    {
      echo "%%lang($_lang) %%dir %{grassdir}/locale/$_lang"
      echo "%%lang($_lang) %%dir %{grassdir}/locale/$_lang/LC_MESSAGES"
      echo "%%lang($_lang) %{grassdir}/locale/$_lang/LC_MESSAGES/*.mo"
    } >> %{_builddir}/grass.lang
done

%check
# Exercise what was built. Use the in-source build tree, NOT the buildroot copy:
# %%install rewrites the buildroot's paths to the final install location, and
# GRASS's launcher deliberately ignores $GISBASE (RuntimePaths sets it with
# use_env_values=False). It only falls back to locating itself when
# %{grassdir} does not exist, so a buildroot-based check silently depends on no
# GRASS being installed on the build host. The in-source tree is self-consistent.
_grass="$(echo bin.*)/grass"

# core: version reporting, region handling, and the Python scripting API
$_grass --tmp-project XY --exec g.version -rge
$_grass --tmp-project XY --exec g.region -p
$_grass --tmp-project EPSG:4326 --exec python3 -c \
    'import grass.script as gs; assert gs.parse_command("g.version", flags="g")["version"].startswith("%{version}")'

# The installed programs embed LD_LIBRARY_PATH pointing at this in-source tree;
# drop it now that the tests are done, so it cannot leak into the generated
# requires at packaging time.
rm -rf dist.* bin.*

%ldconfig_scriptlets

%files devel
%dir %{grassdir}
%{grassdir}/include
%{_sysconfdir}/GRASSDIR

%files doc
%dir %{grassdir}
%{grassdir}/docs

%files -f %{_builddir}/grass.lang
%config %{_sysconfdir}/ld.so.conf.d/grass-%{version}.conf
%{_bindir}/%{name}
%dir %{grassdir}
%{grassdir}/bin
%{grassdir}%{_sysconfdir}
%{grassdir}/gui
%{grassdir}/scripts
%dir %{grassdir}/share
%dir %{grassdir}/share/applications
%{grassdir}/share/applications/grass.desktop
%{grassdir}/share/icons
%dir %{grassdir}/share/metainfo
%{grassdir}/share/metainfo/org.osgeo.grass.appdata.xml
%{_datadir}/applications/grass.desktop
%{_datadir}/pixmaps/grass.png
%dir %{grassdir}/locale
%dir %{grassdir}/utils
%{grassdir}/utils/*.py*
%{grassdir}/utils/g.echo
%{grassdir}/driver
%{grassdir}/fonts
%dir %{grasslib}
%{grasslib}/*.so
%{grassdir}/AUTHORS
%{grassdir}/translators.csv
%{grassdir}/translation_status.json
%{grassdir}/contributors*
%{grassdir}/COPYING
%{grassdir}/GPL.TXT
%{grassdir}/REQUIREMENTS.md
%{grassdir}/CITING
%{grassdir}/INSTALL.md
%exclude %{grassdir}/demolocation

%changelog
