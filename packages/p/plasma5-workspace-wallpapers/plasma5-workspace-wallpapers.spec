#
# spec file for package plasma5-workspace-wallpapers
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


%bcond_without released
Name:           plasma5-workspace-wallpapers
Version:        5.26.4
Release:        0
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 0.0.12
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
Summary:        Additional Plasma Wallpapers
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/plasma-workspace-wallpapers-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/plasma-workspace-wallpapers-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildArch:      noarch

%description
Additional wallpapers for Plasma Workspace.

%prep
%setup -q -n plasma-workspace-wallpapers-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build

  #found conflict of kdebase4-wallpapers-15.08.3-1.1.noarch with plasma5-workspace-wallpapers-5.5.2-50.1.noarch:
  #- /usr/share/wallpapers/Autumn/metadata.desktop
  rm -rf %{buildroot}%{_kf5_sharedir}/wallpapers/Autumn

%files
%defattr(-,root,root)
%license COPYING*
%{_kf5_sharedir}/wallpapers/

%changelog
