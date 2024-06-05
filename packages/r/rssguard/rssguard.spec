#
# spec file for package rssguard
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


%define libver  4_7_2
Name:           rssguard
Version:        4.7.2
Release:        0
Summary:        RSS/ATOM/RDF feed reader
Group:          Productivity/Networking/News/Clients
License:        AGPL-3.0-or-later AND GPL-3.0-only
URL:            https://github.com/martinrotter/rssguard
Source0:        https://github.com/martinrotter/rssguard/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
# PATCH-FIX-OPENSUSE rssguard-4.7.2-add_library_version.patch aloisio@gmx.com -- add version to shared library
Patch0:         rssguard-4.7.2-add_library_version.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core) >= 6.3.0
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Recommends:     nodejs
Recommends:     npm
Obsoletes:      %{name}-lang < %{version}
Provides:       %{name}-lang = %{version}

%description
RSS Guard is a RSS/ATOM feed aggregator developed using the Qt framework.
It supports online feed synchronization.

%package -n lib%{name}-devel
Summary:        Development headers for lib%{name}-%{libver}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-%{libver}

%description -n lib%{name}-devel
Development headers to be used with lib%{name}-%{libver}.

%package -n lib%{name}-%{libver}
Summary:        Shared library for %{name}

%description -n lib%{name}-%{libver}
Shared library for %{name} to be used by external plugins.

%prep
%autosetup -p1
# remove executable bit
find src/librssguard -name "*.h" -exec chmod -x {} \;

%build
%if 0%{?suse_version} == 1500
export CXX=g++-13
%endif
%cmake -DBUILD_WITH_QT6:BOOL=ON \
%if 0%{?suse_version} > 1600 || 0%{?sle_version} >= 150600
    -DENABLE_MEDIAPLAYER_LIBMPV:BOOL=ON \
%else
    -DENABLE_MEDIAPLAYER_LIBMPV:BOOL=OFF \
%endif
    -DUSE_SYSTEM_SQLITE:BOOL=ON
%cmake_build

%install
%cmake_install
# install autostart
mkdir -pv %{buildroot}%{_datadir}/autostart
%fdupes -s %{buildroot}

%post -n lib%{name}-%{libver} -p /sbin/ldconfig
%postun -n lib%{name}-%{libver} -p /sbin/ldconfig

%files
%license LICENSE.md
%dir %{_datadir}/applications
%dir %{_datadir}/autostart
%dir %{_datadir}/metainfo
%dir %{_libdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/io.github.martinrotter.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.martinrotter.%{name}.png
%{_datadir}/metainfo/io.github.martinrotter.%{name}.metainfo.xml
%{_libdir}/%{name}/lib%{name}-*.so

%files -n librssguard-devel
%{_includedir}/lib%{name}

%files -n lib%{name}-%{libver}
%{_libdir}/lib%{name}-%{version}.so

%changelog
