#
# spec file for package kdevelop-pg-qt
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
Name:           kdevelop-pg-qt
Version:        2.3.0
Release:        0
Summary:        Supporting package for the additional plugins for Kdevelop
License:        LGPL-2.0-or-later
URL:            https://www.kdevelop.org
Source0:        https://download.kde.org/stable/kdevelop-pg-qt/%{version}/src/%{name}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/kdevelop-pg-qt/%{version}/src/%{name}-%{version}.tar.xz.sig
Source2:        kdevelop-pg-qt.keyring
%endif
Source99:       kdevelop-pg-qt-rpmlintrc
BuildRequires:  bison
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  flex
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Test) >= %{qt6_version}
Provides:       kdevelop5-pg-qt = %{version}
Obsoletes:      kdevelop5-pg-qt < %{version}
Conflicts:      kdevelop4-pg-qt

%description
Supporting package for the additional plugins for Kdevelop Integrated Development Environment

%prep
%autosetup -p1

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%files
%license COPYING*
%{_kf6_bindir}/kdev-pg-qt
%{_includedir}/kdevelop-pg-qt/
%{_kf6_cmakedir}/KDevelop-PG-Qt/

%changelog
