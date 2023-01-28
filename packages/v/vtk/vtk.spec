#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}

%bcond_with examples
%bcond_with documentation
%bcond_with testing

%ifarch %arm aarch64
%bcond_without gles
%else
%bcond_with    gles
%endif

%define pkgname vtk

# pugixml in Leap 15.x is too old
# fmt in Leap 15.x is too old
# Need haru/hpdf version with HPDF_SHADING, i.e. >= 2.4.0
%if 0%{?suse_version} <= 1500
%bcond_with    fmt
%bcond_with    haru
%bcond_with    pugixml
%else
%bcond_without fmt
%bcond_without haru
%bcond_without pugixml
%endif

%bcond_without gl2ps
%bcond_without java
%bcond_without pegtl

%if "%{flavor}" == ""
%define my_suffix %{nil}
%define my_prefix %_prefix
%define my_bindir %_bindir
%define my_libdir %_libdir
%define my_incdir %_includedir
%define my_datadir %_datadir
%endif

%if "%{flavor}" == "openmpi2"
%define my_suffix  -openmpi2
%define mpi_flavor  openmpi2
%define mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}
%endif

%if "%{flavor}" == "openmpi3"
%{?DisOMPI3}
%define my_suffix  -openmpi3
%define mpi_flavor  openmpi3
%define mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}
%endif

%if "%{flavor}" == "openmpi4"
%{?DisOMPI4}
%define my_suffix  -openmpi4
%define mpi_flavor  openmpi4
%define mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}
%endif

%{?mpi_flavor:%{bcond_without mpi}}%{!?mpi_flavor:%{bcond_with mpi}}

%if %{with mpi}
%define my_prefix %{mpiprefix}
%define my_bindir %{my_prefix}/bin
%define my_libdir %{my_prefix}/%{_lib}/
%define my_incdir %{my_prefix}/include/
%define my_datadir %{my_prefix}/share/
%endif

%define vtklib  lib%{pkgname}1%{?my_suffix}
%define shlib   %{vtklib}

Name:           vtk%{?my_suffix}
Version:        9.2.5
Release:        0
%define series  9.2
Summary:        The Visualization Toolkit - A high level 3D visualization library
# This is a variant BSD license, a cross between BSD and ZLIB.
# For all intents, it has the same rights and restrictions as BSD.
# http://fedoraproject.org/wiki/Licensing/BSD#VTKBSDVariant
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://vtk.org/
Source:         https://www.vtk.org/files/release/%{series}/VTK-%{version}.tar.gz
# FIXME See if packaging can be tweaked to accommodate python-vtk's devel files in a devel package later
# We need to use the compat conditionals here to avoid Factory's source validator from tripping up
Source99:       vtk-rpmlintrc
# PATCH-FIX-OPENSUSE bundled_libharu_add_missing_libm.patch stefan.bruens@rwth-aachen.de -- Add missing libm for linking (gh#libharu/libharu#213)
Patch1:         bundled_libharu_add_missing_libm.patch
# PATCH-FIX-OPENSUSE -- Fix building with Qt GLES builds
Patch7:         0001-Add-missing-guard-required-for-GLES-to-disable-stere.patch
# PATCH-FIX-UPSTREAM -- Fix building with Qt GLES builds
Patch8:         0001-Correct-GL_BACK-GL_BACK_LEFT-mapping-on-GLES.patch
# PATCH-FIX-UPSTREAM -- Fix building with Qt GLES builds
Patch9:         0002-Use-GL_DRAW_BUFFER0-instead-of-GL_DRAW_BUFFER-for-GL.patch
# PATCH-FIX-UPSTREAM
Patch10:        0001-GL_POINT_SPRITE-is-only-available-for-Compatibility-.patch
# PATCH-FIX-UPSTREAM -- Always create python package metadata (egg-info)
Patch17:        0001-Always-generate-Python-Metadata-when-WRAP_PYTHON-is-.patch
# PATCH-FIX-UPSTREAM -- Copy generated metadata to the right directory
Patch18:        0001-Consider-VTK_PYTHON_SITE_PACKAGES_SUFFIX-for-Python-.patch
BuildRequires:  cgns-devel
BuildRequires:  chrpath
BuildRequires:  cmake >= 3.12
BuildRequires:  double-conversion-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  libboost_graph-devel
BuildRequires:  libboost_graph_parallel-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libtiff-devel
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  python3-setuptools
BuildRequires:  utfcpp-devel
BuildRequires:  cmake(Verdict)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5OpenGLExtensions)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(eigen3) >= 3.3.9
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2) >= 2.11.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libiodbc)
BuildRequires:  pkgconfig(liblz4) >= 1.8.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(proj) >= 5.0.0
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
%if %{with documentation}
BuildRequires:  doxygen
BuildRequires:  gnuplot
BuildRequires:  graphviz
%endif
%if %{with fmt}
BuildRequires:  fmt-devel > 9.0
%endif
%if %{with gl2ps}
BuildRequires:  gl2ps-devel > 1.4.0
%endif
%if %{with haru}
BuildRequires:  libharu-devel >= 2.4.0
%endif
%if %{with java}
BuildRequires:  java-devel
%endif
%if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
BuildRequires:  hdf5-%{mpi_flavor}-devel
BuildRequires:  libboost_mpi-devel
BuildRequires:  netcdf-%{mpi_flavor}-devel
BuildRequires:  python3-mpi4py-devel
%endif
%if %{with pugixml}
BuildRequires:  pkgconfig(pugixml) >= 1.11
%endif
%if %{with pegtl}
BuildRequires:  pegtl-devel >= 2.0.0
%endif
%if %{with testing}
BuildRequires:  cli11-devel
BuildRequires:  vtkdata = %{version}
%endif

%description
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

%package     -n %{shlib}
Summary:        The Visualization Toolkit - A high level 3D visualization library
Group:          System/Libraries
Conflicts:      libvtkcompat_gl1
Provides:       %{name} = %{version}

%description -n %{shlib}
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

This package provides the shared libraries for VTK.

%package        devel
Summary:        VTK header files for building C++ code
Group:          Development/Libraries/C and C++
Requires:       %{name}-qt = %{version}
Requires:       %{shlib} = %{version}
Requires:       cgns-devel
Requires:       cmake >= 3.4
Requires:       double-conversion-devel
Requires:       gcc-c++
%{?with_gl2ps:Requires:       gl2ps-devel}
Requires:       hdf5-devel
%{?with_mpi:Requires:       hdf5-%{mpi_flavor}-devel}
Requires:       libjpeg-devel
Requires:       libmysqlclient-devel
Requires:       libnetcdf_c++-devel
Requires:       libtiff-devel
# not strictly necessary, but required by VTKs cmake files
Requires:       python3-%{name} = %{version}
Requires:       utfcpp-devel
%{?with_mpi:Requires:       %{mpi_flavor}}
%{?with_mpi:Requires:       %{mpi_flavor}-devel}
Requires:       cmake(Verdict)
Requires:       cmake(nlohmann_json)
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5OpenGL)
Requires:       pkgconfig(Qt5OpenGLExtensions)
Requires:       pkgconfig(Qt5Sql)
Requires:       pkgconfig(Qt5Widgets)
Requires:       pkgconfig(expat)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(jsoncpp)
Requires:       pkgconfig(libavcodec)
Requires:       pkgconfig(libavdevice)
Requires:       pkgconfig(libavformat)
Requires:       pkgconfig(libavutil)
Requires:       pkgconfig(libiodbc)
Requires:       pkgconfig(liblz4) >= 1.7.3
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(libpng)
Requires:       pkgconfig(libswscale)
Requires:       pkgconfig(netcdf)
Requires:       pkgconfig(theora)
Requires:       pkgconfig(zlib)
%if %{with pegtl}
Requires:       pegtl-devel
%endif
%if %{with pugixml}
Requires:       pkgconfig(pugixml) >= 1.11
%endif
Conflicts:      vtk-compat_gl-devel

%description    devel
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

This provides development libraries and header files required to
compile C++ programs that use VTK to do 3D visualisation.

%package        java-devel
Summary:        Develoment files for VTK Java bindings
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       %{name}-java = %{version}
Requires:       java-devel
Provides:       %{name}-devel:%{my_libdir}/libvtkJava.so

%description    java-devel
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

This provides the Java part of the development files.

%package        devel-doc
Summary:        VTK API documentation
Group:          Documentation/HTML

%description    devel-doc
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

This provides the VTK API documentation useful for developing
programs that use VTK to do 3D visualisation.

%package        java
Summary:        Java bindings for VTK
Group:          Development/Libraries/Java
Requires:       %{shlib} = %{version}
Conflicts:      vtk-compat_gl-java

%description    java
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

This package provides java bindings for VTK.

%package     -n python3-%{name}
Summary:        Python bindings for VTK
Group:          Development/Libraries/Python
# explicitly require the correct mpi flavor, because the automatic
# rpm requirements generator for shared libs fails to distinguish
# between them -- boo#1187161
Requires:       %{name}-qt = %{version}
Requires:       %{shlib} = %{version}
%{?with_mpi:Requires:       python3-mpi4py}
Requires:       python3-numpy
Requires:       python3-qt5
Conflicts:      python3-vtk-compat_gl

%description -n python3-%{name}
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

This package provides python 3.x bindings for VTK.

%package        qt
Summary:        Qt libraries for VTK
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Conflicts:      vtk-compat_gl-qt

%description qt
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

This package provides the Qt libraries for VTK.

# The examples work with any VTK flavor, just package these once
%if "%{flavor}" == ""
%package        examples
Summary:        Examples for VTK
Group:          Documentation/Other
Recommends:     vtkdata = %{version}
Conflicts:      vtk-compat_gl-examples

%description    examples
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

This package contains many examples showing how to use VTK.
Examples are available in the C++, Tcl, Python and Java programming
languages.
%endif

%prep
%setup -n VTK-%{version}
%patch1 -p1
%if %{with gles}
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%endif
%patch17 -p1
%patch18 -p1

# Replace relative path ../../../../VTKData with %%{_datadir}/vtkdata
# otherwise it will break on symlinks.
grep -rl '\.\./\.\./\.\./\.\./VTKData' . | xargs -r perl -pi -e's,\.\./\.\./\.\./\.\./VTKData,%{_datadir}/vtkdata,g'

# Fix erroneous dependency on sqlite3 binary
sed -i -e '/set(vtk_sqlite_build_binary 1)/ s/.*/#\0/' CMakeLists.txt

# Allow testing also without external downloads - https://gitlab.kitware.com/vtk/vtk/-/issues/18692
sed -i -e '/set(vtk_enable_tests "OFF")/ s/.*/#\0/' CMakeLists.txt

%build
%if %{with mpi}
source %{mpiprefix}/bin/mpivars.sh
export CC=mpicc
export CXX=mpicxx
%else
export CC=gcc
export CXX=g++
%endif

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

# The %%cmake macro sets CMAKE_SKIP_RPATH=ON for Leap 15.x which causes build failures
# https://discourse.vtk.org/t/building-fails-generating-wrap-hierarchy-for-vtk-commoncore-unable-to-open-libvtkwrappingtools-so-1
# Disable ioss module for MPI flavors, fails to build with 9.1.0, see MR 8565.
%cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=%{my_prefix} \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}-%{series} \
    -DCMAKE_INSTALL_QMLDIR:PATH=%{my_libdir}/qt5/qml \
    -DVTK_FORBID_DOWNLOADS:BOOL=ON \
    -DVTK_PYTHON_OPTIONAL_LINK:BOOL=OFF \
    -DVTK_BUILD_TESTING:BOOL=%{?with_testing:ON}%{!?with_testing:OFF} \
    -DVTK_DATA_STORE:PATH=/usr/share/vtkdata/.ExternalData \
    -DExternalData_NO_SYMLINKS:BOOL=ON \
    -DVTK_BUILD_EXAMPLES:BOOL=%{?with_examples:ON}%{!?with_examples:OFF} \
    -DVTK_BUILD_DOCUMENTATION:BOOL=%{?with_documentation:ON}%{!?with_documentation:OFF} \
    -DCMAKE_NO_BUILTIN_CHRPATH:BOOL=ON \
%if 0%{?suse_version} <= 1500
    -DCMAKE_SKIP_RPATH:BOOL=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
%endif
    -DVTK_MODULE_ENABLE_VTK_TestingCore=WANT \
    -DVTK_MODULE_ENABLE_VTK_TestingRendering=WANT \
    -DVTK_MODULE_ENABLE_VTK_RenderingContextOpenGL2=YES \
    -DVTK_MODULE_ENABLE_VTK_RenderingLICOpenGL2=%{?with_gles:NO}%{!?with_gles:YES} \
    -DVTK_MODULE_ENABLE_VTK_RenderingFreeTypeFontConfig=YES \
    -DVTK_CUSTOM_LIBRARY_SUFFIX="" \
    -DVTK_GROUP_ENABLE_Imaging=WANT \
%if %{with mpi}
    -DVTK_USE_MPI:BOOL=ON \
    -DVTK_GROUP_ENABLE_MPI=WANT \
%else
    -DVTK_USE_MPI:BOOL=OFF \
%endif
    -DVTK_GROUP_ENABLE_Qt=WANT \
    -DVTK_GROUP_ENABLE_Rendering=WANT \
    -DVTK_GROUP_ENABLE_StandAlone=WANT \
    -DVTK_GROUP_ENABLE_Views=WANT \
    -DVTK_PYTHON_VERSION=3 \
    -DVTK_WRAP_JAVA:BOOL=%{?with_java:ON}%{!?with_java:OFF} \
    -DVTK_WRAP_PYTHON:BOOL=ON \
    -DOpenGL_GL_PREFERENCE:STRING='GLVND' \
    -DVTK_OPENGL_USE_GLES:BOOL=%{?with_gles:ON}%{!?with_gles:OFF} \
    -DVTK_USE_EXTERNAL:BOOL=ON \
    -DVTK_MODULE_USE_EXTERNAL_VTK_exprtk:BOOL=OFF \
    -DVTK_MODULE_USE_EXTERNAL_VTK_fmt:BOOL=%{?with_fmt:ON}%{!?with_fmt:OFF} \
    -DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps=%{?with_gl2ps:ON}%{!?with_gl2ps:OFF} \
    -DVTK_MODULE_USE_EXTERNAL_VTK_ioss:BOOL=OFF \
    -DVTK_MODULE_USE_EXTERNAL_VTK_libharu=%{?with_haru:ON}%{!?with_haru:OFF} \
    -DVTK_MODULE_USE_EXTERNAL_VTK_pugixml=%{?with_pugixml:ON}%{!?with_pugixml:OFF} \
    -DVTK_MODULE_ENABLE_VTK_ioss:BOOL=%{!?with_mpi:WANT}%{?with_mpi:NO} \
    -DVTK_MODULE_ENABLE_VTK_pegtl=%{?with_pegtl:YES}%{!?with_pegtl:NO} \
    -DVTK_MODULE_ENABLE_VTK_zfp:BOOL=NO \
    %{nil}

%cmake_build

# Remove executable bits from sources (some of which are generated)
find . -name \*.c -o -name \*.cxx -o -name \*.h -o -name \*.hxx -o -name \*.gif -exec chmod -x "{}" "+"

%install
%cmake_install

%if %{with examples}
# List of executable examples
cat > examples.list << EOF
AmbientSpheres
Arrays
BalloonWidget
BandedContours
Cone
Cone2
Cone3
Cone4
Cone5
Cone6
Cube
Cylinder
Delaunay3D
Delaunay3DAlpha
DiffuseSpheres
DumpXMLFile
FilledContours
FixedPointVolumeRayCastMapperCT
GPURenderDemo
Generate2DAMRDataSetWithPulse
Generate3DAMRDataSetWithPulse
GenerateCubesFromLabels
GenerateModelsFromLabels
HierarchicalBoxPipeline
ImageSlicing
LabeledMesh
Medical1
Medical2
Medical3
Medical4
MultiBlock
ParticleReader
RGrid
SGrid
Slider
Slider2D
SpecularSpheres
TubesWithVaryingRadiusAndColors
finance
EOF

# Install examples
%if "%{flavor}" == ""
for file in `cat examples.list`; do
  install -p build/bin/$file %{buildroot}%{my_bindir}
done
perl -pi -e's,^,%{my_bindir}/,' examples.list
%endif

%endif

# Move licenses to licensedir instead of %%{my_datadir}/licenses
mkdir -p %{buildroot}%{_licensedir}
mv %{buildroot}%{my_datadir}/licenses/VTK %{buildroot}%{_licensedir}/%{name}

%if ! %{with mpi}
# Generate and install python distribution metadata
pushd build/%{_lib}/python%{python3_version}/site-packages/
python3 setup.py install_egg_info -d %{buildroot}%{python3_sitearch}
popd
%endif

%fdupes %{buildroot}

%check
# Make sure the python library is at least importable
%if %{with mpi}
source %{mpiprefix}/bin/mpivars.sh
export _PYTHON_MPI_PREFIX=`echo %{buildroot}%{my_libdir}/py*/site-packages/`
export PYTHONPATH=$_PYTHON_MPI_PREFIX:$PYTHONPATH
%endif
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{my_libdir}
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitearch}
PYTHONDONTWRITEBYTECODE=1 python3 -c "import vtk"
find %{buildroot} . -name vtk.cpython-3*.pyc -print -delete # drop unreproducible time-based .pyc file
# Unittests
%if %{with testing}
%ctest
%endif

%post   -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig
%if %{with java}
%post   java -p /sbin/ldconfig
%postun java -p /sbin/ldconfig
%endif
%post   qt -p /sbin/ldconfig
%postun qt -p /sbin/ldconfig
%post   -n python3-%{name} -p /sbin/ldconfig
%postun -n python3-%{name} -p /sbin/ldconfig

%files -n %{shlib}
%license Copyright.txt
%{my_libdir}/lib*.so.*
%exclude %{my_libdir}/libvtk*Qt*.so.*
%exclude %{my_libdir}/libvtk*Python*.so.*

%files devel
%license Copyright.txt
%license %{_datadir}/licenses/%{name}/
%if %{without gles}
%{my_bindir}/vtkProbeOpenGLVersion
%endif
%{my_bindir}/%{pkgname}WrapHierarchy
# Should go into java-devel, but referenced by VTK-targets*.cmake
%{my_bindir}/%{pkgname}WrapJava
%{my_bindir}/%{pkgname}ParseJava
%{my_bindir}/%{pkgname}WrapPython
%{my_bindir}/%{pkgname}WrapPythonInit
%{my_libdir}/*.so
%{my_libdir}/vtk-%{series}
%{?with_mpi: %dir %{my_libdir}/cmake/}
%{my_libdir}/cmake/%{pkgname}-%{series}/
%{my_incdir}/%{pkgname}-%{series}/
# VTK JNI
%exclude %{my_libdir}/libvtkJava.so
%exclude %{my_libdir}/cmake/%{pkgname}-%{series}/VTKJava-*.cmake

%if %{with documentation}
%files devel-doc
%license Copyright.txt
%{_docdir}/%{name}-%{series}
%endif

%if %{with java}
%files java
%license Copyright.txt
# VTK JNI
%{my_libdir}/java/

%files java-devel
%{my_libdir}/libvtkJava.so
%{my_libdir}/cmake/%{pkgname}-%{series}/VTKJava-*.cmake
%endif

%files -n python3-%{name}
%license Copyright.txt
%{my_bindir}/%{pkgname}python
%{my_libdir}/libvtk*Python*.so.*
%if %{with mpi}
%{my_bindir}/p%{pkgname}python
%{my_libdir}/py*
%else
%{python3_sitearch}/vtk.py
%{python3_sitearch}/vtk-%{version}*-info
%{python3_sitearch}/vtkmodules
%endif

%files qt
%license Copyright.txt
%{my_libdir}/libvtk*Qt*.so.*
%if %{with mpi}
%dir %{my_libdir}/qt5
%{my_libdir}/qt5/qml
%else
%{_libqt5_archdatadir}/qml
%endif

%if %{with examples}
%if "%{flavor}" == ""
%files examples -f examples.list
%license Copyright.txt
%endif
%endif

%changelog
