#
# spec file for package libkomparediff2-kf5
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


%define kf5_version 5.91.0
%define qt5_version 5.15.2

%define rname libkomparediff2
%bcond_without released
Name:           libkomparediff2-kf5
Version:        24.02.2
Release:        0
Summary:        A library to compare files and strings
License:        (GPL-2.0-or-later AND LGPL-2.0-or-later) AND BSD-2-Clause
URL:            https://www.kde.org
Source:         %{rname}-%{version}.tar.xz
%if %{with released}
Source1:        %{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5KIO) >= %{kf5_version}
BuildRequires:  cmake(KF5Parts) >= %{kf5_version}
BuildRequires:  cmake(KF5XmlGui) >= %{kf5_version}
BuildRequires:  cmake(Qt5Core) >= %{qt5_version}
BuildRequires:  cmake(Qt5Test) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}

%description
A library to compare files and strings, used in Kompare and KDevelop.

%package -n libkomparediff2-5
Summary:        A library to compare files and strings
Requires:       (libkomparediff2-kf5 if kdebugsettings)
Obsoletes:      libkomparediff2-lang < %{version}
%description -n libkomparediff2-5
A library to compare files and strings, used in Kompare and KDevelop.

%package devel
Summary:        Development package for libkomparediff2-kf5
Requires:       libkomparediff2-5 = %{version}
Requires:       cmake(KF5Config) >=  %{kf5_version}
Requires:       cmake(KF5XmlGui) >=  %{kf5_version}
Requires:       cmake(Qt5Core) >= %{qt5_version}
Requires:       cmake(Qt5Widgets) >= %{qt5_version}
# Package was renamed before submitting gear 6 to factory
Provides:       libkomparediff2-devel = 23.08.4
Obsoletes:      libkomparediff2-devel < 23.08.4

%description devel
Development package for libkomparediff2-kf5.

%lang_package -n libkomparediff2-5

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf5 -d build -- -DQT_MAJOR_VERSION:STRING=5

%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --all-name

%ldconfig_scriptlets -n libkomparediff2-5

%files
%{_kf5_debugdir}/libkomparediff2.categories

%files -n libkomparediff2-5
%license COPYING*
%{_kf5_libdir}/libkomparediff2.so.*

%files devel
%{_includedir}/KompareDiff2/
%{_kf5_cmakedir}/LibKompareDiff2/
%{_kf5_libdir}/libkomparediff2.so

%files -n libkomparediff2-5-lang -f %{name}.lang

%changelog
