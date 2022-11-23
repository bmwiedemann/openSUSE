#
# spec file for package rssguard
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


%define libver  4_2_5
Name:           rssguard
Version:        4.2.5
Release:        0
Summary:        RSS/ATOM/RDF feed reader
License:        AGPL-3.0-or-later AND GPL-3.0-only
URL:            https://github.com/martinrotter/rssguard
Source0:        https://github.com/martinrotter/rssguard/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
# PATCH-FIX-OPENSUSE rssguard-4.2.2-add_library_version.patch aloisio@gmx.com -- add version to shared library
Patch2:         rssguard-4.2.2-add_library_version.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core) >= 5.15
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
Recommends:     nodejs
Recommends:     npm
Obsoletes:      %{name}-lang < %{version}
Provides:       %{name}-lang = %{version}

%description
RSS Guard is a RSS/ATOM feed aggregator developed using the Qt framework.
It supports online feed synchronization.

%package -n lib%{name}-devel
Summary:        Development headers for lib%{name}-%{libver}
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
chmod -x resources/desktop/com.github.rssguard.appdata.xml
find src/librssguard -name "*.h" -exec chmod -x {} \;

%build
%cmake
%cmake_build

%install
%cmake_install
# install autostart
mkdir -pv %{buildroot}%{_datadir}/autostart
install -m0644 resources/desktop/com.github.%{name}.desktop.autostart -t %{buildroot}%{_datadir}/autostart
%fdupes -s %{buildroot}

%post -n lib%{name}-%{libver} -p /sbin/ldconfig
%postun -n lib%{name}-%{libver} -p /sbin/ldconfig

%files
%license LICENSE.md
%dir %{_datadir}/applications
%dir %{_datadir}/autostart
%dir %{_datadir}/metainfo
%{_bindir}/%{name}
%{_datadir}/applications/com.github.%{name}.desktop
%{_datadir}/autostart/com.github.%{name}.desktop.autostart
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/metainfo/com.github.%{name}.appdata.xml

%files -n librssguard-devel
%{_includedir}/lib%{name}

%files -n lib%{name}-%{libver}
%{_libdir}/lib%{name}-%{version}.so

%changelog
