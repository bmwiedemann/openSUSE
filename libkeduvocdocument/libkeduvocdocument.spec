#
# spec file for package libkeduvocdocument
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libkeduvocdocument
Version:        19.08.1
Release:        0
Summary:        Library for KDE Education Applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://edu.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  karchive-devel
BuildRequires:  kconfig-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2.0

%description
This package contains the library which is required by the KDE education
applications.

%package -n libKEduVocDocument5
Summary:        Library for KDE Education Applications
Group:          System/GUI/KDE
Recommends:     %{name}-lang
Recommends:     kdeedu-data
Provides:       %{name} = %{version}

%description -n libKEduVocDocument5
This package contains the library which is required by the KDE education
applications.

%package devel
Summary:        Library for KDE Education Applications: Build Environment
Group:          Development/Libraries/KDE
Requires:       libKEduVocDocument5 = %{version}

%description devel
This package contains all necessary files and libraries needed to
develop KDE education applications.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q

%build
%cmake_kf5 -d build -- -DKDE4_USE_COMMON_CMAKE_PACKAGE_CONFIG_DIR=ON
%make_jobs

%install
%kf5_makeinstall -C build
%if %{with lang}
  %find_lang %{name} --with-man --all-name
%endif
%fdupes -s %{buildroot}

%post -n libKEduVocDocument5 -p /sbin/ldconfig
%postun -n libKEduVocDocument5 -p /sbin/ldconfig

%files -n libKEduVocDocument5
%license COPYING*
%doc README
%{_kf5_libdir}/libKEduVocDocument.so.*

%files devel
%license COPYING*
%doc README
%{_kf5_cmakedir}/libkeduvocdocument/
%{_kf5_libdir}/libKEduVocDocument.so
%{_kf5_prefix}/include/libkeduvocdocument/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
