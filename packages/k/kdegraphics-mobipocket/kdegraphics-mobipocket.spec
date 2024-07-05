#
# spec file for package kdegraphics-mobipocket
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


%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kdegraphics-mobipocket
Version:        24.05.2
Release:        0
Summary:        E-book plugin and library
License:        GPL-2.0-or-later
URL:            https://www.kde.org
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_version}

%description
Mobipocket E-book support for Okular.

%package -n libQMobipocket6-2
Summary:        E-book plugin and library

%description -n libQMobipocket6-2
Mobipocket E-book plugin and library.

%package -n kdegraphics-mobipocket-devel
Summary:        E-book plugin and library
Requires:       libQMobipocket6-2 = %{version}

%description -n kdegraphics-mobipocket-devel
Mobipocket E-book plugin and library.

This package provides development files for kdegraphics-mobipocket
library

%prep
%autosetup -p1

%build
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%ldconfig_scriptlets -n libQMobipocket6-2

%files -n libQMobipocket6-2
%license COPYING
%{_kf6_libdir}/libQMobipocket6.so.*

%files -n kdegraphics-mobipocket-devel
%{_includedir}/QMobipocket6/
%{_kf6_cmakedir}/QMobipocket6/
%{_kf6_libdir}/libQMobipocket6.so

%changelog
