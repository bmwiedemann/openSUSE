#
# spec file for package rssguard
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


%define libver  3_6_3
Name:           rssguard
Version:        3.6.3
Release:        0
Summary:        RSS/ATOM/RDF feed reader
License:        GPL-3.0-only AND AGPL-3.0-or-later
URL:            https://github.com/martinrotter/rssguard
Source0:        https://github.com/martinrotter/rssguard/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
# PATCH-FIX-OPENSUSE rssguard-3.6.3-add_library_version.patch aloisio@gmx.com -- add version to shared library
Patch2:         rssguard-3.6.3-add_library_version.patch
# PATCH-FIX-UPSTREAM rssguard-3.6.3-fix_sizeof.patch
Patch3:         rssguard-3.6.3-fix_sizeof.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.12
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
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
# resources_big is not compatible with LTO
%define _lto_cflags %{nil}
%qmake5 PREFIX=%{_prefix} LIBDIR=%{_libdir} USE_WEBENGINE=true
%make_jobs

%install
%qmake5_install
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
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}-%{libver}
%{_libdir}/lib%{name}-%{version}.so

%changelog
