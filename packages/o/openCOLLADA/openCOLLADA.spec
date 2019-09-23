#
# spec file for package openCOLLADA
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global sover 0.3
%global sfx 0_3
#3335ac164e68b2512a40914b14c74db260e6ff7d
#3335ac1
%global upname OpenCOLLADA
%global libname libopenCOLLADA
Name:           openCOLLADA
Version:        1.6.63
Release:        0
#1_%%{shortcommit}
Summary:        Collada 3D import and export libraries
#https://github.com/KhronosGroup/OpenCOLLADA/archive/v1.6.43.tar.gz
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://collada.org/mediawiki/index.php/OpenCOLLADA
## https://github.com/KhronosGroup/OpenCOLLADA/archive/%%{commit}/
Source0:        https://github.com/KhronosGroup/%{upname}/archive/v%{version}.tar.gz#/%{upname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM use proper paths in cmake for install
Patch0:         opencollada-cmake.patch
# PATCH-FIX-UPSTREAM add missing includes
Patch1:         opencollada-includes.patch
# PATCH-FIX-UPSTREAM link to required libraries
# fixed in 1.6.51 Patch2:         opencollada-no-undefined.patch
# PATCH-FIX-UPSTREAM openCOLLADA-signed-char.patch gh#KhronosGroup/OpenCOLLADA#439 dimstar@opensuse.org -- Use signed char; 'char' by itself depends on arch implementation
#included         openCOLLADA-signed-char.patch
# PATCH-FIX-OPENSUSE openCOLLADA-no-daevalidator.patch davejplater@gmail.com - Don't build DAEvalidator app.
Patch4:         openCOLLADA-no-daevalidator.patch
Patch5:         openCOLLADA-pcre-redefined.patch
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpcrecpp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)

%description
COLLADA is an XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender:
* COLLADABaseUtils - Utils used by many of the other projects
* COLLADAFramework - Datamodel used to load COLLADA files
* COLLADAStreamWriter - Sources (Library to write COLLADA files)
* COLLADASaxFrameworkLoader - Library that loads COLLADA files in a
  SAX-like manner into the framework data model
* COLLADAValidator - XML validator for COLLADA files, based on
  the COLLADASaxFrameworkLoader
* GeneratedSaxParser - Library used to load xml files in the way
  used by COLLADASaxFrameworkLoader

%package -n libftoa%{sfx}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries

%description -n libftoa%{sfx}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

%package -n libbuffer%{sfx}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries

%description -n libbuffer%{sfx}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

%package -n libGeneratedSaxParser%{sfx}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries

%description -n libGeneratedSaxParser%{sfx}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

GeneratedSaxParser is the library used to load xml files in the way
used by COLLADASaxFrameworkLoader.

%package -n libMathMLSolver%{sfx}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries

%description -n libMathMLSolver%{sfx}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

%package -n libOpenCOLLADABaseUtils%{sfx}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries

%description -n libOpenCOLLADABaseUtils%{sfx}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

COLLADABaseUtils is the package of utilitie used by many of the other
projects.

%package -n libOpenCOLLADAFramework%{sfx}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries

%description -n libOpenCOLLADAFramework%{sfx}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

COLLADAFramework is the datamodel used to load COLLADA files.

%package -n libOpenCOLLADASaxFrameworkLoader%{sfx}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries

%description -n libOpenCOLLADASaxFrameworkLoader%{sfx}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

COLLADASaxFrameworkLoader is a library that loads COLLADA files in a
SAX-like manner into the data framework model and is used by
COLLADASaxFrameworkLoader.

%package -n libOpenCOLLADAStreamWriter%{sfx}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries

%description -n libOpenCOLLADAStreamWriter%{sfx}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

COLLADAStreamWriter contains the library to write COLLADA files.

%package -n libUTF%{sfx}
Summary:        Collada 3D import and export libraries
Group:          System/Libraries

%description -n libUTF%{sfx}
COLLADA is a XML schema that enables digital asset exchange within
the interactive 3D industry. OpenCOLLADA is a project providing
libraries for 3D file interchange between applications like Blender.

%package     -n %{libname}-doc
Summary:        Developer documentation for %{name}
Group:          Documentation/HTML
Provides:       %{name}-doc > 1_3335ac1
Obsoletes:      %{name}-doc <= 1_3335ac1
BuildArch:      noarch

%description -n %{libname}-doc
This package provides documentation for %{name}.

%package        -n %{libname}-devel
Summary:        Include files for openCOLLADA development
Group:          Development/Libraries/C and C++
Requires:       libGeneratedSaxParser%{sfx} = %{version}
Requires:       libMathMLSolver%{sfx} = %{version}
Requires:       libOpenCOLLADABaseUtils%{sfx} = %{version}
Requires:       libOpenCOLLADAFramework%{sfx} = %{version}
Requires:       libOpenCOLLADASaxFrameworkLoader%{sfx} = %{version}
Requires:       libOpenCOLLADAStreamWriter%{sfx} = %{version}
Requires:       libUTF%{sfx} = %{version}
Requires:       libbuffer%{sfx} = %{version}
Requires:       libftoa%{sfx} = %{version}
Provides:       %{name}-devel > 1_3335ac1
Obsoletes:      %{name}-devel <= 1_3335ac1
Recommends:     %{libname}-doc = %{version}

%description -n %{libname}-devel
This package provides the include files necessary to build and
develop with the %{name} export and import libraries.

%package        -n %{libname}-utils
Summary:        XML validator for COLLADA files
Group:          Development/Tools
Provides:       %{name}-utils > 1_3335ac1
Obsoletes:      %{name}-utils <= 1_3335ac1

%description -n %{libname}-utils
XML validator for COLLADA files, based on the COLLADASaxFrameworkLoader.

%prep
%setup -q -n %{upname}-%{version}
%patch0 -p0 -b .cmake
%patch1 -p0 -b .includes
%patch4
%patch5

# Remove unused bundled libraries
rm -rf Externals/{Cg,expat,lib3ds,LibXML,MayaDataModel,pcre,zlib,zziplib}

# Add some docs, need to fix eol encoding with dos2unix in some files.
find ./ -name .project -delete
cp -pf COLLADAStreamWriter/README README.COLLADAStreamWriter
cp -pf COLLADAStreamWriter/LICENSE ./

iconv -f ISO_8859-1 -t utf-8 COLLADAStreamWriter/AUTHORS > \
  COLLADAStreamWriter/AUTHORS.tmp
touch -r COLLADAStreamWriter/AUTHORS COLLADAStreamWriter/AUTHORS.tmp
mv COLLADAStreamWriter/AUTHORS.tmp COLLADAStreamWriter/AUTHORS

dos2unix -f -k README.COLLADAStreamWriter
dos2unix -f -k LICENSE
dos2unix -f -k README
find htdocs/ -name *.php -exec dos2unix -f {} \;
find htdocs/ -name *.css -exec dos2unix -f {} \;

%build
%cmake \
       -DUSE_STATIC=OFF \
       -DUSE_SHARED=ON \
       -Dsoversion=%{sover}

make %{?_smp_mflags}

%install
%cmake_install

# Manually install binary
mkdir -p %{buildroot}%{_bindir}/
install -p -m 0755 build/bin/* %{buildroot}%{_bindir}/

# Install MathMLSolver headers
mkdir -p %{buildroot}%{_includedir}/MathMLSolver
cp -a Externals/MathMLSolver/include/* %{buildroot}%{_includedir}/MathMLSolver/

%post -n libbuffer%{sfx} -p /sbin/ldconfig
%postun -n libbuffer%{sfx} -p /sbin/ldconfig

%post -n libftoa%{sfx} -p /sbin/ldconfig
%postun -n libftoa%{sfx} -p /sbin/ldconfig

%post -n libGeneratedSaxParser%{sfx} -p /sbin/ldconfig
%postun -n libGeneratedSaxParser%{sfx} -p /sbin/ldconfig

%post -n libMathMLSolver%{sfx} -p /sbin/ldconfig
%postun -n libMathMLSolver%{sfx} -p /sbin/ldconfig

%post -n libOpenCOLLADABaseUtils%{sfx} -p /sbin/ldconfig
%postun -n libOpenCOLLADABaseUtils%{sfx} -p /sbin/ldconfig

%post -n libOpenCOLLADAFramework%{sfx} -p /sbin/ldconfig
%postun -n libOpenCOLLADAFramework%{sfx} -p /sbin/ldconfig

%post -n libOpenCOLLADASaxFrameworkLoader%{sfx} -p /sbin/ldconfig
%postun -n libOpenCOLLADASaxFrameworkLoader%{sfx} -p /sbin/ldconfig

%post -n libOpenCOLLADAStreamWriter%{sfx} -p /sbin/ldconfig
%postun -n libOpenCOLLADAStreamWriter%{sfx} -p /sbin/ldconfig

%post -n libUTF%{sfx} -p /sbin/ldconfig
%postun -n libUTF%{sfx} -p /sbin/ldconfig

%files -n libbuffer%{sfx}
%defattr(-,root,root)
%{_libdir}/libbuffer.so.%{sover}

%files -n libftoa%{sfx}
%defattr(-,root,root)
%{_libdir}/libftoa.so.%{sover}

%files -n libGeneratedSaxParser%{sfx}
%defattr(-,root,root)
%{_libdir}/libGeneratedSaxParser.so.%{sover}

%files -n libMathMLSolver%{sfx}
%defattr(-,root,root)
%{_libdir}/libMathMLSolver.so.%{sover}

%files -n libOpenCOLLADABaseUtils%{sfx}
%defattr(-,root,root)
%{_libdir}/libOpenCOLLADABaseUtils.so.%{sover}

%files -n libOpenCOLLADAFramework%{sfx}
%defattr(-,root,root)
%{_libdir}/libOpenCOLLADAFramework.so.%{sover}

%files -n libOpenCOLLADASaxFrameworkLoader%{sfx}
%defattr(-,root,root)
%{_libdir}/libOpenCOLLADASaxFrameworkLoader.so.%{sover}

%files -n libOpenCOLLADAStreamWriter%{sfx}
%defattr(-,root,root)
%{_libdir}/libOpenCOLLADAStreamWriter.so.%{sover}

%files -n libUTF%{sfx}
%defattr(-,root,root)
%{_libdir}/libUTF.so.%{sover}

%files -n %{libname}-doc
%defattr(-,root,root)
%doc htdocs/

%files  -n %{libname}-devel
%defattr(-,root,root)
%doc README LICENSE README.COLLADAStreamWriter COLLADAStreamWriter/AUTHORS
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_includedir}/*

%files -n %{libname}-utils
%defattr(-,root,root)
%{_bindir}/*

%changelog
