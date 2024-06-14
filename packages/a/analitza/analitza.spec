#
# spec file for package analitza
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
Name:           analitza
Version:        24.05.1
Release:        0
Summary:        A library to add mathematical features to programs
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/education/analitza
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6LinguistTools) >= %{qt6_version}
BuildRequires:  cmake(Qt6OpenGLWidgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6PrintSupport) >= %{qt6_version}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
BuildRequires:  cmake(Qt6Xml) >= %{qt6_version}
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(glew)
Requires:       libAnalitza9 = %{version}
Obsoletes:      analitza5 < %{version}
Provides:       analitza5 = %{version}

%description
The Analitza library lets developers add mathematical features to programs.

%package -n libAnalitza9
Summary:        A library to add mathematical features to programs
Requires:       analitza = %{version}
# Mistakenly contained libAnalitza6, 7 and 8
Conflicts:      libAnalitza5

%description -n libAnalitza9
The Analitza library lets developers add mathematical features to programs.

%package devel
Summary:        Development files for analitza, a mathematical feature library
Requires:       libAnalitza9 = %{version}
Requires:       cmake(Qt6Core) >= %{qt6_version}
Requires:       cmake(Qt6Xml) >= %{qt6_version}
Obsoletes:      analitza5-devel < %{version}

%description devel
Development files for Analitza. The Analitza library lets developers
add mathematical features to programs.

%lang_package

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-qt --all-name

%ldconfig_scriptlets -n libAnalitza9

%files -n libAnalitza9
%license COPYING*
%{_kf6_libdir}/libAnalitza*.so.*

%files devel
%{_includedir}/Analitza6/
%{_kf6_cmakedir}/Analitza6/
%{_kf6_libdir}/libAnalitza*.so

%files
%{_kf6_qmldir}/org/kde/analitza/
%{_kf6_sharedir}/libanalitza/

%files lang -f %{name}.lang

%changelog
