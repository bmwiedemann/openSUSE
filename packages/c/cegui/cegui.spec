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
# Boost >= 1.60 is not supported at the moment, see: https://bitbucket.org/cegui/cegui/issues/1114/pycegui-084-fails-to-build-against-boost
%bcond_with python
# OGRE > 1.9 is not supported at the moment
%bcond_with ogre
Name:           cegui
Version:        0.8.7
Release:        0
Summary:        Crazy Eddie's GUI System
License:        MIT
Group:          System/Libraries
URL:            http://www.cegui.org.uk/
Source0:        http://prdownloads.sourceforge.net/crayzedsgui/%{name}-%{version}.tar.bz2
Source99:       %{name}.changes
# PATCH-FIX-SLED cegui-0.8.3-irrlicht.patch
Patch0:         cegui-0.8.3-irrlicht.patch
# PATCH-FIX-OPENSUSE fix-findluapp.patch -- Find luapp library also if name has a version suffix (e.g. libluapp-5_1), needed for > 13.2
Patch1:         fix-findluapp.patch
Patch2:         use-cpp11.patch
Patch3:         fix-tinyxmlparser-compile.patch
# PATCH-FIX-UPSTREAM fix-pkgconfig-private-dependency.patch -- Fix missing private dependency on glew of CEGUI-OPENGL renderer
Patch4:         fix-pkgconfig-private-dependency.patch
BuildRequires:  Xerces-c-devel
BuildRequires:  cmake >= 2.8.12
BuildRequires:  doxygen
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  gtk2-devel
BuildRequires:  irrlicht-devel >= 1.8
BuildRequires:  libexpat-devel
BuildRequires:  libfreeimage-devel
BuildRequires:  lua51-devel
BuildRequires:  pkgconfig
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(ILU)
BuildRequires:  pkgconfig(OIS)
BuildRequires:  pkgconfig(SILLY)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libxml-2.0)
%if %{with ogre}
BuildRequires:  pkgconfig(OGRE)
%endif
%if %{with python}
BuildRequires:  python
BuildRequires:  python-devel
%endif
BuildRequires:  libtolua++-5_1-devel

%description
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines where such functionality is not natively available, or
severely lacking. The library is object orientated, written in C++, and
targeted at games developers who should be spending their time creating great
games, not building GUI sub-systems!

%package -n lib%{name}%{soname}
Summary:        Crazy Eddie's GUI System
Group:          System/Libraries
Provides:       cegui

%description -n lib%{name}%{soname}
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines where such functionality is not natively available, or
severely lacking. The library is object orientated, written in C++, and
targeted at games developers who should be spending their time creating great
games, not building GUI sub-systems!

%package -n lib%{name}-devel
Summary:        Crazy Eddie's GUI System
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{soname} = %{version}

%description -n lib%{name}-devel
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines where such functionality is not natively available, or
severely lacking. The library is object orientated, written in C++, and
targeted at games developers who should be spending their time creating great
games, not building GUI sub-systems!

This package contains the development libraries and headers.

%package demos-devel
Summary:        Crazy Eddie's GUI System
Group:          Development/Libraries/C and C++
Obsoletes:      cegui-demos

%description demos-devel
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines where such functionality is not natively available, or
severely lacking. The library is object orientated, written in C++, and
targeted at games developers who should be spending their time creating great
games, not building GUI sub-systems!

This package contains some example programs.

%if %{with python}
%package python
Summary:        Crazy Eddie's GUI System
Group:          Development/Libraries/C and C++

%description python
Crazy Eddie's GUI System is a free library providing windowing and widgets for
graphics APIs / engines where such functionality is not natively available, or
severely lacking. The library is object orientated, written in C++, and
targeted at games developers who should be spending their time creating great
games, not building GUI sub-systems!

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
Mem=$(grep MemAvailable /proc/meminfo | awk '{print $2}')
Thr=$(if [ "$((Mem/500000))" -gt "$(nproc)" ]; then echo "$(nproc)"; else echo "$((Mem/500000))"; fi)

cp -r samples Samples
%cmake \
  -DCEGUI_BUILD_RENDERER_NULL=true \
%if %{without python}
  -DCEGUI_BUILD_PYTHON_MODULES=OFF \
%endif
%if %{without ogre}
  -DCEGUI_BUILD_RENDERER_OGRE=OFF \
%endif
  -DCEGUI_BUILD_TESTS=true

make -j$Thr VERBOSE=1

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

%post -n lib%{name}%{soname} -p /sbin/ldconfig
%postun -n lib%{name}%{soname} -p /sbin/ldconfig

%files -n lib%{name}%{soname}
%doc COPYING README.md doc/*-LICENSE
# the *.so files are in the main packaged because they are often
# dynamically loaded, unversioned. So programs would not run without them
%{_libdir}/libCEGUI*.so.*
%{_libdir}/cegui-*

%files -n lib%{name}-devel
%{_includedir}/cegui*
%{_libdir}/libCEGUI*.so
%{_libdir}/pkgconfig/CEGUI*.pc

%files demos-devel
%{_bindir}/tolua*
%{_bindir}/CEGUISampleFramework-0.8
%{_datadir}/cegui*

%if %{with python}
%files python
%{_prefix}/lib*/python*
%endif

%changelog
