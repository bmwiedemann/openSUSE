#
# spec file for package libksane
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


%define _so 5
%define lname libKF5Sane
%define kf5_version 5.26.0
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without lang
Name:           libksane
Version:        19.08.0
Release:        0
Summary:        KDE scanning library
License:        GPL-2.0-or-later
Group:          Development/Libraries/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kwallet-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  pkgconfig
BuildRequires:  sane-backends-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.0

%description
The KDE scanner library provides an API and widgets for using
scanners and other imaging devices supported by SANE.

%package devel
Summary:        Development files for the KDE scanning library
Group:          Development/Libraries/KDE
Requires:       %{lname}%{_so} = %{version}
Requires:       kwallet-devel
Requires:       kwidgetsaddons-devel
Requires:       pkgconfig
Requires:       sane-backends-devel
Requires:       pkgconfig(Qt5Widgets) >= 5.2.0
Obsoletes:      libksane-kf5-devel < %{version}
Provides:       libksane-kf5-devel = %{version}

%description devel
This package contains a library to add scan support to KDE
applications.

%package -n %{lname}%{_so}
Summary:        KDE scan library
Group:          System/Libraries
Recommends:     %{name}-lang
Provides:       %{name} = %{version}

%description -n %{lname}%{_so}
The KDE scanner library provides an API and widgets for using
scanners and other imaging devices supported by SANE.

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %if %{with lang}
    %find_lang %{name} --with-man --all-name
  %endif

%post -n %{lname}%{_so} -p /sbin/ldconfig
%postun -n %{lname}%{_so} -p /sbin/ldconfig

%files -n %{lname}%{_so}
%license COPYING*
%{_kf5_libdir}/%{lname}.so.*
%{_kf5_iconsdir}/hicolor/*/actions/black-white.png
%{_kf5_iconsdir}/hicolor/*/actions/color.png
%{_kf5_iconsdir}/hicolor/*/actions/gray-scale.png

%files devel
%license COPYING*
%{_kf5_cmakedir}/KF5Sane/
%{_kf5_includedir}/KSane/
%{_kf5_includedir}/ksane_version.h
%{_kf5_libdir}/%{lname}.so

%if %{with lang}
%files lang -f %{name}.lang
%license COPYING*
%endif

%changelog
