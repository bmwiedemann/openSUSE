#
# spec file for package grass
#
# Copyright (c) 2022 SUSE LLC
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
%define	shortver 78
%if 0%{?suse_version} >= 1550
BuildRequires:  python3-wxPython
%else
BuildRequires:  python-wxWidgets-devel >= 3.0
%endif

Name:           grass
Version:        7.8.7
Release:        0
Summary:        Geographic Resources Analysis Support System
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Other
URL:            https://grass.osgeo.org/
Source:         https://grass.osgeo.org/grass%{shortver}/source/%{name}-%{version}.tar.gz
Source1:        https://grass.osgeo.org/grass%{shortver}/source/%{name}-%{version}.md5sum
BuildRequires:  -post-build-checks
BuildRequires:  bison
BuildRequires:  blas-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  flex
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  lapack-devel
BuildRequires:  libXmu-devel
BuildRequires:  libbz2-devel
BuildRequires:  libgdal-devel >= 3
BuildRequires:  libgeos-devel >= 3
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libzstd-devel
BuildRequires:  man
BuildRequires:  mysql-devel
BuildRequires:  ncurses-devel >= 5.5
BuildRequires:  netcdf-devel
BuildRequires:  perl
BuildRequires:  postgresql-devel
BuildRequires:  proj >= 6
BuildRequires:  proj-devel >= 6
BuildRequires:  python3-dateutil
BuildRequires:  python3-devel
BuildRequires:  python3-numpy
BuildRequires:  python3-opengl
BuildRequires:  python3-six
BuildRequires:  python3-xml
BuildRequires:  sqlite-devel
BuildRequires:  unixODBC-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
# proj contains the required common data files
Requires:       proj >= 6
Requires:       python3-dateutil
Requires:       python3-numpy
Requires:       python3-opengl
Requires:       python3-xml
Requires:       sqlite >= 3
Requires:       unixODBC
Requires:       xterm
Recommends:     grass-doc
Obsoletes:      grass7
%if 0%{?suse_version} >= 1550
Requires:       python3-wxPython
%else
Requires:       python-wxWidgets >= 2.8
%endif

%package doc
Summary:        Documentation for GRASS GIS 7
Group:          Documentation/Other

%package devel
Summary:        Development files for GRASS GIS 7
Group:          Development/Libraries/C and C++
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
%setup -q -n grass-%{version}

%define grasver -@GRASS_VERSION_MAJOR@.@GRASS_VERSION_MINOR@.@GRASS_VERSION_RELEASE@
%define grasver2 '-${GRASS_VERSION_MAJOR}.${GRASS_VERSION_MINOR}.${GRASS_VERSION_RELEASE}'

sed -i s/%{grasver}//g include/Make/Platform.make.in
sed -i s/%{grasver}//g grass.pc.in
sed -i s/%{grasver2}//g configure
sed -i s/%{grasver2}//g Makefile
sed -i -e "/GRASS_HEADERS_/ s/@GRASS_HEADERS_GIT_.*@/"$(date -d @${SOURCE_DATE_EPOCH} -u +%FT%T%:z)"/" include/version.h.in
cat include/version.h.in

%define grassprefix %{_libdir}
%define grassdir %{grassprefix}/%{name}%{shortver}
%define grasslib %{grassprefix}/%{name}%{shortver}/lib

# configure with shared libs:
# Pick for upstream travis, normal optflags are not supported
export CFLAGS="-O2 -Werror=implicit-function-declaration"

./configure \
	--prefix=%{grassprefix} \
	--enable-shared \
	--enable-socket \
	--enable-largefile \
	--with-blas \
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
	--with-openmp \
	--with-postgres --with-postgres-includes=%{_includedir}/pgsql \
	--with-proj-share=%{_datadir}/proj \
	--with-pthread \
	--with-python \
	--with-bzlib \
    --with-x \
    --with-zstd \
	--with-sqlite \
	--with-wxwidgets

# rpmlint: wrong-script-interpreter /usr/bin/env python3
find . -type f -exec sed -i -e 's:#!%{_bindir}/env python3:#!%{_bindir}/python3:g' {} +

%build
# Make builds reproducible (e.g. "random" colortable example in documentation)
export GRASS_RANDOM_SEED=1234
make prefix=%{grassprefix} PREFIX=%{grassprefix} %{?_smp_mflags}

%install
make prefix=%{buildroot}%{grassprefix} PREFIX=%{buildroot}%{grassprefix} install

# Program sets LD_LIBRARY_PATH pointing to in-source path
# resulting in wrong requires, prevent that
rm -rf dist.*

# don't create a non-standard-directory for a single file
mkdir -p %{buildroot}%{_bindir}
mv %{buildroot}%{grassprefix}/bin/grass%{shortver} %{buildroot}%{_bindir}
rmdir %{buildroot}%{grassprefix}/bin

# changing GISBASE in startup script (deleting %%{buildroot} from path)
sed -i s:%{buildroot}::g %{buildroot}%{_bindir}/grass%{shortver}
sed -i s:%{buildroot}::g %{buildroot}%{grassdir}/include/Make/Grass.make
sed -i s:%{buildroot}::g %{buildroot}%{grassdir}/include/Make/Platform.make
sed -i s:%{buildroot}::g %{buildroot}%{grassdir}%{_sysconfdir}/fontcap
# Make symlinks in /usr/bin/
install -d %{buildroot}%{_bindir}/
pushd %{buildroot}%{_bindir}/
ln -fsv grass%{shortver} grass
popd

# make grass libraries available on the system
install -d %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo %{grasslib} >> %{buildroot}%{_sysconfdir}/ld.so.conf.d/grass-%{version}.conf

mkdir -p %{buildroot}%{_datadir}/applications
cp  %{buildroot}%{grassdir}/share/applications/grass.desktop %{buildroot}%{_datadir}/applications/grass.desktop
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s %{grassdir}/share/icons/hicolor/192x192/apps/grass.png %{buildroot}%{_datadir}/pixmaps/grass.png

rm -rf %{buildroot}%{_libdir}/grass%{shortver}/tools/__pycache__

echo %{grassdir} >%{buildroot}/%{_sysconfdir}/GRASSDIR

%fdupes -s %{buildroot}%{grassdir}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files devel
%{grassdir}/include
%{grasslib}/*.a
%{_sysconfdir}/GRASSDIR

%files doc
%{grassdir}/docs

%files
%config %{_sysconfdir}/ld.so.conf.d/grass-%{version}.conf
%{_bindir}/%{name}
%{_bindir}/%{name}%{shortver}
%{grassdir}/bin/*
%{grassdir}%{_sysconfdir}/*
%{grassdir}/gui/*
%{grassdir}/scripts/*
%{grassdir}/share/applications/grass.desktop
%{grassdir}/share/icons/hicolor/*
%{grassdir}/share/metainfo/org.osgeo.grass.appdata.xml
%{_datadir}/applications/grass.desktop
%{_datadir}/pixmaps/grass.png
%lang(ar) %{grassdir}/locale/ar/LC_MESSAGES/*.mo
%lang(bn) %{grassdir}/locale/bn/LC_MESSAGES/*.mo
%lang(cs) %{grassdir}/locale/cs/LC_MESSAGES/*.mo
%lang(de) %{grassdir}/locale/de/LC_MESSAGES/*.mo
%lang(el) %{grassdir}/locale/el/LC_MESSAGES/*.mo
%lang(es) %{grassdir}/locale/es/LC_MESSAGES/*.mo
%lang(fr) %{grassdir}/locale/fr/LC_MESSAGES/*.mo
%lang(fi) %{grassdir}/locale/fi/LC_MESSAGES/*.mo
%lang(hu) %{grassdir}/locale/hu/LC_MESSAGES/*.mo
%lang(id) %{grassdir}/locale/id_ID/LC_MESSAGES/*.mo
%lang(it) %{grassdir}/locale/it/LC_MESSAGES/*.mo
%lang(ja) %{grassdir}/locale/ja/LC_MESSAGES/*.mo
%lang(ko) %{grassdir}/locale/ko/LC_MESSAGES/*.mo
%lang(lv) %{grassdir}/locale/lv/LC_MESSAGES/*.mo
%lang(ml) %{grassdir}/locale/ml/LC_MESSAGES/*.mo
%lang(pl) %{grassdir}/locale/pl/LC_MESSAGES/*.mo
%lang(pt) %{grassdir}/locale/pt/LC_MESSAGES/*.mo
%lang(pt_br) %{grassdir}/locale/pt_BR/LC_MESSAGES/*.mo
%lang(ru) %{grassdir}/locale/ru/LC_MESSAGES/*.mo
%lang(ro) %{grassdir}/locale/ro/LC_MESSAGES/*.mo
%lang(sl) %{grassdir}/locale/sl/LC_MESSAGES/*.mo
%lang(sl) %{grassdir}/locale/si/LC_MESSAGES/*.mo
%lang(ta) %{grassdir}/locale/ta/LC_MESSAGES/*.mo
%lang(th) %{grassdir}/locale/th/LC_MESSAGES/*.mo
%lang(tr) %{grassdir}/locale/tr/LC_MESSAGES/*.mo
%lang(sl) %{grassdir}/locale/uk/LC_MESSAGES/*.mo
%lang(vi) %{grassdir}/locale/vi/LC_MESSAGES/*.mo
%lang(zh) %{grassdir}/locale/zh/LC_MESSAGES/*.mo
%lang(zh_cn) %{grassdir}/locale/zh_CN/LC_MESSAGES/*.mo
%{grassdir}/tools/*.py*
%{grassdir}/tools/g.echo
%{grassdir}/driver/*
%{grassdir}/fonts/*
%{grasslib}/*.so
%{grassdir}/AUTHORS
%{grassdir}/translators.csv
%{grassdir}/translation_status.json
%{grassdir}/contributors*
%{grassdir}/CHANGES
%{grassdir}/COPYING
%{grassdir}/GPL.TXT
%{grassdir}/REQUIREMENTS.html
%{grassdir}/CITING
%{grassdir}/INSTALL
%exclude %{grassdir}/demolocation

%changelog
