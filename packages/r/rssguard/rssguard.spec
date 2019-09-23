#
# spec file for package rssguard
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


Name:           rssguard
Version:        3.5.9
Release:        0
Summary:        RSS/ATOM/RDF feed reader
License:        GPL-3.0-only AND AGPL-3.0-or-later
Group:          Productivity/Networking/News/Utilities
Url:            https://github.com/martinrotter/rssguard
Source0:        https://github.com/martinrotter/rssguard/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.changes
# PATCH-FIX-UPSTREAM rssguard-3.5.2-fix_no_return_nonvoid.patch
Patch0:         rssguard-3.5.2-fix_no_return_nonvoid.patch
# PATCH-FIX-UPSTREAM rssguard-3.5.9-Qt59.patch
Patch1:         rssguard-3.5.9-Qt59.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core) >= 5.9
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
chmod -x resources/desktop/com.github.rssguard.appdata.xml

%build
# resources_big is not compatible with LTO
%define _lto_cflags %{nil}
%qmake5 PREFIX=%{_prefix} USE_WEBENGINE=true
%make_jobs

%install
%qmake5_install
# install autostart
mkdir -pv %{buildroot}%{_datadir}/autostart
install -m0644 resources/desktop/com.github.%{name}.desktop.autostart -t %{buildroot}%{_datadir}/autostart
%fdupes -s %{buildroot}

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

%changelog
