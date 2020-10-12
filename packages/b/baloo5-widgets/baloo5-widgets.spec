#
# spec file for package baloo5-widgets
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


%define rname baloo-widgets
%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           baloo5-widgets
Version:        20.08.2
Release:        0
Summary:        Framework for searching and managing metadata
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
Source99:       baloo5-widgets-rpmlintrc
BuildRequires:  extra-cmake-modules >= %{kf5_version}
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Baloo)
BuildRequires:  cmake(KF5FileMetaData)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Service)
BuildRequires:  cmake(Qt5Core) >= 5.8.0
BuildRequires:  cmake(Qt5Test) >= 5.8.0
BuildRequires:  cmake(Qt5Widgets) >= 5.8.0
Recommends:     %{name}-lang
Obsoletes:      libKF5BalooWidgets5
Provides:       libKF5BalooNaturalQueryParser1 = %{version}
Obsoletes:      libKF5BalooNaturalQueryParser1 < %{version}
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
Baloo is a framework for searching and managing metada

%package devel
Summary:        Development package for baloo5-widgets
Group:          Development/Libraries/KDE
Requires:       %{name} = %{version}
Requires:       cmake(KF5KIO)
Requires:       cmake(Qt5Widgets) >= 5.8.0
Provides:       baloo-widgets5-devel
Obsoletes:      baloo-widgets5-devel

%description devel
Development package for baloo5-widgets

%lang_package

%prep
%setup -q -n %{rname}-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%dir %{_kf5_plugindir}/kf5/
%dir %{_kf5_plugindir}/kf5/kfileitemaction
%{_kf5_bindir}/baloo_filemetadata_temp_extractor
%{_kf5_debugdir}/baloo-widgets.categories
%{_kf5_libdir}/libKF5BalooWidgets.so.*
%{_kf5_plugindir}/baloofilepropertiesplugin.so
%{_kf5_plugindir}/kf5/kfileitemaction/tagsfileitemaction.so
%{_kf5_servicesdir}/*.desktop

%files devel
%license COPYING*
%{_kf5_includedir}/
%{_kf5_libdir}/libKF5BalooWidgets.so
%{_kf5_cmakedir}/KF5BalooWidgets/

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
