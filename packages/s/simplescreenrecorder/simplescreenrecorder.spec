#
# spec file for package simplescreenrecorder
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           simplescreenrecorder
Version:        0.3.11
Release:        0
Summary:        A feature-rich screen recorder that supports X11 and OpenGL
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
Url:            http://www.maartenbaert.be/simplescreenrecorder
Source:         https://github.com/MaartenBaert/ssr/archive/%{version}.tar.gz
Source9:        baselibs.conf

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg8-devel
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui)       >= 5.7
BuildRequires:  pkgconfig(Qt5Widgets)   >= 5.7
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.7
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec) >= 53
BuildRequires:  pkgconfig(libavformat) >= 53
BuildRequires:  pkgconfig(libavutil) >= 51
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale) >= 2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
%ifarch %{ix86} x86_64
# openGL apps:
Recommends:     libssr-glinject
%if %{_lib} == "lib64"
# 32bit openGL apps at 64bit system:
Suggests:       libssr-glinject-32bit
%endif
%endif

%description
SimpleScreenRecorder is a Linux program that was created to record programs
and games.

The original goal was to create a program that was just really simple to
use, the result is actually a pretty powerful program. It's 'simple' in
the sense that it's easier to use than ffmpeg/avconv or VLC, because it
has a straightforward user interface.

Features:
 * Graphical user interface (Qt-based).
 * Faster than VLC and ffmpeg/avconv.
 * Records the entire screen or part of it, or records OpenGL applications
   directly (similar to Fraps on Windows).
 * Synchronizes audio and video properly (a common issue with VLC and
   ffmpeg/avconv).
 * Reduces the video frame rate if your computer is too slow (rather than
   using up all your RAM like VLC does).
 * Fully multithreaded: small delays in any of the components will never
   block the other components, resulting is smoother video and better
   performance on computers with multiple processors.
 * Pause and resume recording at any time (either by clicking a button or by
   pressing a hotkey).
 * Shows statistics during recording (file size, bit rate, total recording
   time, actual frame rate, ...).
 * Can show a preview during recording, so you don't waste time recording
   something only to figure out afterwards that some setting was wrong.
 * Uses libav/ffmpeg libraries for encoding, so it supports many different
   codecs and file formats (adding more is trivial).
 * Sensible default settings: no need to change anything if you don't want to.
 * Tooltips for almost everything: no need to read the documentation to find
   out what something does.


%ifarch %{ix86} x86_64
%package -n libssr-glinject
Summary:        Simple Screen Recorder openGL plugin
License:        MIT
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n libssr-glinject
This package provides nice openGL apps screencasting support
for Simple Screen Recorder. At 64bit system you may also
install libssr-glinject-32bit for 32bit openGL apps support.
%endif

%prep
%setup -q -n ssr-%{version}

%build
%ifarch %{ix86} x86_64
# /usr/include/qt5/QtCore/qglobal.h:1067:4: error: error "You must build
# your code with position independent code if Qt was built with
# -reduce-relocations. " "Compile your code with -fPIC (-fPIE is not
# enough)." error "You must build your code with position independent code
# if Qt was built with -reduce-relocations."
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%cmake -DWITH_QT5=True
%else
%cmake \
       -DWITH_QT5=True \
       -DWITH_GLINJECT=False
%endif
make V=1 %{?_smp_mflags}

%install
%cmake_install
%fdupes -s %{buildroot}%{_datadir}/icons/hicolor
%suse_update_desktop_file %{name}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc *.txt *.md data/resources/about.htm
%license COPYING
%{_bindir}/%{name}
%{_bindir}/ssr-glinject
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/%{name}
%{_mandir}/*/%{name}*
%{_mandir}/*/ssr-glinject*

%ifarch %{ix86} x86_64
%files -n libssr-glinject
%defattr(-,root,root)
%{_libdir}/libssr-glinject.so
%endif

%changelog
