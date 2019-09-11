#
# spec file for package efl
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


%define sover 1
# git builds from X11:Enlightenment:Nightly need autoreconf
%define _git %(tar -atf %{_sourcedir}/%{name}-*.tar.?z 2> /dev/null | grep -q -m1 'configure$' || echo 1)
# build doc is disabled due to #897122 once the bug is resolved it can be re enabled
%define build_doc 0
# Build doc needs to be defined for build doc man to work
%define build_doc_man 0
%define gstreamer1_present 1
%define build_examples 0
%if !0%{?suse_version} || 0%{?is_opensuse}
%define physics_present 1
%endif
# Currently we don't need to build any  plugins and theres none that make
# sense to build
%define generic_players_present 0
%if 0%{?suse_version} == 1315
%define xinput22_present 0
%else
%define xinput22_present 1
%endif
%if 0%{?suse_version} == 1315
%define xinput22_present 0
%else
%define xinput22_present 1
%endif
# fedora SLEs 12 don't support xine
%if (0%{?suse_version} == 1315 || !0%{?suse_version})
%define xine_present 0
%else
%define xine_present 1
%endif
%ifarch %ix86 x86_64 %{arml} ppc
%if !0%{?suse_version} || 0%{?is_opensuse}
%define luajit_present 1
%endif
%endif
%if 0%{?is_opensuse}
%define poppler_present 1
%else
%define poppler_present 0
%endif
%if 0%{?is_opensuse}
# VLC is broken atm
%define vlc_present 0
%else
%define vlc_present 0
%endif
%if 0%{?suse_version} > 1320 || 0%{?fedora}
%define enable_wayland 1
%endif
# Build with an alternate package names for Mageia
%if 0%{?mageia}
%ifarch x86_64
%define _bit %(getconf LONG_BIT)
%endif
%endif
# If packages are targeted for anything other than openSUSE
%{?!icon_theme_cache_create_ghost:%define icon_theme_cache_create_ghost() touch %{buildroot}%{_datadir}/icons/%1/icon-theme.cache}
%{?!icon_theme_cache_post:%define icon_theme_cache_post() gtk-update-icon-cache %{_datadir}/icons/$1 &> /dev/null || :}
Name:           efl
Version:        1.22.2
Release:        0
# TODO: split package to separate packages and specify licenses correctly
Summary:        Enlightenment Foundation Libraries - set of libraries used (not only) by E17
License:        BSD-2-Clause AND LGPL-2.1-only AND Zlib
Group:          Development/Libraries/C and C++
Url:            https://git.enlightenment.org/core/efl.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ImageMagick
BuildRequires:  autoconf >= 2.5
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  giflib-devel
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libraw-devel
BuildRequires:  libspectre-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python >= 2.5
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dri)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libpng) >= 1.2.10
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang
Recommends:     elua = %{version}
Provides:       ecore = %{version}
Obsoletes:      ecore < %{version}
Provides:       edje-utils = %{version}
Obsoletes:      edje-utils < %{version}
Provides:       eet = %{version}
Obsoletes:      eet < %{version}
Provides:       eeze = %{version}
Obsoletes:      eeze < %{version}
Provides:       efreet = %{version}
Obsoletes:      efreet < %{version}
Provides:       eina = %{version}
Obsoletes:      eina < %{version}
Provides:       emotion = %{version}
Obsoletes:      emotion < %{version}
Provides:       ethumb = %{version}
Obsoletes:      ethumb < %{version}
Provides:       evas = %{version}
Obsoletes:      evas < %{version}
%{?systemd_requires}
%if %{build_doc}
BuildRequires:  doxygen
%endif
%if %{poppler_present}
# boo#864299 need libpoppler-cpp0 for Leap / SLE
BuildRequires:  libpoppler-cpp0
BuildRequires:  libpoppler-devel
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
%ifarch %ix86 x86_64 ppc ppc64 ppc64le s390x armv7l armv7hl armv6l armv6hl aarch64
BuildRequires:  valgrind
%endif
%if 0%{?physics_present}
BuildRequires:  pkgconfig(bullet) >= 2.80
%endif
%if %{vlc_present}
BuildRequires:  pkgconfig(libvlc)
%endif
%if %{xine_present}
BuildRequires:  pkgconfig(libxine)
%endif
%if 0%{?luajit_present}
BuildRequires:  pkgconfig(luajit)
%else
%if 0%{?suse_version} >= 1330
BuildRequires:  pkgconfig(lua5.1)
%else
BuildRequires:  pkgconfig(lua) < 5.2
%endif
%endif
%if 0%{?enable_wayland}
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(libdrm) >= 2.4
BuildRequires:  pkgconfig(libinput) >= 0.6.0
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client) >= 1.11.0
BuildRequires:  pkgconfig(wayland-cursor) >= 1.11.0
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.10
BuildRequires:  pkgconfig(wayland-scanner) >= 1.11.0
BuildRequires:  pkgconfig(wayland-server) >= 1.11.0
BuildRequires:  pkgconfig(xkbcommon)
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

%description
EFL is library collection providing various functionality used (not onyl)
by Enlightenment 17, Terminology, Tizen mobile platform and much more.

%lang_package

%package %{?mageia:-n %{_lib}%{name}-}devel
Summary:        Headers, pkgconfig files and other files for development with EFL
License:        BSD-2-Clause AND LGPL-2.1-only AND Zlib
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       edje = %{version}
Requires:       embryo = %{version}
Requires:       gettext-devel
Requires:       giflib-devel
Requires:       glibc-devel
Requires:       lib%{?mageia:%{?_bit}}ecore%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}ector%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}edje%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}eet%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}eeze%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}efreet%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}efreet_mime%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}efreet_trash%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}eina%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}eio%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}eldbus%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}elementary%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}elocation%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}embryo%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}emile%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}emotion%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}eo%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}ethumb%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}ethumb_client%{sover} = %{version}
Requires:       lib%{?mageia:%{?_bit}}evas%{sover} = %{version}
Requires:       pkgconfig(dbus-1)
Requires:       pkgconfig(dri)
Requires:       pkgconfig(egl)
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(fribidi)
Requires:       pkgconfig(glesv2)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(harfbuzz)
Requires:       pkgconfig(libcurl)
Requires:       pkgconfig(libexif)
Requires:       pkgconfig(libpng) >= 1.2.10
Requires:       pkgconfig(libpulse)
Requires:       pkgconfig(librsvg-2.0)
Requires:       pkgconfig(libtiff-4)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(pixman-1)
Requires:       pkgconfig(sdl)
Requires:       pkgconfig(sndfile)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xcomposite)
Requires:       pkgconfig(xcursor)
Requires:       pkgconfig(xdmcp)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xi)
Requires:       pkgconfig(xinerama)
Requires:       pkgconfig(xp)
Requires:       pkgconfig(xproto)
Requires:       pkgconfig(xrandr)
Requires:       pkgconfig(xscrnsaver)
Requires:       pkgconfig(xtst)
Requires:       pkgconfig(zlib)
Provides:       %{?mageia:%{_lib}}ecore-devel = %{version}
Provides:       %{?mageia:%{_lib}}edbus-devel = %{version}
Provides:       %{?mageia:%{_lib}}edje-devel = %{version}
Provides:       %{?mageia:%{_lib}}eet-devel = %{version}
Provides:       %{?mageia:%{_lib}}eeze-devel = %{version}
Provides:       %{?mageia:%{_lib}}efreet-devel = %{version}
Provides:       %{?mageia:%{_lib}}eina-devel = %{version}
Provides:       %{?mageia:%{_lib}}eio-devel = %{version}
Provides:       %{?mageia:%{_lib}}elementary-devel = %{version}
Provides:       %{?mageia:%{_lib}}embryo-devel = %{version}
Provides:       %{?mageia:%{_lib}}emotion-devel = %{version}
Provides:       %{?mageia:%{_lib}}emotion-generic-players-devel = %{version}
Provides:       %{?mageia:%{_lib}}eo-devel = %{version}
Provides:       %{?mageia:%{_lib}}ethumb-devel = %{version}
Provides:       %{?mageia:%{_lib}}evas-devel = %{version}
Provides:       %{?mageia:%{_lib}}evas-generic-loaders-devel = %{version}
Obsoletes:      %{?mageia:%{_lib}}ecore-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}edbus-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}edje-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eet-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eeze-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}efreet-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eina-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eio-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}elementary-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}embryo-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}emotion-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}emotion-generic-players-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}eo-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}ethumb-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}evas-devel < %{version}
Obsoletes:      %{?mageia:%{_lib}}evas-generic-loaders-devel < %{version}
%if %{xine_present}
Requires:       pkgconfig(libxine)
%endif
%if 0%{?luajit_present}
Requires:       pkgconfig(luajit)
%else
%if 0%{?suse_version} >= 1330
Requires:       pkgconfig(lua5.1)
%else
Requires:       pkgconfig(lua) < 5.2
%endif
%endif
%if %{gstreamer1_present}
Requires:       pkgconfig(gstreamer-1.0)
Requires:       pkgconfig(gstreamer-plugins-base-1.0)
%endif
%if 0%{?physics_present}
Requires:       lib%{?mageia:%{?_bit}}ephysics%{sover} = %{version}
Requires:       pkgconfig(bullet)
%endif
%if 0%{?physics_present}
Provides:       %{?mageia:%{_lib}}ephysics-devel = %{version}
Obsoletes:      %{?mageia:%{_lib}}ephysics-devel < %{version}
%endif

%description %{?mageia:-n %{_lib}%{name}-}devel
Headers, pkgconfig files and other files needed for development with EFL.

%package -n lib%{?mageia:%{?_bit}}ecore%{sover}
Summary:        Ecore, part of EFL
License:        BSD-2-Clause
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}ecore%{sover}
Ecore is a clean and tiny event loop library with many modules to do lots of
convenient things for a programmer, to save time and effort.

%package -n lib%{?mageia:%{?_bit}}ector%{sover}
Summary:        Ector, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}ector%{sover}
Ector provides a new retained rendering library that is used by Evas to
provide Evas_Object_VG. This is a new Evas_Object that provides a vector
graphics scene graph following the SVG specification. It will be considered
a bug if some behaviour does not follow the SVG standard.

Evas_Object_VG provides 3 kind of objects for now: shape, as well as linear
and radial gradients.

%package -n lib%{?mageia:%{?_bit}}edje%{sover}
Summary:        Edje, part of EFL
License:        BSD-2-Clause AND GPL-2.0-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}edje%{sover}
Abstract GUI layout and animation object library.

%package -n lib%{?mageia:%{?_bit}}eldbus%{sover}
Summary:        ELDbus, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}eldbus%{sover}
ELDbus is a wrapper around libdbus for the Enlightenment Foundation Libraries.

%package -n lib%{?mageia:%{?_bit}}eet%{sover}
Summary:        Eet, part of EFL
License:        BSD-2-Clause
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}eet%{sover}
Eet is a tiny library designed to write an arbitrary set of chunks of data
to a file and optionally compress each chunk (very much like a zip file)
and allow fast random-access reading of the file later on. It does not do
zip as a zip itself has more complexity than is needed, and it was much
simpler to implement this once here.

It also can encode and decode data structures in memory, as well as image
data for saving to eet files or sending across the network to other
machines, or just writing to arbitrary files on the system. All data is
encoded in a platform independent way and can be written and read by any
architecture.

%package -n lib%{?mageia:%{?_bit}}eeze%{sover}
Summary:        Eeze, part of EFL
License:        BSD-2-Clause
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}eeze%{sover}
Eeze is a library for manipulating devices through udev with a simple and
fast api. It interfaces directly with libudev, avoiding such middleman
daemons as udisks/upower or hal, to immediately gather device information
the instant it becomes known to the system.  This can be used to determine
such things as:
  * If a cdrom has a disk inserted
  * The temperature of a cpu core
  * The remaining power left in a battery
  * The current power consumption of various parts
  * Monitor in realtime the status of peripheral devices

Each of the above examples can be performed by using only a single eeze
function, as one of the primary focuses of the library is to reduce the
complexity of managing devices.

%package -n lib%{?mageia:%{?_bit}}efl%{sover}
Summary:        EFL's general purpose library
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}efl%{sover}
The foundation components for the Enlightenment foundation libraries.

%package -n lib%{?mageia:%{?_bit}}efreet%{sover}
Summary:        Efreet, part of EFL
License:        BSD-2-Clause
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}efreet%{sover}
Standards handling for FreeDesktop.org standards.

%package -n lib%{?mageia:%{?_bit}}efreet_mime%{sover}
Summary:        Efreet, part of EFL
License:        BSD-2-Clause
Group:          System/Libraries
Conflicts:      lib%{?mageia:%{?_bit}}efreet%{sover} < 1.8

%description -n lib%{?mageia:%{?_bit}}efreet_mime%{sover}
Standards handling for FreeDesktop.org mime types.

%package -n lib%{?mageia:%{?_bit}}efreet_trash%{sover}
Summary:        Efreet, part of EFL
License:        BSD-2-Clause
Group:          System/Libraries
Conflicts:      lib%{?mageia:%{?_bit}}efreet%{sover} < 1.8

%description -n lib%{?mageia:%{?_bit}}efreet_trash%{sover}
Standards handling for FreeDesktop.org trash.

%package -n lib%{?mageia:%{?_bit}}eina%{sover}
Summary:        Eina, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}eina%{sover}
Eina is library handling various data types.

%package -n lib%{?mageia:%{?_bit}}eio%{sover}
Summary:        Eio, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}eio%{sover}
Extension of ecore for parallel I/O operations.

%package -n lib%{?mageia:%{?_bit}}elementary%{sover}
Summary:        Elementary, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}elementary%{sover}
The core shared library for widgets.

%package -n lib%{?mageia:%{?_bit}}elocation%{sover}
Summary:        ELocation, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}elocation%{sover}
A location the shared library.

%if 0%{?enable_wayland}
%package -n lib%{?mageia:%{?_bit}}elput%{sover}
Summary:        Elput, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}elput%{sover}
Elput is a library to handle input devices.

For handling wayland input.
%endif

%package -n lib%{?mageia:%{?_bit}}elua%{sover}
Summary:        Lua bindings for the EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}elua%{sover}
Support for lua within the efl.

%package -n lib%{?mageia:%{?_bit}}embryo%{sover}
Summary:        Embryo, part of EFL
License:        BSD-2-Clause AND Zlib
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}embryo%{sover}
Embryo is a tiny library designed to interpret limited small programs
compiled by the included compiler, embryo_cc. It is mostly a cleaned up and
smaller version of the original Small abstract machine. The compiler is
mostly untouched.

%package -n lib%{?mageia:%{?_bit}}emotion%{sover}
Summary:        Emotion, part of EFL
License:        BSD-2-Clause
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}emotion%{sover}
Emotion is a wrapper that provides a uniform api to a number of different
media libraries.

Currently the supported backends for this.

%package -n lib%{?mageia:%{?_bit}}emile%{sover}
Summary:        Emile, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}emile%{sover}
Emile provides a library to bring together serialization, compression and
ciphering.

It is a low-level library and can be used by anything above Eina. It came
along with a lot re-factoring of our current code base to make use of it
and de-duplicate a lot of existing code.

More refactoring is expected in ecore_con_ssl ciphering and general image
compression.

%package -n lib%{?mageia:%{?_bit}}eo%{sover}
Summary:        Eo, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}eo%{sover}
Eo is library providing basic E object in OOP way of programming.

%package -n lib%{?mageia:%{?_bit}}eolian%{sover}
Summary:        Eolian, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}eolian%{sover}
Eolian is library for binding/code generation based on Eo descriptions.

%package -n lib%{?mageia:%{?_bit}}ethumb%{sover}
Summary:        EThumb, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}ethumb%{sover}
Thumbnail generation library for EFL.

%if 0%{?physics_present}
%package -n lib%{?mageia:%{?_bit}}ephysics%{sover}
Summary:        EPhysics, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}ephysics%{sover}
EPhysics is a wrapper around bullet physics for the enlightenment
foundation libraries.
%endif

%package -n lib%{?mageia:%{?_bit}}evas%{sover}
Summary:        Evas, part of EFL
License:        BSD-2-Clause
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}evas%{sover}
Evas is a clean display canvas API that implements a scene graph, not an
immediate-mode rendering target, is cross-platform, for several target
display systems that can draw anti-aliased text, smooth super and
sub-sampled scaled images, alpha-blend objects and much more.

%package -n lib%{?mageia:%{?_bit}}ethumb_client%{sover}
Summary:        EThumb Client, part of EFL
License:        LGPL-2.1-only
Group:          System/Libraries

%description -n lib%{?mageia:%{?_bit}}ethumb_client%{sover}
Shared library of ethumb client.

%package -n edje
Summary:        Abstract GUI layout and animation object library
License:        BSD-2-Clause
Group:          System/GUI/Other
Requires:       efl = %{version}
Requires:       embryo = %{version}
Requires:       lib%{?mageia:%{?_bit}}edje%{sover} = %{version}

%description -n edje
Abstract GUI layout and animation object library.

This part of the Enlightenment Foundation Libraries.

%package -n elementary
Summary:        The widget set for enlightenment
License:        LGPL-2.1-only
Group:          System/GUI/Other
Requires:       edje = %{version}
Requires:       efl = %{version}
Requires:       enlightenment-theme-dft
Requires:       lib%{?mageia:%{?_bit}}elementary%{sover} = %{version}

%description -n elementary
Set of widgets for enlightenment focused on touch devices.

%if %{build_examples}
%package -n elementary-examples
Summary:        Elementary examples
License:        LGPL-2.1-only
Group:          Documentation/Other

%description -n elementary-examples
Examples of usage of Elementary library.
%endif

%package -n elua
Summary:        LuaJIT bindings for the efl
License:        LGPL-2.1-only
Group:          System/GUI/Other
Requires:       efl = %{version}

%description -n elua
A set of efl bindings for the LuaJIT environment.

%package -n embryo
Summary:        Abstract GUI layout and animation object library
License:        BSD-2-Clause
Group:          System/GUI/Other
Requires:       lib%{?mageia:%{?_bit}}embryo%{sover} = %{version}

%description -n embryo
Embryo is a tiny library designed to interpret limited small programs
compiled by the included compiler, embryo_cc. It is mostly a cleaned up and
smaller version of the original Small abstract machine. The compiler is
mostly untouched.

This part of the Enlightenment Foundation Libraries.

%package -n evas-generic-loaders
Summary:        Set of generic loaders for Evas
License:        GPL-2.0-or-later
Group:          System/GUI/Other

%description -n evas-generic-loaders
Set of generic loaders allowing to open XCF, PDF, PS, RAW,
MPG/AVI/OGV/MOV/MKV/WMV.

Useful only for evas library.

This part of the Enlightenment Foundation Libraries.

%if %{generic_players_present}
%package -n emotion-generic-players
Summary:        Set of generic players for Emotion
License:        GPL-2.0-or-later
Group:          System/GUI/Other

%description -n emotion-generic-players
Set of generic players (currently VLC is supported) allowing to open video
files through emotion.

Useful only for emotion library.

This part of the Enlightenment Foundation Libraries.
%endif

%if %{build_doc}
%if %{build_doc_man}
%package doc-man
Summary:        EFL reference man pages
License:        BSD-2-Clause
Group:          Documentation/Man

%description doc-man
Documentation in form of man pages describing EFL API.
%endif #build_doc_man

%package doc-html
Summary:        EFL reference man pages
License:        BSD-2-Clause
Group:          Documentation/HTML

%description doc-html
Documentation in form of HTML pages describing EFL API.
%endif #build_doc

%if %{build_examples}
%package examples
Summary:        Examples of EFL usage
License:        BSD-2-Clause AND LGPL-2.1-only AND Zlib
Group:          Documentation/Man

%description examples
Examples usage of the EFL library.
%endif

%package testsuite
Summary:        EFL testsuite
License:        BSD-2-Clause AND LGPL-2.1-only AND Zlib
Group:          System/GUI/Other
Requires:       lib%{?mageia:%{?_bit}}efreet%{sover} = %{version}

%description testsuite
Testsuite of EFL package.

%package -n enlightenment-theme-upstream
Version:        0.21.0
Release:        0
Summary:        Default Enlightenment theme
License:        BSD-2-Clause AND LGPL-2.1-only
Group:          System/GUI/Other
Conflicts:      otherproviders(enlightenment-theme-dft)
Provides:       enlightenment-theme = 0.1
Provides:       enlightenment-theme-dft

%description  -n enlightenment-theme-upstream
For use with upstream branding, when using openSUSE themes, when using
openSUSE themes Use the Dark theme instead.

%package -n enlightenment-theme-dark
Version:        0.21.0
Release:        0
Summary:        Default Enlightenment theme(Dark)
License:        BSD-2-Clause AND LGPL-2.1-only
Group:          System/GUI/Other
Provides:       enlightenment-theme

%description  -n enlightenment-theme-dark
The default theme for enlightenment install when using openSUSE branding.

%package -n enlightenment-x-dark-icon-theme
Version:        0.21.0
Release:        0
Summary:        A freedesktop.org compatible icon theme
License:        GPL-3.0-only
Group:          System/GUI/Other

%description -n enlightenment-x-dark-icon-theme
Setting this icon theme as your application icon theme in enlightenment will
make all your applications use the same icon set as the enlightenment
dark (upstream) theme.

Icon themes to match the openSUSE Enlightenment themes are also available.

%prep
%setup -q

# remove __DATE__ and __TIME__
FAKE_BUILDTIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%H:%%M')
FAKE_BUILDDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%b %%e %%Y')
FAKE_DOCDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%a %%b %%d %%Y')
sed -e "s/__TIME__/$FAKE_BUILDTIME/g" \
    -e "s/__DATE__/$FAKE_BUILDDATE/g" \
    -i $(grep -rl '__TIME__\|__DATE__') || :

# it seems that fedora libxcb-devel package doesn't contain xcb-xprint.pc
%if 0%{?fedora_version}
sed -i 's/xcb-xprint//g' {configure.ac,configure} || :
%endif

%build
%if 0%{?_git}
NOCONFIGURE=yes ./autogen.sh
automake --add-missing
%endif

ARGS=""

# efl intentionally compares string pointers in alot of places rather then strings this stops obs complaining
export CFLAGS="%{optflags} -g -Wno-address";

%{!?mageia:%configure} \
%{?mageia:%configure2_5x} \
    --disable-static \
    --disable-silent-rules \
    --disable-tslib \
%ifarch armv6hl armv6l
    --disable-neon \
%endif
%if !0%{?physics_present}
    --disable-physics \
    --enable-i-really-know-what-i-am-doing-and-that-this-will-probably-break-things-and-i-will-fix-them-myself-and-send-patches-abb \
%endif
%if ! %{poppler_present}
    --disable-poppler \
%endif
%if !0%{?luajit_present}
    --enable-lua-old \
%endif
    --enable-harfbuzz \
%if %{xinput22_present}
    --enable-xinput22 \
%endif
%if %{xine_present}
    --enable-xine \
%endif
    --enable-systemd \
    --enable-fb \
%if %{build_doc}
    --enable-doc \
%else
    --disable-doc \
%endif
%if 0%{?enable_wayland}
    --enable-drm \
    --enable-wayland \
    --enable-elput \
    --enable-egl \
    --with-opengl=es \
%endif
    $ARGS

make %{?_smp_mflags}
%if %{build_doc}
make %{?_smp_mflags} doc
%endif

%install
%make_install
%if %{build_examples}
make install-examples DESTDIR=%{buildroot}
%endif

# delete binary with suid bit set :D
rm -f "%{buildroot}/%{_bindir}/eeze_scanner"

%if %{build_doc}
%if %{build_doc_man}
# copy documentation manually
echo "Copying MAN pages"
/bin/cp -vr doc/man %{buildroot}%{_datadir}/
%endif #build_doc_man
# fix line endings
find doc/html -name '*.eps' | xargs sed -i 's@\r@\n@g'
# remove duplicates
%if 0%{?suse_version}
%fdupes -s doc/html
%if %{build_doc_man}
%fdupes -s %{buildroot}%{_mandir}/
%endif #build_doc_man
%endif
%endif #build_doc

# fix permissions
%if %{build_examples} || %{build_doc_man}
find \
%if %{build_doc_man}
     %{buildroot}%{_mandir} \
     doc \
%endif
%if %{build_examples}
     %{buildroot}%{_datadir}/*/examples \
%endif
     -type d -exec chmod 0755 {} \;
find \
%if %{build_doc_man}
     %{buildroot}%{_mandir} \
     doc \
%endif
%if %{build_examples}
     %{buildroot}%{_datadir}/*/examples \
%endif
    -type f -exec chmod 0644 {} \;
%endif

# python gdb pretty printers shouldn't have execute permissions.
chmod 0644 %{buildroot}%{_datadir}/eo/gdb/eo_gdb.py

# create theme version for dark package
cp %{buildroot}%{_datadir}/elementary/themes/default.edj %{buildroot}%{_datadir}/elementary/themes/dark.edj

# move icons as openSUSE also ships
mv %{buildroot}/%{_datadir}/icons/Enlightenment-X %{buildroot}/%{_datadir}/icons/Enlightenment-X-dark
touch %{buildroot}%{_datadir}/icons/Enlightenment-X-dark/icon-theme.cache

find %{buildroot} -type f -name "*.la" -delete -print

%if 0%{?suse_version}
%{suse_update_desktop_file \
    -N "Elementary Configuration" -G "Elementary Configuration" -r elementary_config Enlightenment Settings DesktopSettings}
%{suse_update_desktop_file \
    -N "Elementary Test" -G "Elementary Test" -r elementary_test Enlightenment Development IDE}
%fdupes -s %{buildroot}%{_datadir}/icons/Enlightenment-X-dark
%fdupes -s %{buildroot}%{_datadir}/%{name}/examples
%endif

%find_lang %{name}

%post
/sbin/ldconfig
%if !0%{?mageia}
%systemd_user_post ethumb.service
%endif

%if !0%{?mageia}
%preun
%systemd_user_preun ethumb.service
%endif

%postun
/sbin/ldconfig
%if !0%{?mageia}
%systemd_user_postun ethumb.service
%endif

%post -n lib%{?mageia:%{?_bit}}ecore%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}ecore%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}ector%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}ector%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}edje%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}edje%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}eldbus%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}eldbus%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}eet%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}eet%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}eeze%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}eeze%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}efl%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}efl%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}efreet%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}efreet%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}eina%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}eina%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}eio%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}eio%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}elementary%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}elementary%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}elocation%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}elocation%{sover} -p /sbin/ldconfig

%if 0%{?enable_wayland}
%post -n lib%{?mageia:%{?_bit}}elput%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}elput%{sover} -p /sbin/ldconfig
%endif

%post -n lib%{?mageia:%{?_bit}}elua%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}elua%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}embryo%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}embryo%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}emile%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}emile%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}emotion%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}emotion%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}eo%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}eo%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}eolian%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}eolian%{sover} -p /sbin/ldconfig

%if 0%{?physics_present}
%post -n lib%{?mageia:%{?_bit}}ephysics%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}ephysics%{sover} -p /sbin/ldconfig
%endif

%post -n lib%{?mageia:%{?_bit}}ethumb%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}ethumb%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}ethumb_client%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}ethumb_client%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}evas%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}evas%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}efreet_trash%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}efreet_trash%{sover} -p /sbin/ldconfig
%post -n lib%{?mageia:%{?_bit}}efreet_mime%{sover} -p /sbin/ldconfig
%postun -n lib%{?mageia:%{?_bit}}efreet_mime%{sover} -p /sbin/ldconfig

%if 0%{?suse_version} < 1320 || 0%{?mageia} 
%post -n elementary
%icon_theme_cache_post
%desktop_database_post

%postun -n elementary
%icon_theme_cache_postun
%desktop_database_postun

%post -n edje
%mime_database_post

%postun -n edje
%mime_database_postun
%endif

%if 0%{?suse_version} < 1320 || !0%{?suse_version}
%post -n enlightenment-x-dark-icon-theme
gtk-update-icon-cache %{_datadir}/icons/Enlightenment-X-dark &> /dev/null || :
%endif

%{?suse_version:%files}
%{!?suse_version:%files -f %{name}.lang}
%{_bindir}/*
%exclude %{_bindir}/edje_*
%exclude %{_bindir}/elementary_*
%exclude %{_bindir}/embryo_*
%exclude %{_datadir}/ecore_x/checkme
%exclude %{_datadir}/evas/checkme
%if %{build_examples}
%exclude %{_datadir}/*/examples
%endif
# evas generic loaders
%exclude %{_libdir}/evas/utils/

%if %{generic_players_present}
%exclude %{_libdir}/emotion/generic_players/
%endif

%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/ecore_con
%{_libdir}/ecore_evas
%{_libdir}/ecore_imf
%if 0%{?enable_wayland}
%{_libdir}/ecore_wl2
%endif
%{_libdir}/ecore
%{_libdir}/eeze
%{_libdir}/efreet
%{_libdir}/emotion
%{_libdir}/ethumb
%{_libdir}/ethumb_client
%{_libdir}/evas
%{_datadir}/dbus-1
%{_datadir}/ecore
%{_datadir}/ecore_x
%{_datadir}/emotion
%{_datadir}/eo
%{_datadir}/ethumb
%{_datadir}/evas
%{_userunitdir}/ethumb.service

%if 0%{?suse_version}
%files lang -f %{name}.lang
%endif

%files -n lib%{?mageia:%{?_bit}}efl%{sover}
%{_libdir}/libefl*.so.*

%files -n lib%{?mageia:%{?_bit}}ecore%{sover}
%{_libdir}/libecore*.so.*

%files -n lib%{?mageia:%{?_bit}}ector%{sover}
%{_libdir}/libector*.so.*

%files -n lib%{?mageia:%{?_bit}}edje%{sover}
%{_libdir}/libedje.so.*

%files -n lib%{?mageia:%{?_bit}}eldbus%{sover}
%{_libdir}/libeldbus.so.*

%files -n lib%{?mageia:%{?_bit}}elocation%{sover}
%{_libdir}/libelocation.so.*

%if 0%{?enable_wayland}
%files -n lib%{?mageia:%{?_bit}}elput%{sover}
%{_libdir}/libelput.so.*
%endif

%if 0%{?luajit_present}
%files -n lib%{?mageia:%{?_bit}}elua%{sover}
%{_libdir}/libelua.so.*
%endif

%files -n lib%{?mageia:%{?_bit}}eet%{sover}
%{_libdir}/libeet.so.*

%files -n lib%{?mageia:%{?_bit}}eeze%{sover}
%{_libdir}/libeeze.so.*

%files -n lib%{?mageia:%{?_bit}}efreet%{sover}
%{_libdir}/libefreet.so.*

%files -n lib%{?mageia:%{?_bit}}efreet_mime%{sover}
%{_libdir}/libefreet_mime.so.*

%files -n lib%{?mageia:%{?_bit}}efreet_trash%{sover}
%{_libdir}/libefreet_trash.so.*

%files -n lib%{?mageia:%{?_bit}}eina%{sover}
%{_libdir}/libeina.so.*

%files -n lib%{?mageia:%{?_bit}}eio%{sover}
%{_libdir}/libeio.so.*

%files -n lib%{?mageia:%{?_bit}}elementary%{sover}
%{_libdir}/libelementary.so.*

%files -n lib%{?mageia:%{?_bit}}embryo%{sover}
%{_libdir}/libembryo.so.*

%files -n lib%{?mageia:%{?_bit}}emile%{sover}
%{_libdir}/libemile.so.*

%files -n lib%{?mageia:%{?_bit}}emotion%{sover}
%{_libdir}/libemotion.so.*

%files -n lib%{?mageia:%{?_bit}}eo%{sover}
%{_libdir}/libeo.so.*

%files -n lib%{?mageia:%{?_bit}}eolian%{sover}
%{_libdir}/libeolian.so.*

%if 0%{?physics_present}
%files -n lib%{?mageia:%{?_bit}}ephysics%{sover}
%{_libdir}/libephysics.so.*
%endif

%files -n lib%{?mageia:%{?_bit}}ethumb%{sover}
%{_libdir}/libethumb.so.*

%files -n lib%{?mageia:%{?_bit}}ethumb_client%{sover}
%{_libdir}/libethumb_client.so.*

%files -n lib%{?mageia:%{?_bit}}evas%{sover}
%{_libdir}/libevas.so.*

%files %{?mageia:-n %{_lib}%{name}-}devel
%{_bindir}/elementary_codegen
%{_bindir}/elementary_test
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so
%{_libdir}/libeo_dbg.so.*
%{_libdir}/cmake/
%{_includedir}/efl-1/
%{_includedir}/efl-cxx-1/
%if 0%{?enable_wayland}
%{_includedir}/efl-wl-1/
%endif
%{_includedir}/ecore-1/
%{_includedir}/ecore-audio-1/
%{_includedir}/ecore-avahi-1/
%{_includedir}/ecore-con-1/
%{_includedir}/ecore-evas-1/
%{_includedir}/ecore-fb-1/
%{_includedir}/ecore-file-1/
%{_includedir}/ecore-imf-1/
%{_includedir}/ecore-imf-evas-1/
%{_includedir}/ecore-input-1/
%{_includedir}/ecore-input-evas-1/
%{_includedir}/ecore-ipc-1/
%{_includedir}/ecore-x-1/
%{_includedir}/eldbus-1/
%{_includedir}/elementary-1
%{_includedir}/elocation-1/
%if 0%{?luajit_present}
%{_includedir}/elua-1/
%endif
%{_includedir}/edje-1/
%{_includedir}/eet-1/
%{_includedir}/eeze-1/
%{_includedir}/efreet-1/
%{_includedir}/eina-1/
%{_includedir}/eio-1/
%{_includedir}/embryo-1/
%{_includedir}/emile-1/
%{_includedir}/emotion-1/
%{_includedir}/eo-1/
%{_includedir}/eolian-1/
# C++ headers
%{_includedir}/ecore-cxx-1
%{_includedir}/edje-cxx-1
%{_includedir}/eet-cxx-1
%{_includedir}/eina-cxx-1
%{_includedir}/eio-cxx-1
%{_includedir}/eldbus_cxx-1
%{_includedir}/elementary-cxx-1
%{_includedir}/eo-cxx-1
%{_includedir}/eolian-cxx-1
%{_includedir}/evas-cxx-1

%if 0%{?physics_present}
%{_includedir}/ephysics-1/
%endif
%{_includedir}/ethumb-1/
%{_includedir}/ethumb-client-1/
%{_includedir}/evas-1/
%if 0%{?enable_wayland}
%{_includedir}/ecore-drm2-1/
%{_includedir}/ecore-wl2-1/
%{_includedir}/elput-1/
%endif
%{_datadir}/ecore_x/checkme
%{_datadir}/evas/checkme
%{_datadir}/gdb/

%files -n edje
%{_bindir}/edje_*
%{_datadir}/edje
%if %{build_examples}
%exclude %{_datadir}/edje/examples
%endif
%{_libdir}/edje
%{_datadir}/mime/packages/edje.xml

%files -n elementary
%{_bindir}/elementary_*
%exclude %{_bindir}/elementary_codegen
%exclude %{_bindir}/elementary_test
%{_datadir}/elementary
%if %{build_examples}
%exclude %{_datadir}/elementary/examples
%endif
%exclude %{_datadir}/elementary/themes/*
%{_datadir}/icons/hicolor/
%{_datadir}/applications/elementary*
%{_libdir}/elementary

%if %{build_examples}
%files -n elementary-examples
%{_datadir}/elementary/examples
%endif

%files -n elua
%{_datadir}/elua

%files -n embryo
%{_bindir}/embryo_*
%{_datadir}/embryo

%files -n enlightenment-theme-upstream
%{_datadir}/elementary/themes/default.edj

%files -n enlightenment-theme-dark
%{_datadir}/elementary/themes/dark.edj

%files -n enlightenment-x-dark-icon-theme
%{_datadir}/icons/Enlightenment-X-dark
%ghost %{_datadir}/icons/Enlightenment-X-dark/icon-theme.cache

%files -n evas-generic-loaders
%{_libdir}/evas/utils/

%if %{generic_players_present}
%files -n emotion-generic-players
%{_libdir}/emotion/generic_players/
%endif

%if %{build_doc}
%if %{build_doc_man}
%files doc-man
%{_mandir}/*/*
%endif #build_doc

%files doc-html
%doc doc/html/*

%endif #build_doc

%if %{build_examples}
%files examples
%{_datadir}/*/examples
%exclude %{_datadir}/elementary/examples
%endif

%files testsuite
%{_datadir}/ecore_imf/
%{_datadir}/eeze/
%{_datadir}/efreet/
%{_datadir}/ethumb_client/
%if %{build_examples}
%exclude %{_datadir}/ethumb_client/examples
%endif

%changelog
