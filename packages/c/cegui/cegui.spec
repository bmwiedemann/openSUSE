#
# spec file for package cegui
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2019 Matthias Bach <marix@marix.org>
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


%define soname  -0
%define sover   2
%define libname libCEGUI
# Boost >= 1.60 is not supported at the moment, see: https://bitbucket.org/cegui/cegui/issues/1114/pycegui-084-fails-to-build-against-boost
%bcond_with python
%bcond_without gles
%bcond_without ogre
Name:           cegui
Version:        0.8.7+git20200906
Release:        0
Summary:        Crazy Eddie's GUI System
License:        MIT
Group:          System/Libraries
URL:            http://www.cegui.org.uk/
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}.changes
# PATCH-FIX-UPSTREAM 0001-CMake-Fix-finding-OIS-1.4.patch -- https://github.com/cegui/cegui/commit/c1ce0a9f35b358c3855af56806170695bbc995c7
Patch0:         0001-CMake-Fix-finding-OIS-1.4.patch
# PATCH-FIX-UPSTREAM 0002-Irrlicht-Fix-build-with-version-1.8.patch -- https://github.com/cegui/cegui/pull/1218
Patch1:         0002-Irrlicht-Fix-build-with-version-1.8.patch
# PATCH-FIX-UPSTREAM 0003-pkgconfig-Fix-private-dependency-of-OpenGL-renderer.patch -- https://github.com/cegui/cegui/pull/1218
Patch2:         0003-pkgconfig-Fix-private-dependency-of-OpenGL-renderer.patch
# PATCH-FIX-UPSTREAM 0004-GLES-Fix-library-names-to-look-for.patch -- https://github.com/cegui/cegui/pull/1218
Patch3:         0004-GLES-Fix-library-names-to-look-for.patch
# PATCH-FIX-UPSTREAM 0005-Partially-reverting-1200-c288602.patch -- https://github.com/cegui/cegui/pull/1218
Patch4:         0005-Partially-reverting-1200-c288602.patch
# PATCH-FIX-UPSTREAM 0006-OpenGLES-Renderer-Fix-dependency-on-EGL-on-non-APPLE.patch -- https://github.com/cegui/cegui/pull/1218
Patch5:         0006-OpenGLES-Renderer-Fix-dependency-on-EGL-on-non-APPLE.patch
BuildRequires:  cmake >= 3.9
BuildRequires:  gcc-c++
BuildRequires:  irrlicht-devel >= 1.8
BuildRequires:  libfreeimage-devel
BuildRequires:  libtolua++-5_1-devel
BuildRequires:  lua51-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(ILU)
BuildRequires:  pkgconfig(OIS)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SILLY)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(glm)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sfml-graphics)
BuildRequires:  pkgconfig(sfml-window)
BuildRequires:  pkgconfig(tinyxml2)
%if %{with ogre}
BuildRequires:  ogre-devel
%endif
%if %{with gles}
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glesv1_cm)
%endif
%if %{with python}
BuildRequires:  python
BuildRequires:  python-devel
%endif

%define dsc Crazy Eddie's GUI System is a free library providing windowing and widgets for \
graphics APIs / engines where such functionality is not natively available, or \
severely lacking. The library is object orientated, written in C++, and \
targeted at games developers who should be spending their time creating great \
games, not building GUI sub-systems!

%define renderer_pkg() \
%%package -n %{libname}%{1}Renderer%{soname}-%{sover}\
Summary:        Crazy Eddie's GUI System\
Group:          System/Libraries\
Provides:       cegui\
%%description -n %{libname}%{1}Renderer%{soname}-%{sover}\
%{dsc}\
%%post   -n %{libname}%{1}Renderer%{soname}-%{sover} -p /sbin/ldconfig\
%%postun -n %{libname}%{1}Renderer%{soname}-%{sover} -p /sbin/ldconfig\
%%files  -n %{libname}%{1}Renderer%{soname}-%{sover}\
%{_libdir}/%{libname}%{1}Renderer%{soname}.so.%{sover}*\


%description
%{dsc}

%package -n %{libname}%{soname}
Summary:        Crazy Eddie's GUI System
Group:          System/Libraries
Provides:       cegui

%description -n %{libname}%{soname}
%{dsc}

%renderer_pkg Irrlicht
%renderer_pkg Null
%renderer_pkg Ogre
%renderer_pkg OpenGL
%if %{with gles}
%renderer_pkg OpenGLES
%endif

%package devel
Summary:        Crazy Eddie's GUI System
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{soname} = %{version}
Requires:       %{libname}IrrlichtRenderer%{soname}-%{sover} = %{version}
Requires:       %{libname}NullRenderer%{soname}-%{sover} = %{version}
Requires:       %{libname}OgreRenderer%{soname}-%{sover} = %{version}
Requires:       %{libname}OpenGLRenderer%{soname}-%{sover} = %{version}
%if %{with gles}
Requires:       %{libname}OpenGLESRenderer%{soname}-%{sover} = %{version}
%endif

%description devel
%{dsc}

This package contains the development libraries and headers.

%package demos-devel
Summary:        Crazy Eddie's GUI System
Group:          Development/Libraries/C and C++
Obsoletes:      cegui-demos

%description demos-devel
%{dsc}

This package contains some example programs.

%if %{with python}
%package python
Summary:        Crazy Eddie's GUI System
Group:          Development/Libraries/C and C++

%description python
%{dsc}

This package contains the python interface.
%endif

%prep
%autosetup -p1

# Fix __DATE__ and __TIME__
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
grep -Rl -e "__DATE__" -e "__TIME__" | xargs sed -i -e "s/__DATE__/$DATE/g" -e "s/__TIME__/$TIME/g"

%build
cp -r samples Samples
%cmake \
  -DCEGUI_BUILD_RENDERER_NULL=true \
%if %{without python}
  -DCEGUI_BUILD_PYTHON_MODULES=OFF \
%endif
%if %{without ogre}
  -DCEGUI_BUILD_RENDERER_OGRE=OFF \
%endif
%if %{without gles}
  -DCEGUI_BUILD_RENDERER_OPENGLES=OFF \
%endif
  -DCEGUI_BUILD_TESTS=true
cat cegui/include/CEGUI/Config.h
%make_build

%check
CEGUI_SAMPLE_DATAPATH=datafiles ctest -V

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/CEGUI/examples
cd Samples
cp -r . %{buildroot}%{_datadir}/cegui%{soname}/examples
find %{buildroot}%{_datadir}/cegui* -type f -name "*.orig" -exec rm -f {} \;
%if 0%{?suse_version} < 1500
rm -f %{buildroot}%{_bindir}/CEGUITests-0.8
%endif

%post -n %{libname}%{soname} -p /sbin/ldconfig
%postun -n %{libname}%{soname} -p /sbin/ldconfig

%files -n %{libname}%{soname}
%doc COPYING README.md doc/*-LICENSE
%{_libdir}/%{libname}*.so.*
%exclude %{_libdir}/%{libname}*Renderer*.so.%{sover}*
# the *.so files are in the main packaged because they are often
# dynamically loaded, unversioned. So programs would not run without them
%{_libdir}/cegui-0.8
%exclude %{_libdir}/cegui-0.8/*Demo.so

%files devel
%{_includedir}/cegui*
%{_libdir}/libCEGUI*.so
%{_libdir}/pkgconfig/CEGUI*.pc

%files demos-devel
%{_libdir}/cegui-0.8/*Demo.so
%{_bindir}/tolua*
%{_bindir}/CEGUISampleFramework-0.8
%{_datadir}/cegui*

%if %{with python}
%files python
%{_prefix}/lib*/python*
%endif

%changelog
