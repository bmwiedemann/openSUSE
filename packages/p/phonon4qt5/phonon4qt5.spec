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
%bcond_without lang
Name:           phonon4qt5
Version:        4.11.0
Release:        0
Summary:        Multimedia Platform Abstraction
License:        LGPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://phonon.kde.org/
Source:         https://download.kde.org/stable/%{rname}/%{version}/%{rname}-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM
Patch0:         0001-Remove-phonon-from-the-include-directory.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= 5.60.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libpulse-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  pkgconfig(glib-2.0)

%description
Phonon is a cross-platform portable multimedia support abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%package devel
Summary:        Phonon Multimedia Platform Abstraction
Group:          Development/Libraries/KDE
Requires:       extra-cmake-modules >= 5.60.0
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
Recommends:     phononsettings

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

%package -n phononsettings
Summary:        Settings Tool for Phonon Multimedia Platform Abstraction
Group:          System/Libraries
License:        LGPL-2.0-only OR LGPL-3.0-only
Recommends:     phononsettings-lang

%description -n phononsettings
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

%lang_package -n phononsettings

%prep
%setup -q -n %{rname}-%{version}
%patch0 -p1

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes -s %{buildroot}%{_includedir}/%{name}

%if %{with lang}
  %find_lang libphonon %{name}.lang --with-qt
  %find_lang phononsettings phononsettings.lang --with-qt
%endif

%post   -n libphonon4qt5 -p /sbin/ldconfig
%postun -n libphonon4qt5 -p /sbin/ldconfig

%files -n libphonon4qt5
%license COPYING.LIB
%{_kf5_libdir}/lib%{name}.so.*
%{_kf5_libdir}/lib%{name}experimental.so.*

%files devel
%license COPYING.LIB
%{_includedir}/%{name}
%{_kf5_cmakedir}/%{name}
%{_kf5_sharedir}/%{name}
%{_kf5_libdir}/pkgconfig/%{name}.pc
%{_kf5_libdir}/lib%{name}experimental.so
%{_kf5_libdir}/lib%{name}.so
%{_kf5_mkspecsdir}/qt_phonon4qt5.pri
%dir %{_libqt5_plugindir}/designer/
%{_libqt5_plugindir}/designer/phononwidgets.so

%if %{with lang}
%files lang -f %{name}.lang
%endif

%files -n phononsettings
%{_kf5_bindir}/phononsettings

%if %{with lang}
%files -n phononsettings-lang -f phononsettings.lang
%endif

%changelog
