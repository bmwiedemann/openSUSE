#
# spec file for package kdesdk-scripts
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


%define rname kde-dev-scripts
# Latest stable Applications (e.g. 17.08 in KA, but 17.11.80 in KUA)
%{!?_kapp_version: %define _kapp_version %(echo %{version}| awk -F. '{print $1"."$2}')}
%bcond_without released
Name:           kdesdk-scripts
Version:        22.12.1
Release:        0
Summary:        Scripts for KDE software development
License:        GPL-2.0-only AND GFDL-1.2-only
URL:            https://www.kde.org/
Source:         https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch0:         kde-dev-scripts-4.14.3-fix-bashisms.patch
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5DocTools)
Obsoletes:      kdesdk4-scripts < %{_kapp_version}
Provides:       kdesdk4-scripts = %{_kapp_version}
Obsoletes:      kde-dev-scripts < %{_kapp_version}
Provides:       kde-dev-scripts = %{_kapp_version}

%description
This package contains scripts useful for development of KDE software.

%package kf5-porting
Summary:        Scripts for porting applications to KF5
Obsoletes:      kdesdk4-scripts-kf5-porting < %{version}
Provides:       kdesdk4-scripts-kf5-porting = %{version}

%description kf5-porting
This package contains the scripts to make the porting KDE software from
kdelibs and Qt4 to Qt5 and KDE Frameworks 5.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
export CXXFLAGS="%{optflags} -fPIC"
export CFLAGS="%{optflags} -fPIC"
%cmake_kf5 -d build -- -DCMAKE_CXXFLAGS="%{optflags}" -DCMAKE_CFLAGS="%{optflags}"
%cmake_build

%install
%kf5_makeinstall -C build

%find_lang %{name} --with-man --all-name

%{kf5_post_install}

# Copy the KF5 porting scripts
mkdir -p %{buildroot}%{_datadir}/kf5-port-scripts
cp kf5/* %{buildroot}%{_datadir}/kf5-port-scripts/

%files
%license COPYING COPYING.DOC
%doc README
%{_kf5_appsdir}/uncrustify/
%{_kf5_bindir}/*
%{_mandir}/man1/*%{ext_man}

%files kf5-porting
%license COPYING COPYING.DOC
%doc README
%{_datadir}/kf5-port-scripts/

%files lang -f %{name}.lang

%changelog
