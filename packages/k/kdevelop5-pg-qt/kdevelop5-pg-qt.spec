#
# spec file for package kdevelop5-pg-qt
#
# Copyright (c) 2023 SUSE LLC
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


%bcond_without released
%define rname kdevelop-pg-qt
Name:           kdevelop5-pg-qt
Version:        2.2.2
Release:        0
Summary:        Supporting package for the additional plugins for Kdevelop5
License:        LGPL-2.0-or-later AND GPL-2.0-or-later
Group:          Development/Tools/IDE
URL:            https://www.kdevelop.org/
Source0:        https://download.kde.org/stable/kdevelop-pg-qt/%{version}/src/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/kdevelop-pg-qt/%{version}/src/%{rname}-%{version}.tar.xz.sig
Source2:        %{rname}.keyring
%endif
BuildRequires:  bison
BuildRequires:  extra-cmake-modules
BuildRequires:  flex
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Test)
Conflicts:      kdevelop4-pg-qt

%description
Supporting package for the additional plugins for Kdevelop5 Integrated Development Environment

%prep
%setup -q -n %{rname}-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license COPYING*
%{_kf5_bindir}/kdev-pg-qt
%{_kf5_libdir}/cmake/KDevelop-PG-Qt/
%{_kf5_prefix}/include/kdevelop-pg-qt/

%changelog
