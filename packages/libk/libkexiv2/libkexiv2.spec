#
# spec file for package libkexiv2
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


%define _so     15_0_0
%define lname   libKF5KExiv2
%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libkexiv2
Version:        20.08.2
Release:        0
Summary:        Library to manipulate picture meta data
License:        GPL-2.0-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
Requires:       %{name}-%{_so} = %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  pkgconfig(exiv2) >= 0.25

%description
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata.

%package -n %{lname}-%{_so}
Summary:        Library to manipulate picture meta data
Group:          System/Libraries

%description -n %{lname}-%{_so}
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata.

%package devel
Summary:        Build environment for libkexiv2, a library to manipulate picture meta data
Group:          Development/Libraries/KDE
Requires:       %{lname}-%{_so} = %{version}
Obsoletes:      libkexiv2-kf5-devel < %{version}
Provides:       libkexiv2-kf5-devel = %{version}

%description devel
Libkexiv2 is a wrapper around Exiv2 library to manipulate pictures
metadata.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%post -n %{lname}-%{_so} -p /sbin/ldconfig
%postun -n %{lname}-%{_so} -p /sbin/ldconfig

%files -n %{lname}-%{_so}
%license COPYING*
%doc README
%{_kf5_libdir}/libKF5KExiv2.so.*
%{_kf5_debugdir}/libkexiv2.categories

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5KExiv2/
%{_kf5_includedir}/
%{_kf5_libdir}/libKF5KExiv2.so

%changelog
