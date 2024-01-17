#
# spec file for package recastnavigation
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


%define sonum 1

Name:           recastnavigation
Version:        1.5.1+git20210305.c5cbd53
Release:        0
Summary:        Recast & Detour
License:        Zlib
URL:            https://github.com/recastnavigation/recastnavigation
# No official recent release available, https://github.com/recastnavigation/recastnavigation/issues/434
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake >= 3.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glu)

%description
Recast is state of the art navigation mesh construction toolset for games.
Recast is accompanied with Detour, path-finding and spatial reasoning toolkit.
You can use any navigation mesh with Detour, but of course the data generated
with Recast fits perfectly.

%package devel
Summary:        Include Files for Recastnavigation Libraries
Requires:       libDebugUtils%{sonum} = %{version}
Requires:       libDetour%{sonum} = %{version}
Requires:       libDetourCrowd%{sonum} = %{version}
Requires:       libDetourTileCache%{sonum} = %{version}
Requires:       libRecast%{sonum} = %{version}

%description devel
This package contains files and libraries needed for develeopment with
recastnavigation libraries.

%package -n libDebugUtils%{sonum}
Summary:        Debug Utils Library for Recastnavigation

%description -n libDebugUtils%{sonum}
This package contains the debug utilities library for the recastnavigation.

%package -n libDetour%{sonum}
Summary:        Detour Library for Recastnatnaviagtion

%description -n libDetour%{sonum}
This package contains the detour library part of Recastnatnaviagtion.

%package -n libDetourCrowd%{sonum}
Summary:        Detour Crowd Library for Recastnatnaviagtion

%description -n libDetourCrowd%{sonum}
This package contains the detour crowd library part of Recastnatnaviagtion.

%package -n libDetourTileCache%{sonum}
Summary:        Detour Tile Cache Library for Recastnatnaviagtion

%description -n libDetourTileCache%{sonum}
This package contains the detour tile cache library part of Recastnatnaviagtion.

%package -n libRecast%{sonum}
Summary:        Recast Library for Recastnatnaviagtion

%description -n libRecast%{sonum}
This package contains the recast library of Recastnatnaviagtion.

%prep
%setup -q

%build
%cmake \
    -DRECASTNAVIGATION_DEMO=OFF \
    -DRECASTNAVIGATION_EXAMPLES=OFF \
    -DRECASTNAVIGATION_TESTS=OFF
%cmake_build

%post -n libDebugUtils%{sonum} -p /sbin/ldconfig
%postun -n libDebugUtils%{sonum} -p /sbin/ldconfig

%post -n libDetour%{sonum} -p /sbin/ldconfig
%postun -n libDetour%{sonum} -p /sbin/ldconfig

%post -n libDetourCrowd%{sonum} -p /sbin/ldconfig
%postun -n libDetourCrowd%{sonum} -p /sbin/ldconfig

%post -n libDetourTileCache%{sonum} -p /sbin/ldconfig
%postun -n libDetourTileCache%{sonum} -p /sbin/ldconfig

%post -n libRecast%{sonum} -p /sbin/ldconfig
%postun -n libRecast%{sonum} -p /sbin/ldconfig

%install
%cmake_install

%files devel
%license License.txt
%doc README.md
%{_libdir}/libDebugUtils.so
%{_libdir}/libDetour.so
%{_libdir}/libDetourCrowd.so
%{_libdir}/libDetourTileCache.so
%{_libdir}/libRecast.so
%{_includedir}/recastnavigation
%{_libdir}/pkgconfig/recastnavigation.pc

%files -n libDebugUtils%{sonum}
%{_libdir}/libDebugUtils.so.*

%files -n libDetour%{sonum}
%{_libdir}/libDetour.so.*

%files -n libDetourCrowd%{sonum}
%{_libdir}/libDetourCrowd.so.*

%files -n libDetourTileCache%{sonum}
%{_libdir}/libDetourTileCache.so.*

%files -n libRecast%{sonum}
%{_libdir}/libRecast.so.*

%changelog
