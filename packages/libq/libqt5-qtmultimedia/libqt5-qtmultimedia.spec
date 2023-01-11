#
# spec file for package libqt5-qtmultimedia
#
# Copyright (c) 2021 SUSE LLC
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


# Internal QML imports of examples, internal library used by an example
%global __requires_exclude qmlimport\\((FrequencyMonitor|qmlvideofilter).*|libfftreal.so
%global __provides_exclude libfftreal.so

%define qt5_snapshot 1
%define libname libQt5Multimedia5
%ifarch %{arm} aarch64
%define gles 1
%else
%define gles 0
%endif
%define base_name libqt5
%define real_version 5.15.8
%define so_version 5.15.8
%define tar_version qtmultimedia-everywhere-src-%{version}
Name:           libqt5-qtmultimedia
Version:        5.15.8+kde1
Release:        0
Summary:        Qt 5 Multimedia Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
URL:            https://www.qt.io
Source:         %{tar_version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  alsa-devel
BuildRequires:  fdupes
BuildRequires:  libQt5Gui-private-headers-devel >= %{real_version}
BuildRequires:  libQt5Widgets-private-headers-devel >= %{real_version}
BuildRequires:  libpulse-devel
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libwmf-devel
%if %{qt5_snapshot}
#to create the forwarding headers
BuildRequires:  perl
%endif
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Qml) >= %{real_version}
BuildRequires:  pkgconfig(Qt5Quick) >= %{real_version}
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(openal)

%description
Qt Multimedia is a module that provides a set of QML types and C++
classes to handle multimedia content. It also provides APIs to access
the camera and radio functionality. The included Qt Audio Engine
provides types for 3D positional audio playback and content
management.

%prep
%autosetup -p1 -n %{tar_version}

%package -n %{libname}
Summary:        Qt 5 Multimedia Library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11

%description -n %{libname}
Qt Multimedia is a module that provides a set of QML types and C++
classes to handle multimedia content. It also provides APIs to access
the camera and radio functionality. The included Qt Audio Engine
provides types for 3D positional audio playback and content
management.

%package devel
Summary:        Development files for the Qt5 Multimedia library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/X11
Requires:       %{libname} = %{version}
# The mkspec adds -lpulse-mainloop-glib -lpulse -lglib-2.0
Requires:       libpulse-devel
Requires:       libqt5-qtdeclarative-devel >= %{real_version}
Provides:       libQt5Multimedia-devel = %{version}
Obsoletes:      libQt5Multimedia-devel < %{version}

%description devel
You need this package if you want to compile programs with qtmultimedia.

%package private-headers-devel
Summary:        Non-ABI stable experimental API for the Qt5 Multimedia library
License:        LGPL-3.0-only OR (GPL-2.0-only OR GPL-3.0-or-later)
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}
Requires:       libQt5Gui-private-headers-devel >= %{real_version}
Requires:       libQt5Widgets-private-headers-devel >= %{real_version}
Provides:       libQt5Multimedia-private-headers-devel = %{version}
Obsoletes:      libQt5Multimedia-private-headers-devel < %{version}
BuildArch:      noarch

%description private-headers-devel
This package provides private headers of libqt5-qtmultimedia that are normally
not used by application development and that do not have any ABI or
API guarantees. The packages that build against these have to require
the exact Qt version.

%package examples
Summary:        Qt5 multimedia examples
License:        BSD-3-Clause
Group:          Development/Libraries/X11
Recommends:     %{name}-devel

%description examples
Examples for the libqt5-qtmultimedia module.

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%build
%if %{qt5_snapshot}
#force the configure script to generate the forwarding headers (it checks whether .git directory exists)
mkdir .git
%endif
%qmake5 GST_VERSION=1.0
%make_jobs

%install
%qmake5_install
find %{buildroot}/%{_libdir} -type f -name '*la' -print -exec perl -pi -e 's, -L%{_builddir}/\S+,,g' {} +
find %{buildroot}/%{_libdir} -type f -name '*pc' -print -exec perl -pi -e "s, -L$RPM_BUILD_DIR/?\S+,,g" {} + -exec sed -i -e "s,^moc_location=.*,moc_location=%{_lib}qt5_bindir/moc," -e "s,uic_location=.*,uic_location=%{_lib}qt5_bindir/uic," {} +
# kill .la files
rm -f %{buildroot}%{_libqt5_libdir}/lib*.la

%fdupes -s %{buildroot}/%{_libqt5_includedir}

%files -n %{libname}
%license LICENSE.*
%{_libqt5_libdir}/libQt5*.so.*
%{_libqt5_plugindir}/mediaservice
%{_libqt5_plugindir}/playlistformats
%{_libqt5_plugindir}/audio
%if %{gles}
%{_libqt5_plugindir}/video
%endif
%{_libqt5_archdatadir}/qml/Qt*

%files private-headers-devel
%license LICENSE.*
%{_libqt5_includedir}/Qt*/%{so_version}

%files devel
%license LICENSE.*
%exclude %{_libqt5_includedir}/Qt*/%{so_version}
%{_libqt5_includedir}/Qt*
%{_libqt5_libdir}/cmake/Qt5*
%{_libqt5_libdir}/libQt5*.prl
%{_libqt5_libdir}/libQt5*.so
%{_libqt5_libdir}/pkgconfig/Qt5*.pc
%{_libqt5_archdatadir}/mkspecs/modules/qt_lib_*.pri

%files examples
%license LICENSE.*
%{_libqt5_examplesdir}/

%changelog
