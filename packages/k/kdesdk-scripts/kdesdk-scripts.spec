#
# spec file for package kdesdk-scripts
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


%define rname kde-dev-scripts

%define kf6_version 6.0.0
%define qt6_version 6.6.0

%bcond_without released
Name:           kdesdk-scripts
Version:        24.05.2
Release:        0
Summary:        Scripts for KDE software development
License:        GPL-2.0-only AND GFDL-1.2-only
URL:            https://www.kde.org/
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/release-service/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        applications.keyring
%endif
Patch0:         kde-dev-scripts-4.14.3-fix-bashisms.patch
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6DocTools) >= %{kf6_version}
# For ecm_query_qt
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
Obsoletes:      kdesdk4-scripts < %{version}
Provides:       kdesdk4-scripts = %{version}
Obsoletes:      kde-dev-scripts < %{version}
Provides:       kde-dev-scripts = %{version}

%description
This package contains scripts useful for development of KDE software.

%package kf6-porting
Summary:        Scripts for porting applications to KF6

%description kf6-porting
This package contains helper scripts to port code to Qt6 and KDE Frameworks 6.

%lang_package

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%ifarch ppc64
RPM_OPT_FLAGS="%{optflags} -mminimal-toc"
%endif
%cmake_kf6 -DBUILD_WITH_QT6:BOOL=TRUE

%kf6_build

%install
%kf6_install

%find_lang %{name} --with-man --all-name

# Copy the KF6 porting scripts
mkdir -p %{buildroot}%{_kf6_sharedir}/kf6-port-scripts
cp kf6/* %{buildroot}%{_kf6_sharedir}/kf6-port-scripts/

%files
%license COPYING COPYING.DOC
%doc README
%doc %lang(en) %{_kf6_mandir}/man1/*%{ext_man}
%{_kf6_bindir}/*
%{_kf6_sharedir}/uncrustify/

%files kf6-porting
%license COPYING COPYING.DOC
%{_kf6_sharedir}/kf6-port-scripts/

%files lang -f %{name}.lang

%changelog
