#
# spec file for package kitinerary
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without lang
Name:           kitinerary
Version:        20.08.2
Release:        0
Summary:        Data model and extraction system for travel reservations
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  libopenssl-devel
BuildRequires:  libpoppler-qt5-devel
BuildRequires:  libxml2-devel
BuildRequires:  zlib-devel
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Mime)
BuildRequires:  cmake(KPimPkPass)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Test)
Requires:       libKPimItinerary5 = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
%if 0%{?suse_version} > 1500
BuildRequires:  libphonenumber-devel
BuildRequires:  cmake(ZXing)
%endif

%description
Kitinerary is a library which provides a data model and a system to extract information
from travel reservations. The model can then be reused in other applications.

%package -n libKPimItinerary5
Summary:        Data model and extraction system for travel reservations
Group:          System/Libraries
Recommends:     %{name}
Recommends:     libKPimItinerary5-lang

%description -n libKPimItinerary5
Kitinerary is a library which provides a data model and a system to extract information
from travel reservations. The model can then be reused in other applications.
This package contains the library itself.

%package devel
Summary:        Development files for kitinerary
Group:          Development/Libraries/KDE
Requires:       libKPimItinerary5 = %{version}
Requires:       cmake(KF5CalendarCore)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5Mime)
Requires:       cmake(KPimPkPass)
Requires:       cmake(Qt5Gui)

%description devel
This package contains all necessary include files and libraries needed
to build programs that use the kitinerary library.

%lang_package -n libKPimItinerary5

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --with-qt --all-name
  %endif

%post -n libKPimItinerary5 -p /sbin/ldconfig
%postun -n libKPimItinerary5 -p /sbin/ldconfig

%files
%license LICENSES/*
%{_kf5_libexecdir}/kitinerary-extractor
%dir %{_kf5_sharedir}/mime
%dir %{_kf5_sharedir}/mime/packages
%{_kf5_sharedir}/mime/packages/application-vnd-kde-itinerary.xml

%files -n libKPimItinerary5
%license LICENSES/*
%{_kf5_libdir}/libKPimItinerary.so.*
%{_kf5_debugdir}/*.categories

%files devel
%license LICENSES/*
%dir %{_includedir}/KPim/
%{_includedir}/KPim/KItinerary/
%{_includedir}/KPim/kitinerary/
%{_includedir}/KPim/kitinerary_version.h
%{_kf5_cmakedir}/KPimItinerary/
%{_kf5_libdir}/libKPimItinerary.so

%if %{with lang}
%files -n libKPimItinerary5-lang -f %{name}.lang
%endif

%changelog
