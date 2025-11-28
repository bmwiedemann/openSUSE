#
# spec file for package heroic-epic-integration
#
# Copyright (c) 2025 SUSE LLC and contributors
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

Name:           heroic-epic-integration
Version:        0.4
Release:        0
Summary:        Epic Games Windows integration for Heroic
License:        GPL-3.0-only
URL:            https://github.com/Etaash-mathamsetty/heroic-epic-integration.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  mingw64-cross-cmake
BuildRequires:  mingw64-cross-gcc
BuildRequires:  mingw64-cross-gcc-c++
BuildArch:      noarch

%description
Wrapper process for games launched through Heroic Games Launcher

%prep
%autosetup -p1

%build
mkdir build
cd build
cmake -DCMAKE_TOOLCHAIN_FILE=../windows.cmake ..
make

%install
install -Dm0755 build/heroic-epic-integration.exe %{buildroot}/%{_libexecdir}/heroic/EpicGamesLauncher.exe

%files
%license LICENSE*
%dir %{_libexecdir}/heroic
%{_libexecdir}/heroic/EpicGamesLauncher.exe

%changelog
