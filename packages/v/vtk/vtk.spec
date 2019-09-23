#
# spec file for package vtk
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define pkgname vtk

%if 0%{?suse_version} <= 1500
%bcond_with    pugixml
%else
%bcond_without pugixml
%endif
# Need patched version with HPDF_SHADING
%bcond_with    haru
# Need unrelased version > 1.4.0 with e.g. gl2psTextOptColorBL
%bcond_with    gl2ps

%if "%{flavor}" == ""
%define my_prefix %_prefix
%define my_bindir %_bindir
%define my_libdir %_libdir
%define my_incdir %_includedir
%define my_datadir %_datadir
%endif

%if "%{flavor}" == "openmpi"
%define my_suffix  -openmpi
%define mpi_flavor  openmpi
%define mpiprefix %{_libdir}/mpi/gcc/%{mpi_flavor}
%endif

%if "%{flavor}" == "openmpi2"
%define my_suffix  -openmpi2
%define mpi_flavor  openmpi2
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
Version:        8.2.0
Release:        0
%define series  8.2
# This is a variant BSD license, a cross between BSD and ZLIB.
# For all intents, it has the same rights and restrictions as BSD.
# http://fedoraproject.org/wiki/Licensing/BSD#VTKBSDVariant
Summary:        The Visualization Toolkit - A high level 3D visualization library
License:        BSD-3-Clause
Group:          Productivity/Scientific/Other
URL:            https://vtk.org/
Source:         https://www.vtk.org/files/release/%{series}/VTK-%{version}.tar.gz
# FIXME See if packaging can be tweaked to accommodate python-vtk's devel files in a devel package later
# We need to use the compat conditionals here to avoid Factory's source validator from tripping up
Source99:       vtk-rpmlintrc
# PATCH-FIX-UPSTREAM vtk-fix-file-contains-date-time.patch badshah400@gmail.com -- Fix file containing DATE and TIME
Patch1:         vtk-fix-file-contains-date-time.patch
# PATCH-FIX-OPENSUSE 0001-Allow-compilation-on-GLES-platforms.patch VTK issue #17113 stefan.bruens@rwth-aachen.de -- Fix building with Qt GLES builds
Patch2:         0001-Allow-compilation-on-GLES-platforms.patch
# PATCH-FIX-OPENSUSE bundled_libharu_add_missing_libm.patch stefan.bruens@rwth-aachen.de -- Add missing libm for linking
Patch3:         bundled_libharu_add_missing_libm.patch
# PATCH-FIX-OPENSUSE bundled_exodusii_add_missing_libpthread.patch stefan.bruens@rwth-aachen.de -- Add missing libm for linking
Patch4:         bundled_exodusii_add_missing_libpthread.patch
# PATCH-FIX-OPENSUSE -- Missing libogg symbols
Patch5:         0001-Add-libogg-to-IOMovie-target-link-libraries.patch
# PATCH-FIX-UPSTREAM -- Compatibility for proj4 5.x and 6.0, https://gitlab.kitware.com/vtk/vtk/issues/17554
Patch6:         0001-Make-code-calling-proj4-compatible-with-proj4-5.0-an.patch
BuildRequires:  R-base-devel
BuildRequires:  chrpath
BuildRequires:  cmake >= 3.4
BuildRequires:  double-conversion-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if %{with gl2ps}
BuildRequires:  gl2ps-devel > 1.4.0
%endif
BuildRequires:  gnuplot
BuildRequires:  graphviz
%if %{with mpi}
BuildRequires:  hdf5-%{mpi_flavor}-devel
%endif
BuildRequires:  hdf5-devel
BuildRequires:  java-devel
%if %{with haru}
BuildRequires:  libharu-devel > 2.3.0
%endif
BuildRequires:  libjpeg-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libnetcdf_c++-devel
BuildRequires:  libtiff-devel
%if %{with mpi}
BuildRequires:  %{mpi_flavor}-devel
%endif
BuildRequires:  python3-devel
%if %{with mpi}
BuildRequires:  python3-mpi4py-devel
%endif
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-qt5-devel
BuildRequires:  wget
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
%if 0%{?suse_version} < 1500
# libav pulls in a conflicting libnetcdf version
BuildConflicts: libnetcdf7
BuildConflicts: libavfilter6
%else
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
%endif
BuildRequires:  pkgconfig(libiodbc)
BuildRequires:  pkgconfig(liblz4) >= 1.7.3
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(netcdf)
%if %{with mpi}
BuildRequires:  netcdf-%{mpi_flavor}-devel
%endif
BuildRequires:  pkgconfig(proj)
%if %{with pugixml}
BuildRequires:  pkgconfig(pugixml)
%endif
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(theora)
# Still required with 8.2.x for PythonTkInter
BuildRequires:  pkgconfig(tk)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_graph-devel
BuildRequires:  libboost_graph_parallel-devel
%if %{with mpi}
BuildRequires:  libboost_mpi-devel
%endif
BuildRequires:  libboost_serialization-devel
%else
BuildRequires:  boost-devel
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
Requires:       %{name}-java = %{version}
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
Requires:       python3-%{name} = %{version}
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
%setup -q -n VTK-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%if 0%{?suse_version} > 1500
%patch6 -p1
%endif

# Replace relative path ../../../../VTKData with %%{_datadir}/vtkdata
# otherwise it will break on symlinks.
grep -rl '\.\./\.\./\.\./\.\./VTKData' . | xargs -r perl -pi -e's,\.\./\.\./\.\./\.\./VTKData,%{_datadir}/vtkdata,g'

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
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

# FindJava.cmake looks for javah executable. However,
# the build never invokes the tool. Define a bogus
# Java_JAVAH_EXECUTABLE in order to be able to build
# with JDK10 that does not have this tool, deprecated
# since JDK8.
%cmake \
    -DBUILD_DOCUMENTATION:BOOL=ON \
    -DBUILD_EXAMPLES:BOOL=ON \
    -DBUILD_TESTING:BOOL=OFF \
    -DCMAKE_NO_BUILTIN_CHRPATH:BOOL=ON \
    -DJava_JAVAH_EXECUTABLE:PATH=%{_bindir}/true \
    -DModule_vtkTestingCore:BOOL=ON \
    -DModule_vtkTestingRendering:BOOL=ON \
    -DOpenGL_GL_PREFERENCE:STRING='GLVND' \
    -DVTK_CUSTOM_LIBRARY_SUFFIX="" \
    -DVTK_Group_Imaging:BOOL=ON \
%if %{with mpi}
    -DVTK_Group_MPI:BOOL=ON \
%else
    -DVTK_Group_MPI:BOOL=OFF \
%endif
    -DVTK_Group_Qt:BOOL=ON \
    -DVTK_Group_Rendering:BOOL=ON \
    -DVTK_Group_StandAlone:BOOL=ON \
    -DVTK_Group_Tk:BOOL=ON \
    -DVTK_Group_Views:BOOL=ON \
    -DCMAKE_INSTALL_PREFIX:PATH=%{my_prefix} \
    -DVTK_INSTALL_ARCHIVE_DIR:PATH=%{_lib} \
    -DVTK_INSTALL_LIBRARY_DIR:PATH=%{_lib} \
    -DVTK_INSTALL_PACKAGE_DIR:PATH=%{_lib}/cmake/%{pkgname} \
    -DVTK_INSTALL_QT_DIR:STRING=%{_lib}/qt5/plugins/designer \
    -DVTK_INSTALL_PYTHON_MODULE_DIR:PATH=%{python3_sitearch} \
    -DVTK_PYTHON_VERSION=3 \
    -DVTK_QT_VERSION=5 \
    -DVTK_USE_OGGTHEORA_ENCODER:BOOL=ON \
    -DVTK_USE_SYSTEM_LIBRARIES:BOOL=ON \
    -DVTK_USE_SYSTEM_DIY2=OFF \
    -DVTK_USE_SYSTEM_GL2PS:BOOL=%{?with_gl2ps:ON}%{!?with_gl2ps:OFF} \
    -DVTK_USE_SYSTEM_LIBHARU:BOOL=%{?with_haru:ON}%{!?with_haru:OFF} \
    -DVTK_USE_SYSTEM_LIBPROJ:BOOL=ON \
    -DVTK_USE_SYSTEM_HDF5:BOOL=ON  \
    -DVTK_USE_SYSTEM_MPI4PY=ON \
    -DVTK_USE_SYSTEM_NETCDF:BOOL=ON \
    -DVTK_USE_SYSTEM_PUGIXML:BOOL=%{?with_pugixml:ON}%{!?with_pugixml:OFF} \
    -DVTK_WRAP_JAVA:BOOL=ON \
    -DVTK_WRAP_PYTHON:BOOL=ON \
    -DVTK_WRAP_PYTHON_SIP:BOOL=ON \
    -DVTK_INSTALL_DOC_DIR:PATH=%{_docdir}/%{name}-%{series}

    #-DVTK_EXTERNAL_LIBHARU_IS_SHARED:BOOL=OFF \

%make_jobs
make %{?_smp_mflags} DoxygenDoc

# Remove executable bits from sources (some of which are generated)
find . -name \*.c -o -name \*.cxx -o -name \*.h -o -name \*.hxx -o -name \*.gif -exec chmod -x "{}" "+"

%install
%cmake_install

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

%post   -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig
%post   java -p /sbin/ldconfig
%postun java -p /sbin/ldconfig
%post   -n python3-%{name} -p /sbin/ldconfig
%postun -n python3-%{name} -p /sbin/ldconfig

%files -n %{shlib}
%license Copyright.txt
%{my_libdir}/lib*.so.*
%exclude %{my_libdir}/libvtk*Java.so.1
%exclude %{my_libdir}/libvtk*Python3*.so.1
%exclude %{my_libdir}/libvtkFiltersPython.so.1
%exclude %{my_libdir}/libvtkPythonContext2D.so.1

%files devel
%license Copyright.txt
#%%{my_bindir}/%%{pkgname}EncodeString
#%%{my_bindir}/%%{pkgname}HashSource
%{my_bindir}/%{pkgname}ParseJava
%{my_bindir}/%{pkgname}WrapHierarchy
%{my_bindir}/%{pkgname}WrapJava
%{my_bindir}/%{pkgname}WrapPython
%{my_bindir}/%{pkgname}WrapPythonInit
%{my_libdir}/*.so
%{?with_mpi: %dir %{my_libdir}/cmake/}
%{my_libdir}/cmake/%{pkgname}/
%{my_libdir}/libvtkWrappingTools.a
%{my_incdir}/%{pkgname}-%{series}/
# VTK JNI, PythonTkinter
%exclude %{my_libdir}/libvtk*Java.so
%exclude %{my_libdir}/libvtk*Python3*.so
%exclude %{my_libdir}/libvtkRenderingPythonTkWidgets*.so

%files devel-doc
%license Copyright.txt
%{_docdir}/%{name}-%{series}

%files java
%license Copyright.txt
%{my_libdir}/%{pkgname}.jar
%{my_libdir}/libvtk*Java.so
%{my_libdir}/libvtk*Java.so.1

%files -n python3-%{name}
%license Copyright.txt
%{my_bindir}/%{pkgname}python
%if %{with mpi}
%{my_bindir}/p%{pkgname}python
%{my_libdir}/py*
%else
%{python3_sitearch}/
%endif
%{my_libdir}/libvtk*Python3*.so.1
%{my_libdir}/libvtkFiltersPython.so.1
%{my_libdir}/libvtkPythonContext2D.so.1
%{my_libdir}/libvtkRenderingPythonTkWidgets*.so

%files qt
%license Copyright.txt
%{?with_mpi: %dir %{my_libdir}/qt5/}
%{?with_mpi: %dir %{my_libdir}/qt5/plugins/}
%dir %{my_libdir}/qt5/plugins/designer/
%{my_libdir}/qt5/plugins/designer/libQVTKWidgetPlugin.so

%if "%{flavor}" == ""
%files examples -f examples.list
%license Copyright.txt
%endif

%changelog
