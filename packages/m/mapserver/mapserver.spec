#
# spec file for package mapserver
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2014 Ioda-Net Sàrl, Charmoille, Switzerland. Bruno Friedmann (tigerfoot)
# Copyright (c) 2015 Angelos Tzotsos (kalxas)
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

%bcond_with python
%bcond_with ruby

#
# define python for future reference
%define _with_python 1
%define libname libmapserver2
%define _cgibindir /srv/www/cgi-bin
%if 0%{?suse_version} >= 1500
%define php_name    php7
%else
%define php_name    php5
%endif

Name:           mapserver
Version:        7.6.2
Release:        0
Summary:        Environment for building spatially-enabled internet applications
License:        MIT
Group:          Productivity/Networking/Web/Servers
Url:            https://www.mapserver.org/
Source:         https://download.osgeo.org/mapserver/%{name}-%{version}.tar.gz
Source9:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM mapserver-7.6.1-fix_python_install_path.patch fixing python installation path badly defaulting to arch independent location
Patch0:         mapserver-7.6.1-fix_python_install_path.patch
BuildRequires:  FastCGI-devel
BuildRequires:  apache2-devel
BuildRequires:  autoconf
BuildRequires:  cairo-devel
BuildRequires:  chrpath
BuildRequires:  cmake >= 2.4
BuildRequires:  freetype2-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gd-devel >= 2.0.16
BuildRequires:  giflib-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  libgdal-devel >= 1.10
BuildRequires:  libgeos-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libproj-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  mysql-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  pam
BuildRequires:  pam-devel
BuildRequires:  postgresql-devel >= 9.1
%if 0%{?suse_version} >= 1500
BuildRequires:  postgresql-server-devel >= 9.1
%endif
BuildRequires:  proj
BuildRequires:  libprotobuf-c-devel
BuildRequires:  protobuf-c
BuildRequires:  readline-devel
BuildRequires:  rpm
BuildRequires:  swig
BuildRequires:  update-alternatives
BuildRequires:  xorg-x11-libXpm-devel
BuildRequires:  zlib-devel
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       %{libname} = %{version}-%{release}
Requires:       proj

%description
Mapserver is an internet mapping program that converts GIS data to
map images in real time. With appropriate interface pages,
Mapserver can provide an interactive internet map based on
custom GIS data.

%package -n %{libname}
Summary:        Mapsserver library for mapserver or mapscript module
Group:          System/Libraries

%description -n %{libname}
Mapserver library for mapserver or mapscript module. you need this lib to run mapserver
or any of the mapscript module (php, java, python, ruby)

# We don't require apache2_mod-php5 users could have php5 running 
# with other modes (cgi, php-fpm etc)

%package -n php-mapscript
Summary:        PHP/Mapscript map making extensions to PHP
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}-%{release}
Requires:       apache2
Provides:       php-mapserver = %{version}-%{release}
Obsoletes:      php-mapserver < %{version}-%{release}
BuildRequires:  php-devel
Requires:       php
Requires:       php-gd

%description -n php-mapscript
The PHP/Mapscript extension provides full map customization capabilities within the PHP scripting language.

%package -n perl-mapscript
Summary:        Perl/Mapscript map making extensions to Perl
Group:          Development/Languages/Perl
BuildRequires:  perl-base
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       %{libname} = %{version}-%{release}
Requires:       perl-base
Provides:       mapserver-perl = %{version}-%{release}
Obsoletes:      mapserver-perl < %{version}-%{release}

%description -n perl-mapscript
The Perl/Mapscript extension provides full map customization capabilities
within the Perl programming language.

%if %{with python}
%package -n python-mapscript
Summary:        Python/Mapscript map making extensions to Python
Group:          Development/Languages/Python
%if %{suse_version} >= 1500
%define python_sitearch %(python3 -c "from distutils.sysconfig import get_python_lib; print (get_python_lib(1))")
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-base
%else
%define python_sitearch %(python2 -c "from distutils.sysconfig import get_python_lib; print (get_python_lib(1))")
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-base
%endif
Requires:       %{libname} = %{version}-%{release}
Provides:       mapserver-python = %{version}-%{release}
Obsoletes:      mapserver-python < %{version}-%{release}

%description -n python-mapscript
The Python/Mapscript extension provides full map customization capabilities
within the Python programming language.
%endif

%package -n libjavamapscript
Summary:        Java/Mapscript map making extensions to Java
Group:          Development/Languages/Java
BuildRequires:  java >= 1.6
BuildRequires:  java-devel >= 1.6
BuildRequires:  swig
Requires:       %{libname} = %{version}-%{release}
Requires:       java >= 1.6
Requires:       swig
Provides:       java-mapscript = %{version}-%{release}
Provides:       mapserver-java = %{version}-%{release}
Obsoletes:      java-mapscript < %{version}-%{release}
Obsoletes:      mapserver-java < %{version}-%{release}

%description -n libjavamapscript
The Java/Mapscript extension provides full map customization capabilities
within the Java programming language.

%if %{with ruby}
%package -n ruby-mapscript
Summary:        Ruby/Mapscript map making extensions to Ruby
Group:          Development/Languages/Ruby
BuildRequires:  ruby-common
BuildRequires:  ruby-devel
Requires:       %{libname} = %{version}-%{release}
Requires:       ruby
Provides:       mapserver-ruby = %{version}-%{release}
Obsoletes:      mapserver-ruby < %{version}-%{release}

%description -n ruby-mapscript
The Ruby/Mapscript extension provides full map customization capabilities
within the Ruby programming language.
%endif

%package        devel
Summary:        Mapserver development files
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The Mapserver development package provides necessary files to build
against the C Mapserver library.

%prep
%setup -q -n %{name}-%{version}
%global _default_patch_fuzz 5
%patch0 -p0

%build
mkdir build
cd build
#Pre export the PREFIX ( having it on the command line doesn't expand correctly for
#dynamic postgresql location
export CMAKE_PREFIX_PATH="%{_includedir}:%{_includedir}/fastcgi:%%(pg_config --includedir):%%(pg_config --includedir-server):%%(pg_config --libdir)"
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -fno-strict-aliasing"

#specify all options and play with true/false
#so we always know which option are included in our build.
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_SKIP_RPATH=ON \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DINSTALL_LIB_DIR=%{_libdir} \
        -DCMAKE_C_FLAGS_RELEASE="%{optflags} -fno-strict-aliasing" \
        -DCMAKE_CXX_FLAGS_RELEASE="%{optflags} -fno-strict-aliasing" \
        -DCMAKE_VERBOSE_MAKEFILE=ON \
        -DCMAKE_BUILD_TYPE="Release" \
        -DCMAKE_SKIP_INSTALL_RPATH=ON \
        -DCMAKE_SKIP_RPATH=ON \
        -DWITH_CAIRO=TRUE \
        -DWITH_CLIENT_WFS=TRUE \
        -DWITH_CLIENT_WMS=TRUE \
        -DWITH_CURL=TRUE \
        -DWITH_FCGI=TRUE \
        -DWITH_FRIBIDI=TRUE \
        -DWITH_GD=TRUE \
        -DWITH_GDAL=TRUE \
        -DWITH_GEOS=TRUE \
        -DWITH_GIF=TRUE \
        -DWITH_ICONV=TRUE \
        -DWITH_JAVA=TRUE \
        -DWITH_KML=TRUE \
        -DWITH_LIBXML2=TRUE \
        -DWITH_OGR=TRUE \
        -DWITH_MYSQL=TRUE \
        -DWITH_PERL=TRUE \
        -DCUSTOM_PERL_SITE_ARCH_DIR="%{perl_vendorarch}" \
        -DWITH_PHP=TRUE \
        -DWITH_POSTGIS=TRUE \
        -DWITH_PROJ=TRUE \
        -DUSE_PROJ=TRUE \
        -DWITH_PROTOBUFC=TRUE \
%if %{with python}
        -DWITH_PYTHON=TRUE \
%endif
%if %{with ruby}
        -DWITH_RUBY=TRUE \
%endif
        -DWITH_SOS=TRUE \
        -DWITH_THREAD_SAFETY=TRUE \
        -DWITH_WCS=TRUE \
        -DWITH_WMS=TRUE \
        -DWITH_WFS=TRUE \
        -DWITH_XMLMAPFILE=TRUE \
        -DWITH_POINT_Z_M=TRUE \
        -DWITH_APACHE_MODULE=FALSE \
        -DWITH_SVGCAIRO=FALSE \
        -DWITH_MYSQL=FALSE \
        -DWITH_CSHARP=FALSE \
        -DWITH_ORACLESPATIAL=FALSE \
        -DWITH_ORACLE_PLUGIN=FALSE \
        -DWITH_MSSQL2008=FALSE \
        -DWITH_SDE=FALSE \
        -DWITH_SDE_PLUGIN=FALSE \
        -DWITH_EXEMPI=FALSE \
        -Wno-dev \
        ..

%make_build

%check
# make test

%install
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{_cgibindir}
mkdir -p %{buildroot}%{_libdir}/%{php_name}/extensions
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}%{python_sitearch}/
mkdir -p %{buildroot}/%{_includedir}/%{name}
#Comment this look a bit wired to be useful sub-dir should also needed
# agg, etc 
cp *.h %{buildroot}/%{_includedir}/%{name}/

# fix some exec bits essentially on examples to make rpmlint happy
# and avoid rpm adding require
find ./mapscript/ -type f -iname "*.p[ly]" -exec chmod -x {} \;
find ./mapscript/ -type f -iname "*.rb" -exec chmod -x {} \;
find ./mapscript/ -type f -iname "*.dist" -exec chmod -x {} \;

cd build
%make_install
cd ..

mkdir -p %{buildroot}%{_sysconfdir}/%{php_name}/conf.d/
cat > %{buildroot}%{_sysconfdir}/%{php_name}/conf.d/mapscript.ini <<EOF
; Enable %{name} extension module
; For 6.4 we name the symlink here
extension=php_mapscript.so
EOF

# Install our links
#@ todo : check
# Having them as link is good for bytes, but httpd_daemon should allow
# reading those symlinks which is not the default
ln -s %{_bindir}/mapserv %{buildroot}%{_cgibindir}/mapserv
ln -s %{_bindir}/legend %{buildroot}%{_cgibindir}/legend
ln -s %{_bindir}/scalebar %{buildroot}%{_cgibindir}/scalebar

# remove vera fonts, these are provided system wide
#@todo then we should patch the fonts file example
rm -rf %{buildroot}%{_docdir}/%{name}/tests/vera
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}/tests/vera

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%doc README.rst HISTORY.TXT
%doc MIGRATION_GUIDE.txt
%doc symbols tests
%doc fonts
%{_bindir}/shp2img
%{_bindir}/shptree
%{_bindir}/sortshp
%{_bindir}/tile4ms
%{_bindir}/mapserv
%{_bindir}/legend
%{_bindir}/scalebar
%{_bindir}/msencrypt
%{_bindir}/shptreetst
%{_bindir}/shptreevis
%{_cgibindir}/mapserv
%{_cgibindir}/legend
%{_cgibindir}/scalebar

%files -n %{libname}
%{_libdir}/libmapserver.so.*

%files -n php-mapscript
%doc mapscript/php/README
%doc mapscript/php/examples
%config(noreplace) %{_sysconfdir}/%{php_name}/conf.d/mapscript.ini
%{_libdir}/%{php_name}/extensions/php_mapscript.so*

%files -n perl-mapscript
%doc mapscript/perl/examples
%dir %{perl_vendorarch}/auto/mapscript
%{perl_vendorarch}/auto/mapscript/*
%{perl_vendorarch}/mapscript.pm

%if %{with python}
%files -n python-mapscript
%doc mapscript/python/README.rst
%doc mapscript/python/examples
%doc mapscript/python/tests
%{python_sitearch}/*
%endif

%files -n libjavamapscript
%doc mapscript/java/README
%doc mapscript/java/examples
%doc mapscript/java/tests
%{_libdir}/libjavamapscript.so

%if %{with ruby}
%files -n ruby-mapscript
%doc mapscript/ruby/README
%doc mapscript/ruby/examples
%{rb_sitearchdir}/mapscript.so
%endif

%files devel
%dir %{_includedir}/mapserver
%{_includedir}/mapserver/*
%{_libdir}/libmapserver.so
%{_datadir}/mapserver

%changelog
