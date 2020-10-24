#
# spec file for package vtk
#
# Copyright (c) 2020 SUSE LLC
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

%if 0%{?sle_version} >= 150200
%define DisOMPI1 ExclusiveArch:  do_not_build
%endif
%if !0%{?is_opensuse} && 0%{?sle_version:1} && 0%{?sle_version} < 150200
%define DisOMPI3 ExclusiveArch:  do_not_build
%endif

%ifarch %arm aarch64
%bcond_without gles
%else
%bcond_with    gles
%endif

%define pkgname vtk

# pugixml and gl2ps in Leap 15.x are too old
%if 0%{?suse_version} <= 1500
%bcond_with    pugixml
%bcond_with    gl2ps
%else
%bcond_without pugixml
%bcond_without gl2ps
%endif

# pegtl in Leap 15.1 is too old (< 2.0.0)
# JAVA bindings fail to build
%if 0%{?sle_version} == 150100
%bcond_with    java
%bcond_with    pegtl
%else
%bcond_without java
%bcond_without pegtl
%endif

# Need patched version with HPDF_SHADING
%bcond_with    haru

%if "%{flavor}" == ""
%define my_suffix %{nil}
%define my_prefix %_prefix
%define my_bindir %_bindir
%define my_libdir %_libdir
%define my_incdir %_includedir
%define my_datadir %_datadir
%endif

%if "%{flavor}" == "openmpi"
%{?DisOMPI1}
%if 0%{?suse_version} >= 1550
%define my_suffix  -openmpi1
%define mpi_flavor  openmpi1
%else
%define my_suffix  -openmpi
%define mpi_flavor  openmpi
%endif
%define mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}
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
Version:        9.0.1
Release:        0
%define series  9.0
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
# PATCH-FIX-UPSTREAM
Patch2:         0001-clean-up-some-old-opengl-es-stuff.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-expose-1d-texture-options.patch
# PATCH-FIX-UPSTREAM -- prep for GLES patch, VTK issue #17113 stefan.bruens@rwth-aachen.de
Patch4:         0001-Remove-duplicate-check-for-QOpenGLFunctions_3_2_Core.patch
# PATCH-FIX-UPSTREAM 0001-Allow-compilation-on-GLES-platforms.patch VTK issue #17113 stefan.bruens@rwth-aachen.de -- Fix building with Qt GLES builds
Patch5:         0001-Allow-compilation-on-GLES-platforms.patch
# PATCH-FIX-UPSTREAM -- Fix building with Qt GLES builds
Patch6:         0001-Replace-last-glDrawBuffer-call-with-glDrawBuffers-1.patch
# PATCH-FIX-OPENSUSE -- Fix building with Qt GLES builds
Patch7:         0001-Add-missing-guard-required-for-GLES-to-disable-stere.patch
# PATCH-FIX-UPSTREAM -- Fix building with Qt GLES builds
Patch8:         0001-Correct-GL_BACK-GL_BACK_LEFT-mapping-on-GLES.patch
# PATCH-FIX-UPSTREAM -- Fix building with Qt GLES builds
Patch9:         0002-Use-GL_DRAW_BUFFER0-instead-of-GL_DRAW_BUFFER-for-GL.patch
# PATCH-FIX-UPSTREAM
Patch10:        0001-GL_POINT_SPRITE-is-only-available-for-Compatibility-.patch
# PATCH-FIX-OPENSUSE -- GLES - Does no longer apply to upstream code
Patch11:        0002-Guard-GL_LINE_SMOOTH-for-GLES.patch
# PATCH-FIX-UPSTREAM
Patch12:        0001-Guard-glPointSize-with-GL_ES_VERSION_3_0.patch
# PATCH-FIX-UPSTREAM -- https://gitlab.kitware.com/vtk/vtk/-/merge_requests/7098
Patch13:        0001-Fix-PyVTKAddFile_-function-signature-mismatch.patch
# PATCH-FIX-UPSTREAM -- https://gitlab.kitware.com/vtk/vtk/-/merge_requests/7115
Patch14:        0001-Replace-invalid-GL_LINE-with-GL_LINES-for-glDrawArra.patch
# PATCH-FIX-UPSTREAM -- https://gitlab.kitware.com/vtk/vtk/-/issues/18033
Patch15:        vtk-freetype-2.10.3-replace-FT_CALLBACK_DEF.patch
BuildRequires:  R-base-devel
BuildRequires:  chrpath
BuildRequires:  cmake >= 3.4
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
BuildRequires:  utfcpp-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5OpenGLExtensions)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(eigen3) >= 2.91.0
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libiodbc)
BuildRequires:  pkgconfig(liblz4) >= 1.7.3
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
%if %{with gl2ps}
BuildRequires:  gl2ps-devel > 1.4.0
%endif
%if %{with haru}
BuildRequires:  libharu-devel > 2.3.0
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
BuildRequires:  pkgconfig(pugixml)
%endif
%if %{with pegtl}
BuildRequires:  pegtl-devel >= 2.0.0
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
# not strictly necessary, but required by VTKs cmake files
Group:          Development/Libraries/C and C++
%{?with_java:Requires:       %{name}-java = %{version}}
Requires:       %{name}-qt = %{version}
Requires:       %{shlib} = %{version}
Requires:       R-core-devel
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
Requires:       python3-%{name} = %{version}
Requires:       utfcpp-devel
%{?with_mpi:Requires:       %{mpi_flavor}}
%{?with_mpi:Requires:       %{mpi_flavor}-devel}
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5OpenGL)
Requires:       pkgconfig(Qt5OpenGLExtensions)
Requires:       pkgconfig(Qt5Sql)
Requires:       pkgconfig(Qt5WebKitWidgets)
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
Requires:       pugixml-devel
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
Summary:        Qt Designer plugin for QVTKWidget
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Conflicts:      vtk-compat_gl-qt

%description qt
VTK is a software system for image processing, 3D graphics, volume
rendering and visualization. VTK includes many advanced algorithms
(e.g. surface reconstruction, implicit modelling, decimation) and
rendering techniques (e.g. hardware-accelerated volume rendering,
LOD control).

This package provides a Qt Designer plugin for the QVTKWidget.

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
%patch2 -p1
%patch3 -p1
%if %{with gles}
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%endif
%patch13 -p1
%patch14 -p1
%patch15 -p1

# Replace relative path ../../../../VTKData with %%{_datadir}/vtkdata
# otherwise it will break on symlinks.
grep -rl '\.\./\.\./\.\./\.\./VTKData' . | xargs -r perl -pi -e's,\.\./\.\./\.\./\.\./VTKData,%{_datadir}/vtkdata,g'

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
# -DOpenGL_GL_PREFERENCE:STRING='LEGACY' - see https://gitlab.kitware.com/vtk/vtk/-/merge_requests/6946#note_767329
%cmake \
    -DCMAKE_INSTALL_PREFIX:PATH=%{my_prefix} \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}-%{series} \
    -DVTK_INSTALL_LIBRARY_DIR:PATH=%{_lib} \
    -DVTK_INSTALL_PACKAGE_DIR:PATH=%{_lib}/cmake/%{pkgname} \
    -DVTK_PYTHON_OPTIONAL_LINK:BOOL=OFF \
    -DVTK_BUILD_TESTING:BOOL=ON \
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
    -DVTK_USE_OGGTHEORA_ENCODER:BOOL=ON \
    -DJava_JAVAH_EXECUTABLE=%{_bindir}/true \
    -DVTK_WRAP_JAVA:BOOL=%{?with_java:ON}%{!?with_java:OFF} \
    -DVTK_WRAP_PYTHON:BOOL=ON \
    -DVTK_USE_EXTERNAL:BOOL=ON \
    -DOpenGL_GL_PREFERENCE:STRING='GLVND' \
    -DVTK_OPENGL_USE_GLES:BOOL=%{?with_gles:ON}%{!?with_gles:OFF} \
    -DVTK_MODULE_USE_EXTERNAL_VTK_gl2ps=%{?with_gl2ps:ON}%{!?with_gl2ps:OFF} \
    -DVTK_MODULE_USE_EXTERNAL_VTK_libharu=%{?with_haru:ON}%{!?with_haru:OFF} \
    -DVTK_MODULE_USE_EXTERNAL_VTK_pugixml=%{?with_pugixml:ON}%{!?with_pugixml:OFF} \
    -DVTK_MODULE_ENABLE_VTK_pegtl=%{?with_pegtl:YES}%{!?with_pegtl:NO}

    #-DVTK_EXTERNAL_LIBHARU_IS_SHARED:BOOL=OFF \

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

%fdupes -s %{buildroot}

%check
# Make sure the python library is at least importable
%if %{with mpi}
source %{mpiprefix}/bin/mpivars.sh
export _PYTHON_MPI_PREFIX=`echo %{buildroot}%{my_libdir}/py*/site-packages/`
export PYTHONPATH=$_PYTHON_MPI_PREFIX:$PYTHONPATH
%endif
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{my_libdir}
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitearch}
python3 -c "import vtk"
find %{buildroot} . -name vtk.cpython-3*.pyc -delete # drop unreproducible time-based .pyc file

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
%exclude %{my_libdir}/libvtk*Java.so.1
%exclude %{my_libdir}/libvtk*Python*.so.1

%files devel
%license Copyright.txt
%license %{_datadir}/licenses/%{name}/
%if %{without gles}
%{my_bindir}/vtkProbeOpenGLVersion
%endif
%{my_bindir}/%{pkgname}ParseJava
%{my_bindir}/%{pkgname}WrapHierarchy
%{my_bindir}/%{pkgname}WrapJava
%{my_bindir}/%{pkgname}WrapPython
%{my_bindir}/%{pkgname}WrapPythonInit
%{my_libdir}/*.so
%{my_libdir}/vtk/
%{?with_mpi: %dir %{my_libdir}/cmake/}
%{my_libdir}/cmake/%{pkgname}-%{series}/
%{my_incdir}/%{pkgname}-%{series}/
# VTK JNI, PythonTkinter, QtGUI
%exclude %{my_libdir}/libvtk*Java.so
%exclude %{my_libdir}/libvtk*Python*.so
%exclude %{my_libdir}/libvtk*Qt*.so

%if %{with documentation}
%files devel-doc
%license Copyright.txt
%{_docdir}/%{name}-%{series}
%endif

%if %{with java}
%files java
%license Copyright.txt
%{my_libdir}/libvtk*Java.so
%{my_libdir}/libvtk*Java.so.1
%{my_libdir}/java/
%endif

%files -n python3-%{name}
%license Copyright.txt
%{my_bindir}/%{pkgname}python
%if %{with mpi}
%{my_bindir}/p%{pkgname}python
%{my_libdir}/py*
%else
%{python3_sitearch}/
%endif
%{my_libdir}/libvtk*Python*.so.1
%{my_libdir}/libvtk*Python*.so

%files qt
%license Copyright.txt
%{my_libdir}/libvtk*Qt*.so.*
%{my_libdir}/libvtk*Qt*.so

%if %{with examples}
%if "%{flavor}" == ""
%files examples -f examples.list
%license Copyright.txt
%endif
%endif

%changelog
