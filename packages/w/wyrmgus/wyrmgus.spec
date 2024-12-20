#
# spec file for package wyrmgus
#
# Copyright (c) 2024 SUSE LLC
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


Name:           wyrmgus
Version:        5.3.6
Release:        0
Summary:        Game engine for Wyrmsun
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Real Time
URL:            https://andrettin.github.io/
Source:         https://github.com/Andrettin/Wyrmgus/archive/v%{version}/Wyrmgus-%{version}.tar.gz
Patch0:         wyrmgus-gl-includes.patch
BuildRequires:  cmake
BuildRequires:  libqt5-qtlocation-private-headers-devel
BuildRequires:  libtolua++-5_1-devel
BuildRequires:  lua51-devel
BuildRequires:  oaml-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  gcc11
BuildRequires:  gcc11-c++
%else
BuildRequires:  gcc-c++
%endif
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
BuildRequires:  libboost_date_time1_75_0-devel
%else
BuildRequires:  libboost_date_time-devel >= 1.69.0
%endif

%description
Modified Stratagus engine for Wyrmsun

%package devel
Summary:        Real-time strategy gaming engine development files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
These are the development files for Wyrmsun which is based on the Stratagus engine.

%prep
%autosetup -p1 -n Wyrmgus-%{version}

%build
%if 0%{?sle_version} >= 150400 && 0%{?sle_version} < 160000 && 0%{?is_opensuse}
export CC="gcc-11"
export CXX="g++-11"
%endif
%cmake \
%if 0%{?suse_version} < 1600
  -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
%endif
  -DWITH_BZIP2=ON \
  -DWITH_PHYSFS=ON \
  -DGAMEDIR=%{_bindir} \
  -DOpenGL_GL_PREFERENCE=GLVND \
  -DENABLE_USEGAMEDIR=OFF
%make_jobs

%install
%cmake_install
install -D -m 0644 doc/stratagus.6 %{buildroot}%{_mandir}/man6/wyrmgus.6
install -D -m 0644 gameheaders/stratagus-game-launcher.h %{buildroot}%{_includedir}/wyrmgus-game-launcher.h
rm %{buildroot}%{_docdir}/wyrmgus/wyrmgus/copyright

%files
%license COPYING
%{_bindir}/wyrmgus
%{_mandir}/man6/wyrmgus.6%{?ext_man}

%files devel
%{_includedir}/wyrmgus-game-launcher.h

%changelog
