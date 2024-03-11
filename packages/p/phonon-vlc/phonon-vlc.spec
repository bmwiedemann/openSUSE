#
# spec file for package phonon-vlc
#
# Copyright (c) 2024 SUSE LLC
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
%define rname phonon-backend-vlc
%bcond_without released
Name:           phonon-vlc%{?pkg_suffix}
Version:        0.12.0
Release:        0
Summary:        Phonon VLC Backend
License:        LGPL-2.1-or-later
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/phonon/%{rname}/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/phonon/%{rname}/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        phonon-vlc.keyring
%endif
BuildRequires:  vlc-devel >= 3.0.0
%if 0%{?qt5}
BuildRequires:  extra-cmake-modules >= %{qt5_version}
# Temporarily use the package name to avoid unresolvable build
# BuildRequires:  cmake(Phonon4Qt5) >= 4.11.60
BuildRequires:  phonon-qt5-devel >= 4.11.60
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}
Provides:       phonon4qt5-backend = %{version}
Provides:       phonon4qt5-backend-vlc = %{version}
Obsoletes:      phonon4qt5-backend-vlc < %{version}
%endif
%if 0%{?qt6}
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(Phonon4Qt6) >= 4.10.60
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Provides:       phonon-qt6-backend = %{version}
# AFAIK locale(pkg:xx) might not work with provides, do it explicitly
Recommends:     phonon-vlc-qt5-lang
%endif
# The plugins are split between non-X11 (vlc-noX) and the others, the vlc backend needs both (boo#1219416)
%requires_eq    vlc
%requires_eq    vlc-noX

%description
Phonon is a cross-platform portable Multimedia Support Abstraction,
which allows you to play multiple audio or video formats with the same
quality on all platforms, no matter which underlying architecture is
used.

This is the VLC backend for Phonon

# It's phonon_vlc_qt.qm for both. To avoid conflicts, use the Qt 5 translations
# for both.
%package -n phonon-vlc-lang
Summary:        Translations for package %{name} 
Requires:       (phonon-vlc-qt5 or phonon-vlc-qt6)
Provides:       phonon4qt5-backend-vlc-lang = %{version}
Obsoletes:      phonon4qt5-backend-vlc-lang < %{version}
Provides:       %{name}-lang-all = %{version} 
BuildArch:      noarch

%description -n phonon-vlc-lang
Provides translations for the "%{name}" packages.

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
%find_lang phonon_vlc %{name}.lang --with-qt
%endif

%if 0%{?qt6}
%kf6_install
rm -r %{buildroot}/%{_datadir}/locale/*/*/phonon_vlc_qt.qm
%endif

%post
%{_libdir}/vlc/vlc-cache-gen %{_libdir}/vlc/plugins

%files
%license COPYING.LIB
%doc AUTHORS
%if 0%{?qt5}
%dir %{_kf5_plugindir}/phonon4qt5_backend
%{_kf5_plugindir}/phonon4qt5_backend/phonon_vlc_qt5.so
%endif
%if 0%{?qt6}
%dir %{_kf6_plugindir}/phonon4qt6_backend
%{_kf6_plugindir}/phonon4qt6_backend/phonon_vlc_qt6.so
%endif

%if 0%{?qt5}
%files -n phonon-vlc-lang -f %{name}.lang
%endif

%changelog
