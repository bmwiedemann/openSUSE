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
# Full KF5 version (e.g. 5.33.0)
%{!?_kf5_version: %global _kf5_version %{version}}
# Last major and minor KF5 version (e.g. 5.33)
%{!?_kf5_bugfix_version: %define _kf5_bugfix_version %(echo %{_kf5_version} | awk -F. '{print $1"."$2}')}
%define qt5_version 5.15.2
%bcond_without released
Name:           karchive
Version:        5.116.0
Release:        0
Summary:        Qt 5 addon providing access to numerous types of archives
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{name}-%{version}.tar.xz
%if %{with released}
Source1:        %{name}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  extra-cmake-modules >= %{_kf5_version}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5LinguistTools) >= %{qt5_version}
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
%requires_ge    libQt5Core5

%description -n %{lname}
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

If also provides transparent compression and decompression of data, like the
GZip format, via a subclass of QIODevice.

%lang_package -n %{lname}

%package devel
Summary:        Qt 5 addon providing access to numerous types of archives: Build Environment
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Core) >= %{qt5_version}

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

%find_lang karchive5 --with-man --all-name --with-qt

%ldconfig_scriptlets -n %{lname}

%files -n %{lname}
%license LICENSES/*
%doc README*
%{_kf5_debugdir}/karchive.categories
%{_kf5_debugdir}/*.renamecategories
%{_kf5_libdir}/libKF5Archive.so.*

%files -n %{lname}-lang -f karchive5.lang

%files devel
%{_kf5_includedir}/
%{_kf5_libdir}/cmake/KF5Archive/
%{_kf5_libdir}/libKF5Archive.so
%{_kf5_mkspecsdir}/qt_KArchive.pri

%changelog
