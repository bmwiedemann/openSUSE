#
# spec file for package phonon4qt5
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


%define rname phonon
Name:           phonon4qt5
Version:        4.10.3
Release:        0
Summary:        Multimedia Platform Abstraction
License:        LGPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://phonon.kde.org/
Source:         https://download.kde.org/stable/%{rname}/%{version}/%{rname}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= 1.7.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libpulse-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Designer)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)

%description
Phonon is a cross-platform portable multimedia support abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package devel
Summary:        Phonon Multimedia Platform Abstraction
Group:          Development/Libraries/KDE
Requires:       extra-cmake-modules >= 1.7.0
Requires:       libphonon4qt5 = %{version}

%description devel
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package -n libphonon4qt5
Summary:        Phonon Multimedia Platform Abstraction
Group:          System/Libraries
Recommends:     %{name}-lang
Recommends:     phonon4qt5-backend

%description -n libphonon4qt5
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package lang
Summary:        Translations for package libphonon4qt5
Group:          System/Localization
Requires:       libphonon4qt5 = %{version}
Provides:       %{name}-lang-all = %{version}
BuildArch:      noarch

%description lang
Provides translations for the libphonon4qt5 package.

%prep
%setup -q -n %{rname}-%{version}

%build
  %cmake_kf5 -d build -- -DPHONON_BUILD_PHONON4QT5=ON -DPHONON_INSTALL_QT_EXTENSIONS_INTO_SYSTEM_QT=true -DDBUS_INTERFACES_INSTALL_DIR=%{_kf5_sharedir}/dbus-1/interfaces/
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes -s %{buildroot}%{_includedir}/%{name}

  %find_lang libphonon %{name}.lang --with-qt

%post   -n libphonon4qt5 -p /sbin/ldconfig
%postun -n libphonon4qt5 -p /sbin/ldconfig

%files -n libphonon4qt5
%license COPYING.LIB
%{_kf5_libdir}/lib%{name}.so.*
%{_kf5_libdir}/lib%{name}experimental.so.*

%files devel
%license COPYING.LIB
%{_includedir}/%{name}
%{_kf5_libdir}/cmake/%{name}
%{_kf5_sharedir}/%{name}
%{_kf5_libdir}/pkgconfig/%{name}.pc
%{_kf5_libdir}/lib%{name}experimental.so
%{_kf5_libdir}/lib%{name}.so
%{_libqt5_archdatadir}/mkspecs/modules/qt_phonon4qt5.pri
%{_libqt5_plugindir}/designer/phononwidgets.so
%{_kf5_sharedir}/dbus-1/interfaces/org.kde.Phonon4Qt5.AudioOutput.xml

%files lang -f %{name}.lang

%changelog
