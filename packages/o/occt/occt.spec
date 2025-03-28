#
# spec file for package occt
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


%if 0%{?suse_version} > 1600
%bcond_without docs
%else
%bcond_with    docs
%endif

%define OCCT_TAG 7_8_1

Name:           occt
Version:        7.8.1
Release:        0
%define soname 7_8_1
%define sover  7.8.1
%define sover_len 3
Summary:        OpenCASCADE Official Edition
License:        LGPL-2.1-only WITH OCCT-exception-1.0
Group:          Productivity/Graphics/CAD
URL:            https://www.opencascade.com/open-cascade-technology/
Source0:        https://github.com/Open-Cascade-SAS/OCCT/archive/refs/tags/V%{OCCT_TAG}.tar.gz#/occt-%{version}.tar.gz
Patch0:         https://github.com/Open-Cascade-SAS/OCCT/commit/7236e83dcc1e7284e66dc61e612154617ef715d6.patch#/fix_freetype_tag_type.patch
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
%if %{with docs}
BuildRequires:  doxygen
BuildRequires:  mathjax
%endif

%description
OpenCASCADE is a suite for 3D surface and solid modeling, visualization, data
exchange and rapid application development. It is an excellent platform for
development of numerical simulation software including CAD/CAM/CAE, AEC and
GIS, as well as PDM applications.

%package resources
Summary:        Binary resource files for %{name}
Group:          System/Libraries
BuildArch:      noarch

%description resources
This package contains resource files imported from the libraries.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Provides:       OpenCASCADE-devel = %{version}
Requires:       libopencascade-applicationframework%{soname} = %{version}
Requires:       libopencascade-dataexchange%{soname} = %{version}
Requires:       libopencascade-draw%{soname} = %{version}
Requires:       libopencascade-foundationclasses%{soname} = %{version}
Requires:       libopencascade-modelingalgorithms%{soname} = %{version}
Requires:       libopencascade-modelingdata%{soname} = %{version}
Requires:       libopencascade-visualization%{soname} = %{version}
Requires:       tcl-devel
Requires:       tk-devel
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xmu)
Conflicts:      oce-devel

%description devel
This package contains the files needed for development with OpenCASCADE.

%package devel-doc
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description devel-doc
Developer documentation for OpenCASCADE

%package -n libopencascade-applicationframework%{soname}
Summary:        OpenCASCADE application framework libraries
Group:          System/Libraries

%description -n libopencascade-applicationframework%{soname}
This package contains the OpenCASCADE libraries from the
OpenCASCADE application framework module:
  TKCDF TKLCAF TKCAF TKBinL TKXmlL TKBin TKXml TKStdL
  TKStd TKTObj TKBinTObj TKXmlTObj

%package -n libopencascade-dataexchange%{soname}
Summary:        OpenCASCADE data exchange libraries
Group:          System/Libraries

%description -n libopencascade-dataexchange%{soname}
This package contains the OpenCASCADE libraries from the
OpenCASCADE data exchange module:
  TKVCAF TKXSBase TKSTEPBase TKSTEPAttr TKSTEP209 TKSTEP
  TKIGES TKXCAF TKXDEIGES TKXDESTEP TKSTL TKVRML TKXmlXCAF
  TKBinXCAF TKRWMesh

%package -n libopencascade-draw%{soname}
Summary:        OpenCASCADE Draw support libraries
Group:          System/Libraries
Requires:       %{name}-resources

%description -n libopencascade-draw%{soname}
This package contains support libraries for the
OpenCASCADE DRAWEXE test harness.

%package -n libopencascade-foundationclasses%{soname}
Summary:        OpenCASCADE foundation classes libraries
Group:          System/Libraries

%description -n libopencascade-foundationclasses%{soname}
This package contains the OpenCASCADE libraries from the
OpenCASCADE foundation classes module:
  TKernel TKMath

%package -n libopencascade-modelingalgorithms%{soname}
Summary:        OpenCASCADE modeling algorithms libraries
Group:          System/Libraries

%description -n libopencascade-modelingalgorithms%{soname}
This package contains the OpenCASCADE libraries from the
OpenCASCADE modeling module:
  TKGeomAlgo TKTopAlgo TKPrim TKBO TKShHealing TKBool
  TKHLR TKFillet TKOffset TKFeat TKMesh TKXMesh

%package -n libopencascade-modelingdata%{soname}
Summary:        OpenCASCADE modeling data libraries
Group:          System/Libraries

%description -n libopencascade-modelingdata%{soname}
This package contains the OpenCASCADE libraries from the
OpenCASCADE modeling module:
  TKG2d TKG3d TKGeomBase TKBRep

%package -n libopencascade-visualization%{soname}
Summary:        OpenCASCADE visualization libraries
Group:          System/Libraries

%description -n libopencascade-visualization%{soname}
This package contains the OpenCASCADE libraries from the
OpenCASCADE visualization module:
  TKService TKV3D TKOpenGL TKMeshVS

%package DRAWEXE
Summary:        Development files for %{name}
Group:          Productivity/Graphics/CAD
Conflicts:      oce-DRAWEXE

%description DRAWEXE
This package contains the OpenCASCADE DRAWEXE test
harness executable.

%prep
%autosetup -p1 -n OCCT-%{OCCT_TAG}

%build
%cmake \
  -DCMAKE_POLICY_DEFAULT_CMP0083=NEW \
  -DBUILD_RELEASE_DISABLE_EXCEPTIONS:BOOL=false \
  -DUSE_RAPIDJSON:BOOL=true \
  -DINSTALL_DIR_LIB=%{_lib} \
  -DINSTALL_DIR_CMAKE=%{_lib}/cmake/opencascade \
  -DBUILD_SOVERSION_NUMBERS=%{sover_len} \
  ..
%cmake_build

%if %{with docs}
cd ..
./gendoc -refman -html -mathjax="%{_datadir}/javascript/mathjax"
%endif

%install
%cmake_install

# Make scripts executable
chmod 0755 %buildroot/usr/bin/*

# fixing up broken files
sed -i -e 's,'%{_lib}'\\${OCCT_INSTALL_BIN_LETTER}/,'%{_lib}'/,' %{buildroot}%{_libdir}/cmake/opencascade/*
sed -i -e 's,/lib\$,/'%{_lib}'\$,' %{buildroot}%{_libdir}/cmake/opencascade/*
grep -C5 -E "BIN_LETTER|/lib" %{buildroot}%{_libdir}/cmake/opencascade/*

rm -rf %buildroot/usr/share/doc

%fdupes %{buildroot}%{_datadir}

%post -n libopencascade-applicationframework%{soname} -p /sbin/ldconfig
%postun -n libopencascade-applicationframework%{soname} -p /sbin/ldconfig
%post -n libopencascade-dataexchange%{soname} -p /sbin/ldconfig
%postun -n libopencascade-dataexchange%{soname} -p /sbin/ldconfig
%post -n libopencascade-draw%{soname} -p /sbin/ldconfig
%postun -n libopencascade-draw%{soname} -p /sbin/ldconfig
%post -n libopencascade-foundationclasses%{soname} -p /sbin/ldconfig
%postun -n libopencascade-foundationclasses%{soname} -p /sbin/ldconfig
%post -n libopencascade-modelingalgorithms%{soname} -p /sbin/ldconfig
%postun -n libopencascade-modelingalgorithms%{soname} -p /sbin/ldconfig
%post -n libopencascade-modelingdata%{soname} -p /sbin/ldconfig
%postun -n libopencascade-modelingdata%{soname} -p /sbin/ldconfig
%post -n libopencascade-visualization%{soname} -p /sbin/ldconfig
%postun -n libopencascade-visualization%{soname} -p /sbin/ldconfig

%files -n libopencascade-applicationframework%{soname}
%_libdir/libTKBin.so.%{sover}*
%_libdir/libTKBinL.so.%{sover}*
%_libdir/libTKBinTObj.so.%{sover}*
%_libdir/libTKCAF.so.%{sover}*
%_libdir/libTKCDF.so.%{sover}*
%_libdir/libTKLCAF.so.%{sover}*
%_libdir/libTKStd.so.%{sover}*
%_libdir/libTKStdL.so.%{sover}*
%_libdir/libTKTObj.so.%{sover}*
%_libdir/libTKVCAF.so.%{sover}*
%_libdir/libTKXml.so.%{sover}*
%_libdir/libTKXmlL.so.%{sover}*
%_libdir/libTKXmlTObj.so.%{sover}*

%files -n libopencascade-dataexchange%{soname}
%_libdir/libTKBinXCAF.so.%{sover}*
%_libdir/libTKExpress.so.%{sover}*
%_libdir/libTKRWMesh.so.%{sover}*
%_libdir/libTKXCAF.so.%{sover}*
%_libdir/libTKDE.so.%{sover}*
%_libdir/libTKDECascade.so.%{sover}*
%_libdir/libTKDEGLTF.so.%{sover}*
%_libdir/libTKDEIGES.so.%{sover}*
%_libdir/libTKDEOBJ.so.%{sover}*
%_libdir/libTKDEPLY.so.%{sover}*
%_libdir/libTKDESTEP.so.%{sover}*
%_libdir/libTKDESTL.so.%{sover}*
%_libdir/libTKDEVRML.so.%{sover}*
%_libdir/libTKXSBase.so.%{sover}*
%_libdir/libTKXmlXCAF.so.%{sover}*

%files -n libopencascade-foundationclasses%{soname}
%license LICENSE_LGPL_21.txt OCCT_LGPL_EXCEPTION.txt
%_libdir/libTKernel.so.%{sover}*
%_libdir/libTKMath.so.%{sover}*

%files -n libopencascade-draw%{soname}
%_libdir/libTKDCAF.so.%{sover}*
%_libdir/libTKDraw.so.%{sover}*
%_libdir/libTKQADraw.so.%{sover}*
%_libdir/libTKTObjDRAW.so.%{sover}*
%_libdir/libTKXDEDRAW.so.%{sover}*
%_libdir/libTKXSDRAW.so.%{sover}*
%_libdir/libTKXSDRAWDE.so.%{sover}*
%_libdir/libTKXSDRAWGLTF.so.%{sover}*
%_libdir/libTKXSDRAWIGES.so.%{sover}*
%_libdir/libTKXSDRAWOBJ.so.%{sover}*
%_libdir/libTKXSDRAWPLY.so.%{sover}*
%_libdir/libTKXSDRAWSTEP.so.%{sover}*
%_libdir/libTKXSDRAWSTL.so.%{sover}*
%_libdir/libTKXSDRAWVRML.so.%{sover}*
%_libdir/libTK*Test.so.%{sover}*

%files -n libopencascade-modelingalgorithms%{soname}
%_libdir/libTKBO.so.%{sover}*
%_libdir/libTKBool.so.%{sover}*
%_libdir/libTKFeat.so.%{sover}*
%_libdir/libTKFillet.so.%{sover}*
%_libdir/libTKGeomAlgo.so.%{sover}*
%_libdir/libTKHLR.so.%{sover}*
%_libdir/libTKMesh.so.%{sover}*
%_libdir/libTKOffset.so.%{sover}*
%_libdir/libTKPrim.so.%{sover}*
%_libdir/libTKShHealing.so.%{sover}*
%_libdir/libTKTopAlgo.so.%{sover}*
%_libdir/libTKXMesh.so.%{sover}*

%files -n libopencascade-modelingdata%{soname}
%_libdir/libTKG2d.so.%{sover}*
%_libdir/libTKG3d.so.%{sover}*
%_libdir/libTKGeomBase.so.%{sover}*
%_libdir/libTKBRep.so.%{sover}*

%files -n libopencascade-visualization%{soname}
%_libdir/libTKMeshVS.so.%{sover}*
%_libdir/libTKOpenGl.so.%{sover}*
%_libdir/libTKService.so.%{sover}*
%_libdir/libTKV3d.so.%{sover}*

%files resources
%dir %{_datadir}/opencascade
%{_datadir}/opencascade/resources

%files DRAWEXE
%{_bindir}/custom*
%{_bindir}/draw.sh
%{_bindir}/env.sh
%{_bindir}/DRAWEXE*
%{_datadir}/opencascade/samples
%{_datadir}/opencascade/data

%files devel
%doc README.txt
%{_includedir}/opencascade
%dir %{_libdir}/cmake
%{_libdir}/cmake/opencascade
%{_libdir}/lib*.so
%{_bindir}/ExpToCasExe*

%if %{with docs}
%files devel-doc
%doc doc/refman/html
%endif

%changelog
