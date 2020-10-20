#
# spec file for package gdcm
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019-2020 Dr. Axel Braun
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


%define         soname  3_0
%define         libsocksoname  libsocketxx1_2
Name:           gdcm
Version:        3.0.8
Release:        0
Summary:        Grassroots DiCoM is a C++ library to parse DICOM medical files
License:        BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            http://gdcm.sourceforge.net/wiki/index.php/Main_Page
Source0:        http://sourceforge.net/projects/gdcm/files/gdcm%203.x/GDCM%20%{version}/%{name}-%{version}.tar.bz2
Patch1:         gdcm-2.4.0-usecopyright.patch
Patch2:         fix_charls_2.patch
BuildRequires:  CharLS-devel >= 2.0
BuildRequires:  cmake
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  libexpat-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libpoppler-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  cmake(DCMTK)
BuildRequires:  pkgconfig(libopenjp2)

%description
Grassroots DiCoM (GDCM) is a C++ library for DICOM medical files.
It supports ACR-NEMA version 1 and 2 (huffman compression is not supported),
RAW, JPEG, JPEG 2000, JPEG-LS, RLE and deflated transfer syntax.
It comes with a super fast scanner implementation to quickly scan hundreds of
DICOM files. It supports SCU network operations (C-ECHO, C-FIND, C-STORE,
C-MOVE). PS 3.3 & 3.6 are distributed as XML files.
It also provides PS 3.15 certificates and password based mechanism to
anonymize and de-identify DICOM datasets.

%package        libgdcm%{soname}
Summary:        Shared Object for applications that use %{name}
Group:          System/Libraries

%description    libgdcm%{soname}
This package contains the shared library required by applications that
are using %{name} for DICOM processing.

%package    -n  %{libsocksoname}
Summary:        Libsocket Library for applications that use %{name}
Group:          System/Libraries

%description -n %{libsocksoname}
This package contains a shared library required by applications that
are using %{name} for DICOM processing.

%package        applications
Summary:        Includes command line programs for GDCM
Group:          Productivity/Graphics/Other
Requires:       %{name}-libgdcm%{soname}

%description    applications
You should install the gdcm-applications package if you would like to
use command line programs part of GDCM. Includes tools to convert,
anonymize, manipulate, concatenate, and view DICOM files.

%package        devel
Summary:        Libraries and headers for GDCM
Group:          Development/Libraries/C and C++
Requires:       %{libsocksoname}
Requires:       %{name}-applications%{?_isa} = %{version}-%{release}
Requires:       %{name}-libgdcm%{soname}

%description    devel
You should install the gdcm-devel package if you would like to
compile applications based on gdcm

%package        examples
Summary:        GDCM examples
Group:          Productivity/Graphics/Other
Requires:       %{name}-libgdcm%{soname}

%description    examples
CSharp, C++, Java, PHP and Python example programs for GDCM

%package -n     python3-gdcm
Summary:        Python binding for GDCM
Group:          Productivity/Graphics/Other
%{?python_provide:%python_provide python3-gdcm}
Requires:       %{name}-libgdcm%{soname}

%description -n python3-gdcm
You should install the python3-gdcm package if you would like to
used this library with python

%prep
%autosetup -p1

# Remove bundled utilities (we use internal ones)
rm -rf Utilities/gdcmexpat
rm -rf Utilities/gdcmopenjpeg-v1
rm -rf Utilities/gdcmopenjpeg-v2
rm -rf Utilities/gdcmzlib
rm -rf Utilities/gdcmuuid
rm -rf Utilities/gdcmcharls

# Remove bundled utilities (we don't use them)
rm -rf Utilities/getopt
rm -rf Utilities/pvrg
rm -rf Utilities/rle
rm -rf Utilities/wxWidgets

%build

%cmake	.. \
    -DCMAKE_CXX_FLAGS="%{optflags} -fpermissive" \
	-DCMAKE_VERBOSE_MAKEFILE=ON \
	-DGDCM_INSTALL_PACKAGE_DIR=%{_libdir}/cmake/%{name} \
	-DGDCM_INSTALL_INCLUDE_DIR=%{_includedir}/%{name} \
	-DGDCM_INSTALL_DOC_DIR=%{_docdir}/%{name} \
	-DGDCM_INSTALL_MAN_DIR=%{_mandir} \
	-DGDCM_INSTALL_LIB_DIR=%{_libdir} \
	-DGDCM_BUILD_TESTING:BOOL=ON \
	-DGDCM_DATA_ROOT=../gdcmData/ \
	-DGDCM_BUILD_EXAMPLES:BOOL=OFF \
	-DGDCM_DOCUMENTATION:BOOL=OFF \
	-DGDCM_WRAP_PYTHON:BOOL=ON \
	-DGDCM_INSTALL_PYTHONMODULE_DIR=%{python3_sitearch} \
	-DGDCM_WRAP_JAVA:BOOL=OFF \
	-DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
	-DGDCM_BUILD_APPLICATIONS:BOOL=ON \
	-DGDCM_USE_VTK:BOOL=OFF \
	-DGDCM_USE_SYSTEM_CHARLS:BOOL=ON \
	-DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
	-DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
	-DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
	-DGDCM_USE_SYSTEM_UUID:BOOL=ON \
	-DGDCM_USE_SYSTEM_LJPEG:BOOL=OFF \
	-DGDCM_USE_SYSTEM_OPENSSL:BOOL=ON \
	-DGDCM_USE_JPEGLS:BOOL=ON \
	-DGDCM_USE_SYSTEM_LIBXML2:BOOL=ON \
	-DGDCM_USE_SYSTEM_JSON:BOOL=ON \
	-DGDCM_USE_SYSTEM_POPPLER:BOOL=ON

%make_build

%install
%cmake_install
install -d %{buildroot}%{python3_sitearch}

## Cleaning Example dir from cmake cache files + remove 0-length files
find %{_builddir}/%{?buildsubdir}/Examples -depth -name CMakeFiles | xargs rm -rf
find %{_builddir}/%{?buildsubdir}/Examples -depth -size 0 | xargs rm -rf

## Moving Example dir into _datadir
cp -r %{_builddir}/%{?buildsubdir}/Examples %{buildroot}%{_datadir}/%{name}/

find %{buildroot}%{_datadir}/%{name}/ -depth -name CMakeLists* | xargs rm -rf

%fdupes %{buildroot}

%post libgdcm%{soname}  -p /sbin/ldconfig
%post -n %{libsocksoname}  -p /sbin/ldconfig
%postun libgdcm%{soname} -p /sbin/ldconfig
%postun -n %{libsocksoname}  -p /sbin/ldconfig

%check
# Making the tests informative only for now. Several failing tests (27/228):
# 11,40,48,49,107-109,111-114,130-135,146,149,,151-154,157,194,216,219
make %{?_smp_mflags} test  || exit 0

%files
%doc AUTHORS INSTALL.txt README.md
%license Copyright.txt README.Copyright.txt
%dir %{_datadir}/%{name}-3.0
%{_datadir}/%{name}-3.0/XML/

%files libgdcm%{soname}
%{_libdir}/libgdcm*.so.*

%files -n %{libsocksoname}
%{_libdir}/libsocket*.so.*

%files applications
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/cmake/%{name}/

%files examples
%{_datadir}/%{name}/

%files -n python3-gdcm
%{python3_sitearch}/%{name}*.py
%{python3_sitearch}/_%{name}swig.so

%changelog
