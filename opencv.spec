#
# spec file for package opencv
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


# Build failure with LTO enabled on ppc64le boo#1146096
%ifarch ppc64le
%define _lto_cflags %{nil}
%endif

%define libname lib%{name}
%define soname 410
# disabled by default as many fail
%bcond_with    tests
%bcond_without gapi
%bcond_without ffmpeg
%bcond_without python3
%bcond_without openblas
%if %{with python3}
# Enable python311 for SLE15 in addition to the regular python3 which is python 3.6
%{?sle15allpythons}
%endif

Name:           opencv
Version:        4.10.0
Release:        0
Summary:        Collection of algorithms for computer vision
# GPL-2.0 AND Apache-2.0 files are in 3rdparty/ittnotify which is not build
License:        BSD-3-Clause AND GPL-2.0-only AND Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://opencv.org/
Source0:        https://github.com/opencv/opencv/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Several modules from the opencv_contrib package
Source1:        https://github.com/opencv/opencv_contrib/archive/%{version}.tar.gz#/opencv_contrib-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libeigen3-devel
BuildRequires:  libjpeg-devel
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
# OpenJPEGTargets.cmake erroneously requires the binaries
BuildRequires:  openjpeg2
BuildRequires:  tbb-devel
BuildRequires:  unzip
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libv4lconvert)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(zlib)
Provides:       opencv-qt5 = %{version}
Obsoletes:      opencv-qt5 < %{version}
%if %{with gapi}
BuildRequires:  ade-devel >= 0.1.0
%endif
%if %{with openblas}
BuildRequires:  openblas-devel
%endif
%if %{with python3}
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
%else
BuildRequires:  python3-base
%endif
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
%endif
%if %{with python3}
%if "%pythons" != "python3"
# For Tumbleweed and SLE15 with activated multiflavor
%define python_subpackage_only 1
%python_subpackages
%else
# For old SLE15 with only python3 and possibly old python-rpm-macros
%define python_sitearch %python3_sitearch
%define python_files() -n python3-%{**}
%endif
%endif


%description
OpenCV means Intel Open Source Computer Vision Library. It is a collection of C
functions and a few C++ classes that implement some popular Image Processing and
Computer Vision algorithms.

%package -n %{name}4-cascades-data
Summary:        Classifier cascades for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries
Conflicts:      %{name} < 4.5.1
Provides:       %{name}:%{_datadir}/opencv4/lbpcascades/lbpcascade_silverware.xml
BuildArch:      noarch

%description -n %{name}4-cascades-data
Haar and LBP cascades for face and object detecton

%package -n %{libname}%{soname}
Summary:        Libraries to use OpenCV computer vision
License:        BSD-3-Clause
Group:          System/Libraries

%description -n %{libname}%{soname}
The Open Computer Vision Library is a collection of algorithms and sample code
for various computer vision problems. The library is compatible with IPL and
utilizes Intel Integrated Performance Primitives for better performance.

%package -n libopencv_aruco%{soname}
Summary:        Pattern grid detection libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libopencv_aruco%{soname}
Pattern grid detectiion libraries for OpenCV

%package -n libopencv_face%{soname}
Summary:        Face detection libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries
Conflicts:      %{libname}%{soname} < %{version}-%{release}
Requires:       %{name}4-cascades-data

%description -n libopencv_face%{soname}
Face detection libraries for OpenCV

%package -n libopencv_gapi%{soname}
Summary:        G-API library component for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libopencv_gapi%{soname}
G-API library component for OpenCV

%package -n libopencv_highgui%{soname}
Summary:        Higlevel GUI libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libopencv_highgui%{soname}
Higlevel GUI libraries for OpenCV

%package -n libopencv_imgcodecs%{soname}
Summary:        Image codec libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libopencv_imgcodecs%{soname}
Image codec libraries for OpenCV

%package -n libopencv_superres%{soname}
Summary:        Superresolution libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libopencv_superres%{soname}
Superresolution libraries for OpenCV

%package -n libopencv_objdetect%{soname}
Summary:        Face detection libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries
Requires:       %{name}4-cascades-data

%description -n libopencv_objdetect%{soname}
Object detection libraries for OpenCV

%package -n libopencv_optflow%{soname}
Summary:        Optical flow calculation libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libopencv_optflow%{soname}
Optical flow calculation libraries for OpenCV

%package -n libopencv_videoio%{soname}
Summary:        Video IO libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libopencv_videoio%{soname}
Video IO libraries for OpenCV

%package -n libopencv_videostab%{soname}
Summary:        Video stabilization libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libopencv_videostab%{soname}
Video stabilization libraries for OpenCV

%package -n libopencv_ximgproc%{soname}
Summary:        Image processing libraries for OpenCV
License:        BSD-3-Clause
Group:          System/Libraries

%description -n libopencv_ximgproc%{soname}
Image processing libraries for OpenCV

%package devel
Summary:        Development files for using the OpenCV library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{soname} = %{version}
Requires:       libopencv_aruco%{soname} = %{version}
Requires:       libopencv_face%{soname} = %{version}
Requires:       libopencv_gapi%{soname} = %{version}
Requires:       libopencv_highgui%{soname} = %{version}
Requires:       libopencv_imgcodecs%{soname} = %{version}
Requires:       libopencv_objdetect%{soname} = %{version}
Requires:       libopencv_optflow%{soname} = %{version}
Requires:       libopencv_superres%{soname} = %{version}
Requires:       libopencv_videoio%{soname} = %{version}
Requires:       libopencv_videostab%{soname} = %{version}
Requires:       libopencv_ximgproc%{soname} = %{version}
Requires:       %{name} = %{version}
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(ice)
Requires:       pkgconfig(sm)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xext)
Provides:       %{name}-qt5-devel = %{version}
Obsoletes:      %{name}-qt5-devel < %{version}

%description devel
This package contains the OpenCV C/C++ library and header files, as well as
documentation. It should be installed if you want to develop programs that will
use the OpenCV library.

%if 0%{?python_subpackage_only}
%package -n python-%{name}
Summary:        Python %{python_version} bindings for apps which use OpenCV
License:        BSD-3-Clause
Group:          Development/Libraries/Python
%if "%{python_flavor}" == "python3" || "%{python_provides}" == "python3"
Provides:       python-%{name}-qt5 = %{version}
Obsoletes:      python-%{name}-qt5 < %{version}
%endif

%description -n python-%{name}
This package contains Python %{python_version} bindings for the OpenCV library.
%else

%package -n python3-%{name}
Summary:        Python 3 bindings for apps which use OpenCV
License:        BSD-3-Clause
Group:          Development/Libraries/Python
Provides:       python3-%{name}-qt5 = %{version}
Obsoletes:      python3-%{name}-qt5 < %{version}

%description -n python3-%{name}
This package contains Python 3 bindings for the OpenCV library.
%endif

%package doc
Summary:        Documentation and examples for OpenCV
License:        BSD-3-Clause
Group:          Documentation/Other
# Since this package also contains examples that need -devel to be compiled
Suggests:       %{name}-devel
Provides:       %{name}-qt5-doc = %{version}
Obsoletes:      %{name}-qt5-doc < %{version}
BuildArch:      noarch

%description doc
This package contains the documentation and examples for the OpenCV library.

%prep
%setup -q -a 1
%autopatch -p1

# Only copy over modules we need
mv opencv_contrib-%{version}/modules/{aruco,face,tracking,optflow,plot,shape,superres,videostab,ximgproc} modules/
rm -Rf opencv_contrib-%{version}/modules/*
cp opencv_contrib-%{version}/LICENSE LICENSE.contrib

# Remove Windows specific files
rm -f doc/packaging.txt

%build
%limit_build -m 1800

# openCV does not understand the standard RelWithDebinfo,
#   but has a separate variable for it
# Dynamic dispatch: https://github.com/opencv/opencv/wiki/CPU-optimizations-build-options
# x86: disable SSE on 32bit, do not dispatch AVX and later - SSE3
#      is the highest extension available on any non-64bit x86 CPU
# ARM: ARMv6, e.g. RPi1, only has VFPv2
pushd $PWD
%cmake \
      -DCMAKE_BUILD_TYPE=Release \
      -DBUILD_WITH_DEBUG_INFO=ON \
%if %{with tests}
      -DBUILD_TESTS=ON \
%endif
      -DOPENCV_INCLUDE_INSTALL_PATH=%{_includedir} \
      -DOPENCV_LICENSES_INSTALL_PATH=%{_licensedir}/%{name} \
      -DOPENCV_GENERATE_PKGCONFIG=ON \
      -DINSTALL_C_EXAMPLES=ON \
      -DINSTALL_PYTHON_EXAMPLES=ON \
      -DENABLE_OMIT_FRAME_POINTER=ON \
      -DWITH_QT=ON \
      -DWITH_OPENGL=ON \
      -DOpenGL_GL_PREFERENCE:STRING="GLVND" \
      -DWITH_UNICAP=ON \
      -DWITH_XINE=ON \
      -DWITH_IPP=OFF \
      -DWITH_TBB=ON \
%if %{without gapi}
      -DWITH_ADE=OFF \
      -DWITH_opencv_gapi=OFF \
%else
      -Dade_DIR:PATH=%{_datadir}/ade \
%endif
%ifarch %{ix86}
      -DCPU_BASELINE_DISABLE=SSE \
      -DCPU_DISPATCH=SSE,SSE2,SSE3 \
%endif
%ifarch x86_64
      -DCPU_BASELINE=SSE2 \
      -DCPU_DISPATCH=SSE3,SSE4_1,SSE4_2,FP16,FMA3,AVX,AVX2,AVX512_ICL \
%endif
%ifarch %{arm}
%ifarch armv7l armv7hl
      -DCPU_BASELINE=VFPV3 \
      -DCPU_DISPATCH=NEON \
%else
      -DCPU_BASELINE_DISABLE=NEON,VFPV3 \
%endif
%endif
%ifarch aarch64
      -DCPU_BASELINE=NEON \
      -DCPU_DISPATCH=FP16 \
%endif
%if %{with python3}
      -DOPENCV_SKIP_PYTHON_LOADER=ON \
      -DOPENCV_PYTHON3_VERSION=%{python3_version} \
      -DOPENCV_PYTHON3_INSTALL_PATH=%{python3_sitearch} \
%else
      -DBUILD_opencv_python3=OFF \
%endif
      -DPYTHON_DEFAULT_EXECUTABLE=%{_bindir}/python3 \
      -DOPENCV_DOWNLOAD_TRIES_LIST:STRING="" \
      -DWITH_JASPER=OFF \
      %{nil}

%cmake_build
popd

%if %{with python3}
mkdir pythonbuilds
pushd pythonbuilds
%define __sourcedir ../modules/python
%{python_expand # Build all non-primary flavors (if any) "standalone".
# cmake takes most of the config defined from
# $(OpenCV_BINARY_DIR)/opencv_python_config.cmake written during the main build.
if [ "py%{$python_version}" != "py%{python3_version}" ]; then
  pushd $PWD
  %cmake \
      -DOpenCV_BINARY_DIR=../../build/ \
      -DOPENCV_SKIP_PYTHON_LOADER=ON \
      -DOPENCV_PYTHON_VERSION=%{$python_version} \
      -DOPENCV_PYTHON_STANDALONE_INSTALL_PATH=%{$python_sitearch} \
      %{nil}
  %cmake_build
  popd
fi
}
popd
%endif

%install
%cmake_install
%if %{with python3}
pushd pythonbuilds
%{python_expand #
if [ "py%{$python_version}" != "py%{python3_version}" ]; then
  %cmake_install
fi
}
popd
%endif
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
mv %{buildroot}%{_datadir}/opencv4/samples %{buildroot}%{_docdir}/%{name}-doc/examples

# Fix rpmlint warning "doc-file-dependency"
chmod 644 %{buildroot}%{_docdir}/%{name}-doc/examples/python/*.py

# Remove LD_LIBRARY_PATH wrapper script, we install into proper library dirs
rm %{buildroot}%{_bindir}/setup_vars_opencv4.sh

# Fix duplicated install prefix in pkg-config file
cat %{buildroot}%{_libdir}/pkgconfig/opencv4.pc
sed -i -e 's|//usr||g' %{buildroot}%{_libdir}/pkgconfig/opencv4.pc

%fdupes -s %{buildroot}%{_docdir}/%{name}-doc/examples
%fdupes -s %{buildroot}%{_includedir}

%check
%if %{with tests}
export LD_LIBRARY_PATH=$(pwd)/build/lib:$LD_LIBRARY_PATH
%ctest

# Diagnostics:
%{buildroot}%{_bindir}/opencv_version -v
%{buildroot}%{_bindir}/opencv_version -hw
grep -E 'model|stepping|flags' /proc/cpuinfo | head -n4
%endif

%post -n %{libname}%{soname} -p /sbin/ldconfig
%postun -n %{libname}%{soname} -p /sbin/ldconfig
%post -n libopencv_aruco%{soname} -p /sbin/ldconfig
%postun -n libopencv_aruco%{soname} -p /sbin/ldconfig
%post -n libopencv_face%{soname} -p /sbin/ldconfig
%postun -n libopencv_face%{soname} -p /sbin/ldconfig
%post -n libopencv_gapi%{soname} -p /sbin/ldconfig
%postun -n libopencv_gapi%{soname} -p /sbin/ldconfig
%post -n libopencv_highgui%{soname} -p /sbin/ldconfig
%postun -n libopencv_highgui%{soname} -p /sbin/ldconfig
%post -n libopencv_imgcodecs%{soname} -p /sbin/ldconfig
%postun -n libopencv_imgcodecs%{soname} -p /sbin/ldconfig
%post -n libopencv_objdetect%{soname} -p /sbin/ldconfig
%postun -n libopencv_objdetect%{soname} -p /sbin/ldconfig
%post -n libopencv_optflow%{soname} -p /sbin/ldconfig
%postun -n libopencv_optflow%{soname} -p /sbin/ldconfig
%post -n libopencv_superres%{soname} -p /sbin/ldconfig
%postun -n libopencv_superres%{soname} -p /sbin/ldconfig
%post -n libopencv_videoio%{soname} -p /sbin/ldconfig
%postun -n libopencv_videoio%{soname} -p /sbin/ldconfig
%post -n libopencv_videostab%{soname} -p /sbin/ldconfig
%postun -n libopencv_videostab%{soname} -p /sbin/ldconfig
%post -n libopencv_ximgproc%{soname} -p /sbin/ldconfig
%postun -n libopencv_ximgproc%{soname} -p /sbin/ldconfig


%files
%license LICENSE LICENSE.contrib
%license %{_licensedir}/opencv/*
%{_bindir}/opencv_*
%dir %{_datadir}/opencv4
%exclude %{_datadir}/opencv4/valgrind*

%files -n %{name}4-cascades-data
%{_datadir}/opencv4/*cascades

%files -n %{libname}%{soname}
%license LICENSE LICENSE.contrib
%{_libdir}/libopencv_calib3d.so.*
%{_libdir}/libopencv_core.so.*
%{_libdir}/libopencv_dnn.so.*
%{_libdir}/libopencv_features2d.so.*
%{_libdir}/libopencv_flann.so.*
%{_libdir}/libopencv_imgproc.so.*
%{_libdir}/libopencv_ml.so.*
%{_libdir}/libopencv_photo.so.*
%{_libdir}/libopencv_plot.so.*
%{_libdir}/libopencv_shape.so.*
%{_libdir}/libopencv_stitching.so.*
%{_libdir}/libopencv_tracking.so.*
%{_libdir}/libopencv_video.so.*

%files -n libopencv_aruco%{soname}
%{_libdir}/libopencv_aruco.so.*

%files -n libopencv_face%{soname}
%{_libdir}/libopencv_face.so.*

%if %{with gapi}
%files -n libopencv_gapi%{soname}
%{_libdir}/libopencv_gapi.so.*
%endif

%files -n libopencv_highgui%{soname}
%{_libdir}/libopencv_highgui.so.*

%files -n libopencv_imgcodecs%{soname}
%{_libdir}/libopencv_imgcodecs.so.*

%files -n libopencv_objdetect%{soname}
%{_libdir}/libopencv_objdetect.so.*

%files -n libopencv_optflow%{soname}
%{_libdir}/libopencv_optflow.so.*

%files -n libopencv_superres%{soname}
%{_libdir}/libopencv_superres.so.*

%files -n libopencv_videoio%{soname}
%{_libdir}/libopencv_videoio.so.*

%files -n libopencv_videostab%{soname}
%{_libdir}/libopencv_videostab.so.*

%files -n libopencv_ximgproc%{soname}
%{_libdir}/libopencv_ximgproc.so.*

%files devel
%license LICENSE LICENSE.contrib
%{_includedir}/opencv2/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/opencv4.pc
%dir %{_libdir}/cmake/opencv4
%{_libdir}/cmake/opencv4/OpenCVConfig*.cmake
%{_libdir}/cmake/opencv4/OpenCVModules*.cmake
%{_datadir}/opencv4/valgrind*

%if %{with python3}
%files %{python_files %{name}}
%license LICENSE LICENSE.contrib
%{python_sitearch}/cv2.*.so
%endif

%files doc
%{_docdir}/%{name}-doc/

%changelog
