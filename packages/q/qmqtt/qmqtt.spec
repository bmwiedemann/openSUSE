#
# spec file for package qmqtt
#
# Copyright (c) 2026 SUSE LLC
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


# Upstream sets SOVERSION to the project major version in CMakeLists.txt.
%define sover 1
%global qmqtt_flavor @BUILD_FLAVOR@%{nil}
%if "%{qmqtt_flavor}" == "qt6"
%define qt6 1
%define qt_major 6
%define qt_descr Qt6
# Upstream's qt6_min_version in CMakeLists.txt.
%define qt_min 6.2.4
%endif
%if "%{qmqtt_flavor}" == "qt5"
%define qt5 1
%define qt_major 5
%define qt_descr Qt5
# Upstream's qt5_min_version, which its CMakeLists.txt raises from 5.3.0 to
# this once WebSockets are enabled.
%define qt_min 5.7.0
%endif
%define pname qmqtt
%if 0%{?qt_major}
%define libname lib%{pname}-qt%{qt_major}-%{sover}
%define psuffix -qt%{qt_major}
%endif
Name:           %{pname}%{?psuffix}
Version:        1.0.8
Release:        0
Summary:        MQTT client library for %{qt_descr}
# Legal-Review-Notice: upstream's LICENSE file offers this library under "the
# Eclipse Public License 1.0 and the Eclipse Distribution License 1.0", i.e. a
# disjunctive dual licence, with the two texts shipped as epl-v10 and edl-v10.
# The edl-v10 text is the verbatim three-clause BSD template naming the Eclipse
# Foundation; SPDX has no separate EDL-1.0 identifier and matches that text to
# BSD-3-Clause, which is the arm recorded in the tag below.
# Corroborating evidence inside the tarball: every source file compiled into
# the library carries an in-file BSD-3-Clause notice and nothing else (Ery Lee
# 2013, plus Matthias Dieter Wallnoefer 2016 on qmqtt_ssl_socket*), no file
# carries an EPL notice, and README.md states "New BSD License".
# The disjunction is load-bearing downstream: EPL-1.0 is GPL-incompatible, so
# the GPL-3.0-or-later consumer jaero links this library under the
# BSD-3-Clause arm, which the "OR" grants.
# tests/gtest/gtest/ is a bundled copy of googletest/googlemock (also
# BSD-3-Clause). It is built only for the test suite and never installed, so it
# adds no obligation to any shipped binary.
License:        EPL-1.0 OR BSD-3-Clause
URL:            https://github.com/emqx/qmqtt
Source:         https://github.com/emqx/qmqtt/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE qmqtt-flavoured-install-names.patch -- add a
# QMQTT_PACKAGE_NAME knob so the installed library and its CMake package can be
# renamed, which is what stops the qt5 and qt6 flavours claiming the same files
# and, worse, the same SONAME for two incompatible ABIs. Deliberately NOT sent
# upstream: it exists to serve this package's flavour split, so it stays
# downstream unless upstream asks for the knob.
Patch0:         qmqtt-flavoured-install-names.patch
BuildRequires:  cmake >= 3.9
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(%{qt_descr}Core) >= %{qt_min}
BuildRequires:  pkgconfig(%{qt_descr}Network) >= %{qt_min}
BuildRequires:  pkgconfig(%{qt_descr}Test) >= %{qt_min}
BuildRequires:  pkgconfig(%{qt_descr}WebSockets) >= %{qt_min}
%if "%{qmqtt_flavor}" == ""
ExclusiveArch:  do_not_build
%endif

%description
QMQTT is an MQTT client library for the Qt framework, speaking the MQTT 3.1
and 3.1.1 publish/subscribe protocols on top of QtNetwork. It supports plain
TCP, TLS and WebSocket transports, and offers a topic router that dispatches
incoming messages to subscribers by topic pattern.

This build is linked against %{qt_descr}.

%package -n %{libname}
Summary:        MQTT client library for %{qt_descr}

%description -n %{libname}
QMQTT is an MQTT client library for the Qt framework, speaking the MQTT 3.1
and 3.1.1 publish/subscribe protocols on top of QtNetwork.

This package provides the %{qt_descr} shared library.

%package devel
Summary:        Development files for the %{qt_descr} QMQTT client library
Requires:       %{libname} = %{version}
# The installed CMake export references the Qt imported targets it was linked
# against, so consuming it needs those Qt CMake config files present.
Requires:       cmake(%{qt_descr}Core)
Requires:       cmake(%{qt_descr}Network)
Requires:       cmake(%{qt_descr}WebSockets)

%description devel
QMQTT is an MQTT client library for the Qt framework, speaking the MQTT 3.1
and 3.1.1 publish/subscribe protocols on top of QtNetwork.

This package contains the headers and the CMake package configuration needed
to build %{qt_descr} applications against QMQTT.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
# The two flavours must not claim the same installed files, and above all must
# not claim the same SONAME for two incompatible ABIs, so the library and the
# CMake package are named after the flavour: libqmqtt-qt5.so.1 alongside
# libqmqtt-qt6.so.1, find_package(qmqtt-qt5) alongside find_package(qmqtt-qt6),
# and a headers directory of their own each. The same layout qcustomplot uses.
#
# Upstream probes for Qt6 first and only falls back to Qt5, so each flavour is
# pinned from both ends: the qt5 build refuses Qt6, so a Qt6 development
# package pulled in as a transitive dependency cannot silently flip it, and the
# qt6 build refuses Qt5, which turns the fallback's find_package(... REQUIRED)
# into a hard CMake error instead of a silent Qt5 build.
#
# QT_VERSION_MAJOR has to be supplied, for BOTH flavours. Upstream reads it as
# an ordinary variable, but nothing ever sets it as one: Qt5 does not define it
# at all, and Qt6Config only publishes it as a *directory property* via
# set_directory_properties(), which ${QT_VERSION_MAJOR} does not read. Its
# WebSockets branch therefore expands to find_package(Qt COMPONENTS
# WebSockets), which lands in CMake's own FindQt module and dies looking for
# Qt3 - on either Qt major, not just on Qt5.
#
# BUILD_SHARED_LIBS is switched back off, which here affects the bundled
# googletest and NOTHING else: the library gets its type from qmqtt_SHARED,
# which passes SHARED to add_library() explicitly. googletest built as a shared
# library needs its consumers to define GTEST_LINKED_AS_SHARED_LIBRARY=1, which
# upstream's test target does not, so its global state ends up duplicated
# between libgtest.so and the test binary and the suite aborts at teardown with
# a double free - even with every test filtered out.
%cmake \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
%if 0%{?qt5}
    -DCMAKE_DISABLE_FIND_PACKAGE_Qt6:BOOL=ON \
%else
    -DCMAKE_DISABLE_FIND_PACKAGE_Qt5:BOOL=ON \
%endif
    -DCMAKE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/%{name} \
    -DQMQTT_PACKAGE_NAME=%{name} \
    -DQT_VERSION_MAJOR=%{qt_major} \
    -Dqmqtt_SHARED:BOOL=ON \
    -Dqmqtt_SSL:BOOL=ON \
    -Dqmqtt_WEBSOCKETS:BOOL=ON \
    -Dqmqtt_BUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
# Three Google Test cases assert behaviour the library deliberately moved away
# from and were never updated; upstream never notices because its only CI
# workflow is CodeQL and it does not run this suite at all:
#   * both isConnectedToHost cases expect Client to ask the network object,
#     while ClientPrivate::isConnectedToHost() answers from its own
#     _connectionState and never touches the network;
#   * the auto-reconnect case expects Network::onSocketError() to start the
#     reconnect timer, which now happens in onDisconnected() instead - and the
#     socket mock's disconnectFromHost() never emits disconnected().
# The other 107 cases run and are required to pass.
export GTEST_FILTER='-ClientTest.isConnectedToHostIs*:NetworkTest.networkWillAttemptToReconnectOnConnectionErrorIfAutoReconnectIsTrue_Test'
# Run ctest the way the %%ctest macro does, but verbosely. The whole Google Test
# binary is a single ctest test, so the default summary would only ever say
# "1/1 passed" and the build log would not record which cases actually ran.
pushd %{__builddir}
ctest --force-new-ctest-process %{?_smp_mflags} --verbose
popd

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license LICENSE edl-v10 epl-v10
%{_libdir}/lib%{name}.so.%{sover}*

%files devel
%license LICENSE edl-v10 epl-v10
%doc README.md qmqtt-API.md
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/cmake/%{name}/

%changelog
