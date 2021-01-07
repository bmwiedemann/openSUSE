#
# spec file for package wyrmgus
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


Name:           wyrmgus
Version:        4.0.3
Release:        0
Summary:        Game engine for Wyrmsun
License:        GPL-2.0-only
Group:          Amusements/Games/Strategy/Real Time
URL:            https://andrettin.github.io/
Source:         https://github.com/Andrettin/Wyrmgus/archive/v%{version}/Wyrmgus-%{version}.tar.gz
BuildRequires:  boost-devel >= 1.69.0
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libqt5-qtlocation-private-headers-devel
BuildRequires:  lua51-devel
BuildRequires:  oaml-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Location)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(physfs)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbis)
%if 0%{?suse_version} <= 1320
BuildRequires:  pkgconfig(tolua++)
%else
BuildRequires:  libtolua++-5_1-devel
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
%setup -q -n Wyrmgus-%{version}

%build
%cmake \
  -DWITH_BZIP2=ON \
  -DWITH_PHYSFS=ON \
  -DGAMEDIR=%{_bindir} \
  -DENABLE_USEGAMEDIR=OFF
%make_jobs

%install
%cmake_install
install -D -m 0644 doc/stratagus.6 %{buildroot}%{_mandir}/man6/wyrmgus.6
install -D -m 0644 gameheaders/stratagus-game-launcher.h %{buildroot}%{_includedir}/wyrmgus-game-launcher.h

%files
%license COPYING
%doc README.MD
%{_bindir}/wyrmgus
%{_mandir}/man6/wyrmgus.6%{?ext_man}

%files devel
%{_includedir}/wyrmgus-game-launcher.h

%changelog
