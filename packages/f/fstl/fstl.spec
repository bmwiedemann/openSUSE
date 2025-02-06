#
# spec file for package fstl
#
# Copyright (c) 2025 SUSE LLC
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


Name:           fstl
Version:        0.11.0
Release:        0
Summary:        Fast stl file viewer
License:        AGPL-3.0-only
Group:          Productivity/Graphics/3D Editors
URL:            https://github.com/mkeeter/fstl.git
Source0:        https://github.com/fstl-app/fstl/archive/refs/tags/v%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  cmake >= 2.8.12
BuildRequires:  hicolor-icon-theme
BuildRequires:  icoutils
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Widgets)

%description
Fast stl file viewer.
It is designed to quickly load and render very high-polygon models; showing 2 million triangles at 60+ FPS on a mid-range laptop.

%prep
%setup -q

%build
CFLAGS="%{optflags}"
export CFLAGS
%cmake
%make_build

%install
%cmake_install
cd exe
icotool -x fstl.ico
install -Dm 0755 fstl_1_16x16x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -Dm 0755 fstl_2_32x32x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dm 0755 fstl_3_48x48x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -Dm 0755 fstl_4_64x64x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
install -Dm 0755 fstl_5_128x128x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -Dm 0755 fstl_6_256x256x32.png \
  %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%suse_update_desktop_file -i %{name}

%files
%{_bindir}/fstl
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
