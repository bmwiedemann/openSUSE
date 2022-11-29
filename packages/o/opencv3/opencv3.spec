#
# spec file for package opencv3
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


%define srcname opencv
%define libname lib%{srcname}
%define soname 3_4
# Build failure with LTO enabled on ppc64le boo#1146096
%ifarch ppc64le
%define _lto_cflags %{nil}
%endif
# disabled by default as many fail
%bcond_with tests
%bcond_without qt5
%bcond_without ffmpeg
%if 0%{?suse_version} < 1550
%bcond_without python2
%else
%bcond_with    python2
%endif
%bcond_without python3
%bcond_without openblas
Name:           opencv3
Version:        3.4.18
Release:        0
Summary:        Collection of algorithms for computer vision
# GPL-2.0 AND Apache-2.0 files are in 3rdparty/ittnotify which is not build
License:        Apache-2.0 AND BSD-3-Clause AND GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://opencv.org/
Source0:        https://github.com/opencv/opencv/archive/%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
# This is the FACE module from the opencv_contrib package. Packaged separately to prevent too much unstable modules
Source1:        https://github.com/opencv/opencv_contrib/archive/%{version}.tar.gz#/opencv_contrib-%{version}.tar.gz
# PATCH-FIX-UPSTREAM opencv3-pr19384-tbb2021.patch -- backport tbb 2021 support to opencv3,  https://github.com/opencv/opencv/pull/19384
Patch0:         opencv3-pr19384-tbb2021.patch
# PATCH-FIX-OPENSUSE opencv-build-compare.patch -- avoid republish if some random external version number changes
Patch1:         opencv-build-compare.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libeigen3-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  tbb-devel
BuildRequires:  unzip
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libv4lconvert)
BuildRequires:  pkgconfig(zlib)
Conflicts:      opencv
Provides:       opencv-qt5 = %{version}
Obsoletes:      opencv-qt5 < %{version}
%if %{with openblas}
BuildRequires:  openblas-devel
%endif
%if %{with python2}
BuildRequires:  python2-numpy-devel
BuildRequires:  pkgconfig(python)
%endif
%if %{with python3}
BuildRequires:  python3-numpy-devel
BuildRequires:  pkgconfig(python3)
%endif
%if %{with qt5}
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.0
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
%endif
%if %{with ffmpeg}
BuildRequires:  pkgconfig(libavcodec) < 59
BuildRequires:  pkgconfig(libavformat) < 59
BuildRequires:  pkgconfig(libavutil) < 57
BuildRequires:  pkgconfig(libswscale) < 6
%endif

%description
OpenCV means Intel Open Source Computer Vision Library. It is a collection of C
functions and a few C++ classes that implement some popular Image Processing and
Computer Vision algorithms.

%package -n %{libname}%{soname}
Summary:        Libraries to use OpenCV computer vision
License:        BSD-3-Clause
Group:          System/Libraries

%description -n %{libname}%{soname}
The Open Computer Vision Library is a collection of algorithms and sample code
for various computer vision problems. The library is compatible with IPL and
utilizes Intel Integrated Performance Primitives for better performance.

%package devel
Summary:        Development files for using the OpenCV library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{soname} = %{version}
Requires:       %{name} = %{version}
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Requires:       pkgconfig(ice)
Requires:       pkgconfig(sm)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xext)
Conflicts:      opencv-devel
Provides:       opencv-qt5-devel = %{version}
Obsoletes:      opencv-qt5-devel < %{version}

%description devel
This package contains the OpenCV C/C++ library and header files, as well as
documentation. It should be installed if you want to develop programs that will
use the OpenCV library.

%package -n python2-%{name}
Summary:        Python 2 bindings for apps which use OpenCV
License:        BSD-3-Clause
Group:          Development/Libraries/Python
Conflicts:      python2-opencv
Provides:       python-opencv = %{version}-%{release}
Obsoletes:      python-opencv < %{version}-%{release}
Provides:       python-opencv-qt5 = %{version}
Obsoletes:      python-opencv-qt5 < %{version}

%description -n python2-%{name}
This package contains Python 2 bindings for the OpenCV library.

%package -n python3-%{name}
Summary:        Python 3 bindings for apps which use OpenCV
License:        BSD-3-Clause
Group:          Development/Libraries/Python
Conflicts:      python3-opencv
Provides:       python3-opencv-qt5 = %{version}
Obsoletes:      python3-opencv-qt5 < %{version}

%description -n python3-%{name}
This package contains Python 3 bindings for the OpenCV library.

%package doc
Summary:        Documentation and examples for OpenCV
License:        BSD-3-Clause
Group:          Documentation/Other
Recommends:     python
# Since this package also contains examples that need -devel to be compiled
Suggests:       %{name}-devel
Provides:       opencv-qt5-doc = %{version}
Obsoletes:      opencv-qt5-doc < %{version}

%description doc
This package contains the documentation and examples for the OpenCV library.

%prep
%setup -q -n %{srcname}-%{version} -a 1
%autopatch -p1

# Only copy over modules we need
mv opencv_contrib-%{version}/modules/{face,tracking,plot} modules/
cp opencv_contrib-%{version}/LICENSE LICENSE.contrib

# Remove Windows specific files
rm -f doc/packaging.txt

%build
# Dynamic dispatch: https://github.com/opencv/opencv/wiki/CPU-optimizations-build-options
# x86: disable SSE on 32bit, do not dispatch AVX and later - SSE3
#      is the highest extension available on any non-64bit x86 CPU
# ARM: ARMv6, e.g. RPi1, only has VFPv2
%cmake \
%if %{with tests}
      -DBUILD_TESTS=ON \
%endif
      -DINSTALL_C_EXAMPLES=ON \
      -DINSTALL_PYTHON_EXAMPLES=ON \
      -DENABLE_OMIT_FRAME_POINTER=OFF \
      -DWITH_QT=ON \
      -DWITH_OPENGL=ON \
      -DWITH_UNICAP=ON \
      -DWITH_XINE=ON \
      -DWITH_IPP=OFF \
      -DWITH_TBB=ON \
%ifarch %{ix86}
      -DCPU_BASELINE_DISABLE=SSE \
      -DCPU_DISPATCH=SSE,SSE2,SSE3 \
%endif
%ifarch x86_64
      -DCPU_BASELINE=SSE2 \
      -DCPU_DISPATCH=SSE3,SSE4_1,SSE4_2,AVX,FP16,AVX2 \
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
%if 0%{?suse_version} >= 1500
      -DPYTHON_DEFAULT_EXECUTABLE=%{_bindir}/python3 \
%endif
      -DOPENCV_SKIP_PYTHON_LOADER=ON \
%if %{with python2}
      -DOPENCV_PYTHON2_INSTALL_PATH=%{python2_sitearch} \
%endif
%if %{with python3}
      -DOPENCV_PYTHON3_INSTALL_PATH=%{python3_sitearch} \
%endif
      -DWITH_JASPER=OFF \

make %{?_smp_mflags} VERBOSE=1

%check
%if %{with tests}
export LD_LIBRARY_PATH=$(pwd)/build/lib:$LD_LIBRARY_PATH
%ctest
%endif

%install
%cmake_install
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
mv %{buildroot}%{_datadir}/OpenCV/samples %{buildroot}%{_docdir}/%{name}-doc/examples

# Fix rpmlint warning "doc-file-dependency"
chmod 644 %{buildroot}%{_docdir}/%{name}-doc/examples/python/*.py

# Remove LD_LIBRARY_PATH wrapper script, we install into proper library dirs
rm %{buildroot}%{_bindir}/setup_vars_opencv3.sh

%fdupes -s %{buildroot}%{_docdir}/%{name}-doc/examples
%fdupes -s %{buildroot}%{_includedir}

%post -n %{libname}%{soname} -p /sbin/ldconfig
%postun -n %{libname}%{soname} -p /sbin/ldconfig

%files
%license LICENSE LICENSE.contrib
%license %{_licensedir}/%{name}/*
%{_bindir}/opencv_*
%{_datadir}/OpenCV
%exclude %{_datadir}/OpenCV/OpenCVConfig*.cmake

%files -n %{libname}%{soname}
%license LICENSE LICENSE.contrib
%{_libdir}/libopencv_calib3d.so.*
%{_libdir}/libopencv_core.so.*
%{_libdir}/libopencv_dnn.so.*
%{_libdir}/libopencv_face.so.*
%{_libdir}/libopencv_features2d.so.*
%{_libdir}/libopencv_flann.so.*
%{_libdir}/libopencv_highgui.so.*
%{_libdir}/libopencv_imgcodecs.so.*
%{_libdir}/libopencv_imgproc.so.*
%{_libdir}/libopencv_ml.so.*
%{_libdir}/libopencv_objdetect.so.*
%{_libdir}/libopencv_photo.so.*
%{_libdir}/libopencv_plot.so.*
%{_libdir}/libopencv_shape.so.*
%{_libdir}/libopencv_stitching.so.*
%{_libdir}/libopencv_superres.so.*
%{_libdir}/libopencv_tracking.so.*
%{_libdir}/libopencv_video.so.*
%{_libdir}/libopencv_videoio.so.*
%{_libdir}/libopencv_videostab.so.*

%files devel
%license LICENSE LICENSE.contrib
%{_includedir}/opencv/
%{_includedir}/opencv2/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/opencv.pc
%{_datadir}/OpenCV/OpenCVConfig*.cmake

%if %{with python2}
%files -n python2-%{name}
%license LICENSE LICENSE.contrib
%{python_sitearch}/cv2.so
%endif

%if %{with python3}
%files -n python3-%{name}
%license LICENSE LICENSE.contrib
%{python3_sitearch}/cv2.%{py3_soflags}.so
%endif

%files doc
%{_docdir}/%{name}-doc/

%changelog
