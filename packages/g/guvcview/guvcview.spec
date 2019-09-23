#
# spec file for package guvcview
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         sover 2_0-2

Name:           guvcview
Version:        2.0.6
Release:        0
# Reference to GPL-2.0 in some files?
Summary:        GTK+ UVC Viewer and Capturer
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Video/Players
Url:            http://guvcview.sourceforge.net/
Source0:        https://sourceforge.net/projects/guvcview/files/source/guvcview-src-%{version}.tar.gz
Source90:       pre_checkin.sh
# PATCH-FIX-OPENSUSE guvcview-SUSE.patch -- use SUSE-specific paths
Patch0:         guvcview-SUSE.patch
BuildRequires:  alsa-devel
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gsl-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libpng-devel
BuildRequires:  libpulse-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libusb-1_0-devel
BuildRequires:  libv4l-devel
BuildRequires:  pkg-config
BuildRequires:  portaudio-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(sdl2)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Requires:       alsa-devel
Requires:       glibc-devel
Requires:       gsl-devel
Requires:       libSDL2-devel
Requires:       libgviewaudio-%{sover} = %{version}-%{release}
Requires:       libgviewencoder-%{sover} = %{version}-%{release}
Requires:       libgviewrender-%{sover} = %{version}-%{release}
Requires:       libgviewv4l2core-%{sover} = %{version}-%{release}
Requires:       libpng-devel
Requires:       libpulse-devel
Requires:       libudev-devel
Requires:       libusb-1_0-devel
Requires:       libv4l-devel
Requires:       portaudio-devel
Requires:       pkgconfig(libavcodec)
Requires:       pkgconfig(libavutil)

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
Supplements:    packageand(bundle-lang-other:libgviewv4l2core-%{sover})
BuildArch:      noarch

%description -n libgviewv4l2core-lang
Provides translations to libgviewv4l2core.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1

%build
autoreconf -fiv
%configure --disable-debian-menu \
           --disable-desktop
make %{?_smp_mflags}

%install
%make_install
# Create desktop file as disabled during build
%suse_update_desktop_file -c %{name} "A video viewer and capturer for the linux uvc driver" %{name} %{name} %{name} AudioVideo AudioVideoEditing
%find_lang %{name} %{?no_lang_C}
%find_lang gview_v4l2core libgviewv4l2core.lang %{?no_lang_C}
%fdupes %{buildroot}

rm -f %{buildroot}%{_libdir}/*.{la,a}

%post -n libgviewaudio-%{sover} -p /sbin/ldconfig
%postun -n libgviewaudio-%{sover} -p /sbin/ldconfig

%post -n libgviewencoder-%{sover} -p /sbin/ldconfig
%postun -n libgviewencoder-%{sover} -p /sbin/ldconfig

%post -n libgviewrender-%{sover} -p /sbin/ldconfig
%postun -n libgviewrender-%{sover} -p /sbin/ldconfig

%post -n libgviewv4l2core-%{sover} -p /sbin/ldconfig
%postun -n libgviewv4l2core-%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%dir %{_datadir}/pixmaps/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/pixmaps/%{name}/*.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/*.gz

%files -n libgviewaudio-%{sover}
%defattr(-,root,root)
%{_libdir}/libgviewaudio-*.so.*

%files -n libgviewencoder-%{sover}
%defattr(-,root,root)
%{_libdir}/libgviewencoder-*.so.*

%files -n libgviewrender-%{sover}
%defattr(-,root,root)
%{_libdir}/libgviewrender-*.so.*

%files -n libgviewv4l2core-%{sover}
%defattr(-,root,root)
%{_libdir}/libgviewv4l2core-*.so.*

%files devel
%defattr(-,root,root)
%dir %{_includedir}/guvcview-2
%dir %{_includedir}/guvcview-2/libgviewaudio
%dir %{_includedir}/guvcview-2/libgviewencoder
%dir %{_includedir}/guvcview-2/libgviewrender
%dir %{_includedir}/guvcview-2/libgviewv4l2core
%{_includedir}/guvcview-2/libgviewaudio/gviewaudio.h
%{_includedir}/guvcview-2/libgviewencoder/gviewencoder.h
%{_includedir}/guvcview-2/libgviewrender/gviewrender.h
%{_includedir}/guvcview-2/libgviewv4l2core/gview.h
%{_includedir}/guvcview-2/libgviewv4l2core/gviewv4l2core.h
%{_libdir}/libgviewaudio.so
%{_libdir}/libgviewencoder.so
%{_libdir}/libgviewrender.so
%{_libdir}/libgviewv4l2core.so
%{_libdir}/pkgconfig/libgviewaudio.pc
%{_libdir}/pkgconfig/libgviewencoder.pc
%{_libdir}/pkgconfig/libgviewrender.pc
%{_libdir}/pkgconfig/libgviewv4l2core.pc

%files lang -f %{name}.lang

%files -n libgviewv4l2core-lang -f libgviewv4l2core.lang

%changelog
