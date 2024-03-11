#
# spec file for package phonon
#
# Copyright (c) 2023 SUSE LLC
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


%define phonon_flavor @BUILD_FLAVOR@%{nil}
%if "%{phonon_flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%if "%{phonon_flavor}" == "qt5"
%define qt5 1
%define pkg_suffix -qt5
%define qt5_version 5.15.0
%endif
%if "%{phonon_flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
%global kf6_version 5.240.0
%define qt6_version 6.5.0
%endif
%define rname phonon
%bcond_without released
Name:           phonon%{?pkg_suffix}
Version:        4.12.0
Release:        0
Summary:        Multimedia Platform Abstraction
License:        LGPL-2.0-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/%{rname}/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{rname}/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        phonon.keyring
%endif
Source99:       phonon-rpmlintrc
%if 0%{?qt5}
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Designer) >= %{qt5_version}
BuildRequires:  cmake(Qt5Gui) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
# the gstreamer backend is deprecated upstream
Requires:       phonon-vlc-qt5
%endif
%if 0%{?qt6}
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
# The designer plugin isn't built with Qt6
# BuildRequires:  cmake(Qt6Designer) >= %%{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
# the gstreamer backend is deprecated upstream
Requires:       phonon-vlc-qt6
%endif
BuildRequires:  fdupes
BuildRequires:  libpulse-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)

%description
Phonon is a cross-platform portable multimedia support abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package devel
Summary:        Phonon Multimedia Platform Abstraction
Requires:       libphonon4%{phonon_flavor} = %{version}
%if 0%{?qt5}
Requires:       cmake(Qt5Core) >= %{qt5_version}
Requires:       cmake(Qt5Widgets) >= %{qt5_version}
Provides:       phonon4qt5-devel = %{version}
Obsoletes:      phonon4qt5-devel < %{version}
%endif
%if 0%{?qt6}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Widgets) >= %{qt6_version}
%endif

%description devel
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package -n libphonon4%{phonon_flavor}
Summary:        Phonon Multimedia Platform Abstraction
Recommends:     phonon4qt5-lang
Recommends:     phonon-backend%{pkg_suffix}
Recommends:     phononsettings%{pkg_suffix}
%if 0%{?qt5}
# Was present in phonon4qt5.spec
Provides:       phonon4qt5 = %{version}
%endif

%description -n libphonon4%{phonon_flavor}
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package -n phononsettings%{pkg_suffix}
Summary:        Settings Tool for Phonon Multimedia Platform Abstraction
License:        LGPL-2.0-only OR LGPL-3.0-only
%if 0%{?qt5}
Provides:       phononsettings = %{version}
Obsoletes:      phononsettings < %{version}
Obsoletes:      phononsettings-lang < %{version}
%endif
%if 0%{?qt6}
# conflicting executable name
Conflicts:      phononsettings
Conflicts:      phononsettings-qt5
%endif

%description -n phononsettings%{pkg_suffix}
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

# It's libphonon_qt.qm for both. To avoid conflicts, use the Qt 5 translations
# for both.
%lang_package -n phonon4qt5

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%if 0%{?qt5}
%cmake_kf5 -d build -- -DPHONON_BUILD_QT5:BOOL=TRUE -DPHONON_BUILD_QT6:BOOL=FALSE
%cmake_build
%endif

%if 0%{?qt6}
%cmake_kf6 -DPHONON_BUILD_QT5:BOOL=FALSE -DPHONON_BUILD_QT6:BOOL=TRUE
%kf6_build
%endif

%install
%if 0%{?qt5}
%kf5_makeinstall -C build
%find_lang libphonon %{name}.lang --with-qt
%endif

%if 0%{?qt6}
%kf6_install
rm -r %{buildroot}/%{_datadir}/locale/*/*/libphonon_qt.qm
%endif

%fdupes %{buildroot}

%find_lang phononsettings phononsettings.lang --with-qt

%ldconfig_scriptlets -n libphonon4%{phonon_flavor}

%files -n libphonon4%{phonon_flavor}
%license COPYING.LIB
%{_libdir}/libphonon4%{phonon_flavor}.so.*
%{_libdir}/libphonon4%{phonon_flavor}experimental.so.*

%files devel
%{_includedir}/phonon4%{phonon_flavor}/
%{_libdir}/cmake/phonon4%{phonon_flavor}/
%{_libdir}/libphonon4%{phonon_flavor}.so
%{_libdir}/libphonon4%{phonon_flavor}experimental.so
%{_libdir}/pkgconfig/phonon4%{phonon_flavor}.pc
%if 0%{?qt5}
%{_libdir}/%{phonon_flavor}/mkspecs/modules/qt_phonon4qt5.pri
%dir %{_libdir}/%{phonon_flavor}/plugins/designer/
%{_libdir}/%{phonon_flavor}/plugins/designer/phonon4qt5widgets.so
%endif

%files -n phononsettings%{pkg_suffix} -f phononsettings.lang
%{_bindir}/phononsettings

%if 0%{?qt5}
%files -n phonon4qt5-lang -f %{name}.lang
%endif

%changelog
