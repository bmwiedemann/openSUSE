#
# spec file for package gambas3
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012-2018 Lars Vogdt <lars@linux-schulserver.de>
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


%if 0%{?suse_version} > 1315
%bcond_without gambas_ncurses
%else
%bcond_with    gambas_ncurses
%endif
%if 0%{?suse_version} <= 1320
%bcond_without qt4
%if 0%{?suse_version} != 1315
%bcond_without jit
%endif
%endif
%if 0%{?suse_version} >= 1315
%if 0%{?suse_version} != 1320
%bcond_without qt5
%if 0%{?suse_version} >= 1500
%bcond_without openal
%endif
%endif
%endif
Name:           gambas3
Version:        3.14.3
Release:        0
Summary:        BASIC interpreter under Linux
License:        GPL-2.0-or-later
Group:          Development/Tools/IDE
URL:            http://gambas.sourceforge.net/
Source0:        https://gitlab.com/gambas/gambas/-/archive/%{version}/gambas-%{version}.tar.bz2
Source1:        %{name}.desktop
Source2:        x-gambas.desktop
Source99:       %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE -- add german translation
Patch0:         gambas3-mime_translation.patch
# PATCH-FIX-OPENSUSE llvm.patch avvissu@yandex.ru -- Change the location for an header files
Patch1:         gambas3-3.12.2-llvm.patch
# PATCH-FIX-UPSTREAM poppler-0.88 building fix
Patch2:         gambas3-3.14.3-fix_build_with_poppler-0.88.patch 
BuildRequires:  SDL_image
BuildRequires:  aalib-devel
BuildRequires:  atk-devel
BuildRequires:  dejavu
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gettext-tools
BuildRequires:  glibc-devel
BuildRequires:  gmp-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  mysql-devel
BuildRequires:  openldap2-devel
BuildRequires:  postgresql-devel
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  postgresql-server-devel
%endif
BuildRequires:  shared-mime-info
BuildRequires:  unixODBC-devel
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(SDL_gfx)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(SDL_mixer)
BuildRequires:  pkgconfig(SDL_ttf)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gdkglext-1.0)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  pkgconfig(libclucene-core)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
%if %{with gambas_ncurses}
BuildRequires:  pkgconfig(ncurses)
%endif
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-runtime = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Code is not endian clean.
ExcludeArch:    ppc ppc64
%if %{with qt5}
BuildRequires:  pkgconfig(Qt5Core) >= 5.3.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(poppler-qt5)
%endif
%if %{with qt4}
BuildRequires:  pkgconfig(QtCore) >= 4.5
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(QtOpenGL)
BuildRequires:  pkgconfig(QtSvg)
BuildRequires:  pkgconfig(QtWebKit)
BuildRequires:  pkgconfig(QtXml)
BuildRequires:  pkgconfig(poppler-qt4)
%endif
%if %{with openal}
BuildRequires:  pkgconfig(alure)
BuildRequires:  pkgconfig(openal)
%endif
%if %{with jit}
BuildRequires:  llvm-devel <= 3.5.0
%endif

%description
Gambas is a development environment based on a BASIC interpreter with
object extensions, similar to Visual Basic. With Gambas, you can
design program GUIs, access MySQL or PostgreSQL databases, control
KDE applications, translate your program into many languages, create
network applications, build RPMs of your apps automatically.

%package ide
Summary:        The Gambas Development Enviroment
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}
Requires:       %{name}-devel = %{version}
Requires:       %{name}-gb-args = %{version}
Requires:       %{name}-gb-clipper = %{version}
Requires:       %{name}-gb-db = %{version}
Requires:       %{name}-gb-db-form = %{version}
Requires:       %{name}-gb-desktop = %{version}
Requires:       %{name}-gb-eval-highlight = %{version}
Requires:       %{name}-gb-form = %{version}
Requires:       %{name}-gb-form-dialog = %{version}
Requires:       %{name}-gb-form-editor = %{version}
Requires:       %{name}-gb-form-mdi = %{version}
Requires:       %{name}-gb-form-print = %{version}
Requires:       %{name}-gb-form-stock = %{version}
Requires:       %{name}-gb-image = %{version}
Requires:       %{name}-gb-image-effect = %{version}
Requires:       %{name}-gb-markdown = %{version}
Requires:       %{name}-gb-net = %{version}
Requires:       %{name}-gb-net-curl = %{version}
Requires:       %{name}-gb-settings = %{version}
Requires:       %{name}-gb-util = %{version}
Requires:       %{name}-runtime = %{version}
Requires:       gettext-tools
Requires:       gzip
Requires:       rpm
Requires:       tar
Recommends:     %{name}-gb-cairo = %{version}
Recommends:     %{name}-gb-chart = %{version}
Recommends:     %{name}-gb-complex = %{version}
Recommends:     %{name}-gb-compress = %{version}
Recommends:     %{name}-gb-compress-bzlib2 = %{version}
Recommends:     %{name}-gb-compress-zlib = %{version}
Recommends:     %{name}-gb-crypt = %{version}
Recommends:     %{name}-gb-data = %{version}
Recommends:     %{name}-gb-db-mysql = %{version}
Recommends:     %{name}-gb-db-odbc = %{version}
Recommends:     %{name}-gb-db-postgresql = %{version}
Recommends:     %{name}-gb-db-sqlite3 = %{version}
Recommends:     %{name}-gb-dbus = %{version}
Recommends:     %{name}-gb-geom = %{version}
Recommends:     %{name}-gb-gmp = %{version}
Recommends:     %{name}-gb-gsl = %{version}
Recommends:     %{name}-gb-gtk = %{version}
Recommends:     %{name}-gb-gtk-opengl = %{version}
Recommends:     %{name}-gb-gui = %{version}
Recommends:     %{name}-gb-httpd = %{version}
Recommends:     %{name}-gb-image-imlib = %{version}
Recommends:     %{name}-gb-image-io = %{version}
Recommends:     %{name}-gb-libxml = %{version}
Recommends:     %{name}-gb-logging = %{version}
Recommends:     %{name}-gb-maps = %{version}
Recommends:     %{name}-gb-memcached = %{version}
Recommends:     %{name}-gb-mime = %{version}
Recommends:     %{name}-gb-mysql = %{version}
%if %{with gambas_ncurses}
Recommends:     %{name}-gb-ncurses = %{version}
%else
Provides:       %{name}-gb-ncurses = %{version}-%{release}
Obsoletes:      %{name}-gb-ncurses
%endif
Recommends:     %{name}-gb-net-pop3 = %{version}
Recommends:     %{name}-gb-net-smtp = %{version}
Recommends:     %{name}-gb-opengl = %{version}
Recommends:     %{name}-gb-opengl-glsl = %{version}
Recommends:     %{name}-gb-opengl-glu = %{version}
Recommends:     %{name}-gb-opengl-sge = %{version}
Recommends:     %{name}-gb-openssl = %{version}
Recommends:     %{name}-gb-option = %{version}
Recommends:     %{name}-gb-pcre = %{version}
Recommends:     %{name}-gb-pdf = %{version}
Recommends:     %{name}-gb-report = %{version}
Recommends:     %{name}-gb-sdl = %{version}
Recommends:     %{name}-gb-sdl-sound = %{version}
Recommends:     %{name}-gb-settings = %{version}
Recommends:     %{name}-gb-signal = %{version}
Recommends:     %{name}-gb-util-web = %{version}
Recommends:     %{name}-gb-v4l = %{version}
Recommends:     %{name}-gb-vb = %{version}
Recommends:     %{name}-gb-web-feed = %{version}
Recommends:     %{name}-gb-web-form = %{version}
Recommends:     %{name}-gb-xml = %{version}
Recommends:     %{name}-gb-xml-rpc = %{version}
Recommends:     %{name}-gb-xml-xslt = %{version}
Recommends:     %{name}-gb-form-terminal = %{version}
Recommends:     %{name}-gb-term = %{version}
Recommends:     %{name}-gb-term-form = %{version}
Recommends:     %{name}-script = %{version}
Recommends:     deb
%if %{with qt5}
Requires:       %{name}-gb-qt5 = %{version}
Requires:       %{name}-gb-qt5-ext = %{version}
Requires:       %{name}-gb-qt5-opengl = %{version}
Requires:       %{name}-gb-qt5-webkit = %{version}
%else
Requires:       %{name}-gb-qt4 = %{version}
Requires:       %{name}-gb-qt4-ext = %{version}
Requires:       %{name}-gb-qt4-opengl = %{version}
Requires:       %{name}-gb-qt4-webkit = %{version}
%endif
%if %{with openal}
Recommends:     %{name}-gb-openal = %{version}
%endif
%if %{with jit}
Recommends:     %{name}-gb-jit = %{version}
%endif

%description ide
This package includes the complete Gambas Development Environment, with the
database manager and the help files.

The IDE itself is written in Gambas-BASIC.

%package runtime
Summary:        The Gambas runtime
Group:          Development/Tools/IDE
Requires:       glibc

%description runtime
This package includes the Gambas interpreter needed to run Gambas
applications.

It contains:
  * The interpreter: gbx3.
  * The symbolic link on gbx3: gbr3.
  * The internal component description: gb.component, gb.info and gb.list.
  * The readme files, TODO files, and so on.
  * The gb.debug component: gb.debug.info, gb.debug.list, gb.debug.component,
    gb.debug.so.*, gb.debug.la.
  * The gb.eval component: gb.eval.info, gb.eval.list, gb.eval.component,
    gb.eval.so.*, gb.eval.la.
  * The gb.draw component: gb.draw.info, gb.draw.list, gb.draw.component,
    gb.draw.so.*, gb.draw.la.

%package devel
Summary:        The Gambas devel package
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       gcc
Requires:       gcc-c++

%description devel
This package includes all tools needed to compile Gambas projects without
having to install the complete development environment.

It contains the compiler (gbc3), archiver (gba3) and informer (gbi3).

%package script
Summary:        Program that allows to write script files in Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-devel = %{version}
Requires:       %{name}-runtime = %{version}
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         shared-mime-info
Provides:       %{_bindir}/gbx2

%description script
This package includes the scripter program that allows to write script
files in Gambas.

It contains the scripter (gbs3.gambas).

%package gb-args
Summary:        The first C getopt() interface component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Provides:       %{name}-gb-option = %{version}
Obsoletes:      %{name}-gb-option < 3.4.0

%description gb-args
This class analyses the arguments of the current process.

%package gb-cairo
Summary:        Cairo source pattern for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       cairo

%description gb-cairo
This class represents a Cairo source pattern, as returned by methods like
Cairo.SolidPattern or Cairo.LinearGradient.

%package gb-chart
Summary:        The chart component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-chart
This is the component that draws charts.

%package gb-clipper
Summary:        The clipper component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-clipper
Gambas3 component package for clipper.

%package gb-complex
Summary:        Support complex numbers for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-complex
Support for complex numbers in Gambas.

%package gb-compress
Summary:        A compression component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-compress-bzlib2 = %{version}
Requires:       %{name}-gb-compress-zlib = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-compress
This component allows you to compress/uncompress data or files with
the bzip2 and zip algorithms.

%package gb-compress-bzlib2
Summary:        The bzlib2 compression component for Gambas
Group:          Development/Tools/IDE
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libz.so) --qf '%%{NAME} >= %%{VERSION}')

%description gb-compress-bzlib2
This component allows you to compress/uncompress data or files with
the bzlib2 algorithms.

%package gb-compress-zlib
Summary:        The zlib compression component for Gambas
Group:          Development/Tools/IDE
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libbz2.so) --qf '%%{NAME} >= %%{VERSION}')

%description gb-compress-zlib
This component allows you to compress/uncompress data or files with
the zlib algorithms.

%package gb-crypt
Summary:        Crypt and compare crypted passwords for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       glibc

%description gb-crypt
This component allows you to crypt a password and to compare crypted
passwords by using the DES or MD5 algoritm implemented in the GNU libc
library.

%package gb-data
Summary:        Container datatypes for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-data
gb.data adds new container datatypes to Gambas.

%package gb-db
Summary:        The database component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-db
This component allows you to access many databases management systems,
provided that you install the needed driver packages.

%package gb-db-form
Summary:        The data bound control component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-db = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-db-form
Provides some data bound controls, i.e. controls that can display and edit
database records automatically. Note that it is highly experimental!.

%package gb-gmp
Summary:        The GMP component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-db = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-gmp
Component based on the Gnu Multiple Precision Arithmetic Library that
implements big integers and big rational numbers.

%package gb-db-mysql
Summary:        MySQL database driver for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-db = %{version}
Requires:       %{name}-runtime = %{version}
Requires:       mysql

%description gb-db-mysql
This component allows you to access MySQL databases.

%package gb-db-odbc
Summary:        UnixODBC database driver for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-db = %{version}
Requires:       %{name}-runtime = %{version}
Requires:       unixODBC

%description gb-db-odbc
This component allows you to access to a database thru unixODBC driver.

%package gb-db-postgresql
Summary:        PostgreSQL database driver for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-db = %{version}
Requires:       %{name}-runtime = %{version}
Requires:       postgresql

%description gb-db-postgresql
This component allows you to access Postgresql databases.

%package gb-db-sqlite3
Summary:        SQLite3 database driver for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-db = %{version}
Requires:       %{name}-runtime = %{version}
Requires:       sqlite3

%description gb-db-sqlite3
This component allows you to access Sqlite v. 3.x databases.

%package gb-desktop
Summary:        The desktop component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-desktop
This is a component that provides an access to the Portland project xdg
utilities.

%package gb-dbus
Summary:        D-Bus participation component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       dbus-1

%description gb-dbus
By using this component, you will be able to:
  * Call any method and properties of any application connected to D-Bus.
  * Catch any signal sent by any application connected to D-Bus.
  * Export your own objects to a D-Bus bus.

For more information, see http://dbus.freedesktop.org.

%package gb-eval-highlight
Summary:        Highlighter class for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-eval-highlight
This class reimplements Highlight in gb.eval.

%package gb-form
Summary:        Data bound controls for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-form
This component contain some control elements to be used in both gtk+ and qt
components.

%package gb-form-dialog
Summary:        Dialog class for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-form = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-form-dialog
This component implements Dialog Class.

%package gb-form-editor
Summary:        Text editor for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-eval-highlight = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-form-editor
This component provides the TextEditor control, which is a text editor with
syntax highlighting support.

%package gb-form-mdi
Summary:        Workspace control for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-form = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-form-mdi
This component implements the new Workspace control.

%package gb-form-print
Summary:        Printer class for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-form = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-form-print
This component extends the Printer class with a generic preview and print
dialog.

%package gb-form-stock
Summary:        Stock icon support for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-form = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-form-stock
This class is used for returning predefined icons.

You should not have to use this class directly to get these icons. Use the
Picture class as an array instead.

%package gb-geom
Summary:        The Gambas Geometry hidden component
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-geom
This component implements all geometry classes:
  - Point;
  - PointF;
  - Rect;
  - RectF.

%package gb-gsl
Summary:        GNU Scientific Library interface for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-gui = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-gsl
This component implements polynomials, matrices, vectors and complex
numbers completely.

%package gb-gtk
Summary:        The GTK GUI component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-gui = %{version}
Requires:       %{name}-runtime = %{version}
Requires:       gtk2 >= 2.6.8

%description gb-gtk
This package includes the Gambas GTK GUI component.

%package gb-gtk3
Summary:        The GTK3 GUI component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-gui = %{version}
Requires:       %{name}-runtime = %{version}
Requires:       gtk3 >= 3.0.0

%description gb-gtk3
This package includes the Gambas GTK3 GUI component.

%package gb-gtk-opengl
Summary:        GTK-OpenGL component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-gtk = %{version}

%description gb-gtk-opengl
This component allows to use OpenGL in Gambas/GTK+ applications.

%package gb-gui
Summary:        The Qt/GTK loader component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-gui
This is the component that just loads gb.qt if you are running KDE or
gb.gtk in the other cases. It is used to make your application more
desktop-friendly.

%package gb-httpd
Summary:        The httpd component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-httpd
This component implements an embedded HTTP server for the interpreter.

%package gb-image
Summary:        The image component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-image
This component permits the manipulation of some image objects.

%package gb-image-effect
Summary:        Image filtering routines for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-image = %{version}

%description gb-image-effect
This class reimplements Image in gb.image and adds many effect methods to
the original Image class.

%package gb-image-imlib
Summary:        Gambas image routines based on the Imlib2 library
Group:          Development/Tools/IDE
Requires:       %{name}-gb-image = %{version}
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libImlib2.so) --qf '%%{NAME} >= %%{VERSION}')

%description gb-image-imlib
This components adds image processing methods coming from the imlib2 library.

%package gb-image-io
Summary:        IO operations with images based on gdk-pixbuf for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-image-io
This components allow to load an image from disk, and save an image to disk.
It is based on the gdk-pixbuf library.

%package gb-inotify
Summary:        Filesystem event monitoring for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-inotify
This component allows to monitor filesystem events with Linux
inotify interface.

%package gb-jit
Summary:        The Gambas JIT component
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-jit
This component provides the JIT compiler for Gambas.

%package gb-logging
Summary:        The Gambas logging component
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-logging
This component implements a flexible logging system for Gambas applications.
The formatting of messages is based on the RFC5454 document which describes
the standard "syslog" format.

%package gb-maps
Summary:        Map display for Gambas applications
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-maps
This component allows displaying Google Maps, OpenStreetMap, etc.
inside your application.

%package gb-markdown
Summary:        Gambas Markdown syntax
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-markdown
This component implements the Gambas Markdown syntax.

%package gb-media
Summary:        Gambas interface to the GStreamer library
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-media
This component is a simplified interface to the GStreamer library.

It allows to play, convert, transform... multimedia data from any source to
any format by linking plugins together.

Read the GStreamer documentation for more information.

%package gb-memcached
Summary:        The memcached component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-memcached
This component implements a memcached client.

%package gb-mime
Summary:        MIME message encoder and decoder for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-mime
This component allows to encode and decode MIME messages.

%package gb-mysql
Summary:        MySQL specific routines for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-mysql
gb.mysql allows creating MySQL specific routines and sending
them then to gb.db to be executed.

%if %{with gambas_ncurses}
%package gb-ncurses
Summary:        The ncurses component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-ncurses
This component allows you to use the ncurses library in your Gambas UI.
%endif

%package gb-net
Summary:        The networking component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-net
This component allows you to use TCP/IP and UDP sockets, and to access
any serial ports.

%package gb-net-curl
Summary:        The advanced networking component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       curl

%description gb-net-curl
This component allows your programs to easily become FTP or HTTP clients.

%package gb-net-pop3
Summary:        The POP3 component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-net = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-net-pop3
This component allows to receive mails by using the POP3 protocol.

%package gb-net-smtp
Summary:        The SMTP component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-net = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-net-smtp
This component allows to send mails by using the SMTP protocol.

It supports mail attachments, mail alternatives, and protocol encryption
(SSL or TLS), provided that the openssl program is installed on your system.

%package gb-opengl
Summary:        The OpenGL component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-opengl
This package includes the Gambas OpenGL component.

%package gb-opengl-glu
Summary:        OpenGL complementary routines for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-opengl = %{version}

%description gb-opengl-glu
The GL Utilities "GLU" library is a set of routines designed to complement
the OpenGL graphics system by providing support for mipmapping, matrix
manipulation, polygon tessellation, quadrics, NURBS, and error handling.

%package gb-opengl-glsl
Summary:        High level shading language integration for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-opengl = %{version}

%description gb-opengl-glsl
GLSL (OpenGL Shading Language), also known as GLslang, is a high-level
shading language based on the C programming language. It was created by the
OpenGL ARB to give developers more direct control of the graphics pipeline
without having to use assembly language or hardware-specific languages.

%package gb-opengl-sge
Summary:        The Gambas opengl-sge component
Group:          Development/Tools/IDE
Requires:       %{name}-gb-opengl = %{version}

%description gb-opengl-sge
This component is a simple OpenGL game engine based on the MD2 model format.

%package gb-openssl
Summary:        The Gambas openssl component
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-openssl
This component allows you to use cryptographic functions wrapping libcrypto
from the OpenSSL project.

%if %{with openal}
%package gb-openal
Summary:        The Gambas openal component
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-openal
This component implements an interface to the OpenAL library.
%endif

%package gb-option
Summary:        The second C getopt() interface component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-option
This component implements a command-line arguments parser based on the GNU
getopt() function.

%package gb-pcre
Summary:        The PCRE component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       pcre

%description gb-pcre
This package includes the Gambas PCRE component.

%package gb-pdf
Summary:        The PDF component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-pdf
This component permits the manipulation of PDF documents.

%if %{with qt4}
%package gb-qt4
Summary:        The Qt4 GUI component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       libqt4 >= 4.5

%description gb-qt4
This package includes the Gambas QT4 GUI component.

%package gb-qt4-ext
Summary:        The extended Qt4 GUI component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-qt4 = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-qt4-ext
This component includes somme uncommon QT4 controls.

%package gb-qt4-opengl
Summary:        Qt4-OpenGL component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-qt4 = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-qt4-opengl
This component allows you to use OpenGL inside Qt4/Gambas.

%package gb-qt4-webkit
Summary:        Qt4-WebKit component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-qt4 = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-qt4-webkit
This component allows you to use the Web Browser widget included in
Qt4/Gambas.
%endif

%if %{with qt5}
%package gb-qt5
Summary:        The Qt5 GUI component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       libqt5-qtbase >= 5.3

%description gb-qt5
This package includes the Gambas QT5 GUI component.

%package gb-qt5-ext
Summary:        The extended Qt5 GUI component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-qt5 = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-qt5-ext
This package contains the Gambas3 Qt5 component with additional stuff.

%package gb-qt5-opengl
Summary:        Qt5-OpenGL component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-qt5 = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-qt5-opengl
This component allows you to use OpenGL inside Qt5/Gambas.

%package gb-qt5-webkit
Summary:        The Qt5 Webkit component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-qt5 = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-qt5-webkit
This component allows you to use the Web Browser widget included in
Qt5/Gambas.
%endif

%package gb-report
Summary:        The Gambas report designer component
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-report
This is the Gambas report designer component.

%package gb-report2
Summary:        The Gambas report designer component 2
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-report2
This is the Gambas report designer component number 2.

%package gb-scanner
Summary:        The Gambas scanner component
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-scanner
This component is based on SANE to help dealing with scanners.

%package gb-sdl
Summary:        The SDL component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       SDL_mixer
Requires:       dejavu
Recommends:     %(rpm -qf $(readlink -qne %{_libdir}/libogg.so) --qf '%%{NAME} >= %%{VERSION}')
Recommends:     %(rpm -qf $(readlink -qne %{_libdir}/libvorbis.so) --qf '%%{NAME} >= %%{VERSION}')
Provides:       %{name}-gb-sdl-image = %{version}
Provides:       %{name}-gb-sdl-opengl = %{version}

%description gb-sdl
This component use only the sound part of the SDL library in Gambas.
It allows you to simultaneously play many sounds and a music stored
in a file.

%package gb-sdl-sound
Summary:        Play sounds in Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       SDL

%description gb-sdl-sound
This component allows you to play sounds in Gambas.

This component manages up to 32 sound tracks, that can play sounds from
memory, and one music track that can play a music from a file. Everything
is mixed in real time.

%package gb-settings
Summary:        Application settings management for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-settings
This component allows you to read and write settings with your
application.

%package gb-signal
Summary:        POSIX signal management for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-signal
This component allows to ignore POSIX signals, or intercept them inside an
event handler.

%package gb-util
Summary:        Utility functions for the Gambas interpreter
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-util
This component provides utility functions to the interpreter.

%package gb-util-web
Summary:        Utility functions for Gambas web applications
Group:          Development/Tools/IDE
Requires:       %{name}-gb-util = %{version}
Requires:       %{name}-runtime = %{version}

%description gb-util-web
This component provides utility functions to web applications.

%package gb-v4l
Summary:        The V4L component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}
Requires:       v4l-tools

%description gb-v4l
This package includes the Gambas V4L component.

%package gb-vb
Summary:        The Visual Basic compatibility component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-vb
This component aims at including some functions that imitate the behaviour
of Visual Basic functions. Use it only if you try to port some VB
projects.

%package gb-xml
Summary:        XML tools for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-xml
This component allows you to read and write XML files.

%package gb-libxml
Summary:        The libxml component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-libxml
These components brings the power of the libxml libraries to Gambas.

This component allows you to read and write XML files.

%package gb-xml-rpc
Summary:        The XML-RPC protocol implementation for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-xml-rpc
XML-RPC client based on libxml and libcurl.

%package gb-xml-xslt
Summary:        libxml-based XSLT tools for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-xml-xslt
XSLT (Extensible Stylesheet Language Transformations) is a declarative,
XML-based language used for the transformation of XML documents.

%package gb-web
Summary:        The CGI web component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-web
This is a component for making CGI web applications, with an ASP-like
interface.

%package gb-web-feed
Summary:        The component to generate and parse RSS documents
Group:          Development/Tools/IDE
Requires:       %{name}-gb-web = %{version}

%description gb-web-feed
This package contains the Gambas3 component to generate and parse RSS
documents.

%package gb-web-form
Summary:        The CUI web component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-gb-util = %{version}
Requires:       %{name}-gb-util-web = %{version}
Requires:       %{name}-gb-web = %{version}

%description gb-web-form
This component allows to make the GUI of a web application with the IDE
form editor.

%package gb-form-terminal
Summary:        The terminal emulator component for Gambas
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-form-terminal
This package contains the Gambas3 component for terminal in form.

%package gb-term
Summary:        The component for terminal management with an API
Group:          Development/Tools/IDE
Requires:       %{name}-runtime = %{version}

%description gb-term
This package contains the Gambas3 component for making the GUI of terminal
applications.

%package gb-term-form
Summary:        The component for making the GUI of terminal applications
Group:          Development/Tools/IDE
Requires:       %{name}-gb-term = %{version}

%description gb-term-form
This package contains the Gambas3 component for making the GUI of terminal
applications.

%prep
%autosetup -p1 -n gambas-%{version}

%build
# don't compile in DATE and TIME
BUILDTIME=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%H:%M')
BUILDDATE=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%b %d %Y')
sed -e "s/__TIME__/\"$BUILDTIME\"/" \
    -e "s/__DATE__/\"$BUILDDATE\"/" \
    -i $(grep -rl '__TIME__\|__DATE__')
#
# remove all hidden files which used by a version control system
find . -type f -iname \.gitignore -delete
#

./reconf-all
# needed, or libtool does not create shared libs
export AM_CFLAGS="%{optflags}"
export AM_CXXFLAGS="%{optflags} -std=gnu++11"
#
%if %{with jit}
export LLVM_INCLUDE="$(llvm-config --includedir)"
export LLVM_LIBS="$(llvm-config --libs core)"
%endif
%configure \
    %if %{without qt5}
    --disable-qt5 \
    %endif
    %if %{without qt4}
    --disable-qt4 \
    %endif
    %if %{without jit}
    --disable-jit \
    %endif
    %if %{without gambas_ncurses}
    --disable-ncurses \
    %endif
    %{nil}

# remove %%_smp_mflags to avoid compilation errors
make -j1 V=1

%install
%make_install
install -Dm644 {app/desktop/,%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/}%{name}.svg
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name} Development IDE
#
# install mime type files
install -Dm644 app/mime/application-x-gambasscript.xml %{buildroot}%{_datadir}/mime/application/x-%{name}script.xml
install -Dm644 app/mime/application-x-gambasscript.png %{buildroot}%{_datadir}/pixmaps/x-%{name}script.png
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/mimelnk/application/x-%{name}.desktop
#
# fix wrong link of gambas3 binary
pushd %{buildroot}%{_bindir}
if [ -L "%{name}" ]; then
rm %{name}; ln -s gbx3 %{name}; fi
popd
#
# install help files, even if they are just a few
cp -r ./app/src/%{name}/help %{buildroot}%{_datadir}/%{name}/
rm -rf %{buildroot}%{_datadir}/%{name}/help/wiki/style.css
cp -fv ./app/src/gambas-wiki/.public/style.css %{buildroot}%{_datadir}/%{name}/help/wiki/style.css
#

%if 0%{?suse_version} < 1500
%post runtime
%desktop_database_post
%icon_theme_cache_post

%post script
%mime_database_post
%desktop_database_post

%postun runtime
%desktop_database_postun
%icon_theme_cache_postun

%postun script
%mime_database_postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%dir %{_datadir}/appdata
%dir %{_datadir}/%{name}/template
%{_bindir}/%{name}
%{_bindir}/%{name}.gambas
%{_datadir}/%{name}/template/
%dir %{_datadir}/metainfo
%attr(0644,root,root) %{_datadir}/metainfo/%{name}.appdata.xml
%exclude %{_datadir}/appdata/gambas3.appdata.xml

%files ide
%defattr(-,root,root)
%doc README

%files runtime
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README.commit
%dir %{_libdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/control
%dir %{_datadir}/%{name}/info
%dir %{_datadir}/%{name}/icons
%{_bindir}/gbx3
%{_bindir}/gbr3
%{_libdir}/%{name}/gb.la
%{_libdir}/%{name}/gb.so
%{_libdir}/%{name}/gb.so.*
%{_libdir}/%{name}/gb.debug.*
%{_libdir}/%{name}/gb.draw.*
%{_libdir}/%{name}/gb.eval.component
%{_libdir}/%{name}/gb.eval.la
%{_libdir}/%{name}/gb.eval.so*
%{_datadir}/%{name}/info/gb.info
%{_datadir}/%{name}/info/gb.list
%{_datadir}/%{name}/info/gb.debug.*
%{_datadir}/%{name}/info/gb.eval.info
%{_datadir}/%{name}/info/gb.eval.list
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/%{name}/icons/*gambas*.png
%attr(0644,root,root) %{_libdir}/%{name}/gb.component

%files devel
%defattr(-,root,root)
%{_bindir}/gbc3
%{_bindir}/gba3
%{_bindir}/gbi3
# problem in upstream
%ifarch %{ix86} %{arm}
%{_bindir}/gbh3
%{_bindir}/gbh3.gambas
%endif
%{_datadir}/%{name}/help

%files script
%defattr(-,root,root)
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application
%{_bindir}/gbs3*
%{_bindir}/gbw3*
%{_datadir}/mime/application/*%{name}*
%{_datadir}/pixmaps/x-%{name}script.png
%{_datadir}/mimelnk/application/x-%{name}.desktop

%files gb-args
%defattr(-,root,root)
%{_libdir}/%{name}/gb.args.*
%{_datadir}/%{name}/info/gb.args.info
%{_datadir}/%{name}/info/gb.args.list

%files gb-cairo
%defattr(-,root,root)
%{_libdir}/%{name}/gb.cairo.component
%{_libdir}/%{name}/gb.cairo.la
%{_libdir}/%{name}/gb.cairo.so*
%{_datadir}/%{name}/info/gb.cairo.*

%files gb-chart
%defattr(-,root,root)
%{_libdir}/%{name}/gb.chart.component
%{_libdir}/%{name}/gb.chart.gambas
%{_datadir}/%{name}/info/gb.chart.*

%files gb-clipper
%defattr(-,root,root)
%{_libdir}/%{name}/gb.clipper.la*
%{_libdir}/%{name}/gb.clipper.so*
%{_libdir}/%{name}/gb.clipper.component
%{_datadir}/%{name}/info/gb.clipper.*

%files gb-complex
%defattr(-,root,root)
%{_libdir}/%{name}/gb.complex.*
%{_datadir}/%{name}/info/gb.complex.*

%files gb-compress
%defattr(-,root,root)
%{_libdir}/%{name}/gb.compress.la*
%{_libdir}/%{name}/gb.compress.so*
%{_libdir}/%{name}/gb.compress.component
%{_datadir}/%{name}/info/gb.compress.*

%files gb-compress-bzlib2
%defattr(-,root,root)
%{_libdir}/%{name}/gb.compress.bzlib2.la*
%{_libdir}/%{name}/gb.compress.bzlib2.so*
%{_libdir}/%{name}/gb.compress.bzlib2.component

%files gb-compress-zlib
%defattr(-,root,root)
%{_libdir}/%{name}/gb.compress.zlib.la*
%{_libdir}/%{name}/gb.compress.zlib.so*
%{_libdir}/%{name}/gb.compress.zlib.component

%files gb-crypt
%defattr(-,root,root)
%{_libdir}/%{name}/gb.crypt.component
%{_libdir}/%{name}/gb.crypt.la
%{_libdir}/%{name}/gb.crypt.so*
%{_datadir}/%{name}/info/gb.crypt.*

%files gb-data
%defattr(-,root,root)
%{_libdir}/%{name}/gb.data.*
%{_datadir}/%{name}/info/gb.data.*

%files gb-db
%defattr(-,root,root)
%{_libdir}/%{name}/gb.db.la
%{_libdir}/%{name}/gb.db.so*
%{_libdir}/%{name}/gb.db.component
%{_libdir}/%{name}/gb.db.gambas
%{_datadir}/%{name}/info/gb.db.info
%{_datadir}/%{name}/info/gb.db.list

%files gb-db-form
%defattr(-,root,root)
%{_libdir}/%{name}/gb.db.form.component
%{_libdir}/%{name}/gb.db.form.gambas
%{_datadir}/%{name}/control/gb.db.form/
%{_datadir}/%{name}/info/gb.db.form.*

%files gb-gmp
%defattr(-,root,root)
%{_libdir}/%{name}/gb.gmp.component
%{_libdir}/%{name}/gb.gmp.la
%{_libdir}/%{name}/gb.gmp.so*
%{_datadir}/%{name}/info/gb.gmp.info
%{_datadir}/%{name}/info/gb.gmp.list

%files gb-db-mysql
%defattr(-,root,root)
%{_libdir}/%{name}/gb.db.mysql.*
%{_datadir}/%{name}/info/gb.db.mysql.info
%{_datadir}/%{name}/info/gb.db.mysql.list

%files gb-db-odbc
%defattr(-,root,root)
%{_libdir}/%{name}/gb.db.odbc.component
%{_libdir}/%{name}/gb.db.odbc.la
%{_libdir}/%{name}/gb.db.odbc.so*
%{_datadir}/%{name}/info/gb.db.odbc.*

%files gb-db-postgresql
%defattr(-,root,root)
%{_libdir}/%{name}/gb.db.postgresql.component
%{_libdir}/%{name}/gb.db.postgresql.la
%{_libdir}/%{name}/gb.db.postgresql.so*
%{_datadir}/%{name}/info/gb.db.postgresql.*

%files gb-db-sqlite3
%defattr(-,root,root)
%{_libdir}/%{name}/gb.db.sqlite3.component
%{_libdir}/%{name}/gb.db.sqlite3.la
%{_libdir}/%{name}/gb.db.sqlite3.so*
%{_datadir}/%{name}/info/gb.db.sqlite3.*

%files gb-desktop
%defattr(-,root,root)
%{_libdir}/%{name}/gb.desktop.*
%{_datadir}/%{name}/control/gb.desktop/
%{_datadir}/%{name}/info/gb.desktop.*info
%{_datadir}/%{name}/info/gb.desktop.*list

%files gb-dbus
%defattr(-,root,root)
%{_libdir}/%{name}/gb.dbus*.component
%{_libdir}/%{name}/gb.dbus*.gambas
%{_libdir}/%{name}/gb.dbus.la
%{_libdir}/%{name}/gb.dbus.so*
%{_datadir}/%{name}/info/gb.dbus*.info
%{_datadir}/%{name}/info/gb.dbus.list
%{_datadir}/%{name}/info/gb.dbus*.list

%files gb-eval-highlight
%defattr(-,root,root)
%{_libdir}/%{name}/gb.eval.highlight.component
%{_libdir}/%{name}/gb.eval.highlight.gambas
%{_datadir}/%{name}/info/gb.eval.highlight.info
%{_datadir}/%{name}/info/gb.eval.highlight.list

%files gb-form
%defattr(-,root,root)
%{_libdir}/%{name}/gb.form.component
%{_libdir}/%{name}/gb.form.gambas
%{_datadir}/%{name}/control/gb.form/
%{_datadir}/%{name}/info/gb.form.info
%{_datadir}/%{name}/info/gb.form.list

%files gb-form-dialog
%defattr(-,root,root)
%{_libdir}/%{name}/gb.form.dialog.*
%{_datadir}/%{name}/info/gb.form.dialog.info
%{_datadir}/%{name}/info/gb.form.dialog.list

%files gb-form-editor
%defattr(-,root,root)
%{_libdir}/%{name}/gb.form.editor.component
%{_libdir}/%{name}/gb.form.editor.gambas
%{_datadir}/%{name}/control/gb.form.editor/
%{_datadir}/%{name}/info/gb.form.editor.info
%{_datadir}/%{name}/info/gb.form.editor.list

%files gb-form-mdi
%defattr(-,root,root)
%{_libdir}/%{name}/gb.form.mdi.*
%{_datadir}/%{name}/info/gb.form.mdi.info
%{_datadir}/%{name}/control/gb.form.mdi/
%{_datadir}/%{name}/info/gb.form.mdi.list

%files gb-form-print
%defattr(-,root,root)
%{_libdir}/%{name}/gb.form.print.*
%{_datadir}/%{name}/info/gb.form.print.*

%files gb-form-stock
%defattr(-,root,root)
%{_libdir}/%{name}/gb.form.stock.component
%{_libdir}/%{name}/gb.form.stock.gambas
%{_datadir}/%{name}/info/gb.form.stock.info
%{_datadir}/%{name}/info/gb.form.stock.list

%files gb-geom
%defattr(-,root,root)
%{_libdir}/%{name}/gb.geom.la*
%{_libdir}/%{name}/gb.geom.so*

%files gb-gsl
%defattr(-,root,root)
%{_libdir}/%{name}/gb.gsl.*
%{_datadir}/%{name}/info/gb.gsl.*

%files gb-gtk
%defattr(-,root,root)
%{_libdir}/%{name}/gb.gtk.la
%{_libdir}/%{name}/gb.gtk.so*
%{_libdir}/%{name}/gb.gtk.component
%{_datadir}/%{name}/info/gb.gtk.info
%{_datadir}/%{name}/info/gb.gtk.list

%files gb-gtk3
%defattr(-,root,root)
%{_libdir}/%{name}/gb.gtk3.la
%{_libdir}/%{name}/gb.gtk3.so*
%{_libdir}/%{name}/gb.gtk3.component
%{_datadir}/%{name}/info/gb.gtk3.info
%{_datadir}/%{name}/info/gb.gtk3.list

%files gb-gtk-opengl
%defattr(-,root,root)
%{_libdir}/%{name}/gb.gtk.opengl.la
%{_libdir}/%{name}/gb.gtk.opengl.so*
%{_libdir}/%{name}/gb.gtk.opengl.component
%{_datadir}/%{name}/info/gb.gtk.opengl.info
%{_datadir}/%{name}/info/gb.gtk.opengl.list

%files gb-gui
%defattr(-,root,root)
%{_libdir}/%{name}/gb.gui.*
%{_datadir}/%{name}/info/gb.gui.*

%files gb-httpd
%defattr(-,root,root)
%{_libdir}/%{name}/gb.httpd.*
%{_datadir}/%{name}/info/gb.httpd.*

%files gb-image
%defattr(-,root,root)
%{_libdir}/%{name}/gb.image.la*
%{_libdir}/%{name}/gb.image.so*
%{_libdir}/%{name}/gb.image.component
%{_datadir}/%{name}/info/gb.image.info
%{_datadir}/%{name}/info/gb.image.list

%files gb-image-effect
%defattr(-,root,root)
%{_libdir}/%{name}/gb.image.effect.component
%{_libdir}/%{name}/gb.image.effect.la
%{_libdir}/%{name}/gb.image.effect.so*
%{_datadir}/%{name}/info/gb.image.effect.info
%{_datadir}/%{name}/info/gb.image.effect.list

%files gb-image-imlib
%defattr(-,root,root)
%{_libdir}/%{name}/gb.image.imlib.component
%{_libdir}/%{name}/gb.image.imlib.la
%{_libdir}/%{name}/gb.image.imlib.so*
%{_datadir}/%{name}/info/gb.image.imlib.info
%{_datadir}/%{name}/info/gb.image.imlib.list

%files gb-image-io
%defattr(-,root,root)
%{_libdir}/%{name}/gb.image.io.component
%{_libdir}/%{name}/gb.image.io.la
%{_libdir}/%{name}/gb.image.io.so*
%{_datadir}/%{name}/info/gb.image.io.info
%{_datadir}/%{name}/info/gb.image.io.list

%files gb-inotify
%defattr(-,root,root)
%{_libdir}/%{name}/gb.inotify.component
%{_libdir}/%{name}/gb.inotify.la
%{_libdir}/%{name}/gb.inotify.so*
%{_datadir}/%{name}/info/gb.inotify.info
%{_datadir}/%{name}/info/gb.inotify.list

%files gb-jit
%defattr(-,root,root)
%{_libdir}/%{name}/gb.jit.*
%{_datadir}/%{name}/info/gb.jit.*

%files gb-logging
%defattr(-,root,root)
%{_libdir}/%{name}/gb.logging.*
%{_datadir}/%{name}/info/gb.logging.*

%files gb-markdown
%defattr(-,root,root)
%{_libdir}/%{name}/gb.markdown.component
%{_libdir}/%{name}/gb.markdown.gambas
%{_datadir}/%{name}/info/gb.markdown.info
%{_datadir}/%{name}/info/gb.markdown.list

%files gb-media
%{_libdir}/%{name}/gb.media*.component
%{_libdir}/%{name}/gb.media.form.gambas
%{_libdir}/%{name}/gb.media.la
%{_libdir}/%{name}/gb.media.so*
%{_datadir}/%{name}/control/gb.media.form/
%{_datadir}/%{name}/info/gb.media*.info
%{_datadir}/%{name}/info/gb.media*.list

%files gb-maps
%defattr(-,root,root)
%{_libdir}/%{name}/gb.map.*
%{_datadir}/%{name}/info/gb.map.*
%{_datadir}/%{name}/control/gb.map/

%files gb-memcached
%defattr(-,root,root)
%{_libdir}/%{name}/gb.memcached.*
%{_datadir}/%{name}/info/gb.memcached.*

%files gb-mime
%defattr(-,root,root)
%{_libdir}/%{name}/gb.mime.*
%{_datadir}/%{name}/info/gb.mime.*

%files gb-mysql
%defattr(-,root,root)
%{_libdir}/%{name}/gb.mysql.component
%{_libdir}/%{name}/gb.mysql.gambas
%{_datadir}/%{name}/info/gb.mysql.info
%{_datadir}/%{name}/info/gb.mysql.list

%if %{with gambas_ncurses}
%files gb-ncurses
%defattr(-,root,root)
%{_libdir}/%{name}/gb.ncurses.*
%{_datadir}/%{name}/info/gb.ncurses.*
%endif

%files gb-net
%defattr(-,root,root)
%{_libdir}/%{name}/gb.net.la
%{_libdir}/%{name}/gb.net.so*
%{_libdir}/%{name}/gb.net.component
%{_datadir}/%{name}/info/gb.net.info
%{_datadir}/%{name}/info/gb.net.list

%files gb-net-curl
%defattr(-,root,root)
%{_libdir}/%{name}/gb.net.curl.gambas
%{_libdir}/%{name}/gb.net.curl.la
%{_libdir}/%{name}/gb.net.curl.so*
%{_libdir}/%{name}/gb.net.curl.component
%{_datadir}/%{name}/info/gb.net.curl.info
%{_datadir}/%{name}/info/gb.net.curl.list

%files gb-net-pop3
%defattr(-,root,root)
%{_libdir}/%{name}/gb.net.pop3.*
%{_datadir}/%{name}/info/gb.net.pop3.*
%{_datadir}/%{name}/control/gb.net.pop3/

%files gb-net-smtp
%defattr(-,root,root)
%{_libdir}/%{name}/gb.net.smtp.component
%{_libdir}/%{name}/gb.net.smtp.gambas
%{_datadir}/%{name}/info/gb.net.smtp.info
%{_datadir}/%{name}/info/gb.net.smtp.list
%{_datadir}/%{name}/control/gb.net.smtp/

%files gb-opengl
%defattr(-,root,root)
%{_libdir}/%{name}/gb.opengl.component
%{_libdir}/%{name}/gb.opengl.la
%{_libdir}/%{name}/gb.opengl.so*
%{_datadir}/%{name}/info/gb.opengl.info
%{_datadir}/%{name}/info/gb.opengl.list

%files gb-opengl-glu
%defattr(-,root,root)
%{_libdir}/%{name}/gb.opengl.glu.component
%{_libdir}/%{name}/gb.opengl.glu.la
%{_libdir}/%{name}/gb.opengl.glu.so*
%{_datadir}/%{name}/info/gb.opengl.glu.info
%{_datadir}/%{name}/info/gb.opengl.glu.list

%files gb-opengl-glsl
%defattr(-,root,root)
%{_libdir}/%{name}/gb.opengl.glsl.component
%{_libdir}/%{name}/gb.opengl.glsl.la
%{_libdir}/%{name}/gb.opengl.glsl.so*
%{_datadir}/%{name}/info/gb.opengl.glsl.info
%{_datadir}/%{name}/info/gb.opengl.glsl.list

%files gb-opengl-sge
%defattr(-,root,root)
%{_libdir}/%{name}/gb.opengl.sge.component
%{_libdir}/%{name}/gb.opengl.sge.la
%{_libdir}/%{name}/gb.opengl.sge.so*
%{_datadir}/%{name}/info/gb.opengl.sge.info
%{_datadir}/%{name}/info/gb.opengl.sge.list

%files gb-openssl
%defattr(-,root,root)
%{_libdir}/%{name}/gb.openssl.component
%{_libdir}/%{name}/gb.openssl.la
%{_libdir}/%{name}/gb.openssl.so*
%{_datadir}/%{name}/info/gb.openssl.info
%{_datadir}/%{name}/info/gb.openssl.list

%if %{with openal}
%files gb-openal
%defattr(-,root,root)
%{_libdir}/%{name}/gb.openal.*
%{_datadir}/%{name}/info/gb.openal.*
%endif

%files gb-option
%defattr(-,root,root)
%{_libdir}/%{name}/gb.option.*
%{_datadir}/%{name}/info/gb.option.*

%files gb-pcre
%defattr(-,root,root)
%{_libdir}/%{name}/gb.pcre.*
%{_datadir}/%{name}/info/gb.pcre.*

%files gb-pdf
%defattr(-,root,root)
%{_libdir}/%{name}/gb.pdf.*
%{_datadir}/%{name}/info/gb.pdf.*

%if %{with qt4}
%files gb-qt4
%defattr(-,root,root)
%{_libdir}/%{name}/gb.qt4.la
%{_libdir}/%{name}/gb.qt4.so*
%{_libdir}/%{name}/gb.qt4.component
%{_datadir}/%{name}/info/gb.qt4.info
%{_datadir}/%{name}/info/gb.qt4.list

%files gb-qt4-ext
%defattr(-,root,root)
%{_libdir}/%{name}/gb.qt4.ext.la
%{_libdir}/%{name}/gb.qt4.ext.so*
%{_libdir}/%{name}/gb.qt4.ext.component
%{_datadir}/%{name}/info/gb.qt4.ext.info
%{_datadir}/%{name}/info/gb.qt4.ext.list

%files gb-qt4-opengl
%defattr(-,root,root)
%{_libdir}/%{name}/gb.qt4.opengl.component
%{_libdir}/%{name}/gb.qt4.opengl.la
%{_libdir}/%{name}/gb.qt4.opengl.so*
%{_datadir}/%{name}/info/gb.qt4.opengl.info
%{_datadir}/%{name}/info/gb.qt4.opengl.list

%files gb-qt4-webkit
%defattr(-,root,root)
%{_libdir}/%{name}/gb.qt4.webkit.component
%{_libdir}/%{name}/gb.qt4.webkit.la
%{_libdir}/%{name}/gb.qt4.webkit.so*
%{_datadir}/%{name}/control/gb.qt4.webkit/
%{_datadir}/%{name}/info/gb.qt4.webkit.info
%{_datadir}/%{name}/info/gb.qt4.webkit.list
%endif

%if %{with qt5}
%files gb-qt5
%defattr(-,root,root)
%{_libdir}/%{name}/gb.qt5.component
%{_libdir}/%{name}/gb.qt5.la
%{_libdir}/%{name}/gb.qt5.so*
%{_datadir}/%{name}/info/gb.qt5.info
%{_datadir}/%{name}/info/gb.qt5.list

%files gb-qt5-ext
%{_libdir}/%{name}/gb.qt5.ext.component
%{_libdir}/%{name}/gb.qt5.ext.la
%{_libdir}/%{name}/gb.qt5.ext.so*
%{_datadir}/%{name}/info/gb.qt5.ext.info
%{_datadir}/%{name}/info/gb.qt5.ext.list

%files gb-qt5-opengl
%defattr(-,root,root)
%{_libdir}/%{name}/gb.qt5.opengl.component
%{_libdir}/%{name}/gb.qt5.opengl.la
%{_libdir}/%{name}/gb.qt5.opengl.so*
%{_datadir}/%{name}/info/gb.qt5.opengl.list
%{_datadir}/%{name}/info/gb.qt5.opengl.info

%files gb-qt5-webkit
%defattr(-,root,root)
%{_libdir}/%{name}/gb.qt5.webkit.component
%{_libdir}/%{name}/gb.qt5.webkit.la
%{_libdir}/%{name}/gb.qt5.webkit.so*
%{_datadir}/%{name}/control/gb.qt5.webkit/
%{_datadir}/%{name}/info/gb.qt5.webkit.info
%{_datadir}/%{name}/info/gb.qt5.webkit.list
%endif

%files gb-report
%defattr(-,root,root)
%{_libdir}/%{name}/gb.report.*
%{_datadir}/%{name}/control/gb.report/
%{_datadir}/%{name}/info/gb.report.info
%{_datadir}/%{name}/info/gb.report.list

%files gb-report2
%defattr(-,root,root)
%{_libdir}/%{name}/gb.report2.*
%{_datadir}/%{name}/control/gb.report2/
%{_datadir}/%{name}/info/gb.report2.info
%{_datadir}/%{name}/info/gb.report2.list

%files gb-scanner
%defattr(-,root,root)
%{_libdir}/%{name}/gb.scanner.*
%{_datadir}/%{name}/info/gb.scanner.*

%files gb-sdl
%defattr(-,root,root)
%{_libdir}/%{name}/gb.sdl.la
%{_libdir}/%{name}/gb.sdl.so
%{_libdir}/%{name}/gb.sdl.so.*
%{_libdir}/%{name}/gb.sdl.component
%{_datadir}/%{name}/info/gb.sdl.info
%{_datadir}/%{name}/info/gb.sdl.list

%files gb-sdl-sound
%defattr(-,root,root)
%{_libdir}/%{name}/gb.sdl.sound.component
%{_libdir}/%{name}/gb.sdl.sound.la
%{_libdir}/%{name}/gb.sdl.sound.so*
%{_datadir}/%{name}/info/gb.sdl.sound.info
%{_datadir}/%{name}/info/gb.sdl.sound.list

%files gb-settings
%defattr(-,root,root)
%{_libdir}/%{name}/gb.settings.*
%{_datadir}/%{name}/info/gb.settings.info
%{_datadir}/%{name}/info/gb.settings.list

%files gb-signal
%defattr(-,root,root)
%{_libdir}/%{name}/gb.signal.component
%{_libdir}/%{name}/gb.signal.la
%{_libdir}/%{name}/gb.signal.so*
%{_datadir}/%{name}/info/gb.signal.info
%{_datadir}/%{name}/info/gb.signal.list

%files gb-util
%defattr(-,root,root)
%{_libdir}/%{name}/gb.util.component
%{_libdir}/%{name}/gb.util.gambas
%{_datadir}/%{name}/info/gb.util.info
%{_datadir}/%{name}/info/gb.util.list

%files gb-util-web
%defattr(-,root,root)
%{_libdir}/%{name}/gb.util.web.*
%dir %{_datadir}/%{name}/control/gb.util.web
%{_datadir}/%{name}/control/gb.util.web/
%{_datadir}/%{name}/info/gb.util.web.*

%files gb-v4l
%defattr(-,root,root)
%{_libdir}/%{name}/gb.v4l.*
%{_datadir}/%{name}/info/gb.v4l.*

%files gb-vb
%defattr(-,root,root)
%{_libdir}/%{name}/gb.vb.la
%{_libdir}/%{name}/gb.vb.so*
%{_libdir}/%{name}/gb.vb.component
%{_datadir}/%{name}/info/gb.vb.info
%{_datadir}/%{name}/info/gb.vb.list

%files gb-xml
%defattr(-,root,root)
%{_libdir}/%{name}/gb.xml.component
%{_libdir}/%{name}/gb.xml.gambas
%{_libdir}/%{name}/gb.xml.la
%{_libdir}/%{name}/gb.xml.so*
%{_datadir}/%{name}/info/gb.xml.info
%{_datadir}/%{name}/info/gb.xml.list

%files gb-libxml
%defattr(-,root,root)
%{_libdir}/%{name}/gb.libxml.component
%{_libdir}/%{name}/gb.libxml.la
%{_libdir}/%{name}/gb.libxml.so*
%{_datadir}/%{name}/info/gb.libxml.info
%{_datadir}/%{name}/info/gb.libxml.list

%files gb-xml-rpc
%defattr(-,root,root)
%{_libdir}/%{name}/gb.xml.rpc.component
%{_libdir}/%{name}/gb.xml.rpc.gambas
%{_libdir}/%{name}/gb.xml.html.component
%{_libdir}/%{name}/gb.xml.html.la
%{_libdir}/%{name}/gb.xml.html.so*
%{_datadir}/%{name}/info/gb.xml.rpc.info
%{_datadir}/%{name}/info/gb.xml.rpc.list
%{_datadir}/%{name}/info/gb.xml.html.info
%{_datadir}/%{name}/info/gb.xml.html.list

%files gb-xml-xslt
%defattr(-,root,root)
%{_libdir}/%{name}/gb.xml.xslt.component
%{_libdir}/%{name}/gb.xml.xslt.la
%{_libdir}/%{name}/gb.xml.xslt.so*
%{_datadir}/%{name}/info/gb.xml.xslt.info
%{_datadir}/%{name}/info/gb.xml.xslt.list

%files gb-web
%defattr(-,root,root)
%{_libdir}/%{name}/gb.web.*
%{_datadir}/%{name}/info/gb.web.info
%{_datadir}/%{name}/info/gb.web.list

%files gb-web-feed
%defattr(-,root,root)
%{_datadir}/%{name}/info/gb.web.feed.info
%{_datadir}/%{name}/info/gb.web.feed.list

%files gb-web-form
%defattr(-,root,root)
%{_datadir}/%{name}/control/gb.web.form/
%{_datadir}/%{name}/info/gb.web.form.info
%{_datadir}/%{name}/info/gb.web.form.list

%files gb-form-terminal
%defattr(-,root,root)
%{_libdir}/%{name}/gb.form.terminal.component
%{_libdir}/%{name}/gb.form.terminal.gambas
%{_datadir}/%{name}/control/gb.form.terminal/
%{_datadir}/%{name}/info/gb.form.terminal.info
%{_datadir}/%{name}/info/gb.form.terminal.list

%files gb-term
%defattr(-,root,root)
%{_libdir}/%{name}/gb.term.component
%{_libdir}/%{name}/gb.term.la
%{_libdir}/%{name}/gb.term.so*
%{_datadir}/%{name}/info/gb.term.info
%{_datadir}/%{name}/info/gb.term.list

%files gb-term-form
%defattr(-,root,root)
%{_libdir}/%{name}/gb.term.form.component
%{_libdir}/%{name}/gb.term.form.gambas
%{_datadir}/%{name}/control/gb.term.form/
%{_datadir}/%{name}/info/gb.term.form.info
%{_datadir}/%{name}/info/gb.term.form.list

%changelog
