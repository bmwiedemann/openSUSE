#
# spec file for package kpeoplevcard
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


%bcond_without  lang
Name:           kpeoplevcard
Version:        0.1
Release:        0
Summary:        A vCard plugin for KPeople
License:        LGPL-2.1-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
%if %{with lang}
Source1:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2:        %{name}.keyring
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5Contacts)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5People) >= 5.62
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)

%description
Kpeoplevcard provides a datasource plugin for KPeople that reads vCard files
from the local filesystem.

%package devel
Summary:        Development files for kpeoplevcard, a vCard plugin for KPeople
Group:          Development/Libraries/KDE

%description devel
Development files for kpeoplevcard, a datasource plugin for KPeople that reads
vCard files from the local filesystem.

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

%files
%license COPYING
%{_kf5_plugindir}/kpeople/

%files devel
%{_kf5_cmakedir}/KF5PeopleVCard/

%changelog
