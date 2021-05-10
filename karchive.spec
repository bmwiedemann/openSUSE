#
# spec file for package karchive
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


%define lname   libKF5Archive5
%define _tar_path 5.82
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
# Only needed for the package signature condition
%bcond_without lang
Name:           karchive
Version:        5.82.0
Release:        0
Summary:        Qt 5 addon providing access to numerous types of archives
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/frameworks/%{_tar_path}/%{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
Source99:       baselibs.conf
BuildRequires:  extra-cmake-modules >= %{_kf5_bugfix_version}
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libzstd)

%description
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

If also provides transparent compression and decompression of data, like the
GZip format, via a subclass of QIODevice.

%package -n %{lname}
Summary:        Qt 5 addon providing access to numerous types of archives
Group:          System/GUI/KDE
%requires_ge    libQt5Core5

%description -n %{lname}
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

If also provides transparent compression and decompression of data, like the
GZip format, via a subclass of QIODevice.

%package devel
Summary:        Qt 5 addon providing access to numerous types of archives: Build Environment
Group:          Development/Libraries/KDE
Requires:       %{lname} = %{version}
Requires:       extra-cmake-modules
Requires:       cmake(Qt5Core) >= 5.15.0

%description devel
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

If also provides transparent compression and decompression of data, like the
GZip format, via a subclass of QIODevice. Development files

%prep
%autosetup -p1

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build
%fdupes %{buildroot}

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/karchive.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5Archive.so.*

%files devel
%license LICENSES/*
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Archive/
%{_kf5_libdir}/libKF5Archive.so
%{_kf5_mkspecsdir}/qt_KArchive.pri

%changelog
