#
# spec file for package kmime
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


%define kf5_version 5.60.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           kmime
Version:        20.08.1
Release:        0
Summary:        KDE PIM libraries MIME support
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Codecs) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(Qt5Test) >= 5.2.0
%if %{with lang}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif

%description
This package contains the basic packages for KDE PIM applications.

%package -n libKF5Mime5
Summary:        KDE PIM libraries MIME Support
Group:          Development/Libraries/KDE
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description  -n libKF5Mime5
This package provides MIME support for KDE PIM applications

%package devel
Summary:        Build environment for the KDE PIM MIME libraries
Group:          Development/Libraries/KDE
Requires:       libKF5Mime5 = %{version}
Requires:       cmake(KF5Codecs)

%description devel
This package contains necessary include files and libraries needed
to develop KDE PIM applications.

%lang_package

%prep
%setup -q -n kmime-%{version}

%build
  %cmake_kf5 -d build -- -DBUILD_TESTING=ON -DKF5_INCLUDE_INSTALL_DIR=%{_kf5_includedir}
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n libKF5Mime5 -p /sbin/ldconfig
%postun -n libKF5Mime5 -p /sbin/ldconfig

%files -n libKF5Mime5
%license COPYING*
%{_kf5_libdir}/libKF5Mime.so.*
%{_kf5_debugdir}/kmime.categories

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5Mime/
%{_kf5_includedir}/KMime/
%{_kf5_includedir}/kmime_version.h
%{_kf5_libdir}/libKF5Mime.so
%{_kf5_mkspecsdir}/qt_KMime.pri

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
