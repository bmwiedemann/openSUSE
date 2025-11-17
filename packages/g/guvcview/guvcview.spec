#
# spec file for package guvcview
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2012 Malcolm J Lewis <malcolmlewis@opensuse.org>
# Copyright (c) 2013 Marguerite Su <marguerite@opensuse.org>
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


%define         sover 2_2-2
Name:           guvcview
Version:        2.2.2
Release:        0
Summary:        GTK+ UVC Viewer and Capturer
# Reference to GPL-2.0 in some files?
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://guvcview.sourceforge.net/
#Git-Clone:     git://git.code.sf.net/p/guvcview/git-master
Source0:        https://sourceforge.net/projects/guvcview/files/source/guvcview-src-%{version}.tar.bz2
Source1:        guvcview-qt.desktop
Patch5:         fix-linking.patch
Patch6:         fix-pkgconfig-path.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sdl2)
Recommends:     %{name}-lang

%description
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package     -n libgviewaudio-%{sover}
Summary:        GTK+ UVC Viewer and Capturer
Group:          System/Libraries

%description -n libgviewaudio-%{sover}
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package     -n libgviewencoder-%{sover}
Summary:        GTK+ UVC Viewer and Capturer
Group:          System/Libraries

%description -n libgviewencoder-%{sover}
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package     -n libgviewrender-%{sover}
Summary:        GTK+ UVC Viewer and Capturer
Group:          System/Libraries

%description -n libgviewrender-%{sover}
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package     -n libgviewv4l2core-%{sover}
Summary:        GTK+ UVC Viewer and Capturer
Group:          System/Libraries
Recommends:     libgviewv4l2core-lang

%description -n libgviewv4l2core-%{sover}
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package        devel
Summary:        Development files for guvcview
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libgviewaudio-%{sover} = %{version}-%{release}
Requires:       libgviewencoder-%{sover} = %{version}-%{release}
Requires:       libgviewrender-%{sover} = %{version}-%{release}
Requires:       libgviewv4l2core-%{sover} = %{version}-%{release}
Requires:       libpng-devel
Requires:       pkgconfig(alsa)
Requires:       pkgconfig(gsl)
Requires:       pkgconfig(libavcodec)
Requires:       pkgconfig(libavutil)
Requires:       pkgconfig(libpulse)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(libusb-1.0)
Requires:       pkgconfig(libv4l2)
Requires:       pkgconfig(portaudio-2.0)
Requires:       pkgconfig(sdl2)

%description devel
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

This subpackage contains the header files for developing
applications that want to make use of the GUVC libraries.

%lang_package

%package     -n libgviewv4l2core-lang
Summary:        Languages for libgviewv4l2core
Group:          System/Localization
Requires:       libgviewv4l2core-%{sover} = %{version}
Provides:       libgviewv4l2core-lang-all = %{version}
Supplements:    (bundle-lang-other and libgviewv4l2core-%{sover})
BuildArch:      noarch

%description -n libgviewv4l2core-lang
Provides translations to libgviewv4l2core.

%prep
%autosetup -p1 -n %{name}-src-%{version}

%build
%cmake \
  -DUSE_GTK3=ON \
  -DUSE_QT6=ON \
  -DUSE_SDL2=ON \
  -DINSTALL_DEVKIT=ON
%make_jobs

%install
%cmake_install

# wrapper for guvcview-qt6
echo -e "#!/bin/sh\nexec %{_bindir}/guvcview --gui=qt6 \"\$@\"" > %{buildroot}%{_bindir}/guvcview-qt6
chmod 755 %{buildroot}%{_bindir}/guvcview-qt6

install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}-qt6.desktop

%find_lang %{name} %{?no_lang_C}
%find_lang gview_v4l2core libgviewv4l2core.lang %{?no_lang_C}

%ldconfig_scriptlets -n libgviewaudio-%{sover}
%ldconfig_scriptlets -n libgviewencoder-%{sover}
%ldconfig_scriptlets -n libgviewrender-%{sover}
%ldconfig_scriptlets -n libgviewv4l2core-%{sover}

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-qt6
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-qt6.desktop
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n libgviewaudio-%{sover}
%{_libdir}/libgviewaudio.so.*

%files -n libgviewencoder-%{sover}
%{_libdir}/libgviewencoder.so.*

%files -n libgviewrender-%{sover}
%{_libdir}/libgviewrender.so.*

%files -n libgviewv4l2core-%{sover}
%{_libdir}/libgviewv4l2core.so.*

%files devel
%{_includedir}/gviewaudio.h
%{_includedir}/gviewencoder.h
%{_includedir}/gviewrender.h
%{_includedir}/gviewv4l2core.h
%{_libdir}/libgviewaudio.so
%{_libdir}/libgviewencoder.so
%{_libdir}/libgviewrender.so
%{_libdir}/libgviewv4l2core.so
%{_libdir}/pkgconfig/libgviewaudio.pc
%{_libdir}/pkgconfig/libgviewencoder.pc
%{_libdir}/pkgconfig/libgviewrender.pc
%{_libdir}/pkgconfig/libgviewv4l2core.pc

%files -n libgviewv4l2core-lang -f libgviewv4l2core.lang

%files lang -f %{name}.lang

%changelog
