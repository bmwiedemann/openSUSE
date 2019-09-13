#
# spec file for package analitza
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
Name:           analitza
Version:        19.08.1
Release:        0
Summary:        A library to add mathematical features to programs
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://projects.kde.org/projects/kde/kdeedu/analitza
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  cmake
BuildRequires:  eigen3-devel
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
Requires:       libAnalitza5 = %{version}
Obsoletes:      %{name}5 < %{version}
Provides:       %{name}5 = %{version}
%if %{with lang}
Recommends:     %{name}-lang
%endif

%description
The Analitza library lets developers add mathematical features to programs.

%package -n libAnalitza5
Summary:        A library to add mathematical features to programs
Group:          System/Libraries
Requires:       analitza = %{version}

%description -n libAnalitza5
The Analitza library lets developers add mathematical features to programs.

%package devel
Summary:        Development files for analitza, a mathematical feature library
Group:          Development/Libraries/C and C++
Requires:       libAnalitza5 = %{version}
Obsoletes:      analitza5-devel < %{version}

%description devel
Development files for Analitza. The Analitza library lets developers
add mathematical features to programs.

%if %{with lang}
%lang_package
%endif

%prep
%setup -q -n analitza-%{version}

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --with-qt --all-name
  %endif

%post -n libAnalitza5 -p /sbin/ldconfig
%postun -n libAnalitza5 -p /sbin/ldconfig

%files -n libAnalitza5
%license COPYING*
%{_kf5_libdir}/libAnalitza*.so.*

%files devel
%{_kf5_libdir}/libAnalitza*.so
%{_kf5_prefix}/include/Analitza5/
%{_kf5_cmakedir}/Analitza5/

%files
%{_kf5_qmldir}/
%{_kf5_sharedir}/libanalitza/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
