#
# spec file for package fife
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Nelson Marques <nmarques@opensuse.org>
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


%define sover 0_4_2
%define oname fifengine
Name:           fife
Version:        0.4.2
Release:        0
Summary:        The Flexible Isometric Free Engine, a 2D game engine
License:        LGPL-2.1-or-later
Group:          Amusements/Games/Other
URL:            http://www.fifengine.de
Source:         https://github.com/fifengine/fifengine/archive/%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fifechan-devel
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  swig
BuildRequires:  tinyxml-devel
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} >= 1330
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif

%description
FIFE stands for Flexible Isometric Free Engine and is a cross platform
game creation framework. It provides the ability to create a
game using Python interfaces.

%package -n libfife%{sover}
Summary:        The Flexible Isometric Free Engine, a 2D game engine
Group:          System/Libraries

%description -n libfife%{sover}
FIFE stands for Flexible Isometric Free Engine and is a cross platform
game creation framework. It provides the ability to create a
game using Python interfaces.

%package -n python3-%{name}
Summary:        Python 3 extensions for the FIFE engine
Group:          Amusements/Games/Other
Requires:       python3
Requires:       python3-future

%description -n python3-%{name}
FIFE stands for Flexible Isometric Free Engine and is a cross platform
game creation framework. It provides the ability to create a
game using Python interfaces.

%package devel
Summary:        Development files for the FIFE 2D game engine
Group:          Development/Libraries/Other
Requires:       libfife%{sover} = %{version}
Requires:       python3-fife = %{version}

%description devel
FIFE stands for Flexible Isometric Free Engine and is a cross platform
game creation framework. It provides the ability to create a
game using Python interfaces.

%prep
%setup -q -n %{oname}-%{version}

%build
%define __builddir py3
%cmake \
    -Dbuild-library=ON \
    -Drend-camzone=ON \
    -Drend-grid=ON \
    -Dlibrocket=ON \
    -Dbuild-python=ON \
    -DPYTHON_SITE_PACKAGES=%{python3_sitearch}
make VERBOSE=1 %{?_smp_mflags}
cd ..

%install
%define __builddir py3
%cmake_install

# Blocked by https://github.com/fifengine/fifengine/issues/879
# %%check
# export PYTHONPATH="%%{buildroot}%%{python3_sitearch}"
# python3 ./run_tests.py -a

%post -n libfife%{sover} -p /sbin/ldconfig
%postun -n libfife%{sover} -p /sbin/ldconfig

%files -n libfife%{sover}
%if ( 0%{?suse_version} == 1315 && 0%{?sle_version} == 120100 ) || ! 0%{?is_opensuse}
# Leap 42.1 or SLE
%license LICENSE.md
%doc AUTHORS
%else
%license LICENSE.md AUTHORS
%endif
%{_libdir}/*.so.*

%files -n python3-%{name}
%{python3_sitearch}/*

%files devel
%doc CHANGELOG.md README.md
%{_includedir}/fife/
%{_libdir}/*.so

%changelog
