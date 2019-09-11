#
# spec file for package freeorion
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


Name:           freeorion
Version:        0.4.8
Release:        0
Summary:        A turn-based space empire and galactic conquest (4X) computer game
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Turn Based
URL:            https://freeorion.org/
Source:         FreeOrion_v0.4.8_2018-08-23.26f16b0_Source.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/freeorion/freeorion/pull/1657
Patch0:         appdata.patch
Patch1:         cmake_boost_python.patch
# PATCH-FIX-UPSTREAM https://github.com/freeorion/freeorion/pull/2310
Patch2:         freeorion-0.4.8-remove-boost-signals.patch
BuildRequires:  cmake >= 2.8.5
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  google-roboto-fonts
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_date_time-devel
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_log-devel
BuildRequires:  libboost_python-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libpng-devel
BuildRequires:  python-devel >= 2.7
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data = %{version}
Requires:       google-roboto-fonts

%description
FreeOrion is a turn-based space empire and galactic conquest (4X)
computer game. It is inspired by the tradition of the Master of Orion
games, but is not a clone or remake of that series or any other game.

%package data
Summary:        Data files for FreeOrion, a turn-based space empire game
License:        CC-BY-SA-3.0
Group:          Amusements/Games/Strategy/Turn Based
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
FreeOrion is a turn-based space empire and galactic conquest (4X)
computer game. It is inspired by the tradition of the Master of Orion
games, but is not a clone or remake of that series or any other game.

This package contains all the resource data necessary to run FreeOrion.

%prep
%autosetup -p1 -n src-tarball

%build
mkdir build
cd build

cmake \
-DCMAKE_BUILD_TYPE=Release \
-DCMAKE_INSTALL_PREFIX=%{_prefix} \
-DCMAKE_INSTALL_LIBDIR=%{_lib} \
-DCMAKE_BUILD_WITH_INSTALL_RPATH=1 \
-DPYTHON_INCLUDE_DIR=$(python -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
..

# Only try with one thread since each compilation unit is so large
make %{?_smp_mflags} -j1

%install
%cmake_install

## Resource modifications

# Remove included TTF files as we will use the system ones
cd %{buildroot}%{_datadir}/%{name}/default/data/fonts
rm *.ttf LICENSE.*

# Link to system fonts
ln -s %{_datadir}/fonts/truetype/Roboto-Bold.ttf
ln -s %{_datadir}/fonts/truetype/Roboto-Regular.ttf

%fdupes %{buildroot}/%{_datadir}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license default/COPYING
%doc ChangeLog.md README.md
%{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_datadir}/icons/*
%{_datadir}/applications/freeorion.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/freeorion.appdata.xml

%files data
%{_datadir}/%{name}

%changelog
