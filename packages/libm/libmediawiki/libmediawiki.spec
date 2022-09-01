#
# spec file for package libmediawiki
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_without released
Name:           libmediawiki
Version:        5.38.0
Release:        0
Summary:        Interface for MediaWiki based web services
License:        GPL-2.0-or-later
Group:          Development/Libraries/KDE
URL:            https://invent.kde.org/libraries/libmediawiki
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.85.0
BuildRequires:  cmake(KF5CoreAddons) >= 5.85.0
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Network) >= 5.15.0
BuildRequires:  cmake(Qt5Test) >= 5.15.0

%description
libmediawiki is a KDE C++ interface for MediaWiki based web services as
wikipedia.org.

This package contains the shared library.

%package -n libKF5MediaWiki5
Summary:        Interface for MediaWiki based web services
Group:          System/Libraries

%description -n libKF5MediaWiki5
libmediawiki is a KDE C++ interface for MediaWiki based web services as
wikipedia.org.

This package contains the shared library.

%package devel
Summary:        Development files for libmediawiki
Group:          Development/Libraries/KDE
Requires:       libKF5MediaWiki5 = %{version}
Requires:       cmake(Qt5Core) >= 5.15.0
Requires:       cmake(Qt5Network) >= 5.15.0
Requires:       cmake(KF5CoreAddons) >= 5.85.0

%description devel
libmediawiki is a KDE C++ interface for MediaWiki based web services as
wikipedia.org.

This package contains the development files for libmediawiki.

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%post -n libKF5MediaWiki5 -p /sbin/ldconfig
%postun -n libKF5MediaWiki5 -p /sbin/ldconfig

%files -n libKF5MediaWiki5
%license COPYING COPYING.LIB
%doc AUTHORS README.md
%{_kf5_libdir}/libKF5MediaWiki.so.*

%files devel
%license COPYING COPYING.LIB
%doc AUTHORS COPYING-CMAKE-SCRIPTS README.md
%{_kf5_cmakedir}/KF5MediaWiki/
%{_kf5_includedir}/MediaWiki/
%{_kf5_includedir}/mediawiki_version.h
%{_kf5_libdir}/libKF5MediaWiki.so
%{_kf5_mkspecsdir}/qt_MediaWiki.pri

%changelog
