#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%define         sover0 2_0-2
%define         sover1 2_1-2
%global flavor @BUILD_FLAVOR@%{nil}

%define pname guvcview

%if "%{flavor}" == "qt5"
%bcond_without qt5
%define psuffix -qt5
%else
%bcond_with qt5
%endif

Name:           guvcview%{?psuffix}
Version:        2.0.8
Release:        0
# Reference to GPL-2.0 in some files?
Summary:        GTK+ UVC Viewer and Capturer
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Video/Players
URL:            http://guvcview.sourceforge.net/
Source0:        https://sourceforge.net/projects/guvcview/files/source/guvcview-src-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE guvcview-SUSE.patch -- use SUSE-specific paths
Patch0:         guvcview-SUSE.patch
# PATCH-FIX-OPENSUSE guvcview-qt5-nolibs_qt5names.patch -- use libraries from the GTK+ package
Patch1:         guvcview-qt5-nolibs_qt5names.patch
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
BuildRequires:  libusb-1_0-devel
BuildRequires:  libv4l-devel
BuildRequires:  pkg-config
BuildRequires:  portaudio-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sdl2)
%if %{with qt5}
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libgviewaudio)
BuildRequires:  pkgconfig(libgviewencoder)
BuildRequires:  pkgconfig(libgviewrender)
BuildRequires:  pkgconfig(libgviewv4l2core)
%endif
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package     -n libgviewaudio-%{sover0}
Summary:        GTK+ UVC Viewer and Capturer
Group:          System/Libraries

%description -n libgviewaudio-%{sover0}
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package     -n libgviewencoder-%{sover1}
Summary:        GTK+ UVC Viewer and Capturer
Group:          System/Libraries

%description -n libgviewencoder-%{sover1}
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package     -n libgviewrender-%{sover1}
Summary:        GTK+ UVC Viewer and Capturer
Group:          System/Libraries

%description -n libgviewrender-%{sover1}
A GTK interface for capturing and viewing video from devices
supported by the Linux UVC driver, although it should also work with
any v4l2 compatible device.

%package     -n libgviewv4l2core-%{sover1}
Summary:        GTK+ UVC Viewer and Capturer
Group:          System/Libraries
Recommends:     libgviewv4l2core-lang

%description -n libgviewv4l2core-%{sover1}
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
Requires:       libgviewaudio-%{sover0} = %{version}-%{release}
Requires:       libgviewencoder-%{sover1} = %{version}-%{release}
Requires:       libgviewrender-%{sover1} = %{version}-%{release}
Requires:       libgviewv4l2core-%{sover1} = %{version}-%{release}
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
Requires:       libgviewv4l2core-%{sover1} = %{version}
Provides:       libgviewv4l2core-lang-all = %{version}
Supplements:    (bundle-lang-other and libgviewv4l2core-%{sover1})
BuildArch:      noarch

%description -n libgviewv4l2core-lang
Provides translations to libgviewv4l2core.

%prep
%setup -q -n %{pname}-src-%{version}
%patch0 -p1
%if %{with qt5}
%patch1 -p1
%endif

%build
autoreconf -fiv
%configure --disable-debian-menu \
           --disable-desktop \
%if %{with qt5}
           --disable-gtk3 \
           --enable-qt5 \
           --program-suffix=-qt5 \
%endif
%{nil}
%make_build

%install
%make_install
# Create desktop file as disabled during build
%suse_update_desktop_file -c %{name} "A video viewer and capturer for the linux uvc driver" %{name} %{name} %{name} AudioVideo AudioVideoEditing
%find_lang %{name} %{?no_lang_C}

%if %{with qt5}
mv %{buildroot}%{_datadir}/pixmaps/%{pname}.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
%else
%find_lang gview_v4l2core libgviewv4l2core.lang %{?no_lang_C}
%endif

%fdupes %{buildroot}

rm -f %{buildroot}%{_libdir}/*.{la,a}

%if ! %{with qt5}
%post -n libgviewaudio-%{sover0} -p /sbin/ldconfig
%postun -n libgviewaudio-%{sover0} -p /sbin/ldconfig

%post -n libgviewencoder-%{sover1} -p /sbin/ldconfig
%postun -n libgviewencoder-%{sover1} -p /sbin/ldconfig

%post -n libgviewrender-%{sover1} -p /sbin/ldconfig
%postun -n libgviewrender-%{sover1} -p /sbin/ldconfig

%post -n libgviewv4l2core-%{sover1} -p /sbin/ldconfig
%postun -n libgviewv4l2core-%{sover1} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.1%{ext_man}

%if ! %{with qt5}
%files -n libgviewaudio-%{sover0}
%defattr(-,root,root)
%{_libdir}/libgviewaudio-*.so.*

%files -n libgviewencoder-%{sover1}
%defattr(-,root,root)
%{_libdir}/libgviewencoder-*.so.*

%files -n libgviewrender-%{sover1}
%defattr(-,root,root)
%{_libdir}/libgviewrender-*.so.*

%files -n libgviewv4l2core-%{sover1}
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

%files -n libgviewv4l2core-lang -f libgviewv4l2core.lang
%endif

%files lang -f %{name}.lang

%changelog
