#
# spec file for package libmediawiki
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libmediawiki
Version:        5.37.0
Release:        0
Summary:        Interface for MediaWiki based web services
License:        GPL-2.0+
Group:          Development/Libraries/KDE
Url:            https://cgit.kde.org/libmediawiki.git
Source0:        http://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kcoreaddons-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%description devel
libmediawiki is a KDE C++ interface for MediaWiki based web services as
wikipedia.org.

This package contains the development files for libmediawiki.

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%post -n libKF5MediaWiki5 -p /sbin/ldconfig

%postun -n libKF5MediaWiki5 -p /sbin/ldconfig

%files -n libKF5MediaWiki5
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.LIB README.md
%{_kf5_libdir}/libKF5MediaWiki.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING-CMAKE-SCRIPTS COPYING.LIB README.md
%{_kf5_includedir}/MediaWiki/
%{_kf5_includedir}/mediawiki_version.h
%{_kf5_libdir}/libKF5MediaWiki.so
%{_kf5_cmakedir}/KF5MediaWiki/
%{_kf5_mkspecsdir}/qt_MediaWiki.pri

%changelog
