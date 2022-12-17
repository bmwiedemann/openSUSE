#
# spec file for package libqt5-qtbase
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


%define qt5_snapshot 1
%define journald 1

%ifarch %arm aarch64
%global gles 1
%else
%global gles 0
%endif

%global vulkan 1
%bcond_without harfbuzz

Name:           libqt5-qtbase
Version:        5.15.7+kde177
Release:        0
Summary:        C++ Program Library, Core Components
License:        LGPL-3.0-only or GPL-3.0-with-Qt-Company-Qt-exception-1.1
Group:          System/Libraries
Url:            https://www.qt.io
%define base_name libqt5
%define real_version 5.15.7
%define so_version 5.15.7
%define tar_version qtbase-everywhere-src-%{version}
Source:         %{tar_version}.tar.xz
# to get mtime of file:
Source1:        libqt5-qtbase.changes
Source2:        macros.qt5
Source3:        baselibs.conf
Source4:        qtlogging.ini
Source99:       libqt5-qtbase-rpmlintrc
# patches 0-999 are openSUSE and/or non-upstream(able) patches #
Patch3:         0001-Revert-QMenu-hide-when-a-QWidgetAction-fires-the-tri.patch
# Proposed: https://bugreports.qt.io/browse/QTBUG-88491
Patch4:         0001-Avoid-SIGABRT-on-platform-plugin-initialization-fail.patch
# PATCH-FIX-OPENSUSE disable-rc4-ciphers-bnc865241.diff bnc#865241-- Exclude rc4 ciphers from being used by default
Patch6:         disable-rc4-ciphers-bnc865241.diff
Patch8:         tell-the-truth-about-private-api.patch
# PATCH-FIX-OPENSUSE libqt5-prioritise-gtk2-platformtheme.patch boo#1002900 -- Give Gtk2 Platform Theme (from qtstyleplugins) a priority over Gtk3 PT which currently lacks QGtk3Style.
Patch10:        libqt5-prioritise-gtk2-platformtheme.patch
# PATCH-FEATURE-OPENSUSE 0001-Add-remote-print-queue-support.patch fate#322052 -- Automatically recognize and allow printing to remote cups servers
Patch12:        0001-Add-remote-print-queue-support.patch
# PATCH-FIX-OPENSUSE
Patch21:        0001-Don-t-white-list-recent-Mesa-versions-for-multithrea.patch
Patch24:        fix-fixqt4headers.patch
# patches 1000-2000 and above from upstream 5.15 branch #
# patches 2000-3000 and above from upstream qt6/dev branch #
# Not accepted yet, https://codereview.qt-project.org/c/qt/qtbase/+/255384
Patch2001:      0002-Synthesize-Enter-LeaveEvent-for-accepted-QTabletEven.patch
BuildRequires:  cups-devel
BuildRequires:  double-conversion-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libpng-devel
BuildRequires:  libproxy-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(mtdev)
%if %qt5_snapshot
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  postgresql-devel
BuildRequires:  sqlite3-devel
BuildRequires:  unixODBC-devel
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
%if %gles
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  pkgconfig(glesv2)
%endif
BuildRequires:  libicu-devel
BuildRequires:  tslib-devel
%if %{vulkan}
BuildRequires:  vulkan-devel
%endif

BuildRequires:  pkgconfig(pango)
# Not packaged yet
#BuildRequires:  pkgconfig(md4c)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-sync)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-xinerama)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  xz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
%if %{with harfbuzz}
BuildRequires:  pkgconfig(harfbuzz)
%endif
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xkbcommon) >= 0.4.1
BuildRequires:  pkgconfig(xkbcommon-x11) >= 0.4.1
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)
%if %journald
BuildRequires:  pkgconfig(libsystemd)
%endif
# to get cmake(...) autoprovides
BuildRequires:  cmake

%description
Qt is a set of libraries for developing applications.

This package contains base tools, like string, xml, and network
handling.

%define libqt5_prefix		%{_prefix}
%define libqt5_libdir		%{_libdir}
%define libqt5_archdatadir	%{_libdir}/qt5
%define libqt5_bindir		%{libqt5_archdatadir}/bin
%define libqt5_datadir		%{_datadir}/qt5
%define libqt5_docdir		%{_docdir}/qt5
%define libqt5_examplesdir	%{libqt5_archdatadir}/examples
%define libqt5_includedir	%{_includedir}/qt5
%define libqt5_importdir	%{libqt5_archdatadir}/imports
%define libqt5_libexecdir	%{libqt5_archdatadir}/libexec
%define libqt5_plugindir	%{libqt5_archdatadir}/plugins
%define libqt5_sysconfdir	%{_sysconfdir}/xdg
%define libqt5_translationdir	%{libqt5_datadir}/translations

%prep
%autosetup -p1 -n %{tar_version}

# be sure not to use them
rm -rf src/3rdparty/{libjpeg,freetype,zlib}

%package devel
Summary:        Development files for the Qt5 base library
Group:          Development/Libraries/X11
# External deps shall be found via pkgconfig
Requires:       %{name}-common-devel
Requires:       libQt5Concurrent-devel = %{version}
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5DBus-devel = %{version}
Requires:       libQt5Gui-devel = %{version}
Requires:       libQt5Network-devel = %{version}
Requires:       libQt5OpenGL-devel = %{version}
Requires:       libQt5PlatformHeaders-devel = %{version}
Requires:       libQt5PrintSupport-devel = %{version}
Requires:       libQt5Sql-devel = %{version}
Requires:       libQt5Test-devel = %{version}
Requires:       libQt5Widgets-devel = %{version}
Requires:       libQt5Xml-devel = %{version}

%description devel
You need this package if you want to compile programs with Qt. It
contains the "Qt Crossplatform Development Kit". It does contain
include files and development applications like GUI designers,
translator tools and code generators.

%package common-devel
Summary:        Qt 5 Core Development Binaries
Group:          Development/Libraries/X11
Requires:       gcc-c++
Requires:       pkg-config
# to get cmake(...) autoprovides
Requires:       cmake

%description common-devel
Qt 5 Core Development Binaries. It contains Qt5's moc, qmake,
rcc, uic and syncqt.pl binaries.

%package -n libQt5Core5
Summary:        Qt 5 Core Library
Group:          Development/Libraries/X11
Provides:       libqt5-qtbase = %{version}
Obsoletes:      libqt5-qtbase < %{version}
Recommends:     libqt5-qttranslations

%description -n libQt5Core5
The Qt 5 Core library. It adds these features to C++:

* a mechanism for object communication called signals and slots
* queryable and designable object properties
* hierarchical and queryable object trees that organize
* object ownership in a natural way with guarded pointers (QPointer)
* a dynamic cast that works across library boundaries

%package -n libQt5Core-devel
Summary:        Development files for the Qt5 core library
Group:          Development/Libraries/X11
Requires:       %{name}-common-devel = %{version}
Requires:       libQt5Core5 = %{version}

%description -n libQt5Core-devel
Development files for the Qt5 core library.

%package -n libQt5Core-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 core library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-devel = %{version}

%description -n libQt5Core-private-headers-devel
This package provides private headers of libQt5Core that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libQt5Concurrent5
Summary:        Qt 5 Concurrent Library
Group:          Development/Libraries/X11
Requires:       libQt5Core5 = %{version}

%description -n libQt5Concurrent5
The QtConcurrent namespace provides high-level APIs that help write
multi-threaded programs without using low-level threading primitives
such as mutexes, read-write locks, wait conditions, or semaphores.
Programs written with QtConcurrent automatically adjust the number of
threads used according to the number of processor cores available.

QtConcurrent includes functional programming style APIs for parallel
list processing, including a MapReduce and FilterReduce
implementation for shared-memory (non-distributed) systems, and
classes for managing asynchronous computations in GUI applications.

%package -n libQt5Concurrent-devel
Summary:        Development files for the Qt5 Concurrent library
Group:          Development/Libraries/X11
Requires:       libQt5Concurrent5 = %{version}
Requires:       libQt5Core-devel = %{version}

%description -n libQt5Concurrent-devel
Development files for the Qt5 Concurrent library.

%package -n libQt5DBus5
Summary:        Qt5 D-Bus library
Group:          Development/Libraries/X11
Requires:       libQt5Core5 = %{version}

%description -n libQt5DBus5
The Qt D-Bus module is a library that can be used to perform
inter-process communication using the D-Bus protocol.

%package -n libQt5DBus-devel
Summary:        Development files for the Qt5 D-Bus library
Group:          Development/Libraries/X11
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5DBus5 = %{version}

%description -n libQt5DBus-devel
Development files for the Qt5 D-Bus library. This package also
contains Qt5's qdbusxml2cpp and qdbuscpp2xml binaries.

%package -n libQt5DBus-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 D-Bus library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5DBus-devel = %{version}

%description -n libQt5DBus-private-headers-devel
This package provides private headers of libQt5DBus that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libQt5Network5
Summary:        Qt 5 Network Library
Group:          Development/Libraries/X11
Requires:       libQt5Core5 = %{version}
Requires:       libQt5DBus5 = %{version}

%description -n libQt5Network5
Qt Network provides a set of APIs for programming applications that
use TCP/IP. Operations such as requests, cookies, and sending data
over HTTP are handled by various C++ classes.

%package -n libQt5Network-devel
Summary:        Development files for the Qt5 network library
Group:          Development/Libraries/X11
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Network5 = %{version}

%description -n libQt5Network-devel
Development files for the Qt5 network library.

%package -n libQt5Network-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 network library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5Network-devel = %{version}

%description -n libQt5Network-private-headers-devel
This package provides private headers of libQt5Network that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libQt5OpenGL5
Summary:        Qt 5 OpenGL Library
Group:          Development/Libraries/X11
Requires:       libQt5Widgets5 = %{version}

%description -n libQt5OpenGL5
The Qt OpenGL module provides an OpenGL widget class that can be used
like any other Qt widget, except that it opens an OpenGL display
buffer where the OpenGL API can be used to render the contents.

%package -n libQt5OpenGL-devel
Summary:        Development files for the Qt5 OpenGL library
Group:          Development/Libraries/X11
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Gui-devel = %{version}
Requires:       libQt5OpenGL5 = %{version}
Requires:       libQt5Widgets-devel = %{version}
%if %gles
Requires:       Mesa-libGLESv3-devel
Requires:       pkgconfig(glesv2)
%else
Requires:       pkgconfig(gl)
%endif

%description -n libQt5OpenGL-devel
Development files for the Qt5 OpenGL library.

Warning: This module should not be used anymore for new code. Please
use the corresponding OpenGL classes in Qt GUI.

%package -n libQt5OpenGL-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 OpenGL library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5Gui-private-headers-devel = %{version}
Requires:       libQt5OpenGL-devel = %{version}
Requires:       libQt5Widgets-private-headers-devel = %{version}

%description -n libQt5OpenGL-private-headers-devel
This package provides private headers of libQt5OpenGL that are
normally not used by application development and that do not have any
ABI or API guarantees. The packages that build against these have to
require the exact Qt version.

%package -n libQt5PrintSupport5
Summary:        Qt 5 Print Support Library
Group:          Development/Libraries/X11
Requires:       libQt5Widgets5 = %{version}

%description -n libQt5PrintSupport5
An abstraction over the platform-specific printing systems. Using
this library, Qt applications can print to attached printers and
across networks to remote printers. Qt's printing system also
supports PDF file generation, providing the foundation for basic
report generation facilities.

%package -n libQt5PrintSupport-devel
Summary:        Development files for the Qt5 print support library
Group:          Development/Libraries/X11
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Gui-devel = %{version}
Requires:       libQt5PrintSupport5 = %{version}
Requires:       libQt5Widgets-devel = %{version}

%description -n libQt5PrintSupport-devel
Development files for the Qt5 print support library.

%package -n libQt5PrintSupport-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 print support library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5Gui-private-headers-devel = %{version}
Requires:       libQt5PrintSupport-devel = %{version}
Requires:       libQt5Widgets-private-headers-devel = %{version}
# Includes <cups/ppd.h> in qprint_p.h
Requires:       cups-devel

%description -n libQt5PrintSupport-private-headers-devel
This package provides private headers of libQt5PrintSupport that are
normally not used by application development and that do not have any
ABI or API guarantees. The packages that build against these have to
require the exact Qt version.

%package -n libQt5Xml5
Summary:        Qt 5 Xml Library
Group:          Development/Libraries/X11
Requires:       libQt5Core5 = %{version}

%description -n libQt5Xml5
The Qt XML module provides C++ implementations of the SAX and DOM
standards for XML.

%package -n libQt5Xml-devel
Summary:        Development files for the Qt5 XML library
Group:          Development/Libraries/X11
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Xml5 = %{version}

%description -n libQt5Xml-devel
Development files for the Qt5 XML library.

(The module is not actively maintained anymore. Please use the
QXmlStreamReader and QXmlStreamWriter classes in Qt Core instead.)

%package -n libQt5Test5
Summary:        Qt 5 Test Library
Group:          Development/Libraries/X11
Requires:       libQt5Core5 = %{version}

%description -n libQt5Test5
Qt Test is a framework for unit testing Qt based applications and
libraries. Qt Test provides functionality commonly found in unit
testing frameworks as well as extensions for testing graphical user
interfaces.

%package -n libQt5Test-devel
Summary:        Development files for the Qt5 testing library
Group:          Development/Libraries/X11
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Test5 = %{version}

%description -n libQt5Test-devel
Development files for the Qt5 testing library.

%package -n libQt5Test-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 test library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5Test-devel = %{version}

%description -n libQt5Test-private-headers-devel
This package provides private headers of libQt5Test that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libQt5Widgets5
Summary:        Qt 5 Widgets Library
Group:          Development/Libraries/X11
Requires:       libQt5Gui5 = %{version}

%description -n libQt5Widgets5
The Qt Widgets Module provides a set of UI elements to create classic
desktop-style user interfaces.

%package -n libQt5Widgets-devel
Summary:        Development files for the Qt5 widgets library
Group:          Development/Libraries/X11
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Gui-devel = %{version}
Requires:       libQt5Widgets5 = %{version}

%description -n libQt5Widgets-devel
Development files for the Qt5 widgets library.

%package -n libQt5Widgets-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 widgets library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5Gui-private-headers-devel = %{version}
Requires:       libQt5Widgets-devel = %{version}

%description -n libQt5Widgets-private-headers-devel
This package provides private headers of libQt5Widgets that are
normally not used by application development and that do not have any
ABI or API guarantees. The packages that build against these have to
require the exact Qt version.

%package -n libQt5Sql5-sqlite
Summary:        Qt 5 sqlite plugin
Group:          Development/Libraries/C and C++
Requires:       libQt5Sql5 = %{version}
Provides:       libqt5-sql-sqlite = %{version}
Provides:       libqt5_sql_backend = %{version}
Obsoletes:      libqt5-sql-sqlite < %{version}

%description -n libQt5Sql5-sqlite
The Qt SQL module uses driver plugins to communicate with the
different database APIs.

The Qt SQLite plugin makes it possible to access SQLite databases.
SQLite is an in-process database, which means that it is not
necessary to have a database server. SQLite operates on a single
file, which must be set as the database name when opening a
connection.

%package -n libQt5Sql5-unixODBC
Summary:        Qt 5 unixODBC plugin
Group:          Development/Libraries/C and C++
Requires:       libQt5Sql5 = %{version}
Provides:       libqt5-sql-unixODBC = %{version}
Provides:       libqt5_sql_backend = %{version}
Obsoletes:      libqt5-sql-unixODBC < %{version}

%description -n libQt5Sql5-unixODBC
The Qt SQL module uses driver plugins to communicate with the
different database APIs.

The QODBC driver allows to connect to an ODBC driver manager and
access the available data sources. Note that you also need to install
and configure ODBC drivers for the ODBC driver manager that is
installed on your system.

%package -n libQt5Sql5-postgresql
Summary:        Qt 5 PostgreSQL plugin
Group:          Development/Libraries/C and C++
Requires:       libQt5Sql5 = %{version}
Provides:       libqt5-sql-postgresql = %{version}
Provides:       libqt5_sql_backend = %{version}
Obsoletes:      libqt5-sql-postgresql < %{version}

%description -n libQt5Sql5-postgresql
The Qt SQL module uses driver plugins to communicate with the
different database APIs.

The QPSQL driver supports version 7.3 and higher of the PostgreSQL
server.

%package -n libQt5Sql5-mysql
Summary:        Qt 5 MySQL support
Group:          Development/Libraries/C and C++
Requires:       libQt5Sql5 = %{version}
Provides:       libqt5-sql-mysql = %{version}
Provides:       libqt5_sql_backend = %{version}
Obsoletes:      libqt5-sql-mysql < %{version}

%description -n libQt5Sql5-mysql
A plugin to support MySQL server in Qt applications.

%package -n libQt5Gui5
Summary:        Qt 5 GUI related libraries
Group:          Development/Libraries/C and C++
Recommends:     libqt5-qtimageformats = %{version}
Requires:       libQt5Core5 = %{version}
Requires:       libQt5DBus5 = %{version}
Provides:       libqt5-qtbase-platformtheme-gtk2 = %{version}
Obsoletes:      libqt5-qtbase-platformtheme-gtk2 < %{version}

%description -n libQt5Gui5
The Qt GUI module provides classes for windowing system integration,
event handling, OpenGL and OpenGL ES integration, 2D graphics, basic
imaging, fonts and text. These classes are used internally by Qt's
user interface code and can also be used directly, for instance, to
write applications using low-level OpenGL ES graphics APIs.

For application developers writing user interfaces, Qt provides
higher level APIs, like Qt Quick, which are much more suitable than
the enablers found in the Qt GUI module.

%package platformtheme-gtk3
Summary:        Qt 5 gtk3 plugin
Group:          Development/Libraries/C and C++
Supplements:    packageand(libQt5Gui5:libgtk-3-0)
Requires:       libQt5Gui5 = %{version}

%description platformtheme-gtk3
Qt 5 plugin for better integration with gtk3-based desktop enviroments.

%package platformtheme-xdgdesktopportal
Summary:        Qt 5 XDG Desktop Portal Plugin
Group:          Development/Libraries/C and C++
Requires:       libQt5Gui5 = %{version}
Obsoletes:      %{name}-platformtheme-flatpak < %{version}
Provides:       %{name}-platformtheme-flatpak = %{version}

%description platformtheme-xdgdesktopportal
Qt 5 plugin for integration with flatpak and snap.

%package -n libQt5Gui-devel
Summary:        Development files for the Qt5 GUI library
Group:          Development/Libraries/C and C++
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Gui5 = %{version}
%if %gles
Requires:       Mesa-libGLESv3-devel
Requires:       pkgconfig(gbm)
Requires:       pkgconfig(glesv2)
%else
Requires:       pkgconfig(gl)
%endif
%if %{vulkan}
Requires:       vulkan-devel
%endif
Requires:       pkgconfig(egl)
Requires:       pkgconfig(libdrm)

%description -n libQt5Gui-devel
Development files for the Qt5 GUI library.

%package -n libQt5Gui-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 GUI library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5Gui-devel = %{version}

%description -n libQt5Gui-private-headers-devel
This package provides private headers of libQt5Gui that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libQt5Sql5
Summary:        Qt 5 SQL related libraries
Group:          Development/Libraries/C and C++
Recommends:     libqt5_sql_backend = %{version}
Suggests:       libqt5-sql-sqlite
Requires:       libQt5Core5 = %{version}

%description -n libQt5Sql5
Qt 5 libraries which are used for connection with an SQL server. You
will need also a plugin package for a supported SQL server.

%package -n libQt5Sql-devel
Summary:        Development files for the Qt5 SQL library
Group:          Development/Libraries/C and C++
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Sql5 = %{version}
Suggests:       libQt5Sql5-mysql = %{version}
Suggests:       libQt5Sql5-postgresql = %{version}
Suggests:       libQt5Sql5-sqlite = %{version}
Suggests:       libQt5Sql5-unixODBC = %{version}

%description -n libQt5Sql-devel
Qt 5 libraries which are used for connection with an SQL server. You
will need also a plugin package for a supported SQL server.

%package -n libQt5Sql-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 SQL library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5Sql-devel = %{version}

%description -n libQt5Sql-private-headers-devel
This package provides private headers of libQt5Sql that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package private-headers-devel
Summary:        Non-ABI stable experimental API
Group:          Development/Libraries/C and C++
BuildArch:      noarch
Requires:       %{name}-devel = %{version}
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5DBus-private-headers-devel = %{version}
Requires:       libQt5Gui-private-headers-devel = %{version}
Requires:       libQt5KmsSupport-private-headers-devel = %{version}
Requires:       libQt5Network-private-headers-devel = %{version}
Requires:       libQt5OpenGL-private-headers-devel = %{version}
Requires:       libQt5PlatformSupport-private-headers-devel = %{version}
Requires:       libQt5PrintSupport-private-headers-devel = %{version}
Requires:       libQt5Sql-private-headers-devel = %{version}
Requires:       libQt5Test-private-headers-devel = %{version}
Requires:       libQt5Widgets-private-headers-devel = %{version}

%description private-headers-devel
This package provides private headers of libqt5-qtbase-devel that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package -n libQt5Bootstrap-devel-static
Summary:        Qt Bootstrap module
Group:          Development/Libraries/C and C++
Requires:       %{name}-common-devel = %{version}

%description -n libQt5Bootstrap-devel-static
Qt Bootstrap module.

%package -n libQt5OpenGLExtensions-devel-static
Summary:        Qt OpenGLExtensions module
Group:          Development/Libraries/C and C++
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Gui-devel = %{version}
# List the below ones manually - they are private, but this is a static lib
Requires:       pkgconfig(gl)

%description -n libQt5OpenGLExtensions-devel-static
Qt OpenGLExtensions module.

%package -n libQt5PlatformSupport-devel-static
Summary:        Qt PlatformSupport module
Group:          Development/Libraries/C and C++
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Gui-devel = %{version}
Requires:       libQt5PlatformHeaders-devel = %{version}
# List the below ones manually - they are private, but this is a static lib
Requires:       tslib-devel
Requires:       pkgconfig(Qt5DBus)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libinput)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(mtdev)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xkbcommon) >= 0.4.1
Requires:       pkgconfig(xkbcommon-x11) >= 0.4.1
Requires:       pkgconfig(xrender)

%description -n libQt5PlatformSupport-devel-static
Qt PlatformSupport module.

%package -n libQt5PlatformSupport-private-headers-devel
Summary:        Non-ABI stable experimental API for the  Qt5 platform support library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5Gui-private-headers-devel = %{version}
Requires:       libQt5PlatformSupport-devel-static = %{version}

%description -n libQt5PlatformSupport-private-headers-devel
This package provides private headers of libQt5PlatformSupport that
are normally not used by application development and that do not have
any ABI or API guarantees. The packages that build against these have
to require the exact Qt version.

%package -n libQt5KmsSupport-devel-static
Summary:        Qt KMS support module
Group:          Development/Libraries/X11
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Gui-devel = %{version}

%description -n libQt5KmsSupport-devel-static
Qt module to support Kernel Mode Setting.

%package -n libQt5KmsSupport-private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 KMS support library
Group:          Development/Libraries/X11
BuildArch:      noarch
Requires:       libQt5Core-private-headers-devel = %{version}
Requires:       libQt5Gui-private-headers-devel = %{version}
Requires:       libQt5KmsSupport-devel-static = %{version}

%description -n libQt5KmsSupport-private-headers-devel
This package provides private headers of libQt5KmsSupport that are
normally not used by application development and that do not have any
ABI or API guarantees. The packages that build against these have to
require the exact Qt version.

%package -n libQt5PlatformHeaders-devel
Summary:        Qt 5 PlatformHeaders
Group:          Development/Libraries/X11
# NOTE this needs to be checked on every update - package provides only a low number of headers, so check which 3rd party, or other qtbase includes are used
Requires:       libQt5Core-devel = %{version}
Requires:       libQt5Gui-devel = %{version}
Requires:       pkgconfig(egl)
Requires:       pkgconfig(x11)
%if %gles
Requires:       Mesa-libGLESv3-devel
Requires:       pkgconfig(glesv2)
%else
Requires:       pkgconfig(gl)
%endif

%description -n libQt5PlatformHeaders-devel
Qt 5 PlatformHeaders.

%package examples
Summary:        Qt5 base examples
Group:          Development/Libraries/X11
Recommends:     libqt5-qtbase-devel

%description examples
Examples for the libqt5-qtbase modules.

%build
%define _lto_cflags %{nil}
%ifarch ppc64
  RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="$CXXFLAGS %{optflags} -DOPENSSL_LOAD_CONF"
export CFLAGS="$CFLAGS %{optflags} -DOPENSSL_LOAD_CONF"
export MAKEFLAGS="%{?_smp_mflags}"
%define xkbconfigroot %(pkg-config --variable=xkb_base xkeyboard-config)
#if %qt5_snapshot
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
#endif
# Record mtime of changes file instead of build time
export CHANGES=`stat --format="%y" %{SOURCE1}|cut --characters=1-10`
sed -i 's|qt_instdate=`date +%Y-%m-%d`|qt_instdate=$CHANGES|g' configure
# so non-qt5 apps/libs don't get stripped
sed -i -e 's|^\(QMAKE_STRIP.*=\).*$|\1|g' mkspecs/common/linux.conf

# -no-feature-relocatable is needed to support /usr/lib/sse2 etc., see QTBUG-78948
# -reduce-relocations means copy relocations aren't allowed, and so special
# flags like -fPIC need to be passed when building an application. This breaks
# with LTO (PIE overrides that) and CMake (doesn't pass -fPIC when linking).
# Due to a binutils bug/misunderstanding, this option didn't do as much before 2.35,
# so just disable it for now until a proper alternative appears.

./configure \
	-prefix %{_prefix} \
	-L %{libqt5_libdir} \
	-libdir %{libqt5_libdir} \
	-archdatadir %{libqt5_archdatadir} \
	-bindir %{libqt5_bindir} \
	-datadir %{libqt5_datadir} \
	-docdir %{libqt5_docdir} \
	-examplesdir %{libqt5_examplesdir} \
	-headerdir %{libqt5_includedir} \
	-importdir %{libqt5_importdir} \
	-libexecdir %{libqt5_libexecdir} \
	-plugindir %{libqt5_plugindir} \
	-sysconfdir %{libqt5_sysconfdir} \
	-translationdir %{libqt5_translationdir} \
	-verbose \
	-no-reduce-relocations \
%ifarch %ix86
%if 0%{?sle_version} < 150000
	-no-sse2 -no-pch \
%endif
%endif
	-accessibility \
	-no-strip \
	-opensource \
	-confirm-license \
	-no-separate-debug-info \
	-force-debug-info \
	-shared \
	-xkbcommon \
	-no-bundled-xcb-xinput \
	-dbus-linked \
	-sm \
	-no-rpath \
	-system-libjpeg \
	-openssl-linked \
	-system-libpng \
%if %{with harfbuzz}
	-system-harfbuzz \
%endif
	-fontconfig \
	-system-freetype \
	-cups \
	-system-zlib \
	-zstd \
	-no-pch \
	-glib \
	-sctp \
	-system-sqlite \
%if %journald
	-journald \
%endif
	-libproxy \
	-xcb \
	-egl \
	-eglfs \
%if %gles
	-kms \
	-opengl es2 \
%else
	-opengl desktop \
%endif
	-release \
	-plugin-sql-sqlite -nomake tests \
	-plugin-sql-psql -I/usr/include/pgsql/ -I/usr/include/pgsql/server \
	-plugin-sql-odbc \
	-plugin-sql-mysql -I/usr/include/mysql/ \
	-no-feature-relocatable \
	QMAKE_CFLAGS+="$CFLAGS" \
	QMAKE_CXXFLAGS+="$CXXFLAGS"

make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%ifarch %ix86
%if 0%{?sle_version} < 150000
install -d %{buildroot}%{libqt5_libdir}/sse2/

pushd src/corelib; make clean ; ../../bin/qmake -config sse2; make %{?_smp_mflags}
cp -av ../../lib/libQt5Core.so.* %{buildroot}%{libqt5_libdir}/sse2/
popd

pushd src/gui; ../../bin/qmake -config sse2; make %{?_smp_mflags}
cp -av ../../lib/libQt5Gui.so.* %{buildroot}%{libqt5_libdir}/sse2/
popd
%endif
%endif

install -D -m644 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt5
# argggh, qmake is such a piece of <censored>
find %{buildroot}%{libqt5_libdir} -type f -name '*prl' -exec perl -pi -e "s, -L$RPM_BUILD_DIR/\S+,,g" {} +
find %{buildroot}%{libqt5_libdir} -type f -name '*prl' -exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" {} +
find %{buildroot}%{libqt5_libdir} -type f -name '*la' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} +
# insanity ...
find %{buildroot}%{libqt5_libdir} -type f -name '*pc' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} + -exec sed -i -e "s,^moc_location=.*,moc_location=%libqt5_bindir/moc," -e "s,uic_location=.*,uic_location=%libqt5_bindir/uic," {} +
find %{buildroot}%{libqt5_libdir}/ -name 'lib*.a' -exec chmod -x -- {} +
# kill .la files
rm -fv %{buildroot}%{libqt5_libdir}/lib*.la

# Not sure why these are deleted, but apparently we don't need them?
rm -fv %{buildroot}%{libqt5_libdir}/cmake/Qt5*/Q*Plugin.cmake

# This is only for Apple platforms and has a python2 dep
rm -r %{buildroot}%{libqt5_archdatadir}/mkspecs/features/uikit

# Link all the binaries with -qt5 suffix to %{_bindir}
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{libqt5_bindir}
for i in * ; do
  case "${i}" in
    moc|qdbuscpp2xml|qdbusxml2cpp|qmake|rcc|syncqt|uic)
      ln -s %{libqt5_bindir}/$i %{buildroot}%{_bindir}/${i}-qt5
      ;;
   *)
      # No conflict with Qt4, so keep the original name for compatibility
      ln -s %{libqt5_bindir}/$i %{buildroot}%{_bindir}/${i}-qt5
      ln -s %{libqt5_bindir}/$i %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

chmod 644 %{buildroot}%{libqt5_docdir}/global/template/images/*.png

# Silence logging of xcb errors and qml deprecated connection
# warnings by default
install -Dm644 %{SOURCE4} %{buildroot}%{libqt5_datadir}/qtlogging.ini

%post -n libQt5Core5 -p /sbin/ldconfig

%post -n libQt5Concurrent5 -p /sbin/ldconfig

%post -n libQt5DBus5 -p /sbin/ldconfig

%post -n libQt5Network5 -p /sbin/ldconfig

%post -n libQt5OpenGL5 -p /sbin/ldconfig

%post -n libQt5PrintSupport5 -p /sbin/ldconfig

%post -n libQt5Xml5 -p /sbin/ldconfig

%post -n libQt5Gui5 -p /sbin/ldconfig

%post -n libQt5Sql5 -p /sbin/ldconfig

%post -n libQt5Test5 -p /sbin/ldconfig

%post -n libQt5Widgets5 -p /sbin/ldconfig

%postun -n libQt5Core5 -p /sbin/ldconfig

%postun -n libQt5Concurrent5 -p /sbin/ldconfig

%postun -n libQt5DBus5 -p /sbin/ldconfig

%postun -n libQt5Network5 -p /sbin/ldconfig

%postun -n libQt5OpenGL5 -p /sbin/ldconfig

%postun -n libQt5PrintSupport5 -p /sbin/ldconfig

%postun -n libQt5Xml5 -p /sbin/ldconfig

%postun -n libQt5Gui5 -p /sbin/ldconfig

%postun -n libQt5Sql5 -p /sbin/ldconfig

%postun -n libQt5Test5 -p /sbin/ldconfig

%postun -n libQt5Widgets5 -p /sbin/ldconfig

%files common-devel
%license LICENSE.*
%doc *.txt
%{_rpmconfigdir}/macros.d/macros.qt5
%{_bindir}/moc*
%{libqt5_bindir}/moc*
%{_bindir}/qmake*
%{libqt5_bindir}/qmake*
%{_bindir}/rcc*
%{libqt5_bindir}/rcc*
%{_bindir}/uic*
%{libqt5_bindir}/uic*
%{_bindir}/qvkgen*
%{libqt5_bindir}/qvkgen*
%{_bindir}/tracegen*
%{libqt5_bindir}/tracegen*
%{_bindir}/syncqt.pl*
%{_bindir}/fixqt4headers.pl*
%{libqt5_bindir}/syncqt.pl*
%{libqt5_bindir}/fixqt4headers.pl*
%{_bindir}/qlalr*
%{libqt5_bindir}/qlalr*
%{libqt5_archdatadir}/mkspecs/
%dir %{libqt5_libdir}/cmake
%dir %{libqt5_includedir}
%dir %{libqt5_archdatadir}
%dir %{libqt5_bindir}

%files -n libQt5Core5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Core.so.*
%ifarch %ix86
%if 0%{?sle_version} < 150000
%dir %{libqt5_libdir}/sse2
%{libqt5_libdir}/sse2/libQt5Core.so.*
%endif
%endif
%dir %{libqt5_datadir}
%{libqt5_datadir}/qtlogging.ini

%files -n libQt5Core-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Core.so
%{libqt5_libdir}/libQt5Core.prl
%{libqt5_libdir}/cmake/Qt5Core/
%{libqt5_libdir}/cmake/Qt5/
%{libqt5_libdir}/pkgconfig/Qt5Core.pc
%{libqt5_includedir}/QtCore/
%dir %{libqt5_libdir}/metatypes/
%{libqt5_libdir}/metatypes/qt5core_metatypes.json
%exclude %{libqt5_includedir}/QtCore/%{so_version}
%{libqt5_docdir}

%files -n libQt5Concurrent5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Concurrent.so.*

%files -n libQt5Concurrent-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Concurrent.so
%{libqt5_libdir}/libQt5Concurrent.prl
%{libqt5_libdir}/cmake/Qt5Concurrent/
%{libqt5_libdir}/pkgconfig/Qt5Concurrent.pc
%{libqt5_includedir}/QtConcurrent/

%files -n libQt5DBus5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5DBus.so.*

%files -n libQt5DBus-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5DBus.so
%{libqt5_libdir}/libQt5DBus.prl
%{libqt5_libdir}/cmake/Qt5DBus/
%{libqt5_libdir}/pkgconfig/Qt5DBus.pc
%{libqt5_includedir}/QtDBus/
%exclude %{libqt5_includedir}/QtDBus/%{so_version}
%{libqt5_bindir}/qdbusxml2cpp*
%{_bindir}/qdbusxml2cpp*
%{libqt5_bindir}/qdbuscpp2xml*
%{_bindir}/qdbuscpp2xml*

%files -n libQt5Network5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Network.so.*
%dir %{libqt5_libdir}/qt5
%dir %{libqt5_plugindir}
%{libqt5_plugindir}/bearer

%files -n libQt5Network-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Network.so
%{libqt5_libdir}/libQt5Network.prl
%{libqt5_libdir}/cmake/Qt5Network/
%{libqt5_libdir}/pkgconfig/Qt5Network.pc
%{libqt5_includedir}/QtNetwork/
%exclude %{libqt5_includedir}/QtNetwork/%{so_version}

%files -n libQt5OpenGL5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5OpenGL.so.*

%files -n libQt5OpenGL-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5OpenGL.so
%{libqt5_libdir}/libQt5OpenGL.prl
%{libqt5_libdir}/cmake/Qt5OpenGL/
%{libqt5_libdir}/pkgconfig/Qt5OpenGL.pc
%{libqt5_includedir}/QtOpenGL/
%exclude %{libqt5_includedir}/QtOpenGL/%{so_version}

%files -n libQt5PrintSupport5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5PrintSupport.so.*
%{libqt5_plugindir}/printsupport

%files -n libQt5PrintSupport-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5PrintSupport.so
%{libqt5_libdir}/libQt5PrintSupport.prl
%{libqt5_libdir}/cmake/Qt5PrintSupport/
%{libqt5_libdir}/pkgconfig/Qt5PrintSupport.pc
%{libqt5_includedir}/QtPrintSupport/
%exclude %{libqt5_includedir}/QtPrintSupport/%{so_version}

%files -n libQt5Xml5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Xml.so.*

%files -n libQt5Xml-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Xml.so
%{libqt5_libdir}/libQt5Xml.prl
%{libqt5_libdir}/cmake/Qt5Xml/
%{libqt5_libdir}/pkgconfig/Qt5Xml.pc
%{libqt5_includedir}/QtXml/

%files -n libQt5Test5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Test.so.*

%files -n libQt5Test-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Test.so
%{libqt5_libdir}/libQt5Test.prl
%{libqt5_libdir}/cmake/Qt5Test/
%{libqt5_libdir}/pkgconfig/Qt5Test.pc
%{libqt5_includedir}/QtTest/
%exclude %{libqt5_includedir}/QtTest/%{so_version}

%files -n libQt5Widgets5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Widgets.so.*

%files -n libQt5Widgets-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Widgets.so
%{libqt5_libdir}/libQt5Widgets.prl
%{libqt5_libdir}/cmake/Qt5Widgets/
%{libqt5_libdir}/pkgconfig/Qt5Widgets.pc
%{libqt5_includedir}/QtWidgets/
%{libqt5_libdir}/metatypes/qt5widgets_metatypes.json
%exclude %{libqt5_includedir}/QtWidgets/%{so_version}

%files -n libQt5Gui5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Gui.so.*
%ifarch %ix86
%if 0%{?sle_version:%sle_version} < 150000
%{libqt5_libdir}/sse2/libQt5Gui.so.*
%endif
%endif
%{libqt5_libdir}/libQt5EglFSDeviceIntegration.so.*
%{libqt5_libdir}/libQt5EglFsKmsSupport.so.*
%{libqt5_libdir}/libQt5XcbQpa.so.*
%{libqt5_plugindir}/generic
%{libqt5_plugindir}/imageformats
%{libqt5_plugindir}/platforminputcontexts
%{libqt5_plugindir}/platforms
%{libqt5_plugindir}/egldeviceintegrations
%{libqt5_plugindir}/xcbglintegrations

%files platformtheme-gtk3
%license LICENSE.*
%doc *.txt
%dir %{libqt5_plugindir}/platformthemes
%{libqt5_plugindir}/platformthemes/libqgtk3.so

%files platformtheme-xdgdesktopportal
%license LICENSE.*
%doc *.txt
%dir %{libqt5_plugindir}/platformthemes
%{libqt5_plugindir}/platformthemes/libqxdgdesktopportal.so

%files -n libQt5Gui-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Gui.so
%{libqt5_libdir}/libQt5Gui.prl
%{libqt5_libdir}/libQt5EglFSDeviceIntegration.so
%{libqt5_libdir}/libQt5EglFSDeviceIntegration.prl
%{libqt5_libdir}/cmake/Qt5EglFSDeviceIntegration/
%{libqt5_libdir}/libQt5EglFsKmsSupport.prl
%{libqt5_libdir}/libQt5EglFsKmsSupport.so
%{libqt5_libdir}/cmake/Qt5EglFsKmsSupport/
%{libqt5_libdir}/libQt5XcbQpa.so
%{libqt5_libdir}/libQt5XcbQpa.prl
%{libqt5_libdir}/cmake/Qt5XcbQpa/
%{libqt5_libdir}/cmake/Qt5Gui/
%{libqt5_libdir}/pkgconfig/Qt5Gui.pc
%{libqt5_includedir}/QtGui/
%{libqt5_includedir}/QtEglFSDeviceIntegration/
%{libqt5_includedir}/QtXkbCommonSupport
%{libqt5_libdir}/metatypes/qt5gui_metatypes.json
%exclude %{libqt5_includedir}/QtGui/%{so_version}
%exclude %{libqt5_includedir}/QtEglFSDeviceIntegration/%{so_version}
%exclude %{libqt5_includedir}/QtXkbCommonSupport/%{so_version}

%files devel
%license LICENSE.*
%doc *.txt

%files private-headers-devel
%license LICENSE.*
%doc *.txt

%files -n libQt5Sql5
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Sql.so.*
%dir %{libqt5_plugindir}/sqldrivers

%files -n libQt5Sql-devel
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Sql.so
%{libqt5_libdir}/libQt5Sql.prl
%{libqt5_libdir}/cmake/Qt5Sql/
%{libqt5_libdir}/pkgconfig/Qt5Sql.pc
%{libqt5_includedir}/QtSql/
%exclude %{libqt5_includedir}/QtSql/%{so_version}

%files -n libQt5Sql5-sqlite
%license LICENSE.*
%doc *.txt
%{libqt5_plugindir}/sqldrivers/libqsqlite*.so

%files -n libQt5Sql5-unixODBC
%license LICENSE.*
%doc *.txt
%{libqt5_plugindir}/sqldrivers/libqsqlodbc*.so

%files -n libQt5Sql5-postgresql
%license LICENSE.*
%doc *.txt
%{libqt5_plugindir}/sqldrivers/libqsqlpsql*.so

%files -n libQt5Sql5-mysql
%license LICENSE.*
%doc *.txt
%{libqt5_plugindir}/sqldrivers/libqsqlmysql*.so

%files -n libQt5Bootstrap-devel-static
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5Bootstrap.a
%{libqt5_libdir}/libQt5Bootstrap.prl

%files -n libQt5OpenGLExtensions-devel-static
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5OpenGLExtensions.a
%{libqt5_libdir}/libQt5OpenGLExtensions.prl
%{libqt5_libdir}/cmake/Qt5OpenGLExtensions/
%{libqt5_libdir}/pkgconfig/Qt5OpenGLExtensions.pc
%{libqt5_includedir}/QtOpenGLExtensions/

%files -n libQt5PlatformSupport-devel-static
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5XkbCommonSupport.a
%{libqt5_libdir}/libQt5XkbCommonSupport.prl
%{libqt5_libdir}/cmake/Qt5XkbCommonSupport/
%{libqt5_libdir}/libQt5AccessibilitySupport.a
%{libqt5_libdir}/libQt5AccessibilitySupport.prl
%{libqt5_libdir}/cmake/Qt5AccessibilitySupport/
%{libqt5_libdir}/libQt5DeviceDiscoverySupport.a
%{libqt5_libdir}/libQt5DeviceDiscoverySupport.prl
%{libqt5_libdir}/cmake/Qt5DeviceDiscoverySupport/
%{libqt5_libdir}/libQt5EglSupport.a
%{libqt5_libdir}/libQt5EglSupport.prl
%{libqt5_libdir}/cmake/Qt5EglSupport/
%{libqt5_libdir}/libQt5EventDispatcherSupport.a
%{libqt5_libdir}/libQt5EventDispatcherSupport.prl
%{libqt5_libdir}/cmake/Qt5EventDispatcherSupport/
%{libqt5_libdir}/libQt5FbSupport.a
%{libqt5_libdir}/libQt5FbSupport.prl
%{libqt5_libdir}/cmake/Qt5FbSupport/
%{libqt5_libdir}/libQt5FontDatabaseSupport.a
%{libqt5_libdir}/libQt5FontDatabaseSupport.prl
%{libqt5_libdir}/cmake/Qt5FontDatabaseSupport/
%ifnarch %arm aarch64
%{libqt5_libdir}/libQt5GlxSupport.a
%{libqt5_libdir}/libQt5GlxSupport.prl
%{libqt5_libdir}/cmake/Qt5GlxSupport/
%endif
%{libqt5_libdir}/libQt5InputSupport.a
%{libqt5_libdir}/libQt5InputSupport.prl
%{libqt5_libdir}/cmake/Qt5InputSupport/
%{libqt5_libdir}/libQt5LinuxAccessibilitySupport.a
%{libqt5_libdir}/libQt5LinuxAccessibilitySupport.prl
%{libqt5_libdir}/cmake/Qt5LinuxAccessibilitySupport/
%{libqt5_libdir}/libQt5PlatformCompositorSupport.a
%{libqt5_libdir}/libQt5PlatformCompositorSupport.prl
%{libqt5_libdir}/cmake/Qt5PlatformCompositorSupport/
%{libqt5_libdir}/libQt5ServiceSupport.a
%{libqt5_libdir}/libQt5ServiceSupport.prl
%{libqt5_libdir}/cmake/Qt5ServiceSupport/
%{libqt5_libdir}/libQt5ThemeSupport.a
%{libqt5_libdir}/libQt5ThemeSupport.prl
%{libqt5_libdir}/cmake/Qt5ThemeSupport/
%{libqt5_libdir}/libQt5EdidSupport.a
%{libqt5_libdir}/libQt5EdidSupport.prl
%{libqt5_libdir}/cmake/Qt5EdidSupport/
%if %{vulkan}
%{libqt5_libdir}/libQt5VulkanSupport.a
%{libqt5_libdir}/libQt5VulkanSupport.prl
%{libqt5_libdir}/cmake/Qt5VulkanSupport/
%endif
%{libqt5_includedir}/QtAccessibilitySupport/
%{libqt5_includedir}/QtDeviceDiscoverySupport/
%{libqt5_includedir}/QtEglSupport/
%{libqt5_includedir}/QtEventDispatcherSupport/
%{libqt5_includedir}/QtFbSupport/
%{libqt5_includedir}/QtFontDatabaseSupport/
%ifnarch %arm aarch64
%{libqt5_includedir}/QtGlxSupport/
%endif
%{libqt5_includedir}/QtInputSupport/
%{libqt5_includedir}/QtLinuxAccessibilitySupport/
%{libqt5_includedir}/QtPlatformCompositorSupport/
%{libqt5_includedir}/QtServiceSupport/
%{libqt5_includedir}/QtThemeSupport/
%{libqt5_includedir}/QtEdidSupport/
%if %{vulkan}
%{libqt5_includedir}/QtVulkanSupport/
%endif
%exclude %{libqt5_includedir}/QtAccessibilitySupport/%{so_version}/
%exclude %{libqt5_includedir}/QtDeviceDiscoverySupport/%{so_version}/
%exclude %{libqt5_includedir}/QtEglSupport/%{so_version}/
%exclude %{libqt5_includedir}/QtEventDispatcherSupport/%{so_version}/
%exclude %{libqt5_includedir}/QtFbSupport/%{so_version}/
%exclude %{libqt5_includedir}/QtFontDatabaseSupport/%{so_version}/
%ifnarch %arm aarch64
%exclude %{libqt5_includedir}/QtGlxSupport/%{so_version}/
%endif
%exclude %{libqt5_includedir}/QtInputSupport/%{so_version}/
%exclude %{libqt5_includedir}/QtLinuxAccessibilitySupport/%{so_version}/
%exclude %{libqt5_includedir}/QtPlatformCompositorSupport/%{so_version}/
%exclude %{libqt5_includedir}/QtServiceSupport/%{so_version}/
%exclude %{libqt5_includedir}/QtThemeSupport/%{so_version}/
%exclude %{libqt5_includedir}/QtEdidSupport/%{so_version}/
%if %{vulkan}
%exclude %{libqt5_includedir}/QtVulkanSupport/%{so_version}/
%endif

%files -n libQt5KmsSupport-devel-static
%license LICENSE.*
%doc *.txt
%{libqt5_libdir}/libQt5KmsSupport.a
%{libqt5_libdir}/libQt5KmsSupport.prl
%{libqt5_libdir}/cmake/Qt5KmsSupport/
%exclude %{libqt5_includedir}/QtKmsSupport/%{so_version}/
%{libqt5_includedir}/QtKmsSupport/

%files -n libQt5Core-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtCore/%{so_version}/

%files -n libQt5DBus-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtDBus/%{so_version}/

%files -n libQt5Gui-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtGui/%{so_version}/
%{libqt5_includedir}/QtEglFSDeviceIntegration/%{so_version}
%{libqt5_includedir}/QtXkbCommonSupport/%{so_version}

%files -n libQt5KmsSupport-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtKmsSupport/%{so_version}/

%files -n libQt5Network-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtNetwork/%{so_version}/

%files -n libQt5OpenGL-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtOpenGL/%{so_version}/

%files -n libQt5PlatformSupport-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtAccessibilitySupport/%{so_version}/
%{libqt5_includedir}/QtDeviceDiscoverySupport/%{so_version}/
%{libqt5_includedir}/QtEglSupport/%{so_version}/
%{libqt5_includedir}/QtEventDispatcherSupport/%{so_version}/
%{libqt5_includedir}/QtFbSupport/%{so_version}/
%{libqt5_includedir}/QtFontDatabaseSupport/%{so_version}/
%ifnarch %arm aarch64
%{libqt5_includedir}/QtGlxSupport/%{so_version}/
%endif
%{libqt5_includedir}/QtInputSupport/%{so_version}/
%{libqt5_includedir}/QtLinuxAccessibilitySupport/%{so_version}/
%{libqt5_includedir}/QtPlatformCompositorSupport/%{so_version}/
%{libqt5_includedir}/QtServiceSupport/%{so_version}/
%{libqt5_includedir}/QtThemeSupport/%{so_version}/
%{libqt5_includedir}/QtEdidSupport/%{so_version}/
%if %{vulkan}
%{libqt5_includedir}/QtVulkanSupport/%{so_version}/
%endif

%files -n libQt5PrintSupport-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtPrintSupport/%{so_version}/

%files -n libQt5Sql-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtSql/%{so_version}/

%files -n libQt5Test-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtTest/%{so_version}/

%files -n libQt5Widgets-private-headers-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtWidgets/%{so_version}/

%files -n libQt5PlatformHeaders-devel
%license LICENSE.*
%doc *.txt
%{libqt5_includedir}/QtPlatformHeaders/

%files examples
%license LICENSE.*
%doc *.txt
%{libqt5_examplesdir}/

%changelog
