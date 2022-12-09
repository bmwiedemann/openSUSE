#
# spec file for package analitza
#
# Copyright (c) 2022 SUSE LLC
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


%define soversion 8
%define kf5_version 5.90.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           analitza
Version:        22.12.0
Release:        0
Summary:        A library to add mathematical features to programs
License:        LGPL-2.1-or-later
URL:            https://invent.kde.org/education/analitza
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5PrintSupport)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
Requires:       libAnalitza%{soversion} = %{version}
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}

%description
The Analitza library lets developers add mathematical features to programs.

%package -n libAnalitza%{soversion}
Summary:        A library to add mathematical features to programs
Requires:       analitza = %{version}
# Mistakenly contained libAnalitza6, 7 and 8
%if %{soversion} == 8
Conflicts:      libAnalitza5
%endif

%description -n libAnalitza%{soversion}
The Analitza library lets developers add mathematical features to programs.

%package devel
Summary:        Development files for analitza, a mathematical feature library
Requires:       libAnalitza%{soversion} = %{version}
Obsoletes:      analitza5-devel < %{version}

%description devel
Development files for Analitza. The Analitza library lets developers
add mathematical features to programs.

%lang_package

%prep
%autosetup -p1 -n analitza-%{version}

%build
%cmake_kf5 -d build
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --with-qt --all-name

%post -n libAnalitza%{soversion} -p /sbin/ldconfig
%postun -n libAnalitza%{soversion} -p /sbin/ldconfig

%files -n libAnalitza%{soversion}
%license COPYING*
%{_kf5_libdir}/libAnalitza*.so.%{soversion}*

%files devel
%{_kf5_cmakedir}/Analitza5/
%{_kf5_libdir}/libAnalitza*.so
%{_kf5_prefix}/include/Analitza5/

%files
%{_kf5_qmldir}/
%{_kf5_sharedir}/libanalitza/

%files lang -f %{name}.lang

%changelog
