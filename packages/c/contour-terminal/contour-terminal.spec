#
# spec file for package contour-terminal
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


%bcond_with     qt6
Name:           contour-terminal
Version:        0.3.12.262
Release:        0
Summary:        Modern C++ Terminal Emulator
License:        Apache-2.0
URL:            https://github.com/contour-terminal/contour
Source0:        %{url}/archive/v%{version}/contour-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 782fb7248d6fe643e7163bf57b0bcef50a81a8f7.patch -- fix build with fmt 10
Patch0:         %{url}/commit/782fb7248d6fe643e7163bf57b0bcef50a81a8f7.patch
BuildRequires:  Catch2-2-devel
BuildRequires:  appstream-glib
BuildRequires:  ccache
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  fmt-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libunicode-devel
BuildRequires:  libxcb-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  range-v3-devel
BuildRequires:  utempter-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  cmake(Microsoft.GSL)
BuildRequires:  pkgconfig(tic)
%if %{with qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGL)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Widgets)
%else
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
%endif
Recommends:     kf5-filesystem
Recommends:     kservice
ExclusiveArch:  x86_64 aarch64

%description
Contour is a modern and actually fast, modal, virtual terminal emulator,
for everyday use. It is aiming for power users with a modern feature mindset.

%prep
%autosetup -p1 -n contour-%{version}

%build
%cmake \
%if %{with qt6}
    -DCONTOUR_QT_VERSION=6 \
%else
    -DCONTOUR_QT_VERSION=5 \
%endif

%cmake_build

%install
%cmake_install

rm %{buildroot}%{_datadir}/terminfo/c/contour-latest
ln -s contour %{buildroot}%{_datadir}/terminfo/c/contour-latest
rm %{buildroot}%{_datadir}/contour/LICENSE.txt
rm %{buildroot}%{_datadir}/contour/README.md

desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/contour
%{_datadir}/applications/*.desktop
%dir %{_datadir}/kservices5/ServiceMenus
%{_datadir}/kservices5/ServiceMenus/*.desktop
%dir %{_datadir}/contour
%dir %{_datadir}/contour/shell-integration
%{_datadir}/contour/shell-integration/shell-integration.fish
%{_datadir}/contour/shell-integration/shell-integration.tcsh
%{_datadir}/contour/shell-integration/shell-integration.zsh
%{_datadir}/terminfo/c/contour*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/metainfo/org.contourterminal.Contour.metainfo.xml

%changelog
