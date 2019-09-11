#
# spec file for package libopenshot
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define sover 16
Name:           libopenshot
Version:        0.2.2
Release:        0
Summary:        The core library for the OpenShot video editor
License:        LGPL-3.0-or-later
Group:          Productivity/Multimedia/Other
Url:            http://openshot.org/
Source0:        libopenshot-%{version}.tar.xz
BuildRequires:  ImageMagick-devel
BuildRequires:  cmake
BuildRequires:  cppzmq-devel
BuildRequires:  gcc-c++
BuildRequires:  libopenshot-audio-devel
BuildRequires:  pkgconfig
BuildRequires:  swig
#still broken
#BuildRequires:  pkgconfig(Magick++)
#BuildRequires:  ffmpeg3-devel
# required on 15.0:
#BuildRequires:  ffmpeg-3-libavdevice-devel

BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)

BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(UnitTest++)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(python3)
# currently broken at compile time
#BuildRequires:  ruby-devel

%description
A library for video editing, composition, animation, and playback,
which focuses on The library is written in C++ and includes full
bindings for Python and Ruby.

%package -n     %{name}%{sover}
Summary:        The core library for the OpenShot video editor
Group:          System/Libraries

%description -n %{name}%{sover}
A library for video editing, composition, animation, and playback,
which focuses on The library is written in C++ and includes full
bindings for Python and Ruby. It features:

* Multi-layer compositing
* Video and audio effects (chroma key, color adjustment,
  grayscale, etc.)
* Animation curves (Bézier, linear, constant)
* Time mapping (curve-based slow-down, speed-up, reverse)
* Audio mixing & resampling (curve-based)
* Audio plug-ins (VST & AU)
* Telecine and Inverse Telecine (film to TV, TV to film)
* Frame rate conversions
* Multi-processor support
* Uses ffmpeg for format and codec support

This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description    devel
A library for video editing, composition, animation, and playback,
which focuses on The library is written in C++.

This package contains header files and libraries needed to develop
application that use %{name}.

%package -n     python3-openshot
Summary:        Python bindings for the OpenShot library
Group:          Development/Languages/Python

%description -n python3-openshot
This package provides the Python bindings for the OpenShot library.

%prep
%setup -q

%build
# operators of base classes are not supposed to be used here, we can ignore it therefore.
sed -i '/^set(CMAKE_CXX_FLAGS/d' CMakeLists.txt
export CXXFLAGS="%{optflags} -Wno-return-type"

%cmake \
    -DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" \
    -DCMAKE_CXX_FLAGS="$CXXFLAGS" \
    -DFFMPEG_INCLUDE_DIR=/usr/include/ffmpeg \
    -DUSE_SYSTEM_JSONCPP=ON

make %{?_smp_mflags}

%install
%cmake_install

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc AUTHORS
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so

%files -n python3-openshot
%{python3_sitearch}/*openshot*

%changelog
