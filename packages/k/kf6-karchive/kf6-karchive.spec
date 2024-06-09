#
# spec file for package kf6-karchive
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


%define qt6_version 6.6.0

%define rname karchive
# Full KF6 version (e.g. 6.3.0)
%{!?_kf6_version: %global _kf6_version %{version}}
# Last major and minor KF6 version (e.g. 6.0)
%{!?_kf6_bugfix_version: %define _kf6_bugfix_version %(echo %{_kf6_version} | awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kf6-karchive
Version:        6.3.0
Release:        0
Summary:        Qt 6 addon providing access to numerous types of archives
License:        LGPL-2.0-or-later
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        frameworks.keyring
%endif
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{_kf6_bugfix_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6ToolsTools) >= %{qt6_version}
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)

%description
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

If also provides transparent compression and decompression of data, like the
GZip format, via a subclass of QIODevice.

%package -n libKF6Archive6
Summary:        Qt 6 addon providing access to numerous types of archives
Requires:       kf6-karchive >= %{version}

%description -n libKF6Archive6
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

If also provides transparent compression and decompression of data, like the
GZip format, via a subclass of QIODevice.

%lang_package -n libKF6Archive6

%package devel
Summary:        Development files for kf6-karchive
Requires:       libKF6Archive6 = %{version}

%description devel
KArchive provides classes for easy reading, creation and manipulation of
"archive" formats like ZIP and TAR.

If also provides transparent compression and decompression of data, like the
GZip format, via a subclass of QIODevice. Development files

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6 -DBUILD_QCH:BOOL=TRUE

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang kf6-karchive --with-man --all-name --with-qt

%ldconfig_scriptlets -n libKF6Archive6

%files
%{_kf6_debugdir}/karchive.categories
%{_kf6_debugdir}/karchive.renamecategories

%files -n libKF6Archive6
%license LICENSES/*
%doc README.md
%{_kf6_libdir}/libKF6Archive.so.*

%files devel
%doc %{_kf6_qchdir}/KF6Archive.*
%{_kf6_includedir}/KArchive/
%{_kf6_cmakedir}/KF6Archive/
%{_kf6_libdir}/libKF6Archive.so

%files -n libKF6Archive6-lang -f kf6-karchive.lang

%changelog
