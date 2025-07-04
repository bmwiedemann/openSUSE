#
# spec file for package qt6-base
#
# Copyright (c) 2025 SUSE LLC
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


%define real_version 6.9.1
%define short_version 6.9
%define tar_name qtbase-everywhere-src
%define tar_suffix %{nil}
#
%global qt6_flavor @BUILD_FLAVOR@%{nil}
%if "%{qt6_flavor}" == "docs"
%define pkg_suffix -docs
%endif
#
%ifarch %{arm} aarch64
%global with_gles 1
%endif
%if 0%{?suse_version} > 1500
%bcond_without system_md4c
%endif
Name:           qt6-base%{?pkg_suffix}
Version:        6.9.1
Release:        0
Summary:        Qt 6 core components (Core, Gui, Widgets, Network...)
# Legal: qtpaths is BSD-3-Clause
License:        LGPL-2.1-with-Qt-Company-Qt-exception-1.1 OR LGPL-3.0-only
URL:            https://www.qt.io
Source0:        https://download.qt.io/official_releases/qt/%{short_version}/%{real_version}%{tar_suffix}/submodules/%{tar_name}-%{real_version}%{tar_suffix}.tar.xz
Source99:       qt6-base-rpmlintrc
# Patches 0-100 are upstream patches #
# PATCH-FIX-UPSTREAM 0001-Rename-variable-being-shadowed.patch alarrosa@suse.com -- https://codereview.qt-project.org/c/qt/qtbase/+/638284
Patch0:         0001-Rename-variable-being-shadowed.patch
# Patches 100-200 are openSUSE and/or non-upstream(able) patches #
# No need to pollute the library dir with object files, install them in the qt6 subfolder
Patch100:       0001-CMake-Install-objects-files-into-ARCHDATADIR.patch
%if 0%{?suse_version} == 1500
Patch101:       0001-Use-newer-GCC-on-Leap.patch
%endif
Patch102:       0001-Don-t-strip-binaries-when-building-with-qmake.patch
# Change a couple default build system settings
Patch103:       0001-Change-default-settings-for-Qt-packages.patch
##
BuildRequires:  cmake >= 3.18.3
BuildRequires:  cups-devel
# The default GCC version in Leap 15 is too old
%if 0%{?suse_version} == 1500
BuildRequires:  gcc13-PIE
BuildRequires:  gcc13-c++
%else
BuildRequires:  gcc-c++
%endif
BuildRequires:  libicu-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libproxy-devel
# Feature is disabled by default
# BuildRequires:  lksctp-tools-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl
BuildRequires:  pkgconfig
BuildRequires:  qt6-macros
BuildRequires:  xmlstarlet
BuildRequires:  cmake(double-conversion)
%if %{with system_md4c}
BuildRequires:  cmake(md4c)
%endif
BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(krb5-gssapi)
BuildRequires:  pkgconfig(libb2)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(opengl)
BuildRequires:  pkgconfig(openssl) >= 1.1.1
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(tslib)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
%if 0%{?with_gles}
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  pkgconfig(glesv2)
%endif
# Not available for armv7l, s390x and riscv64
%ifnarch %{arm} s390x riscv64
BuildRequires:  pkgconfig(lttng-ust)
%endif
%if "%{qt6_flavor}" == "docs"
BuildRequires:  qt6-tools
%{qt6_doc_packages}
%endif

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%if !%{qt6_docs_flavor}

%package devel
Summary:        Qt 6 base development meta package
Requires:       qt6-base-common-devel
Requires:       cmake(Qt6Concurrent) = %{real_version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6DBus) = %{real_version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Network) = %{real_version}
Requires:       cmake(Qt6OpenGL) = %{real_version}
Requires:       cmake(Qt6OpenGLWidgets) = %{real_version}
Requires:       cmake(Qt6PrintSupport) = %{real_version}
Requires:       cmake(Qt6Sql) = %{real_version}
Requires:       cmake(Qt6Test) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}
Requires:       cmake(Qt6Xml) = %{real_version}
BuildArch:      noarch

%description devel
This meta-package requires all the qt6-base development packages.

%package private-devel
Summary:        Qt 6 base unstable ABI meta package
Requires:       qt6-base-devel = %{version}
Requires:       qt6-kmssupport-private-devel = %{version}
Requires:       qt6-platformsupport-private-devel = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6DBusPrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6NetworkPrivate) = %{real_version}
Requires:       cmake(Qt6OpenGLPrivate) = %{real_version}
Requires:       cmake(Qt6PrintSupportPrivate) = %{real_version}
Requires:       cmake(Qt6SqlPrivate) = %{real_version}
Requires:       cmake(Qt6TestPrivate) = %{real_version}
Requires:       cmake(Qt6WidgetsPrivate) = %{real_version}
Requires:       cmake(Qt6XmlPrivate) = %{real_version}
BuildArch:      noarch

%description private-devel
This meta-package requires all the qt6-base development packages that do not
have any ABI or API guarantees.

%package common-devel
Summary:        Qt 6 Core development utilities
Requires:       cmake
Requires:       gcc-c++
Requires:       pkgconfig
Requires:       qt6-macros
# qtpaths moved from qt6-tools to qt6-base with Qt 6.2
Provides:       qt6-tools-qtpaths = 6.2.0
Obsoletes:      qt6-tools-qtpaths < 6.2.0

%description common-devel
Qt 6 Core development utilities.
It contains the qtbase utilities and definitions.

%package -n libQt6Concurrent6
Summary:        Qt 6 Concurrent library
Requires:       libQt6Core6 = %{version}

%description -n libQt6Concurrent6
The QtConcurrent namespace provides high-level APIs that help write
multi-threaded programs without using low-level threading primitives
such as mutexes, read-write locks, wait conditions, or semaphores.
Programs written with QtConcurrent automatically adjust the number of
threads used according to the number of processor cores available.

QtConcurrent includes functional programming style APIs for parallel
list processing, including a MapReduce and FilterReduce
implementation for shared-memory (non-distributed) systems, and
classes for managing asynchronous computations in GUI applications.

%package -n qt6-concurrent-devel
Summary:        Development files for the Qt 6 Concurrent library
Requires:       libQt6Concurrent6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}

%description -n qt6-concurrent-devel
Development files for the Qt 6 Concurrent library.

%package -n libQt6Core6
Summary:        Qt 6 Core library
Recommends:     qt6-translations

%description -n libQt6Core6
The Qt 6 Core library. It adds these features to C++:

* a mechanism for object communication called signals and slots
* queryable and designable object properties
* hierarchical and queryable object trees that organize
* object ownership in a natural way with guarded pointers (QPointer)
* a dynamic cast that works across library boundaries

%package -n qt6-core-devel
Summary:        Development files for the Qt 6 Core library
Requires:       libQt6Core6 = %{version}
Requires:       qt6-base-common-devel = %{version}
%if 0%{?suse_version} == 1500
# Some public classes require C++ 17 features
Requires:       gcc13-PIE
Requires:       gcc13-c++
%endif

%description -n qt6-core-devel
Development files for the Qt 6 Core library.

%package -n qt6-core-private-devel
Summary:        Non-ABI stable API for the Qt 6 Core library
Requires:       cmake(Qt6Core) = %{real_version}

%description -n qt6-core-private-devel
This package provides private headers of libQt6Core that do not have any
ABI or API guarantees.

%package -n libQt6DBus6
Summary:        Qt6 D-Bus library
Requires:       libQt6Core6 = %{version}

%description -n libQt6DBus6
The Qt D-Bus module is a library that can be used to perform
inter-process communication using the D-Bus protocol.

%package -n qt6-dbus-devel
Summary:        Development files for the Qt 6 D-Bus library
Requires:       libQt6DBus6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}

%description -n qt6-dbus-devel
Development files for the Qt 6 D-Bus library. This package also
contains Qt6's qdbusxml2cpp and qdbuscpp2xml binaries.

%package -n qt6-dbus-private-devel
Summary:        Non-ABI stable API for the Qt 6 D-Bus library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6DBus) = %{real_version}

%description -n qt6-dbus-private-devel
This package provides private headers of libQt6DBus that do not have any
ABI or API guarantees.

%package -n libQt6Gui6
Summary:        Qt 6 GUI related libraries
Requires:       libQt6Core6 = %{version}
Requires:       libQt6DBus6 = %{version}
# This package provides the wayland QPA and related plugins
Requires:       (qt6-wayland if xwayland)
Recommends:     qt6-imageformats = %{version}

%description -n libQt6Gui6
The Qt GUI module provides classes for windowing system integration,
event handling, OpenGL and OpenGL ES integration, 2D graphics, basic
imaging, fonts and text. These classes are used internally by Qt's
user interface code and can also be used directly, for instance, to
write applications using low-level OpenGL ES graphics APIs.

For application developers writing user interfaces, Qt provides
higher level APIs, like Qt Quick, which are much more suitable than
the enablers found in the Qt GUI module.

%package -n qt6-gui-devel
Summary:        Development files for the Qt 6 GUI libraries
Requires:       libQt6Gui6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6DBus) = %{real_version}
Requires:       pkgconfig(atspi-2)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(vulkan)
Requires:       pkgconfig(xkbcommon) >= 0.4.1
%if 0%{?with_gles}
Requires:       Mesa-libGLESv3-devel
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(glesv2)
%else
Requires:       pkgconfig(gl)
%endif

%description -n qt6-gui-devel
Development files for the Qt 6 GUI libraries.

%package -n qt6-gui-private-devel
Summary:        Non-ABI stable API for the Qt 6 GUI libraries
Requires:       libQt6Gui6 = %{version}
Requires:       qt6-kmssupport-private-devel = %{version}
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6DeviceDiscoverySupportPrivate) = %{real_version}
Requires:       cmake(Qt6EglFSDeviceIntegrationPrivate) = %{real_version}
Requires:       cmake(Qt6EglFsKmsSupportPrivate) = %{real_version}
Requires:       cmake(Qt6FbSupportPrivate) = %{real_version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6InputSupportPrivate) = %{real_version}
Requires:       cmake(Qt6OpenGLPrivate) = %{real_version}
Requires:       pkgconfig(xkbcommon)

%description -n qt6-gui-private-devel
This package provides private headers of libQt6Gui that do not have any
ABI or API guarantees.

%package -n libQt6Network6
Summary:        Qt 6 Network library
Requires:       libQt6Core6 = %{version}
Requires:       libQt6DBus6 = %{version}
# Require network plugins. The library is not very useful without these
Requires:       qt6-network-tls = %{version}
Requires:       qt6-networkinformation-glib = %{version}
Requires:       qt6-networkinformation-nm = %{version}

%description -n libQt6Network6
Qt Network provides a set of APIs for programming applications that
use TCP/IP. Operations such as requests, cookies, and sending data
over HTTP are handled by various C++ classes.

%package -n qt6-network-devel
Summary:        Development files for the Qt 6 Network library
Requires:       libQt6Network6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
# Until https://bugreports.qt.io/browse/QTBUG-87776 is fixed, CMake will
# report the optional WrapOpenSSL dependency is not found. This is expected.
# openSSL is only needed for the private link target.

%description -n qt6-network-devel
Development files for the Qt 6 Network library.

%package -n qt6-network-private-devel
Summary:        Non-ABI stable API for the Qt 6 Network library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Network) = %{real_version}
%requires_ge    %(rpm -q --whatprovides "pkgconfig(openssl)" | grep -v noarch)

%description -n qt6-network-private-devel
This package provides private headers of libQt6Network that do not have any
ABI or API guarantees.

%package -n libQt6OpenGL6
Summary:        Qt 6 OpenGL library
Requires:       libQt6Widgets6 = %{version}

%description -n libQt6OpenGL6
The Qt OpenGL module provides an OpenGL widget class that can be used
like any other Qt widget, except that it opens an OpenGL display
buffer where the OpenGL API can be used to render the contents.

%package -n qt6-opengl-devel
Summary:        Development files for the Qt 6 OpenGL library
Requires:       libQt6OpenGL6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6Gui) = %{real_version}
%if 0%{?with_gles}
Requires:       Mesa-libGLESv3-devel
Requires:       pkgconfig(glesv2)
%else
Requires:       pkgconfig(gl)
%endif

%description -n qt6-opengl-devel
Development files for the Qt 6 OpenGL library.

%package -n qt6-opengl-private-devel
Summary:        Non-ABI stable API for the Qt 6 OpenGL library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6OpenGL) = %{real_version}

%description -n qt6-opengl-private-devel
This package provides private headers of libQt6OpenGL that do not have any
ABI or API guarantees.

%package -n libQt6OpenGLWidgets6
Summary:        Qt 6 OpenGLWidgets library
Requires:       libQt6Widgets6 = %{version}

%description -n libQt6OpenGLWidgets6
The Qt OpenGL Widgets module provides an OpenGLWidgets class that can be used
like any other Qt widget, except that it opens an OpenGL display
buffer where the OpenGL API can be used to render the contents.

%package -n qt6-openglwidgets-devel
Summary:        Development files for the Qt 6 OpenGLWidgets library
Requires:       libQt6OpenGLWidgets6 = %{version}
Requires:       cmake(Qt6OpenGL) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}
%if 0%{?with_gles}
Requires:       Mesa-libGLESv3-devel
Requires:       pkgconfig(glesv2)
%else
Requires:       pkgconfig(gl)
%endif

%description -n qt6-openglwidgets-devel
Development files for the Qt 6 OpenGLWidgets library.

%package -n libQt6PrintSupport6
Summary:        Qt 6 PrintSupport library
Requires:       libQt6Widgets6 = %{version}
Requires:       qt6-printsupport-cups = %{version}

%description -n libQt6PrintSupport6
An abstraction over the platform-specific printing systems. Using
this library, Qt applications can print to attached printers and
across networks to remote printers. Qt's printing system also
supports PDF file generation, providing the foundation for basic
report generation facilities.

%package -n qt6-printsupport-devel
Summary:        Development files for the Qt 6 PrintSupport library
# Due to QTBUG-87776, the dependency needs to be in qt6-printsupport-devel
Requires:       cups-devel
Requires:       libQt6PrintSupport6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6Gui) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}

%description -n qt6-printsupport-devel
Development files for the Qt 6 PrintSupport library.

%package -n qt6-printsupport-private-devel
Summary:        Non-ABI stable API for the Qt 6 PrintSupport library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6PrintSupport) = %{real_version}
Requires:       cmake(Qt6WidgetsPrivate) = %{real_version}

%description -n qt6-printsupport-private-devel
This package provides private headers of libQt6PrintSupport that do not have any
ABI or API guarantees.

%package -n libQt6Sql6
Summary:        Qt 6 SQL related library
Requires:       libQt6Core6 = %{version}

%description -n libQt6Sql6
A Qt 6 library which is used for connection with an SQL server. You
will need also a plugin package for a supported SQL server.

%package -n qt6-sql-devel
Summary:        Development files for the Qt 6 SQL library
Requires:       libQt6Sql6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Suggests:       qt6-sql-mysql = %{version}
Suggests:       qt6-sql-postgresql = %{version}
Suggests:       qt6-sql-sqlite = %{version}
Suggests:       qt6-sql-unixODBC = %{version}

%description -n qt6-sql-devel
Development files for the Qt 6 SQL library

%package -n qt6-sql-private-devel
Summary:        Non-ABI stable API for the Qt 6 SQL library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Sql) = %{real_version}

%description -n qt6-sql-private-devel
This package provides private headers of libQt6Sql that do not have any
ABI or API guarantees.

%package -n libQt6Test6
Summary:        Qt 6 Test library
Requires:       libQt6Core6 = %{version}

%description -n libQt6Test6
Qt Test is a framework for unit testing Qt based applications and
libraries. Qt Test provides functionality commonly found in unit
testing frameworks as well as extensions for testing graphical user
interfaces.

%package -n qt6-test-devel
Summary:        Development files for the Qt 6 Test library
Requires:       libQt6Test6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}

%description -n qt6-test-devel
Development files for the Qt 6 Test library.

%package -n qt6-test-private-devel
Summary:        Non-ABI stable API for the Qt 6 Test library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Test) = %{real_version}

%description -n qt6-test-private-devel
This package provides private headers of libQt6Test that do not have any
ABI or API guarantees.

%package -n libQt6Widgets6
Summary:        Qt 6 Widgets library
Requires:       libQt6Gui6 = %{version}

%description -n libQt6Widgets6
The Qt Widgets library provides a set of UI elements to create classic
desktop-style user interfaces.

%package -n qt6-widgets-devel
Summary:        Development files for the Qt 6 Widgets library
Requires:       libQt6Widgets6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}
Requires:       cmake(Qt6Gui) = %{real_version}

%description -n qt6-widgets-devel
Development files for the Qt 6 Widgets library.

%package -n qt6-widgets-private-devel
Summary:        Non-ABI stable API for the Qt 6 Widgets library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       cmake(Qt6Widgets) = %{real_version}

%description -n qt6-widgets-private-devel
This package provides private headers of libQt6Widgets that do not have any
ABI or API guarantees.

%package -n libQt6Xml6
Summary:        Qt 6 XML library
Requires:       libQt6Core6 = %{version}

%description -n libQt6Xml6
The Qt XML module provides C++ implementations of the SAX and DOM
standards for XML.

%package -n qt6-xml-devel
Summary:        Development files for the Qt 6 XML library
Requires:       libQt6Xml6 = %{version}
Requires:       cmake(Qt6Core) = %{real_version}

%description -n qt6-xml-devel
Development files for the Qt 6 XML library.

(The module is not actively maintained anymore. Please use the
QXmlStreamReader and QXmlStreamWriter classes in Qt Core instead.)

%package -n qt6-xml-private-devel
Summary:        Non-ABI stable API for the Qt 6 XML library
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6Xml) = %{real_version}

%description -n qt6-xml-private-devel
This package provides private headers of libQt6Xml that do not have any
ABI or API guarantees.

%package -n qt6-docs-common
Summary:        Common files for building documentation
BuildArch:      noarch

%description -n qt6-docs-common
This package contains common files used for building Qt documentation.


### Static libraries ###

%package -n qt6-exampleicons-devel-static
Summary:        Qt ExampleIcons module
# TODO
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}

%description -n qt6-exampleicons-devel-static
Qt icon library for examples. This private library can be used by Qt examples.

%package -n qt6-kmssupport-devel-static
Summary:        Qt KMSSupport module
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}

%description -n qt6-kmssupport-devel-static
Qt module to support Kernel Mode Setting.

%package -n qt6-kmssupport-private-devel
Summary:        Non-ABI stable API for the Qt 6 KMSSupport library
Requires:       qt6-kmssupport-devel-static = %{version}

%description -n qt6-kmssupport-private-devel
This package provides private headers of libQt6KmsSupport that do not have any
ABI or API guarantees.

%package -n qt6-platformsupport-devel-static
Summary:        Qt PlatformSupport module
Requires:       cmake(Qt6CorePrivate) = %{real_version}
Requires:       cmake(Qt6GuiPrivate) = %{real_version}
Requires:       pkgconfig(atspi-2)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libinput)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(mtdev)
Requires:       pkgconfig(tslib)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xkbcommon) >= 0.4.1
Requires:       pkgconfig(xkbcommon-x11) >= 0.4.1
Requires:       pkgconfig(xrender)

%description -n qt6-platformsupport-devel-static
Qt PlatformSupport module.

%package -n qt6-platformsupport-private-devel
Summary:        Non-ABI stable API for the  Qt6 PlatformSupport library
Requires:       qt6-platformsupport-devel-static = %{version}

%description -n qt6-platformsupport-private-devel
This package provides private headers of libQt6PlatformSupport that do not have
any ABI or API guarantees.


### Plugins ###

%package -n qt6-networkinformation-glib
Summary:        Network information for QNetworkInformation using GNetworkMonitor

%description -n qt6-networkinformation-glib
Plugin using GNetworkMonitor to get network information such as the
reachability, media type...

%package -n qt6-networkinformation-nm
Summary:        Network information for QNetworkInformation
# Renamed in Qt 6.2
Provides:       qt6-network-informationbackends = 6.2.0
Obsoletes:      qt6-network-informationbackends < 6.2.0

%description -n qt6-networkinformation-nm
Plugin used to get network information such as the reachability, media type...

%package -n qt6-network-tls
Summary:        Backends used to handle secure connections

%description -n qt6-network-tls
TLS (and non-TLS) plugins used by the QSsl classes.

%package -n qt6-platformtheme-gtk3
Summary:        Qt 6 GTK3 plugin
Requires:       libQt6Gui6 = %{version}
Supplements:    (libQt6Gui6 and libgtk-3-0)

%description -n qt6-platformtheme-gtk3
Qt 6 plugin for better integration with GTK3-based desktop environments.

%package -n qt6-platformtheme-xdgdesktopportal
Summary:        Qt 6 XDG Desktop Portal Plugin
Requires:       libQt6Gui6 = %{version}

%description -n qt6-platformtheme-xdgdesktopportal
Qt 6 plugin for integration with Flatpak and Snap.

%package -n qt6-printsupport-cups
Summary:        Qt 6 CUPS plugin
Requires:       libQt6PrintSupport6 = %{version}

%description -n qt6-printsupport-cups
The Qt printsupport CUPS plugin.

%package -n qt6-sql-mysql
Summary:        Qt 6 MySQL support
Requires:       libQt6Sql6 = %{version}

%description -n qt6-sql-mysql
A plugin to access MySQL servers in Qt applications.

%package -n qt6-sql-postgresql
Summary:        Qt 6 PostgreSQL plugin
Requires:       libQt6Sql6 = %{version}

%description -n qt6-sql-postgresql
A plugin to access PostgreSQL servers in Qt applications.

The QPSQL driver supports version 9 and higher of the PostgreSQL
server.

%package -n qt6-sql-sqlite
Summary:        Qt 6 SQLite plugin
Requires:       libQt6Sql6 = %{version}

%description -n qt6-sql-sqlite
A plugin to access SQLite databases in Qt applications.

SQLite is an in-process database, which means that it is not
necessary to have a database server. SQLite operates on a single
file, which must be set as the database name when opening a
connection.

%package -n qt6-sql-unixODBC
Summary:        Qt 6 unixODBC plugin
Requires:       libQt6Sql6 = %{version}

%description -n qt6-sql-unixODBC
A plugin to connect to an ODBC driver manager in Qt applications and
access the available data sources. Note that you also need to install
and configure ODBC drivers for the ODBC driver manager that is
installed on your system.

%{qt6_examples_package}

%endif

%prep
%autosetup -p1 -n %{tar_name}-%{real_version}%{tar_suffix}

# Copy the freetype license file to prevent errors when building docs
cp src/3rdparty/freetype/LICENSE.txt src/gui/painting/FREETYPE_LICENSE.txt
sed -i 's#../../3rdparty/freetype/LICENSE.txt#FREETYPE_LICENSE.txt#' src/gui/painting/qt_attribution.json

# Same thing for blake2
sed -i '/\/3rdparty\/blake2/d' src/corelib/CMakeLists.txt

# We don't want to use these 3rdparty libraries
rm -r src/3rdparty/{blake2,double-conversion,freetype,harfbuzz-ng,libjpeg,libpng,pcre2,sqlite,xcb,zlib}
%if %{with system_md4c}
rm -r src/3rdparty/md4c
%endif
# Remove license files symlinked to deleted 3rdparty libraries
rm LICENSES/{FTL.txt,IJG.txt,libpng-2.0.txt,Zlib.txt}

# Empty file used for the meta packages
cat >> meta_package << EOF
This is a meta package, it does not contain any file
EOF

# Work around an issue with zstd CMake files (boo#1211566)
# TODO: Remove when the issue is fixed
sed -i '/zstd CONFIG/d' cmake/FindWrapZSTD.cmake

%build
%define _lto_cflags %{nil}

# NOTE: ltcg causes linker errors on ppc64
%cmake_qt6 \
    -DINSTALL_ARCHDATADIR:STRING=%{_qt6_archdatadir} \
    -DINSTALL_BINDIR:STRING=%{_qt6_bindir} \
    -DINSTALL_DATADIR:STRING=%{_qt6_datadir} \
    -DINSTALL_DESCRIPTIONSDIR:STRING=%{_qt6_descriptionsdir} \
    -DINSTALL_DOCDIR:STRING=%{_qt6_docdir} \
    -DINSTALL_EXAMPLESDIR:STRING=%{_qt6_examplesdir} \
    -DINSTALL_INCLUDEDIR:STRING=%{_qt6_includedir} \
    -DINSTALL_LIBDIR:STRING=%{_qt6_libdir} \
    -DINSTALL_LIBEXECDIR:STRING=%{_qt6_libexecdir} \
    -DINSTALL_MKSPECSDIR:STRING=%{_qt6_mkspecsdir} \
    -DINSTALL_PLUGINSDIR:STRING=%{_qt6_pluginsdir} \
    -DINSTALL_QMLDIR:STRING=%{_qt6_qmldir} \
    -DINSTALL_SYSCONFDIR:STRING=%{_qt6_sysconfdir} \
    -DINSTALL_TESTSDIR:STRING=%{_qt6_testsdir} \
    -DINSTALL_TRANSLATIONSDIR:STRING=%{_qt6_translationsdir} \
    -DBUILD_WITH_PCH:BOOL=FALSE \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DQT_BUILD_EXAMPLES:BOOL=TRUE \
    -DQT_INSTALL_EXAMPLES_SOURCES:BOOL=TRUE \
    -DQT_BUILD_TESTS:BOOL=FALSE \
    -DQT_CREATE_VERSIONED_HARD_LINK:BOOL=FALSE \
    -DQT_DISABLE_RPATH:BOOL=FALSE \
    -DQT_GENERATE_SBOM:BOOL=FALSE \
%ifnarch ppc64
    -DCMAKE_INTERPROCEDURAL_OPTIMIZATION:BOOL=TRUE \
%endif
    -DFEATURE_elf_private_full_version=TRUE \
    -DFEATURE_enable_new_dtags:BOOL=TRUE \
    -DFEATURE_forkfd_pidfd:BOOL=FALSE \
    -DFEATURE_journald:BOOL=TRUE \
    -DFEATURE_libproxy:BOOL=TRUE \
    -DFEATURE_reduce_relocations:BOOL=FALSE \
    -DFEATURE_relocatable:BOOL=FALSE \
    -DFEATURE_system_sqlite:BOOL=TRUE \
    -DFEATURE_system_xcb_xinput:BOOL=TRUE \
    -DFEATURE_xcb_native_painting:BOOL=TRUE \
    -DINPUT_openssl:STRING=linked \
%if 0%{?with_gles}
    -DINPUT_opengl:STRING=es2 \
    -DFEATURE_opengles3:BOOL=TRUE
%endif

%{qt6_build}

%install
%{qt6_install}

%if !%{qt6_docs_flavor}

# 'BuildFlags: useccache' in the repo prjconf 'taints' qt.toolchain.cmake
sed -i 's#/var/lib/build/ccache#/usr#g' %{buildroot}%{_qt6_cmakedir}/Qt6/qt.toolchain.cmake

# Empty folders provided by libQt6Core6 and qt6-core-common-devel
mkdir -p %{buildroot}%{_qt6_sysconfdir}
mkdir -p %{buildroot}%{_qt6_testsdir}
mkdir -p %{buildroot}%{_qt6_translationsdir}

%{qt6_link_executables}

# CMake modules for plugins are not useful
rm %{buildroot}%{_qt6_cmakedir}/*/*Plugin{Config,ConfigVersion,Targets*}.cmake

# There are no private headers
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_concurrent_private.pri
rm %{buildroot}%{_qt6_mkspecsdir}/modules/qt_lib_openglwidgets_private.pri

# These files are only useful for the Qt continuous integration
rm %{buildroot}%{_qt6_libexecdir}/ensure_pro_file.cmake
rm %{buildroot}%{_qt6_libexecdir}/qt-android-runner.py
rm %{buildroot}%{_qt6_libexecdir}/qt-testrunner.py
rm %{buildroot}%{_qt6_libexecdir}/sanitizer-testrunner.py

# This is only for Apple platforms and has a python2 dep
rm -r %{buildroot}%{_qt6_mkspecsdir}/features/uikit

# Not useful for desktop installs
rm -r %{buildroot}%{_qt6_cmakedir}/Qt6ExamplesAssetDownloaderPrivate
rm -r %{buildroot}%{_qt6_includedir}/QtExamplesAssetDownloader
rm %{buildroot}%{_qt6_descriptionsdir}/ExamplesAssetDownloaderPrivate.json
rm %{buildroot}%{_qt6_libdir}/libQt6ExamplesAssetDownloader.*
rm %{buildroot}%{_qt6_metatypesdir}/qt6examplesassetdownloaderprivate_*_metatypes.json

# E: env-script-interpreter
sed -i 's#!/bin/env python3#!/usr/bin/python3#' %{buildroot}%{_qt6_examplesdir}/corelib/serialization/cbordump/cbortag.py


%ldconfig_scriptlets -n libQt6Concurrent6
%ldconfig_scriptlets -n libQt6Core6
%ldconfig_scriptlets -n libQt6DBus6
%ldconfig_scriptlets -n libQt6Gui6
%ldconfig_scriptlets -n libQt6Network6
%ldconfig_scriptlets -n libQt6OpenGL6
%ldconfig_scriptlets -n libQt6OpenGLWidgets6
%ldconfig_scriptlets -n libQt6PrintSupport6
%ldconfig_scriptlets -n libQt6Sql6
%ldconfig_scriptlets -n libQt6Test6
%ldconfig_scriptlets -n libQt6Widgets6
%ldconfig_scriptlets -n libQt6Xml6

%files devel
%doc meta_package

%files private-devel
%doc meta_package

%files common-devel
# qt6-base-common-devel 'provides' the development related directories
%dir %{_qt6_cmakedir}
%dir %{_qt6_cmakedir}/Qt6BuildInternals
%dir %{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests
%dir %{_qt6_descriptionsdir}
%dir %{_qt6_includedir}
%dir %{_qt6_metatypesdir}
%dir %{_qt6_mkspecsdir}
%dir %{_qt6_mkspecsdir}/modules
%{_bindir}/androiddeployqt6
%{_bindir}/androidtestrunner6
%{_bindir}/qdbuscpp2xml6
%{_bindir}/qdbusxml2cpp6
%{_bindir}/qmake6
%{_bindir}/qt-cmake6
%{_bindir}/qt-cmake-create6
%{_bindir}/qt-configure-module6
%{_bindir}/qtpaths6
%{_qt6_bindir}/androiddeployqt
%{_qt6_bindir}/androidtestrunner
%{_qt6_bindir}/qdbuscpp2xml
%{_qt6_bindir}/qdbusxml2cpp
%{_qt6_bindir}/qmake
%{_qt6_bindir}/qt-cmake
%{_qt6_bindir}/qt-cmake-create
%{_qt6_bindir}/qt-configure-module
%{_qt6_bindir}/qtpaths
%{_qt6_cmakedir}/Qt6/
%{_qt6_cmakedir}/Qt6BuildInternals/Qt6BuildInternalsConfig.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/Qt6BuildInternalsConfigVersion.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/Qt6BuildInternalsConfigVersionImpl.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/QtBuildInternalsExtra.cmake
%{_qt6_cmakedir}/Qt6BuildInternals/QtStandaloneTestTemplateProject/
%{_qt6_cmakedir}/Qt6BuildInternals/StandaloneTests/QtBaseTestsConfig.cmake
%{_qt6_cmakedir}/Qt6HostInfo/
%{_qt6_cmakedir}/Qt6TestInternalsPrivate/
%{_qt6_descriptionsdir}/TestInternalsPrivate.json
%{_qt6_libexecdir}/cmake_automoc_parser
%{_qt6_libexecdir}/moc
%{_qt6_libexecdir}/qlalr
%{_qt6_libexecdir}/qt-cmake-private
%{_qt6_libexecdir}/qt-cmake-private-install.cmake
%{_qt6_libexecdir}/qt-cmake-standalone-test
%{_qt6_libexecdir}/qt-internal-configure-examples
%{_qt6_libexecdir}/qt-internal-configure-tests
%{_qt6_libexecdir}/qvkgen
%{_qt6_libexecdir}/rcc
%{_qt6_libexecdir}/syncqt
%{_qt6_libexecdir}/tracegen
%{_qt6_libexecdir}/tracepointgen
%{_qt6_libexecdir}/uic
%{_qt6_mkspecsdir}/*
%{_qt6_pkgconfigdir}/Qt6Platform.pc
%exclude %{_qt6_mkspecsdir}/modules/*.pri

%files -n libQt6Concurrent6
%{_qt6_libdir}/libQt6Concurrent.so.*

%files -n qt6-concurrent-devel
%{_qt6_cmakedir}/Qt6Concurrent/
# upstream bug, there are no headers in include/QtConcurrent/<version>
%{_qt6_cmakedir}/Qt6ConcurrentPrivate/
%{_qt6_descriptionsdir}/Concurrent.json
%{_qt6_includedir}/QtConcurrent/
%{_qt6_libdir}/libQt6Concurrent.prl
%{_qt6_libdir}/libQt6Concurrent.so
%{_qt6_metatypesdir}/qt6concurrent_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_concurrent.pri
%{_qt6_pkgconfigdir}/Qt6Concurrent.pc

%files -n libQt6Core6
%license LICENSES/*
# libQt6Core6 'provides' the runtime directories except
# %%_qt6_importsdir and %%qt6_qmldir, owned by libQt6Qml6, %%_qt6_docdir
# owned by all documentation packages and %%_qt6_sysconfdir,
# owned by the filesystem package
%dir %{_qt6_archdatadir}
%dir %{_qt6_bindir}
%dir %{_qt6_datadir}
%dir %{_qt6_examplesdir}
%dir %{_qt6_libexecdir}
%dir %{_qt6_pluginsdir}
%dir %{_qt6_testsdir}
%dir %{_qt6_translationsdir}
%{_qt6_libdir}/libQt6Core.so.*

%files -n qt6-core-devel
%{_qt6_cmakedir}/Qt6Core/
%{_qt6_cmakedir}/Qt6CoreTools/
%{_qt6_descriptionsdir}/Core.json
%{_qt6_includedir}/QtCore/
%{_qt6_libdir}/libQt6Core.prl
%{_qt6_libdir}/libQt6Core.so
%{_qt6_metatypesdir}/qt6core_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_core.pri
# workaround for boo#1195368, QTBUG-100370
%{_qt6_mkspecsdir}/modules/qt_lib_core_private.pri
%{_qt6_pkgconfigdir}/Qt6Core.pc
%exclude %{_qt6_includedir}/QtCore/%{real_version}

%files -n qt6-core-private-devel
%{_qt6_cmakedir}/Qt6CorePrivate/
%dir %{_qt6_includedir}/QtCore/
%{_qt6_includedir}/QtCore/%{real_version}/

%files -n libQt6DBus6
%{_qt6_libdir}/libQt6DBus.so.*

%files -n qt6-dbus-devel
%{_qt6_cmakedir}/Qt6DBus/
%{_qt6_cmakedir}/Qt6DBusTools/
%{_qt6_descriptionsdir}/DBus.json
%{_qt6_includedir}/QtDBus/
%{_qt6_libdir}/libQt6DBus.prl
%{_qt6_libdir}/libQt6DBus.so
%{_qt6_metatypesdir}/qt6dbus_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_dbus.pri
%{_qt6_pkgconfigdir}/Qt6DBus.pc
%exclude %{_qt6_includedir}/QtDBus/%{real_version}

%files -n qt6-dbus-private-devel
%{_qt6_cmakedir}/Qt6DBusPrivate/
%dir %{_qt6_includedir}/QtDBus
%{_qt6_includedir}/QtDBus/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_dbus_private.pri

%files -n libQt6Gui6
%dir %{_qt6_pluginsdir}/platformthemes
%{_qt6_libdir}/libQt6EglFSDeviceIntegration.so.*
%{_qt6_libdir}/libQt6EglFsKmsGbmSupport.so.*
%{_qt6_libdir}/libQt6EglFsKmsSupport.so.*
%{_qt6_libdir}/libQt6Gui.so.*
%{_qt6_libdir}/libQt6XcbQpa.so.*
%{_qt6_pluginsdir}/egldeviceintegrations/
%{_qt6_pluginsdir}/generic/
%{_qt6_pluginsdir}/imageformats/
%{_qt6_pluginsdir}/platforminputcontexts/
%{_qt6_pluginsdir}/platforms/
%{_qt6_pluginsdir}/xcbglintegrations/

%files -n qt6-gui-devel
%{_qt6_cmakedir}/Qt6Gui/
%{_qt6_cmakedir}/Qt6GuiTools/
%{_qt6_descriptionsdir}/Gui.json
%{_qt6_includedir}/QtGui/
%{_qt6_libdir}/libQt6Gui.prl
%{_qt6_libdir}/libQt6Gui.so
%{_qt6_metatypesdir}/qt6gui_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_gui.pri
%{_qt6_pkgconfigdir}/Qt6Gui.pc
%exclude %{_qt6_includedir}/QtGui/%{real_version}

%files -n qt6-gui-private-devel
%{_qt6_cmakedir}/Qt6EglFSDeviceIntegrationPrivate/
%{_qt6_cmakedir}/Qt6EglFsKmsGbmSupportPrivate/
%{_qt6_cmakedir}/Qt6EglFsKmsSupportPrivate/
%{_qt6_cmakedir}/Qt6GuiPrivate/
%{_qt6_cmakedir}/Qt6XcbQpaPrivate/
%{_qt6_descriptionsdir}/EglFSDeviceIntegrationPrivate.json
%{_qt6_descriptionsdir}/EglFsKmsGbmSupportPrivate.json
%{_qt6_descriptionsdir}/EglFsKmsSupportPrivate.json
%{_qt6_descriptionsdir}/XcbQpaPrivate.json
%{_qt6_includedir}/QtEglFSDeviceIntegration/
%{_qt6_includedir}/QtEglFsKmsGbmSupport/
%{_qt6_includedir}/QtEglFsKmsSupport/
%dir %{_qt6_includedir}/QtGui
%{_qt6_includedir}/QtGui/%{real_version}/
%{_qt6_libdir}/libQt6EglFSDeviceIntegration.prl
%{_qt6_libdir}/libQt6EglFSDeviceIntegration.so
%{_qt6_libdir}/libQt6EglFsKmsGbmSupport.prl
%{_qt6_libdir}/libQt6EglFsKmsGbmSupport.so
%{_qt6_libdir}/libQt6EglFsKmsSupport.prl
%{_qt6_libdir}/libQt6EglFsKmsSupport.so
%{_qt6_libdir}/libQt6XcbQpa.prl
%{_qt6_libdir}/libQt6XcbQpa.so
%{_qt6_metatypesdir}/qt6eglfsdeviceintegrationprivate_*_metatypes.json
%{_qt6_metatypesdir}/qt6eglfskmsgbmsupportprivate_*_metatypes.json
%{_qt6_metatypesdir}/qt6eglfskmssupportprivate_*_metatypes.json
%{_qt6_metatypesdir}/qt6xcbqpaprivate_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_eglfs_kms_gbm_support_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_eglfs_kms_support_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_eglfsdeviceintegration_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_gui_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_xcb_qpa_lib_private.pri

%files -n libQt6Network6
%{_qt6_libdir}/libQt6Network.so.*

%files -n qt6-network-devel
%{_qt6_cmakedir}/Qt6Network/
%{_qt6_descriptionsdir}/Network.json
%{_qt6_includedir}/QtNetwork/
%{_qt6_libdir}/libQt6Network.prl
%{_qt6_libdir}/libQt6Network.so
%{_qt6_metatypesdir}/qt6network_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_network.pri
%{_qt6_pkgconfigdir}/Qt6Network.pc
%exclude %{_qt6_includedir}/QtNetwork/%{real_version}

%files -n qt6-network-private-devel
%{_qt6_cmakedir}/Qt6NetworkPrivate/
%dir %{_qt6_includedir}/QtNetwork
%{_qt6_includedir}/QtNetwork/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_network_private.pri

%files -n libQt6OpenGL6
%{_qt6_libdir}/libQt6OpenGL.so.*

%files -n qt6-opengl-devel
%{_qt6_cmakedir}/Qt6OpenGL/
%{_qt6_descriptionsdir}/OpenGL.json
%{_qt6_includedir}/QtOpenGL/
%{_qt6_libdir}/libQt6OpenGL.prl
%{_qt6_libdir}/libQt6OpenGL.so
%{_qt6_metatypesdir}/qt6opengl_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_opengl.pri
%{_qt6_pkgconfigdir}/Qt6OpenGL.pc
%exclude %{_qt6_includedir}/QtOpenGL/%{real_version}

%files -n qt6-opengl-private-devel
%{_qt6_cmakedir}/Qt6OpenGLPrivate/
%dir %{_qt6_includedir}/QtOpenGL
%{_qt6_includedir}/QtOpenGL/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_opengl_private.pri

%files -n libQt6OpenGLWidgets6
%{_qt6_libdir}/libQt6OpenGLWidgets.so.*

%files -n qt6-openglwidgets-devel
%{_qt6_cmakedir}/Qt6OpenGLWidgets/
# upstream bug, there are no headers in include/QtOpenGLWidgets/<version>
%{_qt6_cmakedir}/Qt6OpenGLWidgetsPrivate/
%{_qt6_descriptionsdir}/OpenGLWidgets.json
%{_qt6_includedir}/QtOpenGLWidgets/
%{_qt6_libdir}/libQt6OpenGLWidgets.prl
%{_qt6_libdir}/libQt6OpenGLWidgets.so
%{_qt6_metatypesdir}/qt6openglwidgets_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_openglwidgets.pri
%{_qt6_pkgconfigdir}/Qt6OpenGLWidgets.pc

%files -n libQt6PrintSupport6
%dir %{_qt6_pluginsdir}/printsupport
%{_qt6_libdir}/libQt6PrintSupport.so.*

%files -n qt6-printsupport-devel
%{_qt6_cmakedir}/Qt6PrintSupport/
%{_qt6_descriptionsdir}/PrintSupport.json
%{_qt6_includedir}/QtPrintSupport/
%{_qt6_libdir}/libQt6PrintSupport.prl
%{_qt6_libdir}/libQt6PrintSupport.so
%{_qt6_metatypesdir}/qt6printsupport_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_printsupport.pri
%{_qt6_pkgconfigdir}/Qt6PrintSupport.pc
%exclude %{_qt6_includedir}/QtPrintSupport/%{real_version}

%files -n qt6-printsupport-private-devel
%{_qt6_cmakedir}/Qt6PrintSupportPrivate/
%dir %{_qt6_includedir}/QtPrintSupport
%{_qt6_includedir}/QtPrintSupport/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_printsupport_private.pri

%files -n libQt6Sql6
%dir %{_qt6_pluginsdir}/sqldrivers
%{_qt6_libdir}/libQt6Sql.so.*

%files -n qt6-sql-devel
%{_qt6_cmakedir}/Qt6Sql/
%{_qt6_descriptionsdir}/Sql.json
%{_qt6_includedir}/QtSql/
%{_qt6_libdir}/libQt6Sql.prl
%{_qt6_libdir}/libQt6Sql.so
%{_qt6_mkspecsdir}/modules/qt_lib_sql.pri
%{_qt6_metatypesdir}/qt6sql_*_metatypes.json
%{_qt6_pkgconfigdir}/Qt6Sql.pc
%exclude %{_qt6_includedir}/QtSql/%{real_version}

%files -n qt6-sql-private-devel
%{_qt6_cmakedir}/Qt6SqlPrivate/
%dir %{_qt6_includedir}/QtSql
%{_qt6_includedir}/QtSql/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_sql_private.pri

%files -n libQt6Test6
%{_qt6_libdir}/libQt6Test.so.*

%files -n qt6-test-devel
%{_qt6_cmakedir}/Qt6Test/
%{_qt6_descriptionsdir}/Test.json
%{_qt6_includedir}/QtTest/
%{_qt6_libdir}/libQt6Test.prl
%{_qt6_libdir}/libQt6Test.so
%{_qt6_metatypesdir}/qt6test_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_testlib.pri
%{_qt6_pkgconfigdir}/Qt6Test.pc
%exclude %{_qt6_includedir}/QtTest/%{real_version}

%files -n qt6-test-private-devel
%{_qt6_cmakedir}/Qt6TestPrivate/
%dir %{_qt6_includedir}/QtTest
%{_qt6_includedir}/QtTest/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_testlib_private.pri

%files -n libQt6Widgets6
%{_qt6_libdir}/libQt6Widgets.so.*

%files -n qt6-widgets-devel
%{_qt6_cmakedir}/Qt6Widgets/
%{_qt6_descriptionsdir}/Widgets.json
%{_qt6_cmakedir}/Qt6WidgetsTools/
%{_qt6_includedir}/QtWidgets/
%{_qt6_libdir}/libQt6Widgets.prl
%{_qt6_libdir}/libQt6Widgets.so
%{_qt6_metatypesdir}/qt6widgets_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_widgets.pri
%{_qt6_pkgconfigdir}/Qt6Widgets.pc
%exclude %{_qt6_includedir}/QtWidgets/%{real_version}

%files -n qt6-widgets-private-devel
%{_qt6_cmakedir}/Qt6WidgetsPrivate/
%dir %{_qt6_includedir}/QtWidgets
%{_qt6_includedir}/QtWidgets/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_widgets_private.pri

%files -n libQt6Xml6
%{_qt6_libdir}/libQt6Xml.so.*

%files -n qt6-xml-devel
%{_qt6_cmakedir}/Qt6Xml/
%{_qt6_descriptionsdir}/Xml.json
%{_qt6_includedir}/QtXml/
%{_qt6_libdir}/libQt6Xml.prl
%{_qt6_libdir}/libQt6Xml.so
%{_qt6_metatypesdir}/qt6xml_*_metatypes.json
%{_qt6_mkspecsdir}/modules/qt_lib_xml.pri
%{_qt6_pkgconfigdir}/Qt6Xml.pc
%exclude %{_qt6_includedir}/QtXml/%{real_version}

%files -n qt6-xml-private-devel
%{_qt6_cmakedir}/Qt6XmlPrivate/
%dir %{_qt6_includedir}/QtXml
%{_qt6_includedir}/QtXml/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_xml_private.pri

%files -n qt6-docs-common
%dir %{_qt6_docdir}
%{_qt6_docdir}/config/
%{_qt6_docdir}/global/

### Static libraries ###

%files -n qt6-exampleicons-devel-static
%doc src/assets/icons/README
%{_qt6_cmakedir}/Qt6ExampleIconsPrivate/
%{_qt6_descriptionsdir}/ExampleIconsPrivate.json
%{_qt6_includedir}/QtExampleIcons/
%{_qt6_libdir}/libQt6ExampleIcons.a
%{_qt6_libdir}/libQt6ExampleIcons.prl
# There's no mistake, this folder needs to be installed
# These are CMake objects files which are not part of any library
%dir %{_qt6_archdatadir}/objects-*
%{_qt6_archdatadir}/objects-*/ExampleIconsPrivate_resources_1/
%{_qt6_metatypesdir}/qt6exampleiconsprivate_*_metatypes.json

%files -n qt6-kmssupport-devel-static
%{_qt6_cmakedir}/Qt6KmsSupportPrivate/
%{_qt6_descriptionsdir}/KmsSupportPrivate.json
%{_qt6_includedir}/QtKmsSupport/
%{_qt6_libdir}/libQt6KmsSupport.a
%{_qt6_libdir}/libQt6KmsSupport.prl
%{_qt6_metatypesdir}/qt6kmssupportprivate_*_metatypes.json
%exclude %{_qt6_includedir}/QtKmsSupport/%{real_version}

%files -n qt6-kmssupport-private-devel
%dir %{_qt6_includedir}/QtKmsSupport
%{_qt6_includedir}/QtKmsSupport/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_kms_support_private.pri

%files -n qt6-platformsupport-devel-static
%{_qt6_cmakedir}/Qt6DeviceDiscoverySupportPrivate/
%{_qt6_cmakedir}/Qt6FbSupportPrivate/
%{_qt6_cmakedir}/Qt6InputSupportPrivate/
%{_qt6_descriptionsdir}/DeviceDiscoverySupportPrivate.json
%{_qt6_descriptionsdir}/FbSupportPrivate.json
%{_qt6_descriptionsdir}/InputSupportPrivate.json
%{_qt6_includedir}/QtDeviceDiscoverySupport/
%{_qt6_includedir}/QtFbSupport/
%{_qt6_includedir}/QtInputSupport/
%{_qt6_libdir}/libQt6DeviceDiscoverySupport.a
%{_qt6_libdir}/libQt6DeviceDiscoverySupport.prl
%{_qt6_libdir}/libQt6FbSupport.a
%{_qt6_libdir}/libQt6FbSupport.prl
%{_qt6_libdir}/libQt6InputSupport.a
%{_qt6_libdir}/libQt6InputSupport.prl
%{_qt6_metatypesdir}/qt6devicediscoverysupportprivate_*_metatypes.json
%{_qt6_metatypesdir}/qt6fbsupportprivate_*_metatypes.json
%{_qt6_metatypesdir}/qt6inputsupportprivate_*_metatypes.json
%exclude %{_qt6_includedir}/QtDeviceDiscoverySupport/%{real_version}
%exclude %{_qt6_includedir}/QtFbSupport/%{real_version}
%exclude %{_qt6_includedir}/QtInputSupport/%{real_version}

%files -n qt6-platformsupport-private-devel
%dir %{_qt6_includedir}/QtDeviceDiscoverySupport
%dir %{_qt6_includedir}/QtFbSupport
%dir %{_qt6_includedir}/QtInputSupport
%{_qt6_includedir}/QtDeviceDiscoverySupport/%{real_version}/
%{_qt6_includedir}/QtFbSupport/%{real_version}/
%{_qt6_includedir}/QtInputSupport/%{real_version}/
%{_qt6_mkspecsdir}/modules/qt_lib_devicediscovery_support_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_fb_support_private.pri
%{_qt6_mkspecsdir}/modules/qt_lib_input_support_private.pri

### Plugins ###

%files -n qt6-networkinformation-glib
%dir %{_qt6_pluginsdir}/networkinformation/
%{_qt6_pluginsdir}/networkinformation/libqglib.so

%files -n qt6-networkinformation-nm
%dir %{_qt6_pluginsdir}/networkinformation/
%{_qt6_pluginsdir}/networkinformation/libqnetworkmanager.so

%files -n qt6-network-tls
%{_qt6_pluginsdir}/tls/

%files -n qt6-platformtheme-gtk3
%{_qt6_pluginsdir}/platformthemes/libqgtk3.so

%files -n qt6-platformtheme-xdgdesktopportal
%{_qt6_pluginsdir}/platformthemes/libqxdgdesktopportal.so

%files -n qt6-printsupport-cups
%{_qt6_pluginsdir}/printsupport/libcupsprintersupport.so

%files -n qt6-sql-mysql
%{_qt6_pluginsdir}/sqldrivers/libqsqlmysql.so

%files -n qt6-sql-postgresql
%{_qt6_pluginsdir}/sqldrivers/libqsqlpsql.so

%files -n qt6-sql-sqlite
%{_qt6_pluginsdir}/sqldrivers/libqsqlite.so

%files -n qt6-sql-unixODBC
%{_qt6_pluginsdir}/sqldrivers/libqsqlodbc.so

%endif

%changelog
