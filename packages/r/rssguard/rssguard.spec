#
# spec file for package rssguard
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define libver  5_2_4
Name:           rssguard
Version:        5.2.4
Release:        0
Summary:        RSS/ATOM/RDF feed reader
# Legal-Review-Notice: the shipped binaries bundle third-party code; every
# copyleft licence involved is listed in the License tag below.
#  * AGPL-3.0-or-later - src/librssguard/network-web/oauth2service.{h,cpp},
#    taken from QOAuth2 (Jacob Dawid), built into librssguard-%%{version}.so
#  * GPL-3.0-only - RSS Guard itself (LICENSE.md, AppStream project_license)
#    plus the bundled 3rd-party/qtlinq and 3rd-party/qt-publicsuffix
#  * LGPL-2.1-only - 3rd-party/richtexteditor (MRichTextEditor; it also grants
#    the Digia Qt LGPL Exception 1.1), built into librssguard-gmail.so
#  * LGPL-3.0-or-later - 3rd-party/mimesis, built into librssguard-gmail.so
# Legal-Review-Notice: permissive-only bundled code is not itemised above -
# 3rd-party/gumbo is Apache-2.0, 3rd-party/sc/simplecrypt is BSD-3-Clause, and
# the Go modules statically linked into rssguard-article-extractor are MIT,
# BSD-2/3-Clause and Apache-2.0 only (no copyleft in that set).
# Legal-Review-Notice: src/librssguard-xmpp/src/3rd-party/qxmpp
# (LGPL-2.1-or-later) is present in the tarball but is not shipped, because
# BUILD_XMPP_PLUGIN defaults to OFF and is not enabled here.
License:        AGPL-3.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-or-later
URL:            https://github.com/martinrotter/rssguard
#Source0:        https://github.com/martinrotter/rssguard/archive/%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
# PATCH-FIX-OPENSUSE rssguard-add_library_version.patch aloisio@gmx.com -- Rename
# the CMake library target to rssguard-${APP_VERSION} so the shared library is
# installed as librssguard-%%{version}.so. Deliberate downstream-only carry: it
# encodes the openSUSE package layout, so there is nothing to send upstream.
Patch0:         rssguard-add_library_version.patch
# PATCH-FIX-OPENSUSE rssguard-go.patch -- Drop add_dependencies() on the
# "rssguard" target, which rssguard-add_library_version.patch renames; without
# this CMake aborts on a non-existent target. Downstream-only follow-up to that
# patch, so likewise not upstreamable.
Patch1:         rssguard-go.patch
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  golang(API) >= 1.25
# The QSQLITE driver plugin, needed by the test_databasequeries unit test
BuildRequires:  qt6-sql-sqlite
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core) >= 6.5.0
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(sqlite3)
# DatabaseFactory qFatal()s when the QSQLITE driver plugin is missing, and
# SQLite is the default (and only mandatory) storage backend, so this is a hard
# runtime dependency rpm cannot derive - the plugin is loaded, not linked.
Requires:       qt6-sql-sqlite
Recommends:     nodejs
Recommends:     npm
Obsoletes:      %{name}-lang < %{version}
Provides:       %{name}-lang = %{version}

%description
RSS Guard is a RSS/ATOM feed aggregator developed using the Qt framework.
It supports online feed synchronization.

%package -n lib%{name}-devel
Summary:        Development headers for lib%{name}-%{libver}
License:        AGPL-3.0-or-later AND GPL-3.0-only
Requires:       lib%{name}-%{libver}

%description -n lib%{name}-devel
Development headers to be used with lib%{name}-%{libver}.

%package -n lib%{name}-%{libver}
Summary:        Shared library for %{name}
License:        AGPL-3.0-or-later AND GPL-3.0-only

%description -n lib%{name}-%{libver}
Shared library for %{name} to be used by external plugins.

%prep
%autosetup -p1
# remove executable bit
find src/librssguard -name "*.h" -exec chmod -x {} +
# extract go vendor for article-extractor
tar -xzf %{SOURCE1} -C resources/scripts/standalone/article-extractor

%build
# The article-extractor Go binary is built by upstream's own CMake custom
# command, which forwards no build flags on Linux - hand them over through
# GOFLAGS instead, so the shipped binary is PIE and the vendor tree above is
# used rather than the (unreachable) module proxy.
export GOFLAGS="-buildmode=pie -mod=vendor"

%cmake -DBUILD_WITH_QT6:BOOL=ON \
    -DENABLE_MEDIAPLAYER_LIBMPV:BOOL=ON \
    -DENABLE_TESTING:BOOL=ON \
    -DUSE_SYSTEM_SQLITE:BOOL=ON \
    -DNO_UPDATE_CHECK=1
%cmake_build

%install
%cmake_install
# install autostart
mkdir -pv %{buildroot}%{_datadir}/autostart
%fdupes -s %{buildroot}

%check
# The bundled Go article-extractor ships its own tests; they only talk to
# net/http/httptest servers on loopback, so they run in the offline build.
pushd resources/scripts/standalone/article-extractor
go test -mod=vendor ./...
popd
# Upstream's Qt unit tests set QT_QPA_PLATFORM=offscreen themselves (see
# tests/CMakeLists.txt), so no display or Xvfb wrapper is needed here.
# test_textfactory is skipped: its benchmarksDateTimeParsing() QBENCHMARK parses
# 10000 dates per iteration, which needs ~5 minutes and therefore runs into
# QtTest's own 300 s per-function watchdog. It is a benchmark, not a
# correctness check, so the remaining ten test binaries gate the build.
# Spelled --exclude-regex because the %%ctest macro's option string rejects
# the short form.
%ctest --exclude-regex test_textfactory

%ldconfig_scriptlets -n lib%{name}-%{libver}

%files
%license LICENSE.md
%dir %{_datadir}/applications
%dir %{_datadir}/autostart
%dir %{_datadir}/metainfo
%dir %{_libdir}/%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-article-extractor
%{_datadir}/applications/io.github.martinrotter.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/io.github.martinrotter.%{name}.png
%{_datadir}/metainfo/io.github.martinrotter.%{name}.metainfo.xml
%{_libdir}/%{name}/lib%{name}-*.so

%files -n lib%{name}-devel
%{_includedir}/lib%{name}

%files -n lib%{name}-%{libver}
%{_libdir}/lib%{name}-%{version}.so

%changelog
