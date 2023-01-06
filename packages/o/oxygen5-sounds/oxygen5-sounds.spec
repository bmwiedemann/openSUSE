#
# spec file for package oxygen5-sounds
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

Name:           oxygen5-sounds
Version:        5.26.5
%global _plasma5_bugfix 5.26.3
Release:        0
# Full Plasma 5 version (e.g. 5.8.95)
%{!?_plasma5_bugfix: %define _plasma5_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 5.8 in KF5, but 5.8.95 in KUF)
%{!?_plasma5_version: %define _plasma5_version %(echo %{_plasma5_bugfix} | awk -F. '{print $1"."$2}')}
Summary:        Oxygen sounds
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/oxygen-sounds-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/oxygen-sounds-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  extra-cmake-modules >= 5.89.0
BuildRequires:  kf5-filesystem
Obsoletes:      oxygen-sounds5 < %{version}
Provides:       oxygen-sounds5 = %{version}
BuildArch:      noarch

%description
This package contains the default sound set for a KDE Plasma workspace.

%prep
%setup -q -n oxygen-sounds-%{version}

%build
%cmake_kf5 -d build -- -DCMAKE_INSTALL_LOCALEDIR=%{_kf5_localedir}
%cmake_build

%install
  %kf5_makeinstall -C build

%files
%license LICENSES/*
%{_kf5_sharedir}/sounds/*

%changelog
